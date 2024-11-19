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

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

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

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Deploying on Google Cloud

To deploy a Streamlit LangChain RAG app on Google Cloud Platform (GCP) using Google Compute Engine (GCE), the following are the instructions for GCP-specific adjustments.
 
## Create a Google Cloud Virtual Machine (VM) Instance
- Go to the Google Cloud Console (https://console.cloud.google.com/).
- Navigate to Compute Engine > VM Instances.
- Click Create Instance.
- Choose your desired Machine Type (e.g., n1-standard-1).
- Choose your Region and Zone.
- For the OS image, select Ubuntu 22.04 LTS (or any preferred Ubuntu version).
- Set up a Firewall rule to allow HTTP and HTTPS traffic.
- Set up SSH keys for secure login (or you can choose to log in with the Google Cloud Console for SSH access).

## SSH into the VM Instance
Once the VM instance is created:
In the Google Cloud Console, navigate to VM Instances, and click SSH next to your VM instance to log in directly via the browser.
Alternatively, if you are using a terminal (Mac/Linux), you can SSH into the instance using the following command:

`gcloud compute ssh <your-vm-instance-name> --zone <your-zone>`

## Install Docker, Docker Compose, and Pip
After SSH’ing into your VM, follow these steps:

## Switch to Superuser:
`sudo su`

## Update the system (optional but recommended):

`apt-get update`

## Install Docker:
`apt-get install docker.io`

## Enable Docker Service:
`sudo systemctl enable --now docker`

## Install Pip3 (if not already installed):

`apt-get install python3-pip`

## Install Docker Compose:
`pip3 install --user docker-compose`

## Download the latest docker-compose binary:

`sudo curl -L https://github.com/docker/compose/releases/latest/download/docker-compose-$(uname -s)-$(uname -m) -o /usr/local/bin/docker-compose`

Make the docker-compose executable:

`sudo chmod +x /usr/local/bin/docker-compose`

Verify the docker-compose version:
`docker-compose version`

Enable Docker to start on boot:
`sudo systemctl enable docker.service`

Start the Docker service:
`sudo systemctl start docker.service`

Clone Your Git Repository (Optional)
If your app code is stored in a Git repository, clone it to your VM instance:

`git clone <your-repository-url>`
`cd <your-repository-directory>`

Install Python Requirements
Install the required dependencies for the Streamlit LangChain app:

`pip install -r requirements.txt`

Build and Run Docker Containers
a) Build the Docker Image:

`docker build . -t langchain-rag-app:latest`

b) Run Docker Compose:
`docker-compose up`

This will build the necessary Docker containers and start the application in the background.

7. Open Port 8501 in GCP Firewall
Make sure that the necessary ports (e.g., 8501 for Streamlit) are open to the internet by configuring the Firewall rules for your VM instance:

a) Allow Port 8501 in the VM's Firewall:
- In the Google Cloud Console, go to VPC Network > Firewall.
- Click on Create Firewall Rule.
- Give the rule a name (e.g., allow-streamlit).
- Set the Source IP Ranges to 0.0.0.0/0 (this makes it accessible from anywhere).
- Under Protocols and Ports, select Specified protocols and ports and enter tcp:8501.
- Click Create.

b) Verify if the Firewall Rule is Working:
You can check if the port is open by running:

`gcloud compute firewall-rules list`

This will list all the firewall rules for your project, and you can confirm that port 8501 is open.

8. Access the Application
After the container is running and the firewall rules are configured, navigate to the external IP address of your VM instance:

In the VM Instances section of the GCP Console, locate your VM and copy the External IP.
Open your browser and navigate to http://<your-external-ip>:8501.
You should now be able to access your Streamlit app deployed on the Google Cloud VM.

**Notes**:
Scaling: To scale your app in GCP, you can create additional VM instances, use load balancing, or deploy on Google Kubernetes Engine (GKE) for container orchestration.
Storage: If you need persistent storage, consider using Google Cloud Storage or Persistent Disks for saving uploaded files (like PDFs) or other data.
Billing: Ensure that your GCP account is set up with billing enabled to avoid any service interruptions.
This should get your LangChain RAG app running on Google Cloud using Google Compute Engine.
