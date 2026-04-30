from collections import Counter

def find_root_cause(parsed_logs, spikes):
    results = []

    for spike in spikes:
        window_logs = [
            log for log in parsed_logs
            if spike["start"] <= log["timestamp"] <= spike["end"]
        ]

        messages = [log["message"] for log in window_logs if log["level"] in ["ERROR", "CRITICAL"]]
        servers = [log["server"] for log in window_logs]

        if messages:
            top_error = Counter(messages).most_common(1)[0][0]
        else:
            top_error = "Unknown"

        if servers:
            top_server = Counter(servers).most_common(1)[0][0]
        else:
            top_server = "Unknown"

        results.append({
            "start": spike["start"],
            "end": spike["end"],
            "root_cause": top_error,
            "affected_server": top_server
        })

    return results