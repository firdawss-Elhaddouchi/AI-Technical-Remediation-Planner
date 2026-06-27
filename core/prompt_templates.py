import json

SYSTEM_PROMPT = """
You are a senior software architect.

You will receive a prioritized list of technical audit findings.

The priority order has already been calculated and must not be modified.

For each finding, generate:

- remediation
- estimated_days
- dependencies
- backlog_item

Return ONLY valid JSON using this structure:

{
  "remediations": [
    {
      "id": "",
      "remediation": "",
      "estimated_days": 0,
      "dependencies": [],
      "backlog_item": ""
    }
  ]
}
"""


def generate_user_prompt(findings):
    simplified = []

    for finding in findings:
        simplified.append({
            "id": finding["id"],
            "domain": finding["domain"],
            "issue_type": finding["issue_type"],
            "description": finding["description"],
            "priority_score": finding["priority_metrics"]["priority_score"]
        })

    return (
        "Generate the remediation plan for the following prioritized audit findings:\n\n"
        + json.dumps(simplified, indent=2, ensure_ascii=False)
    )