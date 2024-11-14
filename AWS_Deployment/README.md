# Deploying on AWS Cloud
## Logging to the Amazon EC2 instance
For Amazon Linux 2023 based instances, the password is `ec2-user`
For Ubuntu based instance, the password is `ubuntu`

Once you've logged into the EC2 instance via a terminal (Mac/Linux) or PuTTY (Windows), follow the instructions below to install Git, Docker and Docker-Compose on an EC2 instance.

## Switch to the superuser

`sudo su`

## Install Docker

`yum install docker`

## Get pip3 if not already installed

`yum install python3-pip`

## Install Docker-Compose through Pip

`pip3 install --user docker-compose`

## Download the docker-compose binaries

`sudo curl -L https://github.com/docker/compose/releases/latest/download/docker-compose-$(uname -s)-$(uname -m) -o /usr/local/bin/docker-compose`

## Change the permissions of the docker-compose binaries

`sudo chmod +x /usr/local/bin/docker-compose`


## Create a system link between the docker-compose binaries

`ln -s /usr/local/bin/docker-compose /usr/bin/docker-compose`

## Verify docker compose version:

`docker-compose version`

## Enable docker service at AMI boot time:

`sudo systemctl enable docker.service`

## Start the Docker service:

`sudo systemctl start docker.service`

Steps for running the application locally

## Install requirments

`pip install -r requirements.txt`

## Run the Streamlit app
The application can be run locally using VS Code or a terminal using the following command:
`streamlit run app.py`

Navigate to the following link in your browser to access the application
`localhost:8501`

## Docker Commands

`docker build . -t langchain-rag-app:latest`

`docker-compose up`

NOTE: While deploying in EC2 instance, make sure that you allow the inbound port `8501` in the security groups section of EC2.


# Deploying on Azure Cloud

## Set Up Your Azure Virtual Machine (VM)

Log into Azure Portal and create a new Virtual Machine:
   - For Ubuntu-based instances, use username: `azureuser`.
   - Choose a VM size that meets your the app's resource requirements.
   - Under Inbound port rules, add 8501 to allow access to your application.

Connect to Your VM:
- On Mac/Linux, use SSH from your terminal:
`ssh azureuser@<your_vm_public_ip>`
- On Windows, use an SSH client such as PuTTY with the provided public IP.

## Install Required Tools on the Azure VM

Once connected to the VM, follow these instructions to install Git, Docker, and Docker-Compose.

## Switch to Superuser:
`sudo su`

## Update package lists:
`sudo apt update`

## Install Docker:
`sudo apt install -y docker.io`

## Install pip3 (Python Package Manager):
`sudo apt install -y python3-pip`


## Install Docker-Compose via pip:
`pip3 install docker-compose`

## Download Docker-Compose Binaries:
Use the following command to download the latest Docker-Compose binaries:

`sudo curl -L "https://github.com/docker/compose/releases/latest/download/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose`

## Set Permissions for Docker-Compose:
`sudo chmod +x /usr/local/bin/docker-compose`

## Create a System Link for Docker-Compose:
`sudo ln -s /usr/local/bin/docker-compose /usr/bin/docker-compose`

## Verify Docker-Compose Installation:
`docker-compose --version`

## Enable Docker to Start on Boot:
`sudo systemctl enable docker.service`

## Start the Docker Service:
`sudo systemctl start docker.service`

## Clone Your Application’s Repository:
`git clone <your_repo_url>`
`cd <your_repo_name>`

## Install Python Dependencies:
`pip install -r requirements.txt`

## Run the Application Locally for Testing:
`streamlit run app.py`

## Use Docker to Containerize and Run the Application
`docker build . -t langchain-rag-app:latest`
`docker-compose up`

**NOTE**:
If you're facing issues with the firewall Settings on Azure, you need to allow inbound traffic on Port 8501:
In Azure Portal, go to your VM’s Networking settings.
Under Inbound port rules, add Rule to allow Port 8501 for HTTP access to your Streamlit application.
Open a browser and go to http://<your_vm_public_ip>:8501 to access the RAG application.
