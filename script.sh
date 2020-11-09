#!/bin/bash

systemctl stop firewalld

rpm -i /root/jdk.rpm

rpm -i /root/hadoop.rpm --force

mkdir /dn

\cp -rvf /root/hdfs-site.xml /etc/hadoop/hdfs-site.xml

\cp -rvf /root/core-site.xml /etc/hadoop/core-site.xml
