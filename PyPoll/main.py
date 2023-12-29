import os
import csv

def array_sum(arr):
    total = 0
    for num in arr:
        total += num
    return total

# Path to collect data from the Resources folder
pto_hours_csv = os.path.join('', 'Resources', 'election_data.csv')
total_votes = 0 
previus_votes = 0
winner = ""
list_votes = []
total = 0

# Read in the CSV file
with open(pto_hours_csv, 'r') as csvfile:
    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')

    header = next(csvreader)

    # Loop through the data
    for row in csvreader:
        total_votes += 1
        # I skip first line(column title) and secund line(initial value)
        if csvreader.line_num > 1:
            for i in range(len(list_votes)):
                if list_votes[i][0] == row[2]:
                    list_votes[i][1]+= 1
                    break
            else:
                list_votes.append([row[2], 1])
                continue
    else:
           # print("Election Results")
       # print("-------------------------")
       # print(f"Total Votes:  {str(total_votes)}")
       # print("-------------------------")
        #for i in range(len(list_votes)):
        #    print(f"{list_votes[i][0]}: {str(round((list_votes[i][1] * 100) / total_votes, 3))}% ({str(list_votes[i][1])})")
        #    if list_votes[i][1] > previus_votes:
       #         previus_votes = list_votes[i][1]
       #         winner = i

       # print("-------------------------")
       # print(f"Winner: {list_votes[winner][0]}")
       # print("-------------------------")


        result = ""
        result += "Election Results\n"
        result += "-------------------------\n"
        result += f"Total Votes:  {str(total_votes)}\n"
        result += "-------------------------\n"
        for i in range(len(list_votes)):
            result += f"{list_votes[i][0]}: {str(round((list_votes[i][1] * 100) / total_votes, 3))}% ({str(list_votes[i][1])})\n"
            if list_votes[i][1] > previus_votes:
                previus_votes = list_votes[i][1]
                winner = i

        result += "-------------------------\n"
        result += f"Winner: {list_votes[winner][0]}\n"
        result += "-------------------------\n"

print(result)  # Output the entire result

# Open the file using "write" mode. Specify the variable to hold the contents
with open(os.path.join("", "analysis", "result.txt"), 'w') as txtfile:

    txtfile.write(result)
