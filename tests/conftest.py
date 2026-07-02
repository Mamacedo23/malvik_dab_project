import os
import sys
import pytest

# Force Spark's driver and worker subprocesses to use the same Python
# interpreter as the one running pytest (the venv's python). Without this,
# PySpark falls back to whatever "python"/"python3" resolves to on PATH,
# which can be a different, incompatible Python version and causes
# "Connection reset" errors when the driver and worker try to talk.
os.environ["PYSPARK_PYTHON"] = sys.executable
os.environ["PYSPARK_DRIVER_PYTHON"] = sys.executable

# Run the tests from the root directory
sys.path.append(os.getcwd())

@pytest.fixture(scope="session")
def spark():
    try:
        from databricks.connect import DatabricksSession
        spark = DatabricksSession.builder.getOrCreate()
    except:
        try:
            from pyspark.sql import SparkSession
            spark = SparkSession.builder.getOrCreate()
        except:
            raise ImportError("Neither DatabricksSession nor SparkSession could be imported")
    return spark
        