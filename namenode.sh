#!/bin/bash

systemctl stop firewalld

rpm -i jdk.rpm

rpm -i hadoop.rpm --force

mkdir /nn

\cp -rvf /root/auto_hadoop/core-site.xml /etc/hadoop/core-site.xml

\cp -rvf /root/auto_hadoop/hdfs-site1.xml /etc/hadoop/hdfs-site.xml

hadoop namenode -format

hadoop-daemon.sh start namenode

hadoop dfsadmin -report
