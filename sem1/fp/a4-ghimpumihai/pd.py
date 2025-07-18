def can_partition(nums):
    total_sum = sum(nums)

    # If the sum is odd, we cannot partition it into two equal subsets
    if total_sum % 2 != 0:
        return False, [], []

    target = total_sum // 2
    n = len(nums)

    # DP table to check if a subset with sum `target` can be formed
    dp = []
    for i in range(n + 1):
        dp.append([False] * (target + 1))
    dp[0][0] = True

    for i in range(1, n + 1):
        dp[i][0] = True  # There's always a way to form sum 0 (by taking no elements)

    for i in range(1, n + 1):
        for j in range(1, target + 1):
            if j >= nums[i - 1]:
                dp[i][j] = dp[i - 1][j] or dp[i - 1][j - nums[i - 1]]
            else:
                dp[i][j] = dp[i - 1][j]

    if not dp[n][target]:
        return False, [], []

    # If partition is possible, find one of the partitions
    subset1 = []
    subset2 = nums.copy()
    i, j = n, target
    while i > 0 and j > 0:
        if dp[i - 1][j]:
            i -= 1
        else:
            subset1.append(nums[i - 1])
            subset2.remove(nums[i - 1])
            j -= nums[i - 1]
            i -= 1

    return True, subset1, subset2

# Example input from the problem statement
n=int(input())
A=[]
for i in range(n):
    A.append(int(input()))

# Call the function with the example input
result, subset1, subset2 = can_partition(A)
if result:
    print("Subset 1:", subset1)
    print("Subset 2:", subset2)
else:
    print("Impossible to divide into 2 subsets")