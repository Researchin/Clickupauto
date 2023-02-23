import requests
from datetime import datetime, timezone, timedelta

# Set your ClickUp API key and list ID
api_key = "your_api_key"
list_id = "your_list_id"

# Set the new status for tasks that have been open for more than 4 hours
new_status = "COMPLETE"
# Define the ClickUp API endpoint URLs
tasks_url = f"https://api.clickup.com/api/v2/list/{list_id}/task"
update_task_url = "https://api.clickup.com/api/v2/task/"

# Define the headers for the ClickUp API requests
headers = {"Authorization": api_key}

# Get the list of tasks in the specified ClickUp list
response = requests.get(tasks_url, headers=headers)
tasks = response.json()["tasks"]

# Loop through each task and check its creation time
for task in tasks:
    # Get the creation time of the task
    created_time_timestamp = int(task["date_created"][:-3])
    created_time = datetime.fromtimestamp(created_time_timestamp, tz=timezone.utc)

    # Get the current time
    current_time = datetime.now(timezone.utc)
    
    # Calculate the time difference between the current time and the creation time
    time_diff = current_time - created_time
    
    # Check if the time difference is greater than 4 hours
    if time_diff > timedelta(hours=4):
        # Update the task's status
        task_id = task["id"]
        update_data = {"status": new_status}
        update_response = requests.put(f"{update_task_url}{task_id}", json=update_data, headers=headers)