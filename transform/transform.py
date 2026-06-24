import logging
import pandas as pd


def transform_data(data):

    users = data["users"]
    products = data["products"]
    purchases = data["purchases"]
    sessions = data["sessions"]
    interactions = data["interactions"]
    reviews = data["reviews"]

    users = users.drop_duplicates()
    products = products.drop_duplicates()
    purchases = purchases.drop_duplicates()

    users["signup_date"] = pd.to_datetime(users["signup_date"])
    products["date_added"] = pd.to_datetime(products["date_added"])
    purchases["order_date"] = pd.to_datetime(purchases["order_date"])
    reviews["review_date"] = pd.to_datetime(reviews["review_date"])
    interactions["timestamp"] = pd.to_datetime(interactions["timestamp"])
    sessions["start_time"] = pd.to_datetime(sessions["start_time"])

    users.fillna(0, inplace=True)
    products.fillna(0, inplace=True)

    dim_users = users[
        [
            "user_id",
            "age",
            "gender",
            "country",
            "city",
            "loyalty_tier"
        ]
    ].drop_duplicates()

    dim_products = products[
        [
            "product_id",
            "product_name",
            "category",
            "subcategory",
            "brand"
        ]
    ].drop_duplicates()

    sales = purchases.merge(
        dim_users,
        on="user_id",
        how="left"
    )

    sales = sales.merge(
        dim_products,
        on="product_id",
        how="left"
    )

    sales["calculated_revenue"] = (
        sales["quantity"] *
        sales["unit_price"]
    )

    mismatch_count = (
        sales["total_amount"] !=
        sales["calculated_revenue"]
    ).sum()

    logging.info(
        f"Revenue Mismatches: {mismatch_count}"
    )

    fact_sales = sales[
        [
            "purchase_id",
            "order_id",
            "user_id",
            "product_id",
            "session_id",
            "quantity",
            "unit_price",
            "total_amount",
            "order_date"
        ]
    ]

    return (
        dim_users,
        dim_products,
        fact_sales,
        mismatch_count
    )