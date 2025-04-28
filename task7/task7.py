import csv

def getSum(data):
    my_sum = 0
    for i in data:
        my_sum += i
    
    return my_sum
    
def getAvg(data):
    return getSum(data)/len(data)

def getMin(data):
    my_min = data[0]
    for i in data:
        if i < my_min:
            my_min = i;
            
    return my_min

def getMax(data):
    my_max = data[0]
    for i in data:
        if i > my_max:
            my_max = i;
            
    return my_max

infile = open("temperature_data.csv")
reader = csv.reader(infile)

headings = []
headings = next(reader)

data = []

for line in reader:
    # we only care about the temperature value, which is column 1 (indexing at 0)
    data.append(float(line[1]))

# Temporary variables to hold the data
my_avg = getAvg(data)
my_min = getMin(data)
my_max = getMax(data)

# Print data with f-strings
print(f"Average: {my_avg}")
print(f"Min: {my_min}")
print(f"Max: {my_max}")
