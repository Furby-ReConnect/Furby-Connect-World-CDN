import requests
import json
from tqdm import tqdm
import os

rootUrl = "https://furbyapp.s3.amazonaws.com/"

with open('output.json', 'r') as file:
    furbyData = json.loads(file.read())


for file in furbyData:
    #if ('staging' in file["Key"] and file["Key"][-1] != '/'):
    if (file["Key"][-1] != '/'):
        print(file["Key"])

        folder = os.path.join('./output/', '/'.join(file["Key"].split('/')[:-1]))
        filePath = os.path.join('./output/', file["Key"])
        os.makedirs(folder, exist_ok=True)

        # Download file
        response = requests.get(rootUrl + file["Key"], stream=True)

        fileSize = response.headers["Content-Length"]

        pBar = tqdm(total=int(fileSize), desc=str(file["Key"]))
        with open(filePath, 'wb') as downloadFile:
            for chunk in response.iter_content(chunk_size=1024):
                downloadFile.write(chunk)
                pBar.update(1024)
        pBar.close()

