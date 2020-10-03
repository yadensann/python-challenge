#  Py Me up, Charlie (PyPoll)

# Import modules
import csv 
import os 

# Path to csv file
userhome = os.path.expanduser('~')

csvpath = userhome + '/Desktop/python-challenge.git/PyPoll/Resources/electiondata_copy.csv'

data = []
vote_count = []
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

# print(voterID[0:5])
# print(candidates[0:5])

vote_count={}
for each_candidate in candidates: 
    # each_candidate='khan'
    # if 'khan' in vote_count
    # then add 1 to vote_count['khan'] -> vote_count['khan'] is the value and the current vote count for 'khan'
    # else -> meaning 'khan' is not in vote_count
    # then add 'khan' as key and set 1 as value -> meaning first time he's getting a vote

    if each_candidate in vote_count: 
        # assign vote_count for that candidate to be itself plus 1
        vote_count[each_candidate]=vote_count[each_candidate]+1
    else: 
        vote_count[each_candidate]=1
    # print(vote_count)

# print(f'FINAL VOTE COUNT: {vote_count}')
# initiate a variable to store highest vote
max_vote=0
# initiate a variablle to store name
max_name=''
# iterate through the keys of vote_count
for each_candidate in vote_count: 
    # each_candidate = 'khan'
    # pct_vote=vote_count['khan'] -> 220K
    #   / total_vote_Count
    # print pct_vote each time
    total_votes = vote_count[each_candidate]
    pct_vote=total_votes/total_vote_count*100
    # print(f'{each_candidate} received {round(pct_vote, 2)}% of vote')
    # check if the vote count for current candidate in the loop is greater than the current max vote
    # if yes, then time to have a new winner -> set max vote and max name to new values
    # else
    if vote_count[each_candidate]>max_vote: 
        max_name=each_candidate
        max_vote=vote_count[each_candidate]



    print(f' {each_candidate} received {round(pct_vote, 2)}% of vote with {total_votes} total votes')

print(f'-----------------------------')

print(f'Total vote count is {total_vote_count}. ')

print(f'-----------------------------')
print(f'The winner is {max_name} with {vote_count[max_name]} votes')
