========================================================================================================================================
TLRU cache package (A second branch (refactoring) in this repo change for a WebSocket server, and improve the priority node management.
========================================================================================================================================

Library for a TLRU(Least Recently Used) cache. This library work with a web server and accept REST request:

1. GET http://ip_address:port/cache?key=key_for_cache
    This request respond with the key's value
2. POST http://ip_address:port/cache?key=key_for_cache&value=value&minutes=minutes
    This request accept the value and minutes for due date of the key's cache, return JSON with the value saved.

******************************
Libraries
******************************

1. Server Library: This Software allow to run the cache server and wait for client requests
2. Client Library: This python software will allow to connect to the server(s) and interact with the cache.

******************************
Software Components
******************************

1. Model: Basic structures for manage the data
2. use_cases: Implement the logic for "set" and "get" the data from the cache. TODO: It's necessary to improve the data structure for Nodes, so that the search will be faster. The cache logic allow to order the keys with the due_time of each node.


******************************
Geo Distributed Implementation
******************************

The final objective of this software is to build a Geo Distributed LRU (Least Recently Used) cache with time expiration. This functionality was not built. The steps to build this is:

**Server**:

1. Create a file with the cluster configuration, each node or server must have this file, where we will write the address to connect to each server, and the priority.
2. The server priority allow us to manage the fault tolerance, because when there area lost of data,  the server with more priority is the reference.
3. The order of request must be  share with the priority server, and this server is in charge to replicate the instruction to the others servers in the cluster.
4. When a server detect data inconsistency (compare with se priority server), this server must manage a status and refuse new requests until restore the data consistency.
5. If the fail is with the priority server, the next server in priority is in charge of the integrity of the cluster.
6. Implement a security layer
7. Implement a fail recovery, with a request to a health server and load the data over the network or by a file.
8. Control a node replace if the time_stamp is greater than the previous node.

**Client**:

1. Create a file to write the serves to connect an his priority
2. Define the closest server within the file. This is the main server to interact with the client.
3. Allow to switch between servers, if the main or another server don't respond or don't have a valid status.
4. This library allow to connect to the cache cluster like a package and the user or program don't have to implement http request.
