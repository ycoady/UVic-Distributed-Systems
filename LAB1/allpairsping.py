# send a probe message to each neighbor
def probe_neighbors(port):

  for neighborip in mycontext["neighborlist"]:
    mycontext['sendtime'][neighborip] = getruntime()
    sendmess(neighborip, port, 'ping',getmyip(),port)

    sendmess(neighborip, port,'share'+encode_row(getmyip(), mycontext["neighborlist"], mycontext['latency'].copy()))
    # sleep in between messages to prevent us from getting a huge number of 
    # responses all at once...
    sleep(.5)

  # Call me again in 10 seconds
  while True:
    try:
      settimer(10,probe_neighbors,(port,))
      return
    except Exception, e:
      if "Resource 'events'" in str(e):
        # there are too many events scheduled, I should wait and try again
        sleep(.5)
        continue
      raise
  


# Handle an incoming message
def got_message(srcip,srcport,mess,ch):
  if mess == 'ping':
    sendmess(srcip,srcport,'pong')
  elif mess == 'pong':
    # elapsed time is now - time when I sent the ping
    mycontext['latency'][srcip] = getruntime() - mycontext['sendtime'][srcip]

  elif mess.startswith('share'):
    mycontext['row'][srcip] = mess[len('share'):]



def encode_row(rowip, neighborlist, latencylist):

  retstring = "<tr><td>"+rowip+"</td>"
  for neighborip in neighborlist:
    if neighborip in latencylist:
      retstring = retstring + "<td>"+str(latencylist[neighborip])[:4]+"</td>"
    else:
      retstring = retstring + "<td>Unknown</td>"

  retstring = retstring + "</tr>"
  return retstring


# Displays a web page with the latency information
def show_status(srcip,srcport,connobj, ch, mainch): 

  webpage = "<html><head><title>Latency Information</title></head><body><h1>Latency information from "+getmyip()+' </h1><table border="1">'

  webpage = webpage + "<tr><td></td><td>"+ "</td><td>".join(mycontext['neighborlist'])+"</td></tr>"

  # copy to prevent a race
#  connobj.send(encode_row(getmyip(), mycontext['neighborlist'], mycontext['latency'].copy()))

  for nodeip in mycontext['neighborlist']:
    if nodeip in mycontext['row']:
      webpage = webpage + mycontext['row'][nodeip]+'\n'
    else:
      webpage = webpage + '<tr><td>'+nodeip+'</td><td>No Data Reported</td></tr>\n'

  # now the footer...
  webpage = webpage + '</table></html>'

  # send the header and page
  connobj.send('HTTP/1.1 200 OK\nContent-Type: text/html\nContent-Length: '+str(len(webpage))+'\nServer: Seattle Testbed\n\n'+webpage) 

  # and we're done, so let's close this connection...
  connobj.close()



if callfunc == 'initialize':

  # this holds the response information (i.e. when nodes responded)
  mycontext['latency'] = {}

  # this remembers when we sent a probe
  mycontext['sendtime'] = {}

  # this remembers row data from the other nodes
  mycontext['row'] = {}
  
  # get the nodes to probe
  mycontext['neighborlist'] = []
  for line in file("neighboriplist.txt"):
    mycontext['neighborlist'].append(line.strip())

  ip = getmyip() 
  if len(callargs) != 1:
    raise Exception, "Must specify the port to use"
  pingport = int(callargs[0])

  # call gotmessage whenever receiving a message
  recvmess(ip,pingport,got_message)  

  probe_neighbors(pingport)

  # we want to register a function to show a status webpage (TCP port)
  pageport = int(callargs[0])
  waitforconn(ip,pageport,show_status)  

