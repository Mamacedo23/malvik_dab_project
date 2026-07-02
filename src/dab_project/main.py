def session_function():
    try:
        from databricks.connect import DatabricksSession
        spark = DatabricksSession.builder.getOrCreate()
    except ImportError:
        try:
            from pyspark.sql import SparkSession
            spark = SparkSession.builder.getOrCreate()
        except ImportError:
            raise ImportError("Neither DatabricksSession nor SparkSession could be imported")
    return spark