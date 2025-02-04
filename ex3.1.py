import json
import matplotlib.pyplot as plt

# Load data from the JSON file
with open('internetdata.json', 'r') as file:
    data = json.load(file)

# Separate the data into two groups
below_10000 = [item['internetuserate'] for item in data if item['incomeperperson'] 
               is not None and item['incomeperperson'] < 10000 and item['internetuserate'] is not None]
above_or_equal_10000 = [item['internetuserate'] for item in data if item['incomeperperson'] 
                        is not None and item['incomeperperson'] >= 10000 and item['internetuserate'] is not None]

# Plot histogram for countries with income below 10,000
plt.figure()
plt.hist(below_10000, bins=20, edgecolor='black')
plt.title('Internet Usage for Countries with Income < 10,000')
plt.xlabel('Internet Usage Rate (%)')
plt.ylabel('Frequency')
plt.savefig('hist1.png')
plt.close()

# Plot histogram for countries with income at or above 10,000
plt.figure()
plt.hist(above_or_equal_10000, bins=20, edgecolor='black')
plt.title('Internet Usage for Countries with Income >= 10,000')
plt.xlabel('Internet Usage Rate (%)')
plt.ylabel('Frequency')
plt.savefig('hist2.png')
plt.close()
