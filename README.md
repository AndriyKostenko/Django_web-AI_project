# Hello, this is my Django_web+AI_project.

Features:

- Game
- Video-hosting 
- Recognizing of pictures (Tensorflow)
- Obtaining the weather 
- Searching the location

Stack:

- Python3
- Django3
- Tensorflow2
- Keras
- MySQL
- Docker
- Docker-Compose
- HTML/CSS/JS

Also were hosted on AWS(EC2).


# To start the project via Docker u have to:

1) git clone https://github.com/AndriyKostenko/Django_web-AI_project.git (copy the project)

2) python3 -m venv venv (installing virtual env.)

3) pip3 install -r requirements.txt (installing all the requirements for the following project)

4) docker-compose up --build (Build the Docker Image with Docker containers)

5) docker exec -it persikwebsite_web_1 /bin/bash (to enter into container)
    - python manage.py makemigrations (for database)
    - python manage.py migrate (for database)
    - python manage.py createsuperuser (for admin panel)

(Use 'sudo' in case of working on Linux)


https://user-images.githubusercontent.com/91188777/184371627-a459cff9-f8b1-41dd-a5ae-77c5835b459e.mp4




