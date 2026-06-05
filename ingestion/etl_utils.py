import pandas as pd
from sqlalchemy import create_engine
from datetime import datetime

engine = create_engine(
    "postgresql+psycopg2://postgres:postgres@localhost:5432/flight_analytics"
)


def write_audit_log(
    source_name,
    records_loaded,
    start_time,
    end_time,
    status,
    error_message=None
):

    log_df = pd.DataFrame([{
        "source_name": source_name,
        "records_loaded": records_loaded,
        "start_time": start_time,
        "end_time": end_time,
        "status": status,
        "error_message": error_message
    }])

    log_df.to_sql(
        "etl_execution_log",
        engine,
        schema="audit",
        if_exists="append",
        index=False
    )


def load_csv_to_postgres(
    source_file,
    target_schema,
    target_table
):

    start_time = datetime.now()

    try:

        df = pd.read_csv(source_file)

        df["source_file"] = source_file.split("/")[-1]
        df["load_timestamp"] = datetime.now()

        df.to_sql(
            target_table,
            engine,
            schema=target_schema,
            if_exists="append",
            index=False
        )

        end_time = datetime.now()

        write_audit_log(
            source_name=source_file,
            records_loaded=len(df),
            start_time=start_time,
            end_time=end_time,
            status="SUCCESS"
        )

        print(f"Loaded {len(df)} records into {target_schema}.{target_table}")

    except Exception as e:

        end_time = datetime.now()

        write_audit_log(
            source_name=source_file,
            records_loaded=0,
            start_time=start_time,
            end_time=end_time,
            status="FAILED",
            error_message=str(e)
        )

        raise


def load_large_csv_to_postgres(
    source_file,
    target_schema,
    target_table,
    chunksize=50000
):

    start_time = datetime.now()

    total_rows_loaded = 0

    try:

        for chunk in pd.read_csv(
            source_file,
            chunksize=chunksize
        ):
            # Remove useless index column
            if "Unnamed: 0" in chunk.columns:
                chunk = chunk.drop(columns=["Unnamed: 0"])

            # Standardize column names
            chunk.columns = [col.lower() for col in chunk.columns]

            chunk["source_file"] = source_file.split("/")[-1]
            chunk["load_timestamp"] = datetime.now()

            chunk.to_sql(
                target_table,
                engine,
                schema=target_schema,
                if_exists="append",
                index=False,
                method="multi"
            )

            total_rows_loaded += len(chunk)

            print(
                f"Loaded {total_rows_loaded:,} rows..."
            )

        end_time = datetime.now()

        write_audit_log(
            source_name=source_file,
            records_loaded=total_rows_loaded,
            start_time=start_time,
            end_time=end_time,
            status="SUCCESS"
        )

        print(
            f"\nCompleted load of {total_rows_loaded:,} rows"
        )

    except Exception as e:

        import traceback

        end_time = datetime.now()

        print("\nFULL ERROR:")
        traceback.print_exc()

        write_audit_log(
            source_name=source_file,
            records_loaded=total_rows_loaded,
            start_time=start_time,
            end_time=end_time,
            status="FAILED",
            error_message=traceback.format_exc()
        )

        raise