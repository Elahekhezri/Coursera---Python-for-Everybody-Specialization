
# Answer:

import re
f = open(file, "r")
txt = f.read()
print (sum([int(x) for x in re.findall("[0-9]+", txt)]))
