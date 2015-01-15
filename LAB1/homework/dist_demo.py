include geoip_uvic.repy

if callfunc == 'initialize':
    print "Distance to Victoria %.2f km." % (geoip_distance("142.104.193.247", getmyip()))