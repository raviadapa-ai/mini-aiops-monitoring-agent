def check_alerts(metrics):
    alerts = []

    if metrics["error_rate"] > 5:
        alerts.append("⚠️ Moderate error rate")

    if metrics["error_rate"] > 15:
        alerts.append("🚨 High error rate")

    if metrics["avg_latency"] > 120:
        alerts.append("⚠️ High latency")

    return alerts