import json
from pathlib import Path

file_name = Path(__file__).parent.parent/"testdata"/"credentials.json"

class DataReader:

    def credentials(self):
        with open(file_name,"r") as file:
            data = json.load(file)
            return data["userCredentials"]
            # user_email = data["userCredentials"][0]["userEmail"]
            # password = data["userCredentials"][0]["password"]


