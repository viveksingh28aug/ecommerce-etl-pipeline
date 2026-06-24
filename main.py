import logging

from extract.extract import extract_data
from transform.transform import transform_data
from quality.quality_checks import run_quality_checks
from load.load import load_data


logging.basicConfig(
    filename="logs/etl.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logging.info("ETL Started")


def main():

    data = extract_data()

    (
        dim_users,
        dim_products,
        fact_sales,
        mismatch_count
    ) = transform_data(data)

    run_quality_checks(
        fact_sales,
        mismatch_count
    )

    load_data(
        fact_sales,
        dim_users,
        dim_products
    )

    print("\n===== ETL SUMMARY =====")

    print(
        f"dim_users loaded: {len(dim_users)}"
    )

    print(
        f"dim_products loaded: {len(dim_products)}"
    )

    print(
        f"fact_sales loaded: {len(fact_sales)}"
    )

    print(
        "Star Schema created successfully"
    )

    logging.info(
        "ETL Completed Successfully"
    )


if __name__ == "__main__":
    main()