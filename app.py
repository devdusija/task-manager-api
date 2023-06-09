from flask import Flask, jsonify, request

app = Flask(__name__)

task = ["HEllo"]

@app.route('/tasks',methods=['GET'])
def list():
    return jsonify(task)


if __name__ == '__main__':
    app.run()