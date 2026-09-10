from typing import Literal, TypedDict

from fastapi import FastAPI, WebSocket, WebSocketDisconnect


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

        try:
            while True:
                try:
                    data = await websocket.receive_json()
                    print(f"data received from FE: {data}")
                except Exception as e:
                    print(f"recieve_json error: {type(e).__name__} {e}")
                    raise

                await websocket.send_json(
                    {
                        "type": "success",
                        "message": f"Your plan selection: {data['planId']} has been upgraded successfully. Thank for your choice",
                    }
                )
        except WebSocketDisconnect:
            print("Client disconnected")
