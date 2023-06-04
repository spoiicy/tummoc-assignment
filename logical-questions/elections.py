candidates = {
        "akshit":0,
        "tarun":0,
        "ahna":0
    }


def voting(name):
    if name in candidates:
        candidates[name] +=1
    else:
        print(name,"is candidate name")
def print_winner():
    maxi = -1
    winners = set()
    for name,votes in candidates.items():
        if(votes > maxi): 
            maxi = votes
            winners.clear()
            winners.add(name)
        if(votes == maxi):
            winners.add(name)
    print(winners)
    

#-------------------------

candidate_names = ["akshit","ahna","tarun","ahna","tarun","ahna","tarun", "mukul"]
for name in candidate_names:
    voting(name)
print (candidates)
print_winner()