# What was learned

with open tells python to acces a file within the brackets and w puts the function into write mode. 

json.dump creates a string out of the tasks list and then writes into the decided file. 
json.dump combines json.dumps (creates json string) and file.write (writing to file)

json.load should be used rather than file.read() as this will ensure that the program reads the list as a list and not a string