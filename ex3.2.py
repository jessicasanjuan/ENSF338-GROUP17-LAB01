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

avgtimes = []
numrecords = [1000, 2000, 5000, 10000]

for i in numrecords:
    avgtimes.append(timeit.timeit(lambda : mod_size_custom(doc, 42, i), number=100) / 100)

slope, intercept = np.polyfit(numrecords, avgtimes, 1)
plt.scatter(numrecords, avgtimes)
linevalues = [slope * x + intercept for x in numrecords]
plt.plot(numrecords, linevalues, 'r')
plt.xlabel("Number of Records")
plt.ylabel("Processing time (s)")
plt.savefig("output.3.2.png")

print("The linear model is: t = %.2e * n + %.2e" % (slope, intercept))

doc.reverse()
json_obj = json.dumps(doc, indent=4)
file = open(file="output.2.3.json", mode='w', encoding="UTF-8")
file.write(json_obj)