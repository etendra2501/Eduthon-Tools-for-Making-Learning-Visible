 ## **VirtualTree**

*A webapp aimed for students to share their work through portfolios with peers, in an easy and fun way.*

**Required Dependancies**
1. Python 3.7 or above
2. Django                  `pip install Django`
3. Django REST framework   `pip install djangorestframework`
4. Django CORS Headers     `pip install django-cors-headers`
5. Python Dotenv           `pip install python-dotenv`

**Steps to setup locally**
1. Install the required dependancies using command terminal.
2. Run terminal in the root directory.
3. Type `$ cd backend` in the terminal.
4. Next type `$ py manage.py makemigrations` followed by `$ py manage.py createsuperuser`.
5. Create a new superuser with some dummy name, email and a password (superuser is required for admin access).
6. Run the django server using `$ py manage.py runserver`.
7. Head over to the browser and open the localhost `http://127.0.0.1:8000/admin`. Login with the superuser credentials.
8. To access the **User Registration** API, use the address ` http://127.0.0.1:8000/api/account/register`.
9. To access the **User Profile** API, use ` http://127.0.0.1:8000/api/profiles`.