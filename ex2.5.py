import json
import timeit

"""
This function iterates through the json file, looking for the 'size' field in 'payload'. 
It then changes the value of the 'size' field to n.
"""

def mod_size(doc, n):
    for object in doc:
        # Objects are dicts
        for i in object:
            if i == "payload":
                if "size" in object[i]:
                    # size found inside of payload
                    object[i]["size"] = n


read = open(file="large-file.json", mode='r', encoding="UTF-8")

doc = json.load(read)
elapsed = timeit.timeit(lambda : mod_size(doc, 42), number=10)
average = elapsed / 10
print("Average time for modifying every size field in the file: ", average)


doc.reverse()
json_obj = json.dumps(doc, indent=4)
file = open(file="output.2.3.json", mode='w', encoding="UTF-8")
file.write(json_obj)