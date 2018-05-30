from flask import Flask, request
from boltiot import Bolt

bolt = Bolt('7bc48b25-f5c8-4ef3-9477-c599835583da','BOLT3729610')

app = Flask(__name__)

@app.route('/')
def home():
    return "<h1>Welcome to the jungle</h1>"

@app.route('/request_task',methods=['GET','POST'])
def handle_task_request():
    if(request.method == 'POST'):
        command_string = request.form.get('text',None)
        #bolt.serialWrite(str(command_string))
        return "Deva is on his way"

if __name__ == '__main__':
    app.run(debug = True)
