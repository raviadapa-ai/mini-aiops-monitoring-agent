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

def normalize_error(msg):
    msg = msg.lower()

    if "timeout" in msg:
        return "DB Timeout"
    if "connection" in msg:
        return "DB Connection Issue"
    if "lock" in msg:
        return "DB Lock Issue"

    return "Other"

def summarize_root_causes(rca_results):
    normalized = [normalize_error(r["root_cause"]) for r in rca_results]

    counts = Counter(normalized)
    top_issue = counts.most_common(1)[0]

    return {
        "dominant_issue": top_issue[0],
        "occurrences": top_issue[1],
        "all_issues": counts
    }