# Exercise 10. Finding Extremes (Min/Max) in a List

# Practice Problem: Given a list of integers, find and print both the largest and the smallest numbers.

# Exercise Purpose: This exercise explores “Aggregate Functions.” While Python has built-in tools for this, understanding how to identify extremes is critical for data normalization, where you often need to find the range of a dataset before processing it.

# Given Input: nums = [45, 2, 89, 12, 7]

# Expected Output: Largest: 89 Smallest: 2

nums = [45, 2, 89, 12, 7]
large_num = nums[0]
small_num = nums[0]
for i in nums:
    if i > large_num:
       large_num = i
    if i < small_num:
        small_num = i

print(f"Largest: {large_num}")
print(f"Smallest: {small_num}")

print("=============================")

nums = [45, 2, 89, 12, 7]

largest = max(nums)
smallest = min(nums)

print(f"Largest: {largest}")
print(f"Smallest: {smallest}")