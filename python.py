import csv
import os

budget_data = os.path.join("Resources", "budget_data.csv")
budget_analysis = os.path.join("analysis", "budget_analysis.txt")

#place holder variables
Months_total = 0
specefic_change = []
list_of_change = []
greatestin = ["", 0]
greatestde = ["", 999999999999999]
total = 0


with open(budget_data) as financiances:
    read = csv.reader(financiances)

    header = next(read)

    first_row = next(read)
    total_months = months_total + 1
    total = total + int(first_row[1])
    prev = int(first_row[1])

    for row in read:

        Months_total = 1 + Months_total 
        total = total + int(row[1])

        change = int(row[1]) - prev
        prev = int(row[1])
        list_of_change = net_change_list + [net_change]
        specefic_change = specefic_change + [row[0]]

        if change > greatestin[1]:
            greatestin[0] = row[0]
            greatestin[1] = change

        
        if change < greatestde[1]:
            greatestde[0] = row[0]
            greatestde[1] = change

  net_avg = sum(list_of_change) / len(list_of_change)

output = (
    f"\nFinancial Analysis\n"
    f"----------------------------\n"
    f"Total Months: {Months_total}\n"
    f"Total: ${total}\n"
    f"Average  Change: ${net_avg:.2f}\n"
    f"Greatest Increase in Profits: {greatestin[0]} (${greatestin[1]})\n"
    f"Greatest Decrease in Profits: {greatestede[0]} (${greatestde[1]})\n")

# Print the output (to terminal)
print(output)

# Export the results to text file
with open(file_to_output, "w") as txt_file:
    txt_file.write(output)
