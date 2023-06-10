# Task Manager API

The Task Manager API is a simple RESTful API for managing tasks. It allows you to create, retrieve, update, and delete tasks, as well as list all tasks. The API is built using Python and Flask.

## Setup

1. Clone the repository:

```bash
git clone https://github.com/devdusija/task-manager-api.git
```
2. Install Flask
```
pip install flask
```
Run the python file to start a server
```
python app.py
```


The application will be accessible at http://localhost:5000.

# API Endpoints
### List all tasks
Endpoint: GET /tasks
Description: Retrieves a list of all tasks.  
Response: JSON array containing task objects.  
### Create a new task  
Endpoint: POST /tasks
Description: Creates a new task.  
Request body: JSON object containing task details (title, description, due_date).  
Response: JSON object containing the created task.  
### Retrieve a single task  
Endpoint: GET /tasks/{task_id}  
Description: Retrieves a specific task by its ID.  
Response: JSON object representing the task.  
### Update an existing task
Endpoint: PUT /tasks/{task_id}  
Description: Updates an existing task.  
Request body: JSON object containing updated task details (title, description, due_date, status).  
Response: JSON object representing the updated task.  
## Delete a task
Endpoint: DELETE /tasks/{task_id}  
Description: Deletes a specific task by its ID.  
Response: JSON object confirming the deletion.  

# Task Object Structure
A task object has the following properties:

ID: The unique identifier of the task.  
Title: The title or name of the task.  
Description: The description or details of the task.  
Due Date: The due date of the task.  
Status: The status of the task (Incomplete, In Progress, or Completed).  

# Error Handling
The API handles errors gracefully and returns appropriate error responses in case of invalid requests or resource not found.  

# Future Improvements
Here are some potential improvements for the Task Manager API:

1. Implement authentication and authorization mechanisms.  
2. Add pagination support for listing tasks.  
3. Integrate a persistent database for storing tasks.  
4. Implement filtering and sorting options for task retrieval.  
