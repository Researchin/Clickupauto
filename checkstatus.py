import requests

# Set the API key and task ID
api_key = "your_api_key"
task_id = "task_id"
# Set the API endpoint
endpoint = f"https://api.clickup.com/api/v2/task/{task_id}"
# Set the headers
headers = {
    "Authorization": f"Token {api_key}",
    "Content-Type": "application/json"
}

# Make the API request
response = requests.get(endpoint, headers=headers)

# Check the status code
if response.status_code == 200:
    # Print the task status
    task = response.json()
    print(task["status"]["name"])
else:
    # Print the error message
    print(response.text)
