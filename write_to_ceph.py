import rados
from init_spark_ceph_connection import cluster


ioctx = cluster.open_ioctx('spark_ceph')

print "Writing object to Ceph."
ioctx.write("testObj", "hello world")






