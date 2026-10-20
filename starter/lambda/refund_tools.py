import json


def lambda_handler(event, context):
    custom = context.client_context.custom
    full_name = custom.get("bedrockAgentCoreToolName", "")
    tool_name = full_name.split("___")[-1]

    if tool_name == "initiate_refund":
        result = {
            "status": "DEMO_CREATED",
            "order_id": event.get("order_id"),
            "amount": event.get("amount"),
            "reason": event.get("reason"),
            "message": "Demo refund request created; no real payment was processed."
        }
    elif tool_name == "check_refund_status":
        result = {
            "refund_id": event.get("refund_id"),
            "status": "DEMO_PENDING",
            "message": "Demo refund status retrieved successfully."
        }
    elif tool_name == "get_return_label":
        result = {
            "order_id": event.get("order_id"),
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
