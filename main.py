from ingestion.log_reader import read_logs
from processing.parser import parse_log
from processing.metrics import compute_metrics
from alerting.alerts import check_alerts
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
LOG_PATH = os.path.join(BASE_DIR, "data", "logs.txt")

def run_pipeline():
    logs = read_logs(LOG_PATH)
    parsed_logs = []
    for log in logs:
        parsed = parse_log(log.strip())
        if parsed:
            parsed_logs.append(parsed)

    metrics = compute_metrics(parsed_logs)
    alerts = check_alerts(metrics)

    return {
        "metrics": metrics,
        "alerts": alerts
   } 
if __name__ == "__main__":
    run_pipeline()