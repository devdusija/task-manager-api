from flask import Flask, jsonify, request

app = Flask(__name__)

tasks = []

@app.route('/tasks',methods=['GET'])
def list():
    return jsonify(tasks)

@app.route('/tasks', methods=['POST'])
def create_task():
    task = {
        'id': len(tasks) + 1,
        'title': request.json.get('title'),
        'description': request.json.get('description'),
        'due_date': request.json.get('due_date'),
        'status': 'Incomplete'
    }
    tasks.append(task)
    return jsonify(task), 201

@app.route('/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    task = next((task for task in tasks if task['id'] == task_id), None)
    if task:
        return jsonify(task)
    else:
        return jsonify({'error': 'Task not found'}), 404
    

@app.route('/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    task = next((task for task in tasks if task['id'] == task_id), None)
    if task:
        task['title'] = request.json.get('title', task['title'])
        task['description'] = request.json.get('description', task['description'])
        task['due_date'] = request.json.get('due_date', task['due_date'])
        task['status'] = request.json.get('status', task['status'])
        return jsonify(task)
    else:
        return jsonify({'error': 'Task not found'}), 404
    
@app.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    task = next((task for task in tasks if task['id'] == task_id), None)
    if task:
        tasks.remove(task)
        return jsonify({'message': 'Task deleted'})
    else:
        return jsonify({'error': 'Task not found'}), 404
if __name__ == '__main__':
    app.run()