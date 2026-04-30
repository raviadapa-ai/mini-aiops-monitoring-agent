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