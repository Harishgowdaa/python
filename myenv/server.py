from flask import Flask, jsonify
from flask_cors import CORS
import re, uuid

app=Flask(__name__)
CORS(app)
@app.route('/mac')
def welcome():
    data =':'.join(re.findall('..', '%012x' % uuid.getnode()))
    return jsonify(data) 
if __name__=='__main__':
    app.run(debug=True)


# import re, uuid

# data_to_pass = ':'.join(re.findall('..', '%012x' % uuid.getnode()))
# print(data_to_pass)