# Ledmastree


# Installation

It is assumed that python3 and nodejs is already installed.

```
$ git clone https://github.com/joms/ledmastree.git
$ cd backend
$ pip3 install -r requirements.txt
$ cd ../frontend
$ npm install && npm build
```

## Autostart

It's useful if the backend would start when your Raspberry PI boots. This could be done in the following way:

```
$ chmod +x /home/pi/autostart.sh
$ crontab -e
```

Add the following line to your cron file: `@reboot sh /home/pi/launch-backend.sh >/home/pi/logs/cronlog 2>&1`

# Usage

To run the Flask backend you need to define the application path before it.

```
$ export export FLASK_APP=/home/pi/ledmastree/backend/app.py
$ python3 -m flask run --host=0.0.0.0
```

You can now access the API on your Raspberry PI through port 5000: http://localhost:5000/ledmastree/api/v1/leds

## nginx

If you want to access the API through port 80, an nginx reverse proxy is recommended:

```
$ sudo touch /etc/nginx/sites-available/proxy
$ sudo nano /etc/nginx/sites-available/proxy

# Raspberry PI xmas tree reverse proxy
server {
    listen 80;
    server_name localhost;

    location /api{
        proxy_pass http://127.0.0.1:5000/ledmastree/api;
    }
}

$ sudo ln -s /etc/nginx/sites-available/proxy /etc/nginx/sites-enabled/proxy
$ sudo service nginx reload
```

# TODO

- ~~Pattern support~~
- Proper frontend
- GET parameter support
- ~~Twitter~~ Inspired by [this Reddit post](https://www.reddit.com/r/raspberry_pi/comments/7hunue/i_made_twitter_powered_christmas_lights_any_time/)
- Alexa implementation
