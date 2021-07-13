# Printing-portal
A printing portal website developed using Django Framework,where user can upload his/her document to be printed and can pay respective amount using integrated epayment gateway.
The website includes seperate login system for general users and shopkeeper authenticated with microsoft auth.

## Installation
python and django need to be installed

```bash
pip install django
```
##Usage

Go to the Printing-Portal folder and run 

```bash
python manage.py runserver
```

Then go to the browser and enter the url **http://loaclhost:8000**

## Login

The login page is common for customer and shopkeeper.  
The username is their microsoft outlook email-id and password is thier respective email password.

You can access the django admin page at **http://127.0.0.1:8000/admin**, after creating new admin user by following command

```bash
python manage.py createsuperuser
```
## User
There is no need to create any user from admin page.

The email of shopkeeper need to be defined at function store_user in authhelper file under tutorial folder.

Also the email of shopkeeper need to be defined at place order function in views file under task folder 

## Screenshots

### Signin page

![Screenshot (72)](https://user-images.githubusercontent.com/69042089/125435090-413ba80c-8e85-4d12-808b-8b9cb3b54629.png)


![Screenshot (71)](https://user-images.githubusercontent.com/69042089/125435064-353976d8-045b-464b-bb71-44ba61a8f5a2.png)

### Customer Page 

![Screenshot (73)](https://user-images.githubusercontent.com/69042089/125435093-0971652a-170c-4a1b-bdbf-65a529d11952.png)

#### new order 

![Screenshot (80)](https://user-images.githubusercontent.com/69042089/125436118-9b89335b-9246-4ac1-accf-09d1c5b1189e.png)


#### Payment Gateway

![Screenshot (76)](https://user-images.githubusercontent.com/69042089/125435099-a042c70f-b6fb-4a4e-83fe-e3d98f31f2fe.png)

![Screenshot (77)](https://user-images.githubusercontent.com/69042089/125436472-966d2627-bcdb-4989-8e40-2431a0e45251.png)

#### Old Transactions

![Screenshot (74)](https://user-images.githubusercontent.com/69042089/125435096-dce88c36-175b-4c56-9a8a-c9a77ab6d8a1.png)

### Shopkeeper Page


![Screenshot (78)](https://user-images.githubusercontent.com/69042089/125435106-5b06c955-5593-44e2-a0fd-5d3a6a3f7550.png)

#### Recent Orders


![Screenshot (81)](https://user-images.githubusercontent.com/69042089/125436899-b341ef13-55b2-449c-adcd-0226b5d5129e.png)


![Screenshot (79)](https://user-images.githubusercontent.com/69042089/125435108-5140247f-c6a2-421b-92e6-2c7c04e16e1e.png)