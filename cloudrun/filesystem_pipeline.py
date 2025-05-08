import dlt
from dlt.sources.filesystem import filesystem, read_csv_duckdb


def read_csv_with_duckdb() -> None:
    """Read CSV files using DuckDB and load them into BigQuery.

    This function reads CSV files from the configured bucket URL and loads them
    into BigQuery using dlt's DuckDB integration. It processes files in chunks
    of 1000 rows and includes headers.
    """
    try:

        pipeline = dlt.pipeline(
            pipeline_name="bigquery_ohio_voter_data",
            destination="bigquery",
        )

        # load all the CSV data, including headers
        voter_files = filesystem()
        # voter_files.apply_hints(incremental=dlt.sources.incremental("modification_date"))

        filesystem_pipe = voter_files | read_csv_duckdb(chunk_size=10000, header=True)
        # filesystem_pipe.apply_hints(incremental=dlt.sources.incremental("registration_date"))

        load_info = pipeline.run(
            filesystem_pipe,
            write_disposition={"disposition": "merge", "strategy": "upsert"},
            primary_key="SOS_VOTERID",
            dataset_name="cta_voter_files",
            table_name="ohio_voter_data",
        )

        print(f"Load info: {load_info}")
        print(f"Normalize info: {pipeline.last_trace.last_normalize_info}")

        return load_info
    except Exception as e:
        print(f"Error in read_csv_with_duckdb: {str(e)}")
        raise


if __name__ == "__main__":
    read_csv_with_duckdb()
