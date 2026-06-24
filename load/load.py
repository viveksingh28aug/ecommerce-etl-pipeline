import logging
from config.config import engine


def load_data(
        fact_sales,
        dim_users,
        dim_products):

    fact_sales.to_sql(
        "fact_sales",
        engine,
        if_exists="append",
        index=False
    )

    dim_users.to_sql(
        "dim_users",
        engine,
        if_exists="append",
        index=False
    )

    dim_products.to_sql(
        "dim_products",
        engine,
        if_exists="append",
        index=False
    )

    logging.info(
        f"fact_sales loaded: {len(fact_sales)} rows"
    )

    logging.info(
        f"dim_users loaded: {len(dim_users)} rows"
    )

    logging.info(
        f"dim_products loaded: {len(dim_products)} rows"
    )