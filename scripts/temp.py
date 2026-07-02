from databricks.connect import DatabricksSession

spark = DatabricksSession.builder.serverless(True).getOrCreate()


spark.sql("SELECT 1").show()