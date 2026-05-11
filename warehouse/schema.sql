CREATE TABLE intel_events (
    event_id SERIAL PRIMARY KEY,
    event_time TIMESTAMP,
    event_type VARCHAR(50),
    entity_id VARCHAR(100),
    latitude DOUBLE PRECISION,
    longitude DOUBLE PRECISION,
    source_system VARCHAR(100),
    confidence_score FLOAT
);

CREATE TABLE tracked_entities (
    entity_id VARCHAR(100) PRIMARY KEY,
    entity_type VARCHAR(50),
    first_seen TIMESTAMP,
    last_seen TIMESTAMP,
    risk_score FLOAT
);

CREATE TABLE geospatial_activity (
    activity_id SERIAL PRIMARY KEY,
    entity_id VARCHAR(100),
    region VARCHAR(100),
    activity_level FLOAT,
    timestamp TIMESTAMP
);