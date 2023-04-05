import os 
import csv
filename = "C:\Rupal\AA UNCC Course\Python_homework\python-challenge\PyPoll\Resources\election_data.csv"

# opens the csv file and then reads the data in file 
with open(filename) as csvfile:
    csvdata = list(csv.reader(csvfile))[1:]

#all the value output are stored in output.txt file 
with open("analysis/output.txt", "w") as file:
   #The total number of votes cast
    totalvotes = len(csvdata)
    file.write(f'Election Results\n-------------------------------------------\n')
    file.write (f'Total Votes : %s \n' % totalvotes)
    file.write("-------------------------------------------\n")
    candidate = {}

    #loop is created to count complete list of candidates who received votes
    for cdata in csvdata:
        cname = cdata[2]
        if cname in candidate:
            candidate [cname] += 1
        else:
            candidate[cname] = 1  

    #The percentage of votes and total no of votes each candidate won which is stored in output.txt file 
    for c , v in candidate.items():
        file.write( f'%s: %.3f%% (%s)\n' % (c, (v/totalvotes * 100), v) )

    file.write(f'\n-------------------------------------------\n')
    #The winner of the election based on popular vote
    file.write('Winner: ' + max(candidate, key=candidate.get))
    file.write(f'\n-------------------------------------------')

#open the ouptut.txt file and read and print the data 
with open("analysis/output.txt") as file:
    prtfile = file.read()
print(prtfile)
