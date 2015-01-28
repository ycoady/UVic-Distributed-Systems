## *"Hello GEE!"* in 10 easy steps by:

1. Allocating yourself a slicelet

2. Writing a script to install the necessary software (geoip-bin and wget), and a geoIP [database] (http://geolite.maxmind.com/download/geoip/database/GeoLiteCity.dat)

3. Writing a script to make sure everything installed correctly

4. Putting both scripts on the nodes using the [Fabric](http://www.cs.cornell.edu/projects/fabric/) 'put' command

5. Using Fabric with a parallel decorator to run the install and check scripts

6. Writing a script to get the local IP address out of ifconfig

7. Extending the script to get the host IP address as well

8. Using that IP address to get the lat long of the server

9. Writing a [curl] (http://curl.haxx.se/docs/manpage.html) command to send slicename, private_ip, public_ip, hostname, lat, long to the Lively server Rick will set up

10. Writing a Fabric command to do this in parallel on all the nodes

Details [here!] (https://docs.google.com/a/us-ignite.org/document/d/18hUrCyJvJ2xBqh5z6xFVNERnV8tcsB2HHhq3wtR6Uj8/edit?usp=sharing)
