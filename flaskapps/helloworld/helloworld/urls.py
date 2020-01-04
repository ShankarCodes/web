from .app import app as app
from .views import home_page
from . import api
url = app.add_url_rule

urlpath = [
url('/','home',api.get_post),

]

