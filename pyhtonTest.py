import requests
import webbrowser

# List of test users with their user IDs (pins)
user_ids = [
    12345, 12346, 12347, 12348, 12349, 12350, 12351, 12352, 12353, 12354,
    12355, 12356, 12357, 12358, 12359, 12360, 12361, 12362, 12363, 12364,
    12365, 12366, 12367, 12368, 12369, 12370, 12371, 12372, 12373, 12374
]



for user_id in user_ids:
    webbrowser.open(f"http://localhost:3000/player/?pin={user_id}")
