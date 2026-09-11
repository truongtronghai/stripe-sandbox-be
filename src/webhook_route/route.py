import uuid
from datetime import UTC, datetime

from fastapi import FastAPI, Request

from src.db.get_db import get_dynamodb
from src.db.subscription_table import ensure_subscription_table
from utils.converters.raw_bytes_literal import to_dict


def get_webhook_route(app: FastAPI):
    @app.post("/stripe-webhook")
    async def stripe_webhook(request: Request):
        payload = await request.body()

        stripe_data = to_dict(payload)

        event_data = stripe_data.get("data") or {}
        event_object = event_data.get("object") or {}

        if stripe_data.get("type") == "invoice.payment_succeeded":
            # print(
            #     f"Payment was successful! Account name: {event_object.get('account_name')}, Customer: {event_object.get('customer')}, Amount: {event_object.get('amount_paid')}"
            # )

            table = None
            try:
                db = get_dynamodb()
                table = ensure_subscription_table(db)
            except Exception as e:
                print(f"Webhook connects to DB failed: {type(e).__name__} {e}")
                raise

            try:
                table.put_item(
                    Item={
                        "subscriptionId": str(uuid.uuid4()),
                        "planId": "",
                        "email": "truongtronghai@gmail.com",
                        "created_at": datetime.now(UTC).isoformat(),
                        "account_name": event_object.get("account_name"),
                        "customerId": event_object.get("customer"),
                        "amount_paid": event_object.get("amount_paid"),
                    }
                )
            except Exception as e:
                print(f"Webhook put_item failed: {type(e).__name__} {e}")
                raise

        return {"received": True}
