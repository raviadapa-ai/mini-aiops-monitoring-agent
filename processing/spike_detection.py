from collections import deque

def detect_spikes(parsed_logs, window_size=5, threshold=20):
    """
    Detect error spikes in sliding windows
    window_size = number of logs per window
    threshold = error % to trigger spike
    """

    spikes = []
    window = deque()

    for log in parsed_logs:
        window.append(log)

        if len(window) > window_size:
            window.popleft()

        if len(window) == window_size:
            total = len(window)
            errors = sum(1 for l in window if l["level"] in ["ERROR", "CRITICAL"])

            error_rate = (errors / total) * 100
            print("Window error rate:", error_rate)
            if error_rate > threshold:
                spikes.append({
                    "start": window[0]["timestamp"],
                    "end": window[-1]["timestamp"],
                    "error_rate": round(error_rate, 2)
                })

    return spikes

def merge_spikes(spikes):
    if not spikes:
        return []

    merged = []
    current = spikes[0]

    for next_spike in spikes[1:]:
        if next_spike["start"] <= current["end"]:
            # overlap → merge
            current["end"] = max(current["end"], next_spike["end"])
            current["error_rate"] = max(current["error_rate"], next_spike["error_rate"])
        else:
            merged.append(current)
            current = next_spike

    merged.append(current)
    return merged