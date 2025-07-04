from pandera import Column, DataFrameSchema, Check

brand_comparison_schema = DataFrameSchema({
    "product_type": Column(str, nullable=False),
    "brand_A": Column(str, nullable=False),
    "price_A": Column(float, Check.gt(0), nullable=False),
    "rating_A": Column(float, Check.in_range(0, 5), nullable=True),
    "num_ratings_A": Column(int, Check.ge(0), nullable=True),

    "brand_B": Column(str, nullable=False),
    "price_B": Column(float, Check.gt(0), nullable=False),
    "rating_B": Column(float, Check.in_range(0, 5), nullable=True),
    "num_ratings_B": Column(int, Check.ge(0), nullable=True),

    "price_difference": Column(float, nullable=True),
    "price_diff_percentage": Column(float, nullable=True),
    "rating_variance": Column(float, nullable=True),
    "better_brand_by_rating": Column(str, Check.isin(["A", "B", "Equal"]), nullable=True),
})

//ingestion script
import pandas as pd
from schemas.brand_comparison_schema import brand_comparison_schema

def ingest_brand_comparison(file_path):
    print(f"Ingesting file: {file_path}")
    df = pd.read_excel(file_path)
    validated_df = brand_comparison_schema.validate(df)
    validated_df.to_csv("staging/brand_comparison_clean.csv", index=False)
    print("Brand Comparison Data Validated and Saved.")
//
