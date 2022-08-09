 
python3 -m venv venv

source venv/bin/activate

pip3 install -r requirements.txt 

python manage.py makemigrations (initialize the db)
python manage.py migrate

install mysql client

create user: root
password: password

$ mysql -u root -p (for creating the initial database)

python manage.py createsuperuser (for access to admin panel)

python manage.py runserver