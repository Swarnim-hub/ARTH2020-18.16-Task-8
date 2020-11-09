import os
os.system("espeak-ng here_we_create_docker_container__so_we_start_docker_services")
os.system("systemctl start docker")
name=input("enter your docker name")
os.system("docker run -it --name {} -p 99:80 centos:latest".format(name))
