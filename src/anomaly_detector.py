# src/anomaly_detector.py
def detect(self, record):
    reasons = []

    if record["response_time_ms"] > self.response_time_threshold:
        reasons.append("High response time")

    if record["cpu_percent"] > self.cpu_threshold:
        reasons.append("High CPU utilization")

    if record["memory_percent"] > self.memory_threshold:
        reasons.append("High memory utilization")

    if record.get("log_level", "").upper() in {"WARNING", "ERROR"}:
        reasons.append("Error log detected")

    if not reasons:
        return None

    return {
        "timestamp": record["timestamp"],
        "service": record["service"],
        "type": "ANOMALY",
        "reasons": reasons,
        "source": record
    }
