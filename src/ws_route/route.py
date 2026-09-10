import uuid
from datetime import UTC, datetime
from typing import Literal, TypedDict

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


def get_ws_route(app: FastAPI):
    @app.websocket("/ws")
    async def websocket_endpoint(websocket: WebSocket):
        await websocket.accept()

        table = None

        try:
            await websocket.send_json(
                {
                    "type": "inProgress",
                    "message": "Your plan selection is being processed. Please wait for a moment.",
                }
            )
            db = get_dynamodb()
            table = ensure_subscription_table(db)
        except Exception as e:
            await websocket.send_json(
                {
                    "type": "error",
                    "message": "Database connection error. Please try again later.",
                }
            )
            await websocket.close()
            raise

        try:
            while True:
                try:
                    data = await websocket.receive_json()
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
                    plan_id = data.get("planId", "Trial")
                    table.put_item(
                        Item={
                            "subscriptionId": str(uuid.uuid4()),
                            "planId": plan_id,
                            "email": data.get("email", "truongtronghai@gmail.com"),
                            "created_at": datetime.now(UTC).isoformat(),
                        }
                    )

                    await websocket.send_json(
                        {
                            "type": "success",
                            "message": f"Your plan selection: {plan_id.upper()} has been upgraded successfully. Thank for your choice",
                        }
                    )
                except Exception as e:
                    print(f"put_item error: {type(e).__name__} {e}")
                    plan_id = data.get("planId", "Trial")
                    await websocket.send_json(
                        {
                            "type": "error",
                            "message": f"Your plan selection: {plan_id.upper()} has been upgraded successfully. Thank for your choice",
                        }
                    )
        except WebSocketDisconnect:
            print("Client disconnected")
