def analyze_threat(alert: dict) -> dict:
    severity = alert.get("severity", "Unknown")
    alert_type = alert.get("alert_type", "Unknown Alert")

    return {
        "alert_type": alert_type,
        "severity": severity,
        "analysis": f"Detected a {severity} severity {alert_type}.",
        "recommendation": "Review the source IP and affected system."
    }

if __name__ == "__main__":
    sample_alert = {
        "alert_type": "SSH Brute Force",
        "severity": "High"
    }

    print(analyze_threat(sample_alert))