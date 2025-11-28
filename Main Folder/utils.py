import pandas as pd
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
df_lux = os.path.join(BASE_DIR, "luxury_package.csv")
df_five = os.path.join(BASE_DIR, "Five_Star_Package.csv")

import pandas as pd

def load_packages():

    df_lux = pd.read_csv("luxury_package.csv")
    df_five = pd.read_csv("Five_Star_Package.csv")

    df_lux = df_lux.fillna("–")
    df_five = df_five.fillna("–")

    for df in (df_lux, df_five):
        df["rating"] = pd.to_numeric(df["rating"], errors="coerce")
        df["num_reviews"] = pd.to_numeric(df["num_reviews"], errors="coerce")

    return df_lux, df_five

def clean_df(df):
    df = df.copy()
    df = df.drop_duplicates()
    df = df.fillna("-")
    return df

def lisbon_attr():
    df = pd.read_csv("lisbon_attractions.csv")

    df = df.dropna(subset=["rating", "num_reviews"])
    df = df[df["num_reviews"].astype(int) >= 10]
    df = clean_df(df)

    return df

def lisbon_hotels():
    df = pd.read_csv("lisbon_hotels.csv")
    df = df.dropna(subset=["rating", "num_reviews"])
    df = clean_df(df)
    return df

def lisbon_rest():
    df = pd.read_csv("lisbon_restaurants.csv")
    df = df.dropna(subset=["rating", "num_reviews"])
    df = clean_df(df)
    return df

def lux_a():
    df = pd.read_csv("luxury_attractions.csv")
    df = df.dropna(subset=["rating", "num_reviews"])
    df = clean_df(df)
    return df
                   