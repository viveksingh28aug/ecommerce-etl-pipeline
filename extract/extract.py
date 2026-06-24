import pandas as pd
import logging


def extract_data():

    users = pd.read_csv("data/users.csv")
    products = pd.read_csv("data/products.csv")
    purchases = pd.read_csv("data/purchases.csv")
    sessions = pd.read_csv("data/sessions.csv")
    interactions = pd.read_csv("data/interactions.csv")
    reviews = pd.read_csv("data/reviews.csv")

    logging.info("Data Extracted Successfully")

    return {
        "users": users,
        "products": products,
        "purchases": purchases,
        "sessions": sessions,
        "interactions": interactions,
        "reviews": reviews
    }