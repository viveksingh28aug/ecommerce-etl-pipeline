import logging


def run_quality_checks(
        fact_sales,
        mismatch_count):

    null_user_ids = (
        fact_sales["user_id"]
        .isnull()
        .sum()
    )

    null_product_ids = (
        fact_sales["product_id"]
        .isnull()
        .sum()
    )

    duplicate_purchases = (
        fact_sales["purchase_id"]
        .duplicated()
        .sum()
    )

    negative_quantities = (
        fact_sales["quantity"] < 0
    ).sum()

    print("\n===== DATA QUALITY REPORT =====")

    print(
        "Null User IDs:",
        null_user_ids
    )

    print(
        "Null Product IDs:",
        null_product_ids
    )

    print(
        "Duplicate Purchases:",
        duplicate_purchases
    )

    print(
        "Negative Quantities:",
        negative_quantities
    )

    print(
        "Revenue Mismatches:",
        mismatch_count
    )

    logging.info(
        f"Null User IDs: {null_user_ids}"
    )

    logging.info(
        f"Null Product IDs: {null_product_ids}"
    )

    logging.info(
        f"Duplicate Purchases: {duplicate_purchases}"
    )

    logging.info(
        f"Negative Quantities: {negative_quantities}"
    )

    logging.info(
        f"Revenue Mismatches: {mismatch_count}"
    )