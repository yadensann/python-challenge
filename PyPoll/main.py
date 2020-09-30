#  Py Me up, Charlie (PyPoll)

# Import modules
import csv 
import os 

# Path to csv file
userhome = os.path.expanduser('~')

csvpath = userhome + '/Desktop/python-challenge.git/PyPoll/Resources/electiondata_copy.csv'

data = []
vote_count = []
winner = [] #based on popular vote 
list_of_candidates = [] #who received votes
percentages = []
voting_percentage = []
number_votes = 0
voterID = []
total_vote_count = []
candidates = []

# Opening csv file using csvpath 
with open(csvpath) as csvfile:
# csv reader specifies delimiter and variable that separates data 
    csvreader = csv.reader(csvfile, delimiter = ',')
    next(csvreader, None)
    
    data = list(csvreader)


    for row in data:

            voterID.append(row[0]) 
            # county.append(row[1])
            candidates.append(row[2])

    total_vote_count = len(voterID)
    # print(total_vote_count)    


    number_votes = number_votes + 1
    candidate = row[2]


    if candidate in list_of_candidates:
        candidate_index = list_of_candidates.index(candidate)
        vote_count[candidate_index] = vote_count[candidate_index] + 1
    else:
    # #If name is not in list, append to end of list and adding 1
        list_of_candidates.append(candidate)
        vote_count.append(1)


#  print(total_vote_count) #Total Votes: 3521001

# #Goes through candidate list by increments of 1, accounting for repeat names

max_votes = vote_count[0]
max_index = 0

votes = []
county = []
candidates = []

for count in range(len(list_of_candidates)):

 
    voting_percentage = vote_count[count] / number_votes * 100
    percentages.append(voting_percentage)
# print(percentages)
    if vote_count[count] > max_votes:
        max_votes = vote_count[count]
        # print(max_votes)
        max_index = count

winner = [max_index]
# print(winner)



print(f'Election Results')
print(f'-----------------------------')
print("Total Votes: " + str(total_vote_count))
print(f'-----------------------------')
print(f'Khan: ')
print(f'Correy: ')
print(f"O'Tooley: ")
print(f'-----------------------------')
print("Winner: " + str(winner))