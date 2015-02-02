## GEE Portal Crash January 29 And Status

### The Crash
The GEE Portal crashed at the start of CS 462, Lab #2 on Thursday, January 29, and was down for about 27 hours while the GEE team diagnosed and fixed the problem!

### The Cause
There were roughly 250 simultaneous slice-creation events at the start of the lab.  This caused the slice-creation scripts, which invoke Ansible to create the containers on the nodes, to overload and corrupted the Ansible template.
The 250 simultaneous slice-creation events were caused by an unfortunate combination of events.  When the portal was written, slice “creation” was an instantaneous event; because populating slices on PlanetLab was somewhat slow, we had pre-allocated the slices and simply delivered the slice information and credentials to the user when he asked for a slice.  However, when we moved to the Docker infrastructure, actual slice creation was faster than before, and we had the opportunity in future to permit users to use their own custom images from DockerHub.  For these reasons, we decided to abandon pre-allocation, which meant that slice creation now takes on the order of a few seconds to a couple of minutes, depending on network conditions.  We didn’t, however, update the portal to display an in-progress page, leaving the same page with a Get-a-Slicelet button, and no feedback to the user about what was happening.

Slice creation slows down when a node is misbehaving, and by bad luck the GENI rack at the Naval Postgraduate School had gone offline.  So a labful of students were staring at “Get a Slicelet!” screens, which weren’t responding.  The natural assumption on a user’s part is that the link was broken, or not being followed, so naturally a number clicked a few times.  Fifteen students clicking six times a minute (not unreasonable) can generate 250 clicks in an hour; worse, we weren’t checking whether we were already processing another request for that student, and this caused the crash.

### What We’ve Done
First, when we get a slice-create request, we check to see if we’re already doing a request for that user.  If we are, we simply hand him his dashboard.  Second, when we get a slice-create request, the first thing we do is display an in-progress page to the user, with a link to take him to his dashboard.  Third, we now display the slice status (Processing/Running/Error) on the dashboard.  “Processing” means that the slice is in the process of being created.  Fourth, we prevent the user from deleting a slice that is still in-process.  The combination of these things should give the user better visibility into what’s going on with his slice status, and prevent incidents like the one we had last week.  Further, since we’re handing the user his slice credentials and fabfile, he can start work on his own machine even before his slice gets into Running state.

### Still In The Works
We want to make slice creation faster.  The only thing which slows it down right now is a malfunctioning node, so we’re going to detect this and simply omit misbehaving nodes from the slice.
