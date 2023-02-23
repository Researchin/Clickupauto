import requests
import datetime
import json

# Set up the API endpoint and parameters
api_key = 'your_api_key'
list_id ='your_list_id'
endpoint = f'https://api.clickup.com/api/v2/list/{list_id}/task'

# Set up the request headers with the API key
headers = {
    'Authorization': api_key,
    'Content-Type': 'application/json'
}

# Get the current time
now = datetime.datetime.now()

# Send the GET request to get all tasks in the list
response = requests.get(endpoint, headers=headers)

# Check if the request was successful
if response.status_code == 200:
    # Get the JSON response data
    data = response.json()

    # Loop through the tasks
    for task in data['tasks']:
        # Get the time the task was created
        created_time = datetime.datetime.fromtimestamp(int(task['date_created'])/1000)

        # Check if 4 hours have passed since the task was created
        if now - created_time >= datetime.timedelta(minutes=2):
            # Add a comment to the task
            task_id = task['id']
            comment_text = 'Task has been open for more than 2 minutes'

            # Set up the request data with the comment text
            data = {'comment_text': comment_text}

            # Send the POST request to add the comment to the task
            comment_endpoint = f'https://api.clickup.com/api/v2/task/{task_id}/comment'
            comment_response = requests.post(comment_endpoint, headers=headers, data=json.dumps(data))

            # Check if the comment was added successfully
            if comment_response.status_code == 200:
                print(f'Comment added to task {task_id}')
            else:
                print(f'Error adding comment to task {task_id}: {comment_response.text}')
else:
    print(f'Error getting tasks: {response.text}')
