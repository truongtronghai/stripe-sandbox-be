from fastapi import FastAPI, Request
from pydantic import BaseModel

# The key fix was: Python modules cannot use hyphens
# DO NOT USE "-" in folder name
# and the import must be a real module path, not a quoted string.
from src.ws_route.route import get_ws_route
from utils.converters.raw_bytes_literal import to_dict

app = FastAPI()


class Item(BaseModel):
    name: str
    price: float
    is_offer: bool | None = None


@app.get("/")
def read_root():
    return {"message": "Hello, World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: str | None = None):
    return {"item id": item_id, "query": q}


@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    return {"item_name": item.name, "item_id": item_id}


@app.post("/stripe-webhook")
async def stripe_webhook(request: Request):
    payload = await request.body()

    print(to_dict(payload))

    return {"received": True}


get_ws_route(app)
