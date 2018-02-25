#!/bin/sh
# This script will install spark on ubuntu16.04

# Add the Java PPA
apt-add-repository ppa:webupd8team/java

# Install the Java
apt-get update
apt-get install oracle-java8-installer

# Install Scala
mkdir /opt/scala
cd /opt/scala
wget http://downloads.lightbend.com/scala/2.12.1/scala-2.12.1.deb
dpkg -i scala-2.12.1.deb

# Install the Apache Spark
#mkdir /opt/spark
#cd /opt/spark
#wget http://d3kbcqa49mib13.cloudfront.net/spark-2.0.2-bin-hadoop2.7.tgz
#tar -xvf spark-2.0.2-bin-hadoop2.7.tgz

# or download spark source code and build
cd ~
git clone https://github.com/yzhan298/spark.git
build/mvn -T12 -DskipTests clean package



