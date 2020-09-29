# # Py Me Up, Charlie (PyBank)

# # Import modules 
# # Change directory
import csv
import os

# # Path to csv file 
userhome = os.path.expanduser('~')

csvpath = userhome + '/Desktop/python-challenge.git/PyBank/Resources/budgetdata_hw.csv'


# Opening CSV file using csvpath
with open(csvpath) as csvfile:

#CSV reader specifies delimiter and variable that holds places
	csvreader = csv.reader(csvfile, delimiter = ',')
	next(csvreader, None)
	# csvfile.readline(0)
	data = list(csvreader)

	month = []
	revenue = []
	total_revenue = []
	change_in_revenue = []
	average_change = []
	greatest_increase = []
	greatest_decrease = []

	# print(data)

	for row in data:
	#Total months over entire period
		month.append(row[0])
		revenue.append(row[1])
	# print(revenue)

	#Total revenue over entire period 
	revenue_value = map(int,revenue)
	total_revenue = (sum(revenue_value))
	# print(total_revenue)

	# Average change in 'Profit/Losses over entire period
	for i in range(len(revenue) - 1):
		profit_loss = int(revenue [i + 1]) - int(revenue[i])
		change_in_revenue.append(profit_loss)
	final_revenue = sum(change_in_revenue)
	# print(final_revenue)


	average_change = (final_revenue) / len(change_in_revenue)
	# print(average_change)

# Greatest Increase value	
	greatest_increase = max(change_in_revenue)
	n = change_in_revenue.index(greatest_increase)
	greatest_increase_month = month[n + 1]
	# print(greatest_increase)

# Greatest Decrease value
	greatest_decrease = min(change_in_revenue)
	j = change_in_revenue.index(greatest_decrease)
	greatest_decrease_month = month[j + 1]
	# print(greatest_decrease)

	# PRINT STATEMENTS
	print(f'Financial Analysis')
	print(f'-----------------------------')
	print("Total Count of Months: " + str(len(month)))
	print("Net Total Amount: " + '$'+ str(total_revenue))
	print("Average Change: " + '$' + str(round(average_change, 2)))
	print("Greatest Increase in Profits: " + (greatest_increase_month) + ' ' + "(" + '$' + str(greatest_increase) + ")" )
	print("Greatest Decrease in Profits: " + (greatest_decrease_month) + ' ' + "(" + '$' + str(greatest_decrease) + ")" )