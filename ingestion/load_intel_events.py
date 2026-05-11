import pandas as pd

from ingestion.synthetic_data_generator import generate_batch
from warehouse.db_connection import get_engine


def main():

    print("Generating synthetic GEOINT events...")

    events = generate_batch(500)

    df = pd.DataFrame(events)

    print(df.head())

    engine = get_engine()

    print("Loading events into PostgreSQL...")

    df.to_sql(
        "intel_events",
        engine,
        if_exists="append",
        index=False
    )

    print(f"Inserted {len(df)} records successfully!")


if __name__ == "__main__":
    main()