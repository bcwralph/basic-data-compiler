import os

source_1 = "program/data"

append_file = open("appended_data.csv","w")

counter = 0
for i in os.listdir(source_1):
    sf = open(source_1+'/'+i,'r')
    header = sf.readline()
    line = sf.readline()
    if counter == 0: 
        append_file.write(header)
    while line != '':
        append_file.write(line)
        line = sf.readline()
    sf.close()
    counter+=1

append_file.flush()
append_file.close()