import subprocess,os
config = { 
    'FLASK_ENV':'DEVELOPMENT',
    'FLASK_APP':'shankapp',
    'FLASK_DEBUG':'1',
    
    }
    


for key in config:
    os.environ[key] = config[key]

subprocess.run(r'run.bat')