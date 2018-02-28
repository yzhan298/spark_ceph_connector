# This script will connect Spark with Ceph
# We can read the data from Ceph to Spark, and 
# we also can write data to Ceph from Spark

import rados
from pyspark.sql import SparkSession

# Connect Ceph cluster 
try:
        cluster = rados.Rados(conffile='/home/cc/SIRIUS-Ceph/docker/configdir/ceph.conf')
except TypeError as e:
        print 'Argument validation error: ', e
        raise e

print "Created cluster handle."

try:
        cluster.connect()
except Exception as e:
        print "connection error: ", e
        raise e
finally:
        print "Connected to the cluster."

# List Ceph pools
print "\nAvailable Pools"
print "----------------"
pools = cluster.list_pools()
for pool in pools:
	print pool

# Initiate Ceph test pool
print "\n\nI/O Context and Object Operations"
print "================================="

if not cluster.pool_exists('spark_ceph'):
        raise RuntimeError('No test  pool exists')
	cluster.create_pool('spark_ceph')
ioctx = cluster.open_ioctx('spark_ceph')
print "\nThe connection is done. Please start testing."


'''
print "\nContents of object 'hw'\n------------------------"
tempFile = ioctx.read("hw")

spark = SparkSession.builder.appName("test").getOrCreate()

sc=spark.sparkContext

rdd = sc.parallelize([tempFile])

print(rdd.collect())
'''


