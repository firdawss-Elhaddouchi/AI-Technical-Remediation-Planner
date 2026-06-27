import json

# Flexible and easily maintainable priority configuration
PRIORITY_CONFIG = {
    "Hardcoded Secrets": {"impact": 5, "effort": 1},
    "SQL Injection": {"impact": 5, "effort": 3},
    "Vulnerable Dependencies": {"impact": 5, "effort": 2},
    "Missing Rate Limiting": {"impact": 4, "effort": 2},
    "Weak Cryptography": {"impact": 4, "effort": 2},
    "Broken Object Level Authorization": {"impact": 4, "effort": 3},
    "Missing Index": {"impact": 4, "effort": 3},
    "N+1 Query Deficit": {"impact": 4, "effort": 3},
    "Monolithic File Anti-Pattern": {"impact": 4, "effort": 5},
    "Low Test Coverage": {"impact": 4, "effort": 5},
    "Missing CI/CD Pipelines": {"impact": 4, "effort": 3},
    "Permissive CORS Policy": {"impact": 3, "effort": 1},
    "Absolute Paths Usage": {"impact": 3, "effort": 1},
    "Missing Connection Pooling": {"impact": 3, "effort": 1},
    "Missing Cache Layer": {"impact": 3, "effort": 3},
    "Missing ACID Transactions": {"impact": 3, "effort": 3},
    "Missing Containerization": {"impact": 3, "effort": 3}
}

def load_audit_report(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)

def calculate_priority_metrics(findings):
    """
    Calculate the Priority Score and rank findings deterministically
    before sending them to the LLM.
    """
    for finding in findings:
        issue_type = finding["issue_type"]

        # Retrieve the predefined metrics from the configuration.
        # If the issue type is not found, fall back to the default values (1, 1).
        metrics = PRIORITY_CONFIG.get(issue_type, {"impact": 1, "effort": 1})

        impact = metrics["impact"]
        effort = metrics["effort"]
        # Higher impact and lower implementation effort increase remediation priority.
        score = round(impact / effort, 2)

        finding["priority_metrics"] = {
            "impact": impact,
            "effort": effort,
            "priority_score": score
        }

    # Automatically sort findings by descending Priority Score
    findings.sort(key=lambda x: x["priority_metrics"]["priority_score"], reverse=True)

    return findings