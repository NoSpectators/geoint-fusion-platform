import random
from datetime import datetime, timedelta


ENTITY_TYPES = [
    "vehicle",
    "person",
    "aircraft",
    "vessel",
    "device"
]


REGIONS = [
    "Eastern Europe",
    "Middle East",
    "South China Sea",
    "North Africa",
    "Arctic Zone"
]


def generate_entities(n=50):

    entities = []

    for i in range(n):

        entity_id = f"ENT-{1000 + i}"

        first_seen = datetime.utcnow() - timedelta(
            days=random.randint(30, 365)
        )

        last_seen = datetime.utcnow() - timedelta(
            hours=random.randint(1, 72)
        )

        risk_score = round(random.uniform(0.1, 0.95), 2)

        entity = {
            "entity_id": entity_id,
            "entity_type": random.choice(ENTITY_TYPES),
            "first_seen": first_seen,
            "last_seen": last_seen,
            "risk_score": risk_score
        }

        entities.append(entity)

    return entities


def generate_geospatial_activity(entities):

    activities = []

    for entity in entities:

        for _ in range(random.randint(3, 10)):

            activity = {
                "entity_id": entity["entity_id"],
                "region": random.choice(REGIONS),
                "activity_level": round(random.uniform(0.1, 1.0), 2),
                "timestamp": datetime.utcnow() - timedelta(
                    hours=random.randint(1, 500)
                )
            }

            activities.append(activity)

    return activities