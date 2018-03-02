import rados
from init_spark_ceph_connection import cluster


ioctx = cluster.open_ioctx('spark_ceph')

with open('testdata', 'r+') as myfile:
	file_obj=myfile.read()
	#file_obj=myfile.read().replace('\n', '')

print "Writing object to Ceph."
ioctx.write("testObj", file_obj)






