from flask import Flask, abort
from flask import jsonify
from flask import request

app = Flask(__name__)

musicDB=[
     {
         'id':'1',
         'artist':'Micheal Jackson',
         'year':'1982',
         'albumname':'thriller',
         'trackname':'The Girl Is Mine'
     },
     {
         'id':'2',
         'artist':'Micheal Jackson',
         'year':'2001',
         'albumname':'invincible',
         'trackname':'heart breaker'
     },
     {
         'id':'3',
         'artist':'Micheal Jackson',
         'year':'1987',
         'albumname':'bad',
         'trackname':'just good friends'
     },
     {
         'id':'4',
         'artist':'Shakira',
         'year':'2010',
         'albumname':'sale el sol',
         'trackname':'loca'
     },
     {
         'id':'5',
         'artist':'Shakira',
         'year':'2001',
         'albumname':'laundry service',
         'trackname':'objection'
     },
{
         'id':'6',
         'artist':'Shakira',
         'year':'2014',
         'albumname':'shakira',
         'trackname':'empire'
     },
{
         'id':'7',
         'artist':'madonna',
         'year':'2015',
         'albumname':'rebel heart',
         'trackname':'devil pray'
     },
    {
        'id': '8',
        'artist': 'pink floyd',
        'year': '2014',
        'albumname': 'the endless river',
        'trackname': 'things left unsaid'
    },
{
         'id':'9',
         'artist':'Elton John',
         'year':'1993',
         'albumname':'duets',
         'trackname':'tear drops'
     },
{
         'id':'10',
         'artist':'led zeppelin',
         'year':'2003',
         'albumname':'how the west was won',
         'trackname':'immigrant song'
     },
{
         'id':'11',
         'artist':'justin bieber',
         'year':'2011',
         'albumname':'under the mistletoe',
         'trackname':'fa la la'
     },
{
         'id':'12',
         'artist':'pitbull',
         'year':'2015',
         'albumname':'dale',
         'trackname':'como yo le doy'
     },

 ]

@app.route('/music/musictrack',methods=['GET'])
def getAllTracks():
    return jsonify({'music':musicDB})

@app.route('/music/musictrack/<trackId>',methods=['GET'])
def getTracksById(trackId):
    usr = [ music for music in musicDB if (music['id'] == trackId) ]
    return jsonify({'music':usr})

@app.route('/music/musictrack',methods=['POST'])
def createTracks():
    dat = {
    'id':request.json['id'],
    'artist':request.json['artist'],
    'year':request.json['year'],
    'albumname': request.json['albumname'],
    'trackname': request.json['trackname']
    }
    musicDB.append(dat)
    return jsonify(dat)


@app.route('/music/musictrack/<trackId>',methods=['PUT'])
def updateTracksById(trackId):
    usr = [ music for music in musicDB if (music['id'] == trackId) ]
    if 'artist' in request.json :
        usr[0]['artist'] = request.json['artist']
    if 'year' in request.json:
        usr[0]['year'] = request.json['year']
    if 'albumname' in request.json:
        usr[0]['albumname'] = request.json['albumname']
    if 'trackname' in request.json:
        usr[0]['trackname'] = request.json['trackname']
    return jsonify({'emp':usr[0]})

@app.route('/music/musictrack/<trackId>',methods=['DELETE'])
def deleteTracksById(trackId):
    usr = [music for music in musicDB if (music['id'] == trackId) ]

    if len(usr) == 0:
       abort(404)

    musicDB.remove(usr[0])
    return jsonify({'response':'Success'})


@app.route('/')
def hello_world():
    return 'go to http://127.0.0.1:5000/music/musictrack'


if __name__ == '__main__':
    app.run()
