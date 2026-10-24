import json
import random
import string


def lambda_handler(event, context):
    custom = getattr(getattr(context, "client_context", None), "custom", None) or {}
    full_name = custom.get("bedrockAgentCoreToolName", "")
    tool_name = full_name.split("___")[-1]

    if tool_name == "initiate_refund":
        result = {
            "refund_id": "REF-" + "".join(
                random.choices(string.ascii_uppercase + string.digits, k=8)
            ),
            "order_id": event.get("order_id", "ORD-001"),
            "status": "APPROVED",
            "amount": event.get("amount") or 139.99,
            "message": "Demo refund approved. No real payment was processed."
        }
    elif tool_name == "check_refund_status":
        result = {
            "refund_id": event.get("refund_id"),
            "status": "DEMO_PENDING",
            "message": "Demo refund status retrieved successfully."
        }
    elif tool_name == "get_return_label":
        order_id = event.get("order_id")
        result = {
            "order_id": order_id,
            "label_status": "DEMO_READY",
            "tracking_number": "DEMO-TRACK-1001",
            "message": "Demo return label generated; no real shipment was booked."
        }
    else:
        return {"error": f"Unsupported tool: {tool_name}"}

    return {
        "content": [
            {"type": "text", "text": json.dumps(result)}
        ]
    }
