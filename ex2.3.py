import json

read = open(file="large-file.json", mode='r', encoding="UTF-8")

doc = json.load(read)
for object in doc:
    # Objects are dicts
    for i in object:
        if i == "payload":
            if "size" in object[i]:
                # size found inside of payload
                object[i]["size"] = 42
            """
            Comment!!!!
            
            if "pull_request" in object[i]:
                if "head" in object[i]["pull_request"]: 
                    if "repo" in object[i]["pull_request"]["head"]:
                        if "size" in object[i]["pull_request"]["head"]["repo"]:
                            # Found size inside of object[i]["pull_request"]["head"]["repo"]
                            object[i]["pull_request"]["head"]["repo"]["size"] = 42
            """
doc.reverse()
json_obj = json.dumps(doc, indent=4)
file = open(file="output.2.3.json", mode='w', encoding="UTF-8")
file.write(json_obj)