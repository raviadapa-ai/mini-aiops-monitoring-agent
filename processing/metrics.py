def compute_metrics(parsed_logs):
    total = len(parsed_logs)
    errors = sum(1 for log in parsed_logs if log["level"] in ["ERROR", "CRITICAL"])

    latencies = [log["latency"] for log in parsed_logs if log["latency"]]

    avg_latency = sum(latencies)/len(latencies) if latencies else 0

    error_rate = (errors / total) * 100 if total else 0

    return {
        "total_logs": total,
        "error_rate": error_rate,
        "avg_latency": avg_latency
    }