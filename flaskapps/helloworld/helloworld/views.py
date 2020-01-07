from flask import render_template
from flask import Response

def home_page():
    return Response(render_template('index.html'),status=200,mimetype='text/html')