import re

def parse_log(line):
    pattern = r'(\S+ \S+) (\w+) (\w+) (.+)'
    match = re.match(pattern, line)

    if not match:
        return None

    timestamp, level, server, message = match.groups()

    latency = None
    if "ms" in message:
        latency_match = re.search(r'(\d+)ms', message)
        if latency_match:
            latency = int(latency_match.group(1))

    return {
        "timestamp": timestamp,
        "level": level,
        "server": server,
        "message": message,
        "latency": latency
    }