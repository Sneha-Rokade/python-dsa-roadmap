# Day 1: DSA Basics + Time & Space Complexity

## Goal

Understand how to measure efficiency of code and build the foundation for problem solving.

---

# What is DSA?

**DSA = Data Structures + Algorithms**

* **Data Structures** → Data Structures is about how data can be stored in different structures (Array, Linked List, etc.)

* **Algorithms** → Algorithms is about how to solve different problems, often by searching through and manipulating data structures.

# Data Structures
Data Structures are a way of storing and organizing data in a computer.

Python has built-in support for several data structures, such as lists, dictionaries, and sets.

Other data structures can be implemented using Python classes and objects, such as 
Data Structures:

Lists and Arrays
Stacks
Queues
Linked Lists
Hash Tables
Trees
Binary Trees
Binary Search Trees
AVL Trees
Graphs

# Algorithms
Algorithms are a way of working with data in a computer and solving problems like sorting, searching, etc.

Linear Search
Binary Search
Bubble Sort
Selection Sort
Insertion Sort
Quick Sort
Counting Sort
Radix Sort
Merge Sort

---

# Time Complexity

## Definition

Time complexity measures how fast an algorithm runs as input size increases.
Represented using **Big-O Notation**

---

## 🔥 Common Time Complexities

| Complexity | Meaning       | Example              |
| ---------- | ------------- | -------------------- |
| O(1)       | Constant time | Access array element |
| O(n)       | Linear        | Loop through array   |
| O(log n)   | Logarithmic   | Binary search        |
| O(n²)      | Quadratic     | Nested loops         |

---

## 💡 Examples

### O(1) — Constant Time

```python
def get_first(arr):
    return arr[0]
```

---

### O(n) — Linear Time

```python
def print_all(arr):
    for num in arr:
        print(num)
```

---

### O(n²) — Quadratic Time

```python
def print_pairs(arr):
    for i in arr:
        for j in arr:
            print(i, j)
```

---

# Space Complexity

## Definition

Space complexity measures how much extra memory is used.

---

## Examples

## O(1) Space

```python
def sum_array(arr):
    total = 0
    for num in arr:
        total += num
    return total
```

---

### O(n) Space

```python
def copy_array(arr):
    new_arr = []
    for num in arr:
        new_arr.append(num)
    return new_arr
```

---

# Why Complexity Matters

Example:

* Input size = 1,000,000

| Approach | Performance |
| -------- | ----------- |
| O(n)     | Fast        |
| O(n²)    | Very Slow   |

Interviewers expect you to choose **optimal solutions**

---

# Key Rules to Remember

1. Ignore constants
   O(2n) = O(n)

2. Drop lower terms
   O(n² + n) = O(n²)

3. Focus on worst-case

---

# Problem Solving Approach

When solving any problem:

1. Understand input size
2. Try brute force
3. Optimize using better approach
4. Analyze time complexity

---

# Practice Problems (Day 1)

## 1. Find Maximum Element

```python
def find_max(arr):
    max_val = arr[0]
    for num in arr:
        if num > max_val:
            max_val = num
    return max_val
```

 Time Complexity: O(n)

---

## 2. Reverse an Array

```python
def reverse_array(arr):
    return arr[::-1]
```

Time Complexity: O(n)

---

## 3. Sum of Array

```python
def sum_array(arr):
    total = 0
    for num in arr:
        total += num
    return total
```

Time Complexity: O(n)

---

# Key Takeaways

* Always think about **efficiency**
* Learn to identify patterns
* Practice consistently

