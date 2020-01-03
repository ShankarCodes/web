import sys
import os 
import shutil

help = ''' A command Line utility to generate skeletons for flask apps
Usage: sflask.py <projectname>
Example sflask.py blog
'''
def generate_project(projectname):
    if not os.path.exists(projectname):
        os.makedirs(projectname)
    else:
        i = input(projectname+" Already Exists!! Do You Want to Overwrite?[Y/n]")
        if i in ['y','Y','Yes','yes','YES']:
           shutil.rmtree(projectname)           
           os.makedirs(projectname)
    
    os.chdir(projectname)
    os.mkdir('templates')
    
    app = open('app.py','w')
    app.write('''
# A Basic Flask App
from flask import Flask
app = Flask(__name__)
''')
    app.close()
    
    init = open('__init__.py','w')
    init.write('''from .app import app
from . import routes''')
    init.close()
    
    routes = open('routes.py','w')
    routes.write('''from .app import app
from flask import render_template
@app.route('/')
def home_page():
    return render_template('index.html')''')
    routes.close()
    os.chdir('templates')
    
    index = open('index.html','w')
    index.write('''<html>
<title>
Hello
</title>
<body>
<h1>Welcome To Flask</h1>
</body>
</html>
''')
def main():
    if len(sys.argv)>1:
        projectname = sys.argv[1]
        generate_project(projectname)
    else:
        projectname = input("Enter Project Name:")
        generate_project(projectname)
if __name__ == '__main__':
    main()