import os
import json
import time
from nomie_tool import NomieComp
from flask import json
from flask import jsonify
from flask import Flask
from flask import request

app = Flask(__name__)

# Initiate NomieComp object
myNomie = NomieComp()

@app.route("/")
def main():
    return "Nomie computation interface."

def get_parameter(request_data, name):
    try:
        return request_data.args.get(name)
    except:
        try:
            return request_data.json[name]
        except:
            return None

def includes_required(parameters):
    cleared = True
    for i in parameters:
        if i == None:
            cleared = False
    return cleared

@app.route("/count", methods=['GET'])
def parse_request():
    toReturn = None
    # Possible parameters w/ default values
    label = None
    start = None
    end = time.time()
    cached = False
    # Retreive actual values
    label = get_parameter(request, 'label')
    start = get_parameter(request, 'start')
    inputEnd = get_parameter(request, 'end')
    if inputEnd:
        end = inputEnd
    else:
        end = None
    if includes_required([label, start]):
        data = myNomie.count(label, start, end, cached)
        if not data['count'] == None:
            toReturn = { 'success': True, 'count': data['count'] }
        else:
            toReturn = { 'success': False, 'message': data['message'] }
    else:
        toReturn = { 'success': False, 'message': 'Missing required parameters' }
    return json.dumps(toReturn)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 4000))
    app.run(host='0.0.0.0', port=port, debug=True)
