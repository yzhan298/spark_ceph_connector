import rados
from write_to_ceph import ioctx

print "\nClosing the connection."
ioctx.close()

print "Shutting down the handle."
cluster.shutdown()


