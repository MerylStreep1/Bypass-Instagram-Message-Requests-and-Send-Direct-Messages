import requests

class InstagramAPI:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.api_url = "https://graph.instagram.com/v13.0"

    def login(self):
        # Login to Instagram API
        response = requests.post(f"{self.api_url}/access_token", data={
            "client_id": self.username,
            "client_secret": self.password,
            "grant_type": "client_credentials"
        })
        self.access_token = response.json()["access_token"]

    def send_direct_message(self, recipient_username, message):
        # Send direct message to recipient
        response = requests.post(f"{self.api_url}/direct_v2/threads", headers={
            "Authorization": f"Bearer {self.access_token}"
        }, data={
            "recipient_users": [recipient_username],
            "thread_type": "generic",
            "generic_thread": {
                "text": message
            }
        })
        return response.json()

# Example usage
api = InstagramAPI("your_username", "your_password")
api.login()
api.send_direct_message("recipient_username", "Hello, this is a direct message!")
