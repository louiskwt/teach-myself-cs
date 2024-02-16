# How NodeJS work

- it's a runtime environment that executes JS code and serves as an interface to the system running in the machine through the event loop created by libuv (which is written in C)

- it's the libuv and node itself that do the heavy lifting to handle file IO, networking, etc.

- Node handles incoming data as stream and use Eventemitter to pass on the Incoming Instance (request) to the JavaScript environment so that the JavaScript code has access to the request

- JavaScript can then send back the response to NodeJS as return
