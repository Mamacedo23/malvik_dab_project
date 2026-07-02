# trest_citibike_utils.py
import os
import sys

# Run the tests from the root directory
sys.path.append(os.getcwd())

import datetime
from src.utils.datetime_utils import timestamp_to_date_col
from src.dab_project.main import session_function
# from pyspark.sql import SparkSession

def test_timestamp_to_date_col(spark):
    
    # Create a SparkSession
    data = [(datetime.datetime(2025, 4, 10, 10, 30, 0),)]
    schema = "ride_timestamp timestamp"    
    df = spark.createDataFrame(data, schema=schema)
    
    # Use the utility to add a date column
    result_df = timestamp_to_date_col(spark, df, "ride_timestamp", "ride_date")
    
    # Assert that the new column has the correct date values
    row = result_df.select("ride_date").first()
    
    expected_date = datetime.date(2025, 4, 10) # Expected: 2025-04-10
    
    assert row["ride_date"] == expected_date