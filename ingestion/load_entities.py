import pandas as pd

from ingestion.entity_simulator import (
    generate_entities,
    generate_geospatial_activity
)

from warehouse.db_connection import get_engine


def main():

    print("Generating tracked entities...")

    entities = generate_entities(50)

    entities_df = pd.DataFrame(entities)

    print(entities_df.head())

    print("Generating geospatial activity...")

    activities = generate_geospatial_activity(entities)

    activities_df = pd.DataFrame(activities)

    print(activities_df.head())

    engine = get_engine()

    print("Loading tracked_entities table...")

    entities_df.to_sql(
        "tracked_entities",
        engine,
        if_exists="append",
        index=False
    )

    print("Loading geospatial_activity table...")

    activities_df.to_sql(
        "geospatial_activity",
        engine,
        if_exists="append",
        index=False
    )

    print("Entity and activity load complete!")


if __name__ == "__main__":
    main()