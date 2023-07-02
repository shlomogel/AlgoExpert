def numberOfWaysToMakeChange(n, denoms):
    ways = [0 for _ in range(n+1)]
    ways[0] = 1
    
    for d in denoms:
        for ammout in range(1, n+1):
            if d <= ammout:
                ways[ammout] += ways[ammout - d]
    return ways[n]

r = numberOfWaysToMakeChange(n=10, denoms=[1,2,5,10])
print(f"{r} ways return a 10 ")

def minNumberOfCoinsForChange(n, denoms):
    ways = [float("inf") for _ in range(n+1)]
    ways[0] = 0
    
    for d in denoms:
        for ammout in range(1, n+1):
            if d <= ammout:
                ways[ammout] = min(ways[ammout], 1 + ways[ammout - d])
    if ways[n] == float("inf"):
        return -1
    return ways[n]

r = minNumberOfCoinsForChange(n=10, denoms=[1,2,5,10])
print(f"{r} ways return a 10 ")
