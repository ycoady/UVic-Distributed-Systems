# Getting AbeBook's Scrunch Server running on GEE

## Log into GEE and run...

<pre class="command-line">
apt-get update
apt-get install -y build-essential
apt-get install -y python2.7-dev
apt-get install -y python-pip
apt-get install -y wget 
apt-get install -y unzip
apt-get install -y uwsgi uwsgi-plugin-python
</pre>

## Prepare Web server directory and install dependencies:

<pre class="command-line">
cd /root
mkdir www
cd www
wget http://www.scrunch.ca/static/scrunch-code.zip
unzip scrunch-code.zip
chown www-data:www-data -R /root/www
pip install -r requirements/prod.txt
pip install -r requirements/dev.txt
</pre>

## Install nginx:

<pre class="command-line">
apt-get install -y  nginx-full
rm /etc/nginx/sites-enabled/default
</pre>

## Make nginx config file:

<pre class="command-line">
vi /etc/nginx/sites-enabled/scrunch
</pre>

<pre class="command-line">
server {
        listen 80;
          server_name localhost
          server_tokens off;
          access_log /var/log/nginx/scrunch_access.log;
          error_log /var/log/nginx/scrunch_error.log;

          location / {
                  root /root/www;
                  include uwsgi_params;
                  uwsgi_pass unix:/tmp/uwsgi.sock;
        }

        location /static {
                alias /root/www;
        }
}
</pre>


## Restart nginx:

<pre class="command-line">
service nginx restart
</pre>

## Make 'Hello World' program:

<pre class="command-line">
cd /root/www
vi hello.py
</pre>

<pre class="command-line">
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

if __name__ == '__main__':
    app.run(host='0.0.0.0')
</pre>

## Make  uWSGI configuration yaml script:

<pre class="command-line">
vi app.yaml
uwsgi:
  socket: /tmp/uwsgi.sock
  master: 1
  workers: 1
  chmod-socket: 666
  auto-procname: 1
  plugins: python
  python-path: .
  uid: www-data
  gid: www-data
  pidfile: /tmp/uwsgi.pid
  daemonize: /var/log/uwsgi.log
  module: hello:app
</pre>

## Start up 'Hello world' program:

<pre class="command-line">
uwsgi --yaml app.yaml
</pre>

## Setup SSH tunnel forwarding traffic to the GEE nginx server:

<pre class="command-line">
ssh -L 8080:localhost:80 -i id_rsa -F ssh-config slice343.pcvm3-1.instageni.stanford.edu -N
</pre>

## Access your Scrunch server from your local browser:

<pre class="command-line">
http://localhost:8080
</pre>
