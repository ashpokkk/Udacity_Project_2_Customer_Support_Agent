from strands.models.bedrock import BedrockModel
import os


def load_model() -> BedrockModel:
    """Get Bedrock model client using IAM credentials."""
    return BedrockModel(
        model_id="us.amazon.nova-2-lite-v1:0",
        region_name=os.getenv("AWS_REGION", "us-east-1"),
    )
