import mhelp

from flask import jsonify
from flask import request,make_response

db = mhelp.MDB("blog","posts")

def get_posts(username):
    response = db.get({'name':username})
    i = str(response.pop('_id'))
    response['id'] = i
    response['link'] = request.base_url + i
    return jsonify(response)
    
def get_post(username,i):
    try:
        res = db.get_by_id(i)
    except:
        return jsonify({"error":"bad request","message":"Invalid Id"}),400
    res.pop('_id')
    return jsonify(res)