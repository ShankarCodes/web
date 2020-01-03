from flask import Flask,request,jsonify,redirect,make_response
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from mhelp import MDB
from bson.json_util import dumps
from bson.json_util import loads
engine = MDB('flask_api','test')

udb={
	'shankar':["My First Post","The Second in the Series","The Third in the Series"],
	'roopa':['Shankar is powerful','Hello How are you'],
	'hari':['Shankar is great','whitey eats a lot'],
	'whitey':['I like food','I like Chappati','I like biscut','I like rats']
}


app = Flask(__name__)
limiter = Limiter(
    app,
    key_func=get_remote_address,
    default_limits=['1 per second',]#"200 per day", "50 per hour"]
)

limiter.init_app(app)

@app.route('/')
def home_page():
    return "The Home Page"

@app.route('/api/v1/<username>/post/<int:postid>/')
#@limiter.limit('10 per 10 seconds')
def get_post(username,postid):
	try:
		tr = udb[username][postid-1]
		return jsonify(tr)
	except:
		return "Not Found"

@app.route('/api/v1/<username>/posts/')
def get_all_posts(username):
	try:
		tr = udb[username]
		return jsonify(tr)
	except:
		return "Not Found"

def change(x):
    del x['_id']
    return x

@app.route('/api/v1/')
def allget():
    udb = [i for i in map(change,[row for row in engine.get_many()])]
    return jsonify(udb)

@app.route('/api/v1/<username>/post/new/')
def add_post(username):
	try:
		if request.args.get('content'):
		    udb[username].append(request.args.get('content'))
		    return redirect(f'/api/v1/{username}/post/{len(udb[username])}')
		else:
			return make_response("Bad Request",401)
	except:
		return "Bad Request"
if __name__=='__main__':
    app.run(debug=True)