from flask import Flask, request
from boltiot import Bolt

bolt = Bolt('<your-Bolt-API-Key>','<your-Bolt-Device ID>')

app = Flask(__name__)

@app.route('/test')
def home():
    return "<h1>Welcome to the jungle</h1>"

@app.route('/',methods=['GET','POST'])
def handle_task_request():
    if(request.method == 'POST'):
        command_string = request.form.get('text',None)
        bolt.serialWrite(str(command_string))
        return "Your wish is my command"

if __name__ == '__main__':
    app.run(debug = True)
