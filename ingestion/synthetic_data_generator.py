import random
from datetime import datetime, timedelta

EVENT_TYPES = [
    "movement",
    "signal_detected",
    "border_crossing",
    "satellite_ping",
    "communication_intercept"
]

SOURCE_SYSTEMS = [
    "UAV",
    "SAT",
    "SIGINT",
    "OSINT"
]


def generate_event():

    return {
        "event_time": datetime.utcnow() - timedelta(
            minutes=random.randint(0, 10000)
        ),

        "event_type": random.choice(EVENT_TYPES),

        "entity_id": f"ENT-{random.randint(1000, 9999)}",

        "latitude": round(random.uniform(-90, 90), 6),

        "longitude": round(random.uniform(-180, 180), 6),

        "source_system": random.choice(SOURCE_SYSTEMS),

        "confidence_score": round(random.uniform(0.40, 0.99), 2)
    }


def generate_batch(n=100):

    return [generate_event() for _ in range(n)]