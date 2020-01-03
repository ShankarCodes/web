import sys
import subprocess
import os 
def handle(i):
    if i == 'help':
        print('runserver     :To Run the Server')
    elif i == 'runserver':
        config = { 
        'FLASK_ENV':'DEVELOPMENT',
        'FLASK_APP':'shankapp',
        'FLASK_DEBUG':'1',
        }
        for key in config:
            os.environ[key] = config[key]
        subprocess.run(r'run.bat')
    else:
        os.system(i)
        
print('Flask Manager')
print('Version 1.0.0')
print('©Shankar 2020. All Rights Reserved')

while True:
    try:
        inp = input('Fmanage>')
        handle(inp)
    except:
        input('Press any key to continue.....')
        
    
    
