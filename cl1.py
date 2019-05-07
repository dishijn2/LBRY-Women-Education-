import requests
url = "https://spee.ch/api/claim/long-id"

r = requests.post(url,{"claimId":"f","claimName":"monibu"})