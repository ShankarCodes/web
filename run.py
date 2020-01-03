import subprocess,os
config = { 
    'path1':'path1value',
    'path2':'path2value',
    'username':'shankar',
    'password':'asmaplepassword',
    
    }
    


for key in config:
    os.environ[key] = config[key]
    
subprocess.run('run.bat')