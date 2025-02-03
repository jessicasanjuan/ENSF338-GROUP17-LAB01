import json
import timeit
import matplotlib.pyplot as plt
import numpy as np

"""
This function iterates through the entire json file, looking for the 'size' field in 'payload'. 
It then changes the 'size' field to n.
"""

def mod_size(doc, n):
    for object in doc:
        # Objects are dicts
        for i in object:
            if i == "payload":
                if "size" in object[i]:
                    # size found inside of payload
                    object[i]["size"] = n


"""
This function iterates through the entire json file, looking for the 'size' field in 'payload'. 
It then changes the 'size' field to n. After 'max' records have been processed, the 
function returns.
"""

def mod_size_custom(doc, n, max):
    rec = 0
    for object in doc:
        # Objects are dicts
        for i in object:
            if i == "payload":
                if "size" in object[i]:
                    # size found inside of payload
                    object[i]["size"] = n
        rec += 1
        if rec == max:
            return

read = open(file="large-file.json", mode='r', encoding="UTF-8")
doc = json.load(read)
times = timeit.repeat(stmt= lambda: mod_size_custom(doc, 42, 1000), repeat=1000, number=1)
plt.hist(x=times, range=(0.00015, 0.0004))
plt.xlabel("Processing Time")
plt.ylabel("Number of measurements")
plt.savefig("output.3.3.png")

doc.reverse()
json_obj = json.dumps(doc, indent=4)
file = open(file="output.2.3.json", mode='w', encoding="UTF-8")
file.write(json_obj)