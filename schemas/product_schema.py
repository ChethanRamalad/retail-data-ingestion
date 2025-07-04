import pandera as pa
from pandera import Column, DataFrameSchema, Check

product_schema = DataFrameSchema({
    "product_name": Column(str, nullable=False),
    "price": Column(float, Check.gt(0), nullable=False),
    "rating": Column(float, Check.in_range(0, 5), nullable=True),
    "url": Column(str, nullable=False),
    "category": Column(str, nullable=True),
    "brand": Column(str, nullable=True),
    "fabric": Column(str, nullable=True),
    "color": Column(str, nullable=True),
    "pattern": Column(str, nullable=True),
    "sleeve_type": Column(str, nullable=True),
    "neckline": Column(str, nullable=True),
    "occasion": Column(str, nullable=True),
    "fit": Column(str, nullable=True),
    "product_description": Column(str, nullable=True),
    "wash_care": Column(str, nullable=True),
    "origin": Column(str, nullable=True),
    "sku": Column(str, nullable=False),
    "size_availability": Column(str, nullable=True),
    "size_chart": Column(str, nullable=True),
})
