def levenshtein_distance(source, target):
    m, n = len(source), len(target)
 
    dp = [[0] * (n + 1) for _ in range(m + 1)]


    for i in range(m + 1):
        dp[i][0] = i
    

    for j in range(n + 1):
        dp[0][j] = j


    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if source[i - 1] == target[j - 1]:
                cost = 0
            else:
                cost = 1
            dp[i][j] = min(dp[i - 1][j] + 1,       
                           dp[i][j - 1] + 1,       
                           dp[i - 1][j - 1] + cost) 

    return dp[m][n]



