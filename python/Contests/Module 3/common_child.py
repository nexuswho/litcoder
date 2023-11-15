def common_child(s1, s2):
    n = len(s1)

    # Create a 2D array to store the length of the common child
    dp = [[0] * (n + 1) for _ in range(n + 1)]

    # Fill in the dp array using bottom-up dynamic programming
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    return dp[n][n]


# Exercise-1
s1_1 = "pqrs"
s2_1 = "opqs"
output_1 = common_child(s1_1, s2_1)
print(f"Exercise-1 Output: {output_1}")

# Exercise-2
s1_2 = "pacb"
s2_2 = "opqs"
output_2 = common_child(s1_2, s2_2)
print(f"Exercise-2 Output: {output_2}")
