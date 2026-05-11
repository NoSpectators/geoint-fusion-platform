from warehouse.db_connection import get_engine
import pandas as pd


def compute_risk_scores():

    engine = get_engine()

    query = """
    SELECT 
        t.entity_id,
        t.entity_type,
        COUNT(i.event_id) AS event_count,
        AVG(i.confidence_score) AS avg_confidence
    FROM tracked_entities t
    JOIN intel_events i
        ON t.entity_id = i.entity_id
    GROUP BY t.entity_id, t.entity_type;
    """

    df = pd.read_sql(query, engine)

    # Normalize components into a simple risk model
    df["event_score"] = df["event_count"] / df["event_count"].max()
    df["confidence_score"] = 1 - df["avg_confidence"]  # lower confidence = higher risk

    df["risk_score"] = (
        0.6 * df["event_score"] +
        0.4 * df["confidence_score"]
    )

    df["risk_score"] = df["risk_score"].round(3)

    return df


def main():

    df = compute_risk_scores()

    print("\nTop Risk Entities:\n")

    print(
        df.sort_values("risk_score", ascending=False)
          .head(10)
    )


if __name__ == "__main__":
    main()