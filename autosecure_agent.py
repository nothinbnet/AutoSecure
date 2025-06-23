
import json

# Simulated user access data
user_access_data = {
    "user_1": {"email": "jane.doe@company.com", "roles": ["admin", "billing"], "compliance_flags": ["excessive_privileges"]},
    "user_2": {"email": "john.smith@company.com", "roles": ["read-only"], "compliance_flags": []},
}

# Simulated device compliance data
device_compliance_data = {
    "jane.doe@company.com": {"encryption": True, "firewall": True, "updates": False},
    "john.smith@company.com": {"encryption": True, "firewall": True, "updates": True},
}

# Slack Bot simulated response logic
def slack_bot_response(user_email):
    compliance = device_compliance_data.get(user_email, {})
    if not compliance:
        return f"No device compliance data found for {user_email}."

    non_compliant = [k for k, v in compliance.items() if not v]
    if non_compliant:
        return f"⚠️ Device for {user_email} is non-compliant on: {', '.join(non_compliant)}"
    return f"✅ Device for {user_email} is fully compliant."

# Access Review Agent logic
def access_review(user_id):
    user_data = user_access_data.get(user_id)
    if not user_data:
        return f"No access data found for {user_id}."

    response = {
        "email": user_data["email"],
        "roles": user_data["roles"],
        "compliance_flags": user_data["compliance_flags"],
        "status": "⚠️ Review needed" if user_data["compliance_flags"] else "✅ Access in compliance"
    }
    return json.dumps(response, indent=2)

# Generate a sample audit report
def generate_audit_report():
    report = {
        "device_compliance_summary": device_compliance_data,
        "access_review_summary": user_access_data,
    }
    return json.dumps(report, indent=2)

# Sample usage
if __name__ == "__main__":
    print("Slack Bot Response for jane.doe@company.com:")
    print(slack_bot_response("jane.doe@company.com"))
    print("\nAccess Review for user_1:")
    print(access_review("user_1"))
    print("\nAudit Summary Report:")
    print(generate_audit_report())
