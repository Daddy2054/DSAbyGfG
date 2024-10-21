'''
complete the function winner() that takes an array of strings arr, and length of arr n as parameters and returns an array of string of length 2. First element of the array should be the name of the candidate and second element should be the number of votes that candidate got in string format. If there is a draw between two candidates, then print lexicographically smaller name.'''
def winner(arr):
    votes = {}
    for name in arr:
        if name in votes:
            votes[name] += 1
        else:
            votes[name] = 1
    
    max_votes = max(votes.values())
    winners = [name for name, count in votes.items() if count == max_votes]
    winners.sort()
    
    return [winners[0], str(max_votes)]

arr = ["john", "johnny", "jackie", "johnny", "john", "jackie", "jamie", "jamie", "john", "johnny", "jamie", "johnny", "john"]
result = winner(arr)
print(result)  # Output: ['john', '5']

arr = ["xandy","blake","clark"]
print(winner(arr))
print(winner(['john', 'johnny', 'jackie', 'johnny', 'john'])) # ['john', '2']