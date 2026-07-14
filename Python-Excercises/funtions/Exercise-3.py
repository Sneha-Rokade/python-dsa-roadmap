# 6. Count Vowels

# 👉 Function to count vowels in a string

str1 = "Hello! Good Afternoon"

def count_vowels(str):
    count = 0
    vowels = "aeiou"
    for ch in str.lower():
        if ch in vowels:
            count += 1
    return count
result = count_vowels(str1)
print(f"The Given Strings {result}")