Django Application Deployment using Docker on AWS EC2
📌 Project Description

This project demonstrates how a Django web application is dockerized and deployed on an AWS EC2 instance.
The application runs inside a Docker container and is exposed through the EC2 public IP.

The purpose of this project is to showcase Docker fundamentals and cloud deployment using AWS EC2.

Technologies Used

Django (Python)

Docker

AWS EC2 (Ubuntu)

Gunicorn

Git & GitHub

📂 Project Structure
.
├── Dockerfile
├── requirements.txt
├── manage.py
├── project_name/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
└── README.md

⚙️ Deployment Steps
1️⃣ Create EC2 Instance

Ubuntu 22.04

Open inbound ports:

22 (SSH)

8000 (Application)

2️⃣ Install Docker on EC2
sudo apt update
sudo apt install -y docker.io git
sudo systemctl start docker
sudo systemctl enable docker
sudo usermod -aG docker ubuntu

3️⃣ Clone Repository
git clone https://github.com/<your-username>/<repo-name>.git
cd <repo-name>

4️⃣ Build Docker Image
docker build -t django-app .

5️⃣ Run Docker Container
docker run -d -p 8000:8000 django-app

6️⃣ Configure Django Allowed Hosts
ALLOWED_HOSTS = ["<EC2_PUBLIC_IP>", "localhost", "127.0.0.1"]

🌐 Application Access
http://<EC2_PUBLIC_IP>:8000

✅ Outcome

Django application successfully containerized using Docker

Application deployed and running on AWS EC2

Accessible via public IP

📌 Notes

This project focuses only on Dockerization and EC2 deployment

Intended for learning and DevOps practice purposes
<img width="1383" height="747" alt="image" src="https://github.com/user-attachments/assets/24b7e0aa-3817-4ca9-bcaf-fb2db60f066c" />

