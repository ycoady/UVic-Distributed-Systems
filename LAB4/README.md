## BitTorrent versus HTTP!

### Goal and Objective
In this lab, we’re going to compare the performance of a file download over HTTP and using BitTorrent.  You’re going to:
* Learn how to set up a webserver
* Learn how to set up a Torrent and a private tracker
* Run an experiment using Fabric (timing is critical here)
* Extract the results and present them

### Stuff you’ll Need
* Webserver: Apache2, BitTorrent
* Clients: aria2c

## What You’ll Produce
A report showing:
* Bandwidth between the http server and each client
* Bandwidth between the http server and each client, when each client is trying to transmit in parallel
* Download time for a standard test file, when each client tries to download in turn
* Download time for a standard test file, when the clients try to download simultaneously
* Torrent time for a standard test file, one client
* Torrent time for a standard test file, three clients working in parallel
* Fabric Operations and Concepts
* Running a task in parallel (@parallel)
* Roles (env.roledefs.update, @roles)
* File operations (put/get)

### Code You’ll Write (all straightforward, but fun in teams!)
* Something that generates a big file (100MB or so) for the test
* A shell script to capture the begin time of a job and save to a file
* A shell script to capture the end time of a job and save to a file
* A short python or shell script to look at the times and file size and report duration and rate

The model solution that we had had about five lines of code in each of these; as before, not a lot of programming in this lab.  The goal is to learn about the infrastructure and conducting experiments!

Step by Step details are [here!] (https://docs.google.com/document/d/1qyXj94BPk-SwQmTlVwnb0lyLIrLny-Z2o5g_P3UDHhs/edit?usp=sharing)
