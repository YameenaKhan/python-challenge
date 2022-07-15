import os
import csv

Pybank_csv = os.path.join(".", "Resources","budget_data.csv")

months = []
NetTotalPnL = 0
PnlValues = []
ChangesinPNL = []

with open(Pybank_csv) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter= ",")
    header_row = next(csv_file)
    #print(header_row)

    for row in csv_reader:
        #Reading Months in a list
        months.append(row[0])
        
        #Reading Profit/loss Values in a list
        PnlValues.append(int(row[1]))

#Getting the total month count in dataset
TotalMonth_count = len(months)


NetTotalPnL = sum(PnlValues)

for v in range(1,len(PnlValues)):
    change = PnlValues[v]-PnlValues[v-1]
    ChangesinPNL.append(change)
                
Average = sum(ChangesinPNL)/len(ChangesinPNL)
Average = round(Average, 2)

#print(Average)

MaxChange= max(ChangesinPNL)
#print(MaxChange)
MaxIndex = ChangesinPNL.index(MaxChange)+1
#print(MaxIndex)
MaxMonth = months[MaxIndex]
#print(MaxMonth)



MinChange = min(ChangesinPNL)
#print(MinChange)
MinIndex = ChangesinPNL.index(MinChange)+1
#print(MinIndex)
MinMonth = months[MinIndex]
#print(MinMonth)


print(TotalMonth_count)
print(NetTotalPnL)
print(Average)
print(MaxChange)
print(MaxMonth)            
print(MinChange)       
print(MinMonth)


print("Financial Analysis")  
print("-------------------------------") 
print(f"Total Months: {TotalMonth_count}")
print(f"Total: ${NetTotalPnL}")
print(f"Average Change: ${Average}")
print(f"Greatest Increase in Profits: {MaxMonth} (${MaxChange})")
print(f"Greatest Decrease in Profits: {MinMonth} (${MinChange})")

result = f"""
Financial Analysis
-------------------------------
Total Months: {TotalMonth_count}       
Total: ${NetTotalPnL}
Average Change: ${Average}
Greatest Increase in Profits: {MaxMonth} (${MaxChange})
Greatest Decrease in Profits: {MinMonth} (${MinChange})
"""

print(result)

output_path = os.path.join("analysis", "result.txt")
with open (output_path, 'w') as textfile:
    textfile.write(result)

    