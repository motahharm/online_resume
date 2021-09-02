# Online Resume

Online Resume With Django

Installation
----
    git clone https://github.com/motahharm/online_resume.git
    cd online_resume
    pip3 install -r requirements.txt

Run
----
    python3 manage.py makemigrations
    python3 manage.py migrate
    python3 manage.py createsuperuser #or you can use admin and admin for login
    python3 manage.py runserver
    
Urls:
----
127.0.0.1:8000 is default url<br>
you can use other urls like localhost:8000 or *your ip*:8000:<br>

    python3 manage.py runserver 0.0.0.0 #run on all your ips

you can edit port like localhost:5050 :<br>

    python3 manage.py runserver *your port*
    
edit url and port:

    python3 manage.py runserver 0.0.0.0:*your port*

- (your url) : (your port) =>  is home
- (your url) : (your port) /profile/list =>  is list of resumes
- (your url) : (your port) /resume/ (id resume) =>  is show resume

ScreenShots:
----

![](ScreenShots/1.png)<br>
![](ScreenShots/2.png)<br>
![](ScreenShots/3.png)<br>
![](ScreenShots/4.png)<br>
