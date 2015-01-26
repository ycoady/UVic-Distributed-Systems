## Project Idea: RPC and Two-Phase Commit!

This is a *very* classic exercise for all students, everywhere, learning about distributed systems!  It is a great thought exercise, and will use things we are/will be talking about in the course.  It has 3 pieces:

1. A durable key/value store.
2. A two-phase commit protocol to coordinate writes to replicas of the key/value store.
3. RPC to coordinate the replica processes.

## What is a durable key/value store?

Using something like an sqlite database library (you can write your own, but you really don't have to!) make sure you support the following 3 operations:

* put(k, v): stores the value "v" with key "k"
* del(k): deletes the entry for key "k"
* v = get(k): returns the value associated with key "k"

in a way that is "durable": if your process quits and is restarted, all values that were "put" must be retrievable using a "get", and any value that was deleted must not be available.  

## What does this have to do with Two-Phase Commit?

It is great that your key/value store is durable, but now your job is to replicate it by using a single *coordinator* process with multiple *replica* processes.  

The *coordinator* process should use RPC for the 3 operations (put, del, get).  Any state changing operations (put, del), should use two-phase commit to coordinate the operation between replicas.  Operations that preserve state (get), can just be sent to a replica at random.  Multiple clients should be able to connect to the coordinator and issue requests concurrently. 

The *replicas* should each be an instance of your durable key/value store, and expose an RPC interface for the coordinator to interact with them.  Operations should be allowed to execute concurrently.  To keep it simple, assume that if two or more operations manipulate the same key, the first to arrive should be able to proceed while the others should not be able to commit.

Note that two-phase commit requires that the coordinator and the replicas will need to use logging to keep durable state.  This means you need to:

* implement logging
* figure out what to log
* determine how to replay the log when recovering

## Is this a Fault-Tolerant System?

YES!  If either the master or any of the replicas fail, you need to make sure your two-phase commit protocol does the right thing... and even more importantly, when whoever failed recovers, your two-phase commit needs to recover and proceed in the right way!

## How do you test this?!

Implement a client program to interact with the coordinator, which in turn will interact with your replicas.  You don't have to be too fancy with the configuration of the system, but you will have to figure out how to (at the very least) fire up a bunch of processes and hard wire which process exist and where they are running to configure your system.  

Launch multiple clients to hammer on the coordinator concurrently. Test as many cases as you can, in particular try knocking out the master during the period of uncertainty!
