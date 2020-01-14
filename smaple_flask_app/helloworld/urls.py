from .app import app as app
from . import viewsw
from . import api

url = app.add_url_rule

API = '/api/v1'

urlpath = [
url('/','home',views.home_page),
url(API+'/<username>/posts/','get_posts',api.get_posts),
url(API+'/<username>/posts/<i>','get_post',api.get_post),
]

