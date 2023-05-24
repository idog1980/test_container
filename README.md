# Welcome to Github Session - Test Container

This is a python script creates a small docker container on your local machine with nginx on it.
nginx is a very slim open source web server that out of the box can do many things, for us though, is suppose to display html/pictures we give to it.

**There is no need to commit anything to this repo**

# What do I need to do in order to use it?

1st , Please verify you have python installed on your machine.
you can verify it by running :`python3 --version`
If you get an error please go ahead and install python on your mac from [Here](https://www.python.org/downloads/) Or simply google how to do it.

2nd, Please verify you have docker on your machine, you cannot run docker containers without the hypervisor.
you can verify if you have docker by running `docker ps`.
Again, if you know you don't have it or get an error on the command you can download it from [Here](https://docs.docker.com/desktop/install/mac-install/) or use brew commands like `brew install docker`
> Please note that docker desktop is a hypervisor, it means it needs hardware compatibility so make sure if you go to the website that you download **intel or M1 chips version for your hardware**

## How to run it?

1. You'll need it on your local machine, if you dont know how to get it, your not paying attention already.
2. once you get it you can run it following this command : `python3 container.py [option]`
	You have 2 flags in the script:
- `-s` to start launch the container
- `-t` to stop the container and remove it from your local machine (including the image) 		

When running the script with `-s` flag, it will check whether you have docker installed and if not will ask you to install it.
The next step is provide him your code directory , you can verify it in terminal by used the `pwd` command on the code directory and paste it to the input.


** You are ready to start learning **
