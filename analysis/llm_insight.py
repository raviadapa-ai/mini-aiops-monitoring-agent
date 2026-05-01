import os
import textwrap
from dotenv import load_dotenv

load_dotenv()

def generate_incident_report(summary, spikes, root_cause):

    prompt = f"""
You are an AIOps incident analyst.

SUMMARY:
{summary}

SPIKES:
{spikes}

ROOT CAUSE:
{root_cause}

Generate:
1. What happened
2. Root cause
3. Impact
4. Recommendation
Keep it concise and technical.
"""

    # -----------------------------
    # MOCK RESPONSE (safe fallback)
    # -----------------------------
    brief_text = (
        "Between 10:00 and 10:04, multiple error spikes were observed across server1, "
        "server2, and server3. The majority of failures were related to database timeouts, "
        "indicating potential DB saturation or connection pool exhaustion."
    )

    # Normalize only (remove extra spaces/newlines)
    brief_text = " ".join(brief_text.split())

    return {
        "what_happened": "System experienced repeated database-related failures causing multiple error spikes.",
        "root_cause": "Database instability (timeouts and connection issues)",
        "impact": "Increased error rate and degraded API performance",
        "recommendation": "Check DB connection pool, optimize queries, and scale database resources",
        "brief": brief_text   # 👈 clean paragraph output
    }

    # -----------------------------
    # REAL LLM (optional)
    # -----------------------------
    """
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content
    """