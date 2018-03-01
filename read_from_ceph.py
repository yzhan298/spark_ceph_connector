import rados
from pyspark.sql import SparkSession
from init_spark_ceph_connection import cluster

# Connect to Ceph test pool
ioctx = cluster.open_ioctx('spark_ceph')

# Read testobj stored in Ceph
fileInCeph = ioctx.read("testObj")
print "Reading from Ceph."

# Start Spark session
spark = SparkSession.builder.appName("ceph").getOrCreate()

# Create a Sparkcontext object, which tells Spark
# how to access the Spark cluster
sc=spark.sparkContext

# Create RDD. Data is operated in parallel.
rdd = sc.parallelize([fileInCeph])

print(rdd.collect())


