import os
import csv

def array_sum(arr):
    total = 0
    for num in arr:
        total += num
    return total

# Path to collect data from the Resources folder
pto_hours_csv = os.path.join('', 'resources', 'budget_data.csv')
total_month = 0 
previous_value = 0
list_changes = []
list_month = []
result = ""
total = 0

# Read in the CSV file
with open(pto_hours_csv, 'r') as csvfile:
    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')

    header = next(csvreader)

    # Loop through the data
    for row in csvreader:
        total_month += 1
        # I skipped first line(column title) and second line(initial value)
        if csvreader.line_num > 2:
            list_changes.append(int(row[1]) - previous_value)
            list_month.append(row[0])

        previous_value = int(row[1])
        total += int(row[1])
    
    else:
        # print(f"Financial Analysis")
        # print(f"----------------------------")
        # print(f"Total Months: {str(total_month)}")
        # print(f"Total: ${str(total)}")
        # print(f"Average Change: ${str(round(array_sum(list_changes)/len(list_changes), 2))}")
        # print(f"Greatest Increase in Profits: ${list_month[list_changes.index(max(list_changes))]} (${str(max(list_changes))})")
        # print(f"Greatest Decrease in Profits: ${list_month[list_changes.index(min(list_changes))]} (${str(min(list_changes))})")
        result = "Financial Analysis\n"
        result += "----------------------------\n"
        result += "Total Months: "+str(total_month)+"\n"
        result += "Total: $"+str(total)+"\n"
        result += "Average Change: $"+str(round(array_sum(list_changes)/len(list_changes), 2))+"\n"
        result += "Greatest Increase in Profits: "+list_month[list_changes.index(max(list_changes))]+" ($"+str(max(list_changes))+")\n"
        result +="Greatest Decrease in Profits: "+list_month[list_changes.index(min(list_changes))] +" ($"+str(min(list_changes))+")\n"
        print(result)

# Open the file using "write" mode. Specify the variable to hold the contents
with open(os.path.join("", "analysis", "result.txt"), 'w') as txtfile:

    txtfile.write(result)

