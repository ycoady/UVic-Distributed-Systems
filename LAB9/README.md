# Installing Flask, AbeBook's Scrunch on Amazon EC2

## Get an Amazon Web Services Account
1. Get an account here:

	http://aws.amazon.com
	
	(you will need a Amazon Account/Credit Card & Cell phone to verify your account)

2. Create key pair (EC2 Dashboard)

	-If you access EC2 from Linux change permission on key
	<pre class="command-line">
		chmod 400 mykey.pem 
	</pre>
	
	- If you access EC2 from Windows using putty you will have to convert your key from *.pem to *.ppk using puttygen, see here:
	
	http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/get-set-up-for-amazon-ec2.html#prepare-for-putty

3. Makes sure your Region is set to 'US-Oregon' (Top right EC2 menu bar)

4. Create a Security Group (EC2 Dashboard)

	Allow Inbound: HTTP/HTTPS/SSH

5. Launch AMI Instance (EC2 Dashboard)
	-Check tick 'Free tier only' check box.
	-Choose Amazon Linux AMI 2014.09.2 (HVM)
	-Filter for 'Micro Instances' in next dialog (t2.micro)
	-Edit Security Group

6. Connect to your Micro AWS Instance
	-Use ssh with the key you generated/downloaded earlier.
	<pre class="command-line">
		ssh -i mykey.pem ec2-user@[machine IP]
	</pre>

7. TERMINATE YOUR INSTANCE
	-<b>DO IT!!!!! PLEASE!!!!!!</b>

## Install basic and required packages

For the packages below are enough to run a Flask 'Hello World' program we use to get you started (you will need some more packes to run AbeBook's Scrunch server).

<pre class="command-line">
sudo su
yum upgrade -y
</pre>

To begin with, you must install some bare bone packages
Flask, Jinja2 and Werkzeug will be automatically installed below.

<pre class="command-line">
yum install -y gcc-c++
yum install -y python-devel
yum -y install python-pip

pip install uwsgi
pip install flask
pip install flask-debugtoolbar
</pre>

## Install and setup web-server

You can host your Flask app directly, but <i>nginx</i>, is the better choice if you want your project to scale (you can choose other web-servers like <i>Apache</i> as well, but the instructions here are for <i>nginx</i> .

<pre class="command-line">yum install -y nginx</pre>

After installation, change configuration file for proxy setup.

<pre class="command-line">vi /etc/nginx/nginx.conf</pre>

Find the <i>location /</i> section, and change it to as follow:

<pre class="code">
location / {
    include uwsgi_params;
    uwsgi_pass 127.0.0.1:10080;
}
</pre>

Then, start your Web server

<pre class="code">
service nginx start
</pre>

## Create 'Hello, World' program

In your project folder create your first python app.

<pre class="code">
cd /usr/share/nginx/html/
mkdir hello
cd hello
</pre>

<pre class="command-line">vi hello.py</pre>

<pre class="code">
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10080)
</pre>

## Setup uWSGI

To configure uWSGI server create a config file as follows:

<pre class="command-line">vi app.yaml</pre>

<pre class="code">
uwsgi:
  socket: 127.0.0.1:10080
  master: 1
  workers: 1
  chmod-socket: 666
  auto-procname: 1
  python-path: .
  pidfile: /tmp/uwsgi.pid
  daemonize: /var/log/uwsgi.log
  module: hello:app
</pre>

## Start uWSGI

Using the config file, you can easily start uWSGI server:

<pre class="command-line">uwsgi --yaml app.yaml</pre>

In case, you want to run it as other user's, you can use <i>--uid</i> option additionally.
And, because our config specify that uWSGI processes are executed as daemon, if you want to stop them all, you can run:

<pre class="command-line">kill -INT `cat /tmp/uwsgi.pid`</pre>

## Installing AbeBook's Scrunch
Now that you have a running <i>Flask/nginx</i> environment, adapt the code from AbeBook's Scrunch Server to work on your machine such that it will use a database to store the shortened URLs (you may use sqlite as a basic key value store or get fancier and make your key value store distributed using additional AWS instances ).

Get code for scrunch here:

http://www.scrunch.ca

<pre class="command-line">
wget http://www.scrunch.ca/static/scrunch-code.zip
</pre>

## Shut down your running AWS instances!
- In the EC2 Dashboard click 'Running Instances' and right click on your instance in the leist and select 'Instance State' > 'Terminate'.

