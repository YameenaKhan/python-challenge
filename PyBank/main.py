import os
import csv

Pybank_csv = os.path.join(".", "Resources","budget_data.csv")

#Setting empty lists to store values 
months = []
PnlValues = []
ChangesinPNL = []

#Opening and reading Pybank csv file
with open(Pybank_csv) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter= ",")
    #Storing HeaderRow
    header_row = next(csv_file)
    

    for row in csv_reader:
        #Storing Months in a list
        months.append(row[0])
        
        #Storing Profit/loss Values in a list
        PnlValues.append(int(row[1]))

#Getting the total month count in dataset
TotalMonth_count = len(months)

#Getting the Net Total Profit & Loss in the given dataset
NetTotalPnL = sum(PnlValues)

#Running a for loop to get changes in profit and loss from month to month to calculate the average
for v in range(1,len(PnlValues)):
    change = PnlValues[v]-PnlValues[v-1]
    ChangesinPNL.append(change)

#Getting the average change in Profit and Loss               
Average = sum(ChangesinPNL)/len(ChangesinPNL)
Average = round(Average, 2)


#Extracting the Max Change and the corresponding month from the list of ChangesinPNL
MaxChange= max(ChangesinPNL)
MaxIndex = ChangesinPNL.index(MaxChange)+1
MaxMonth = months[MaxIndex]



#Extracting the Min Change and the corresponding month from the list of ChangesinPNL
MinChange = min(ChangesinPNL)
MinIndex = ChangesinPNL.index(MinChange)+1
MinMonth = months[MinIndex]



#Formatting and storing the desired result in a Variable called "result_PyBank"
result_PyBank = f"""
Financial Analysis
-------------------------------
Total Months: {TotalMonth_count}       
Total: ${NetTotalPnL}
Average Change: ${Average}
Greatest Increase in Profits: {MaxMonth} (${MaxChange})
Greatest Decrease in Profits: {MinMonth} (${MinChange})
"""

#Printing Result
print(result_PyBank)

#Exporting result to a Txt.file in the analysis folder
output_path = os.path.join("analysis", "result_PyBank.txt")
with open (output_path, 'w') as textfile:
    textfile.write(result_PyBank)

