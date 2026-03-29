import pandas as pd

def detect_anomalies(df):
    anomalies = []

    #1. Excessive Login Attempts
    failed = df[df['action'] == 'auth.fail']
    failed_counts = failed.groupby('uid').size()

    for user, count in failed_counts.items():
        if count > 10:
            user_data = failed[failed['uid'] == user]

            anomalies.append({
                "user_id": user,
                "anomaly_type": "excessive_failed_logins",
                "severity": "warning",
                "start_time": user_data['ts'].min(),
                "end_time": user_data['ts'].max(),
                "reason": f"{count} failed login attempts"
            })

    #  2. High Activity Spike (INFO)
    activity_counts = df.groupby('uid').size()

    for user, count in activity_counts.items():
        if count > 200:
            user_data = df[df['uid'] == user]

            anomalies.append({
                "user_id": user,
                "anomaly_type": "high_activity_spike",
                "severity": "info",
                "start_time": user_data['ts'].min(),
                "end_time": user_data['ts'].max(),
                "reason": f"{count} actions detected"
            })

    # 3. Multiple IP Usage (CRITICAL)
    ip_counts = df.groupby('uid')['src_ip'].nunique()

    for user, count in ip_counts.items():
        if count > 5:
            user_data = df[df['uid'] == user]

            anomalies.append({
                "user_id": user,
                "anomaly_type": "multiple_ip_access",
                "severity": "critical",
                "start_time": user_data['ts'].min(),
                "end_time": user_data['ts'].max(),
                "reason": f"User accessed from {count} different IPs"
            })

    # Convert to DataFrame
    return pd.DataFrame(anomalies)