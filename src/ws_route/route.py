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
                data = await websocket.receive_json()
                print(f"data received from FE: {data}")

                try:
                    await websocket.send_json(
                        {
                            "type": "success",
                            "message": f"Server sends back: {data}",
                        }
                    )
                except KeyError:
                    await websocket.send_text(
                        "Having error in key of received data. Try again later"
                    )
        except WebSocketDisconnect:
            print("Client disconnected")
