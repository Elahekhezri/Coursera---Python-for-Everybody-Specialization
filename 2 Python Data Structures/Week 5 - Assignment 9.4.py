# Description: Write a program to read through the mbox-short.txt and figure out who has sent the greatest number of mail messages.
  ## The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail. 
  ## The program creates a Python dictionary that maps the sender's mail address to a count of the number of times they appear in the file. 
  ## After the dictionary is produced, the program reads through the dictionary using a maximum loop to find the most prolific committer.
  
 

# Answer:

name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
fh = open(name)
count = dict()


for line in fh:
    if line.startswith("From "):
        lst = line.split()
        sender = lst[1]
        count[sender] = count.get(sender,0) + 1

for key in count:
    if count[key] == max(count.values()):
        print(key, count[key])
