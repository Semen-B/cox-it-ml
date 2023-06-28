# Cox.it test task

## Pre-requisites
* Python (3.9+)
* Docker

## Deploy local instance

1. Clone the project 
   * `git clone (https://github.com/Semen-B/cox-it-ml.git)`
2. Create virtual environment
   * `virtualenv venv`
   * `source venv/bin/activate`
3. Install dependencies 
   * `pip3 install -r requirements.txt`
4. Run the server
   * `python3 src/main.py`
5. Server should be running at `http://127.0.0.1:8000/docs`


## Deploy remote instance (EC2)

6. Create docker image via cmd command:
   * `docker build -t image_name:version_5 .`
7. Push docker image to docker hub:
   * `docker push <registry-address>:<repository-name>`
8. Set EC2 instance on [Visit AWS](https://aws.amazon.com)
9. Connect to EC2 instance shell
10. Update the package lists by running the command:
    * `sudo apt update`
11. Install Docker by running the command: 
    * `sudo apt install docker.io`
12. Start the Docker service:
    * `sudo systemctl start docker`
13. Enable Docker to start on boot: 
    * `sudo systemctl enable docker`
14. Pull docker image from docker hub: 
    * `docker pull registry-address/repository-name`
15. Run the Docker container on the EC2 instance: 
    * `docker run -d -p 80:8000 --name container-name registry-address/repository-name.`
