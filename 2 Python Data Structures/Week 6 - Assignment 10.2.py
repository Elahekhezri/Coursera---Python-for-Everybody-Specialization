# Description: Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for each of the messages. 
  ## You can pull the hour out from the 'From ' line by finding the time and then splitting the string a second time using a colon.
  ## From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
  ## Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below.
  
  
  
  
  
 # Answer:

name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
fh = open(name)
count = dict()

for line in fh:
    if line.startswith("From "):
        time = line[line.find(" "):line.find(":")]
        lines = time.strip().split(" ")
        hour = lines[-1]
        count[hour] = count.get(hour, 0) + 1
items = list(count.items())
items.sort()
for hour, dis in items:
    print(hour, dis)
        
