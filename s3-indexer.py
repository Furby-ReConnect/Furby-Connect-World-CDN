import xml.etree.ElementTree as xml
import requests
import json

url = "https://furbyapp.s3.amazonaws.com/?marker="
nextURL = url
depth = 0

namespaces = {
    "amazon": "http://s3.amazonaws.com/doc/2006-03-01/"
}
contentsList = []

while True:
    depth += 1
    print("Depth:", depth)
    print("URL:", nextURL)
    xmlData = xml.fromstring(requests.get(nextURL).content)

    isTruncated = xmlData.find("amazon:IsTruncated", namespaces)
    contents = xmlData.findall("amazon:Contents", namespaces)

    for contentThing in contents:
        contentsList.append({
            "Key": contentThing.find("amazon:Key", namespaces).text,
            "LastModified": contentThing.find("amazon:LastModified", namespaces).text,
            "ETag": contentThing.find("amazon:ETag", namespaces).text,
            "Size": contentThing.find("amazon:Size", namespaces).text,
            "StorageClass": contentThing.find("amazon:StorageClass", namespaces).text,
#            "OwnerID": contentThing.find("amazon:Owner", namespaces).find("amazon:ID", namespaces).text,
#            "OwnerDisplayName": contentThing.find("amazon:Owner", namespaces).find("amazon:DisplayName", namespaces).text,
        })

    if (isTruncated.text == 'true'):
        #nextURL = url + xmlData.find("amazon:NextMarker", namespaces).text
        nextURL = url + contentsList[-1]["Key"]
    else:
        break

print("Writing to JSON...")
with open('./output.json', 'w', encoding='utf8') as file:
    file.write(json.dumps(contentsList, indent=2))