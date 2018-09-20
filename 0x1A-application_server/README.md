# 0x1A. Application server

20180917 - The purpose of this project is to introduce the use of Gunicorn application server configuration

### 0-welcome_gunicorn-upstart_config, 0-welcome_gunicorn-nginx_config
Configuration file for Upstart and Nginx to deploy a simple flask application that returns "Hello HBNB!" when http://127.0.0.1/airbnb-onepage/ is visited

### 1-pass_parameter-upstart_config, 1-pass_parameter-nginx_config
Configuration file for Upstart and Nginx to deploy a flask application that serves web_flask/6-number_odd_or_even.py

### 2-api-upstart_config, 2-api-nginx_config
Configuration file for Upstart and Nginx to deploy a flask application that serves api/v1/app.py from your AirBnB_clone_v3

### 3-complete_webapp-upstart_config, 3-complete_webapp-nginx_config_ 
Configuration file for Upstart and Nginx to deploy a flask application that serves web_dynamic/2-hbnb.py from AirBnB_clone_v4
