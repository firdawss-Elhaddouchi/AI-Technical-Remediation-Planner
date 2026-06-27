import json 
from core.config import API_KEY, MODEL_NAME
from core.prompt_templates import (
    SYSTEM_PROMPT,
    generate_user_prompt
)

from google import genai

from core.prompt_templates import (
    SYSTEM_PROMPT,
    generate_user_prompt
)


client = genai.Client(api_key=API_KEY)


def generate_remediation_plan(processed_findings):
    """
    Generate remediation plan using Gemini (new SDK)
    """

    prompt = f"""
{SYSTEM_PROMPT}

IMPORTANT:
Return ONLY valid JSON. No explanations. No markdown.

User Request:
{generate_user_prompt(processed_findings)}
"""

    response = client.models.generate_content(
        model= MODEL_NAME,
        contents=prompt
    )

    text = response.text.strip()

    if "```" in text:
        text = text.replace("```json", "").replace("```", "").strip()

    return json.loads(text)