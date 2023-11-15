def legoWall(n, m):
    mod = 1000000007

    # Initialize a 2D array to store the number of ways to build the wall
    dp = [[0] * (m + 1) for _ in range(n + 1)]

    # Base case: there is only one way to build a wall of height 0
    dp[0][0] = 1

    # Dynamic programming to calculate the number of ways
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            # Calculate the number of ways to build the current brick
            dp[i][j] = dp[i][j - 1] + dp[i - 1][j]

            # Take modulo 1000000007 to avoid overflow
            dp[i][j] %= mod

    # Subtract the number of ways for the wall with a hole in the last column
    for i in range(1, n + 1):
        dp[i][m] = (dp[i][m] - dp[i - 1][m] + mod) % mod

    # Sum up the number of ways for all brick types to build the entire wall
    result = dp[n][m]

    return result


# Exercise-1
input_n1 = 2
input_m1 = 2
output_1 = legoWall(input_n1, input_m1)
print(f"Exercise-1 Output: {output_1}")

# Exercise-2
input_n2 = 4
input_m2 = 4
output_2 = legoWall(input_n2, input_m2)
print(f"Exercise-2 Output: {output_2}")
