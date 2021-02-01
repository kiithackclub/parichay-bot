import requests
from urllib.parse import quote

class Airtable:
    def __init__(self, API_KEY, BASE_URL, workspace_id):
        self.API_KEY = API_KEY
        self.BASE_URL = BASE_URL
        self.workspace_id = workspace_id
    
    def get_members_by_discord_id(self, discord_id, table_id):
        discord_id = quote(discord_id)
        query = f"?fields%5B%5D=notes&filterByFormula=(%7Bdiscord%7D+%3D+%27{discord_id}%27)"
        url = self.BASE_URL + "/" + self.workspace_id + "/" + table_id + "/" + query
        headers = {
            "Authorization": "Bearer " + self.API_KEY
        }
        return requests.get(url, headers=headers)
    