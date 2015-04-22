# tkGet
A small python script to graph the delay on the network.

This python script connects to the given url (via a HTTP-get request) and measures the duration of this call.
The duration is displayed in bars on the screen.
In the current version it will display 100 bars on a 500x500 window.

The application uses 2 threads, one for drawing and one for sending requests.
This application will most likely only work on python 3.
