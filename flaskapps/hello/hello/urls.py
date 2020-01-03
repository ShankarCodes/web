from .app import app as app
from .views import home_page

url = app.add_url_rule

urlpath = [
url('/','home',home_page),

]

