# restful-API-design using Flask
Given task:
1) Design and implement a rest API for a discography application
2) Application handles artists,their albums and list of tracks in the album
3) Application should allow CRUD operations via python( Flask or Django).

--> Project that I have implemented:

I designed and implemented a rest API for a discography application via python microframework Flask in pycharam tool. And the developed application undergoes CRUD operations.

* Flask installation:

->For Windows use command: from flask import Flask

->For virtualenv use command:
  $ pip install Flask
  $ FLASK_APP=hello.py flask run
  It will run on http://localhost:5000/

* PyCharm is an Integrated Development Environment (IDE) used in computer programming, specifically for the Python language. It is developed by the Czech company JetBrains.

>> Firstly, I created a database in jsonify format for each album with respect to artist given with unique id and also information about year and one of the trackname with respect to album. The data base is named as musicDB.

>> And then for implement crud operations to the application a music path is given i.e, /music/musictrack .
>> For create,read,update,delete applicaion a post, get, PUT, Delete requests are given with in the code.

The code which is written in python using microframework flask is excuted in Pycharm tool. When you run the application a http://127.0.0.1:5000/ link is generated in the pycharam tool. When you click on the http://127.0.0.1:5000/ link it redirects to web browser. When you go to http://127.0.0.1:5000/music/musictrack you can see the database in the web browser.

>> To verify and validate CRUD operations to the developed application a "Advanced rest client " is a google chrome web extension is used.
By giving http://127.0.0.1:5000/music/musictrack link to advanced rest client you can do all the CRUD operations.
