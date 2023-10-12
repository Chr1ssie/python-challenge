import os
import csv

# Files to load and output
file_to_load = os.path.join("Resources/budget_data.csv")
file_to_output = os.path.join("analysis/budget_analysis.txt")

totalMonths = 0
prevNet = 0
monthToMonthChange = []
netChangeList = []
netTotal = 0
greatestincrease =["", 0] 
greatestDecrease =["",9999999999999999999999]
netTotal = 0


with open (file_to_load) as net_data:
    csv_reader = csv.DictReader(net_data)

    for row in csv_reader:
        
        totalMonths = totalMonths + 1
        netTotal = netTotal + int(row["Profit/Losses"])

        netChange = int(row["Profit/Losses"]) - prevNet
        prevNet = int(row["Profit/Losses"])
        netChangeList = netChangeList + [netChange]
        monthToMonthChange = monthToMonthChange + [row["Date"]]

        if (netChange > greatestincrease[1]):
            greatestincrease[0] = row["Date"]
            greatestincrease[1] = netChange

            
        if (netChange < greatestDecrease[1]):
            greatestDecrease[0] = row["Date"]
            greatestDecrease[1] = netChange

            netAverage = sum(netChangeList)/len(netChangeList)

            output = (
                f"\nFinancial Analysis\n"
                f"----------------------------\n"
                f"Total Months: {totalMonths}\n"
                f"Total Net: ${netTotal}\n"
                f"Average Net Change: ${netAverage}\n"
                f"Greatest Increase in Profit: {greatestincrease[0]} (${greatestincrease[1]})\n"
                f"Greatest Decrease in Profit: {greatestDecrease[0]} (${greatestDecrease[1]})\n"
            )

    print(output)


with open(file_to_output, "w") as txt_file:
    txt_file.write(output)
