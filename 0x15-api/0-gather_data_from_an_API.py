import sys
import requests

# Check if employee ID argument is provided
if len(sys.argv) < 2:
    print("Please provide the employee ID as an argument.")
    exit()

employee_id = sys.argv[1]
base_url = "https://jsonplaceholder.typicode.com"

# Send GET request to retrieve employee info and TODO list
try:
    employee_response = requests.get(f"{base_url}/users/{employee_id}")
    todo_response = requests.get(f"{base_url}/todos?userId={employee_id}")
except requests.exceptions.RequestException as e:
    exit()

# Check if the requests were successful
if employee_response.status_code != 200:
    exit()

if todo_response.status_code != 200:
    exit()

employee_info = employee_response.json()
todo_list = todo_response.json()

# Count the number of completed and total tasks
total_tasks = len(todo_list)
completed_tasks = len([task for task in todo_list if task['completed']])

# Print employee TODO list progress
print(f"Employee {employee_info['name']} is done with tasks({completed_tasks}/{total_tasks}):")

# Print titles of completed tasks
for task in todo_list:
    if task['completed']:
        print(f"\t{task['title']}")

