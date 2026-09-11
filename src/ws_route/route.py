import asyncio
from typing import Literal, TypedDict

from boto3.dynamodb.conditions import Key
from fastapi import FastAPI, WebSocket, WebSocketDisconnect

from src.db.get_db import get_dynamodb
from src.db.subscription_table import ensure_subscription_table


class SuccessResponse(TypedDict):
    type: Literal["success"]
    message: str
    planId: str | None


class InProgressResponse(TypedDict):
    type: Literal["inProgress"]
    message: str
    planId: str | None


class ErrorResponse(TypedDict):
    type: Literal["error"]
    message: str
    planId: str | None


PlanSelectionResponse = SuccessResponse | InProgressResponse | ErrorResponse

PLAN_INFO = {
    "trial": {
        "name": "Trial Plan",
        "price": 0,
        "description": "This is a trial plan for 7 days.",
    },
    "professional": {
        "name": "Professional Plan",
        "price": 29,
        "description": "This is a professional plan for individuals.",
    },
    "enterprise": {
        "name": "Enterprise Plan",
        "price": 99,
        "description": "This is an enterprise plan for businesses.",
    },
}

MAX_SCAN_ATTEMPTS = 40
SCAN_POLL_INTERVAL_SECONDS = 1.0


def get_ws_route(app: FastAPI):
    @app.websocket("/ws")
    async def websocket_endpoint(websocket: WebSocket):
        await websocket.accept()

        table = None

        try:
            db = get_dynamodb()
            table = ensure_subscription_table(db)
        except Exception:
            await websocket.send_json(
                {
                    "type": "error",
                    "message": "Database connection error. Please try again later.",
                }
            )
            await websocket.close()
            raise

        try:
            plan_id = "NoPlan"  # default plan_id
            while True:
                try:
                    data = await websocket.receive_json()

                    # these make plan_id overcome type checking issues
                    raw_plan_id = data.get("planId")
                    plan_id = raw_plan_id if isinstance(raw_plan_id, str) else "NoPlan"

                    if plan_id is not None:
                        await websocket.send_json(
                            {
                                "type": "inProgress",
                                "message": "Your plan selection is being processed. Please wait for a moment.",
                            }
                        )
                except Exception as e:
                    print(f"recieve_json error: {type(e).__name__} {e}")
                    raise

                try:
                    # data_received: {
                    #   type: "selectPlan",
                    #   planId,
                    #   email: "truongtronghai@gmail.com",
                    #   token: "sampleToken",
                    #   accountName: "Hai Truong sandbox",
                    # }
                    price_of_plan = (
                        PLAN_INFO[plan_id]["price"] if plan_id in PLAN_INFO else 0
                    )
                    account_name = data.get("accountName", "Unknown Account")
                    email = data.get("email", "Unknown Email")

                    # print(
                    #     f"Received plan selection: planId={plan_id}, accountName={account_name}, email={email}, price={price_of_plan}"
                    # )

                    matching_items = []

                    for attempt in range(MAX_SCAN_ATTEMPTS):
                        response = table.scan(
                            FilterExpression=(
                                Key("account_name").eq(account_name)
                                & Key("email").eq(email)
                                & Key("amount_paid").eq(price_of_plan * 100)
                            )
                        )
                        # print(
                        #     f"response from DynamoDB scan (attempt {attempt + 1}/{MAX_SCAN_ATTEMPTS}): {response}"
                        # )
                        if response.get("Items"):
                            matching_items = response["Items"]
                            break

                        await asyncio.sleep(SCAN_POLL_INTERVAL_SECONDS)

                    if matching_items:
                        await websocket.send_json(
                            {
                                "type": "success",
                                "message": f"Your plan selection: {PLAN_INFO[plan_id]['name']} has been upgraded successfully. Thank for your choice",
                            }
                        )

                        break
                    else:
                        await websocket.send_json(
                            {
                                "type": "error",
                                "message": "No payment found for this plan selection. Please try again later.",
                            }
                        )

                except Exception:
                    await websocket.send_json(
                        {
                            "type": "error",
                            "message": "An error occurred while processing your plan selection. Please try again later.",
                        }
                    )
                    raise

        except WebSocketDisconnect:
            print("Client disconnected")
