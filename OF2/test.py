import re

#def arc_adjust(lines, vertices):
   
   # return lines

with open("/Users/treygower/Desktop/blockMeshDict1.example", "r") as file:
    lines = file.readlines()

arcs = lines[94:126]
pattern = r'arc (\d+) (\d+)'
match = re.search(pattern, arcs[18])
arc = [match.group(0),int(match.group(1)),int(match.group(2))]
print(arc)
#values = r' \d+ \d+'
#print(match.groups())

#calculate midpoints

#arc_adjust(lines)

#with open("/Users/treygower/Desktop/blockMeshDict123_updated.txt", "w") as file:
#        file.write()
