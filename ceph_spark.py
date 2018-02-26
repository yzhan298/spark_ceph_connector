import rados
from pyspark.sql import SparkSession

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

print "\n\nI/O Context and Object Operations"
print "================================="

print "\nCreating a context for the 'data' pool"
if not cluster.pool_exists('data'):
        raise RuntimeError('No data pool exists')
ioctx = cluster.open_ioctx('data')

print "\nContents of object 'hw'\n------------------------"
tempFile = ioctx.read("hw")

spark = SparkSession.builder.appName("test").getOrCreate()

sc=spark.sparkContext

rdd = sc.parallelize([tempFile])

print(rdd.collect())
