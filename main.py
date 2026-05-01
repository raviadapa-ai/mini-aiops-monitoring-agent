from ingestion.log_reader import read_logs
from processing.parser import parse_log
from processing.metrics import compute_metrics
from alerting.alerts import check_alerts
from processing.spike_detection import detect_spikes, merge_spikes
from analysis.root_cause import find_root_cause, summarize_root_causes
from analysis.llm_insight import generate_incident_report
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
    raw_spikes = detect_spikes(parsed_logs)
    spikes = merge_spikes(raw_spikes)
    rca = find_root_cause(parsed_logs, spikes)
    summary = summarize_root_causes(rca)
    llm_report = generate_incident_report(summary, spikes, rca)

    return {
        "metrics": metrics,
        "alerts": alerts,
        "spikes": spikes,
        "root_cause" : rca,
        "summary" : summary,
        "llm_report" : llm_report
   } 
if __name__ == "__main__":
    run_pipeline()