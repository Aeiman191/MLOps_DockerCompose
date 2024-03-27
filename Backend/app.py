from flask import Flask, request
from pymongo import MongoClient

app = Flask(__name__)
client = MongoClient('mongodb', 27017)
db = client.webapp

@app.route('/submit', methods=['POST'])
def submit_data():
    data = request.json
    db.users.insert_one(data)
    return 'Data submitted successfully!'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
