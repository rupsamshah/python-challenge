import os
import csv
filename = u'C:\Rupal\AA UNCC Course\Python_homework\python-challenge\PyBank\Resources\/budget_data.csv'

#to open csvfile and reading csvfile
with open(filename) as csvfile:
    csvdata = list(csv.reader(csvfile))[1:] 

#this will print the Financial Analysis in output txt file
with open("analysis/output.txt", "w") as file:
    file.write("Financial Analysis\n--------------------------------\n")

    # The total number of months included in the dataset
    file.write('Total Months: %s\n' % len(csvdata))
    Total = sum([int(i[1]) for i in csvdata])

    file.write('Total: $%s' % Total)
    file.write("\n")

    #The net total amount of "Profit/Losses" over the entire period
    lossbucket = []
    profitbucket = []
    baseamount = int(csvdata[0][1])

    nettotal = []
    for cdata in csvdata[1:]:
        amt = int(cdata[1])
        if amt != baseamount:
            nettotal.append(amt-baseamount)
        if amt < 0:
            lossbucket.append([cdata[0], abs(baseamount - amt)])
        else:
            profitbucket.append([cdata[0], abs(amt -baseamount)])
        baseamount = amt
    
    # The changes in "Profit/Losses" over the entire period, and then the average of those changes
    file.write(f'Average Change: $%.2f\n' % (sum(nettotal)/len(nettotal)))

    # The greatest increase in profits (date and amount) over the entire period
    max_increase_num = max(data[1] for data in profitbucket)
    max_increase_idx = [data[1] for data in profitbucket].index(max_increase_num)
    max_increase_month = profitbucket[max_increase_idx][0]

    # The greatest decrease in profits (date and amount) over the entire period
    max_decrease_num = max(data[1] for data in lossbucket)
    max_decrease_idx = [data[1] for data in lossbucket].index(max_decrease_num)
    max_decrease_month = lossbucket[max_decrease_idx][0]

    #to generate greatest increase and greatest decrease
    file.write("Greatest Increase In Profit : %s ($%s)\n" % (max_increase_month, max_increase_num))
    file.write("Greatest Decrease In Profit : %s ($%s)" % (max_decrease_month, -max_decrease_num))

# to open the ouput.txt file and then printing the data from the file 
with open("analysis/output.txt") as file:
    prtfile = file.read()
print(prtfile)