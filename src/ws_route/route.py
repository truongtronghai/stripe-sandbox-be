from fastapi import FastAPI, WebSocket, WebSocketDisconnect


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
                            "type": "response",
                            "message": f"Hello {data['name']}",
                        }
                    )
                except KeyError:
                    await websocket.send_text(
                        "Having error in key of received data. Try again later"
                    )
        except WebSocketDisconnect:
            print("Client disconnected")
