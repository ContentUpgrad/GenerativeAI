
#### Logging to the Amazon EC2 instance
For Amazon Linux 2023 based instances, the password is `ec2-user`
For Ubuntu based instance, the password is `ubuntu`

Once you've logged into the EC2 instance via a terminal (Mac/Linux) or PuTTY (Windows), follow the instructions below to install Git, Docker and Docker-Compose on an EC2 instance.

### Switch to the superuser
`sudo su`

### Install Docker
`yum install docker`

### Get pip3 if not already installed
`yum install python3-pip`

### Install Docker-Compose through Pip
`pip3 install --user docker-compose`


### Download the docker-compose binaries
`sudo curl -L https://github.com/docker/compose/releases/latest/download/docker-compose-$(uname -s)-$(uname -m) -o /usr/local/bin/docker-compose`


### Change the permissions of the docker-compose binaries
`sudo chmod +x /usr/local/bin/docker-compose`


### Create a system link between the docker-compose binaries
`ln -s /usr/local/bin/docker-compose /usr/bin/docker-compose`

### Verify docker compose version:
`docker-compose version`

### Enable docker service at AMI boot time:
`sudo systemctl enable docker.service`

### Start the Docker service:
`sudo systemctl start docker.service`


# Steps for running the application locally

### Install requirments
`pip install -r requirements.txt`

### Run the Streamlit app
The application can be run locally using VS Code or a terminal using the following command:
`streamlit run app.py`

Navigate to the following link in your browser to access the application
`localhost:8501`

# Docker Commands

`docker build . -t langchain-rag-app:latest`

`docker-compose up`

**NOTE**: While deploying in EC2 instance, make sure that you allow the inbound port `8501` in the security groups section of EC2.