Communication contract:

Expectations for Group Partnership
1.We will communicate via Discord and iMessage
2.Since Isaac is 8 hours ahead, a response time of 24hrs or less
is best.
3.Assignments will be turned in on time
4.Log updates and progress each meeting/session to stay on
track
5.Communicate any issues, bugs, difficulties as soon as possible
to help progression and assignments done.

Part 1: microservice_for_isaac

First we open up the microservice_for_isaac directory to see app.py and service.py

service.py contains a function requests data from another API in Isaac’s project to get a few data points on his top Spotify songs. More specifically the averages of danceability, tempo, and energy.

This data is then transformed into a matplotlib graph and then turned into a png.file that can be returned.

app.py is a very small Flask application/API that has a route which returns the image from the service function from earlier.

To start this web server we run flask run —port 8000

Part 2: spotipy-visualizer

Now that the web server for the microservice is running, we navigate over to the spotipy-visualizer project.

The basic part of this project is displaying a UI window that has a button which displays a bar graph.

app.py is all of the routing, services.py are helper functions, and window.py is the main window. 

We open up a terminal and type flask run —port 5000 to start another web server on port 5000.

We have a route called getAveragesFromSongFeatures which is what our other api calls to get the average data.

Now that the web server is running on port 5000 and the other on port 8000 we go to window.py.

In window.py is a function called get_avg_featues which makes an API get request to our route on port 8000 and opens up the image of the bar graph. 

Now in window.py we hit run in VS Code and then go to the average button. Booom the plot appears.