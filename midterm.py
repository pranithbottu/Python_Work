###################
#	Midterm
#	Due: Tuesday, November 28 2017
###################

# Array Almost Product
#
# Write a function that, given a list of integers, will return a list of
# integers 'output' wherein the value of output[i] is the product of all the
# numbers in the input array except for input[i].
#
# You will lose points if your solution uses division.
# Your solution should run in O(n) time.
# Your solution should not allocate any space other than the output list.
#
# Example(s)
# ----------
# Example 1:
#   Input: [2,3,4,5]
#       Output should be [3*4*5, 2*4*5, 2*3*4]
#   Output: [60, 40, 30, 24]
#
# Example 2:
#   Input: [3,6,9,-3,2,-2]
#   Output:
#   [648, 324, 216, -648, 972, -972]
#
# Parameters
# ----------
# arr : List[int]
#   A list of integers. You may assume len(arr) > 1
#
# Returns
# -------
# List[int]
#   Returns a list where every element of the list is the product of
#   all the numbers in the input list except for the number at the index
#   being evaluated.
#

def array_almost_product(arr):
    round_one = []
    agg = 1
    for i in range(0, len(arr)):
        if i == 0:
            round_one.append(1)
        else:
            round_one.append(agg*arr[i-1])
            agg = agg*arr[i-1]
    round_two = []
    agg = 1
    for i in range(len(arr)-1, -1, -1):
        if i == (len(arr)-1):
            round_two.append(1)
        else:
            round_two.insert(0, agg*arr[i+1])
            agg = agg*arr[i+1]
    final = []
    for i in range(0, len(arr)):
        final.append(round_one[i]*round_two[i])
    return final

#print(array_almost_product([2,3,4,5]))
#print(array_almost_product([3,6,9,-3,2,-2]))

# Pascal's Triangle
#
# Write a function that, given an index i, returns the i'th row of Pascal's Triangle.
#
# This Wikipedia page on Pascal's triangle may be useful:
#   https://en.wikipedia.org/wiki/Pascal%27s_triangle
#
# Your solution should run in O(i) time and use O(i) space.
#
# Example(s)
# ----------
# Example 1:
#   Input: 2
#   Output: [1,2,1]
#
# Example 2:
#   Input: 6
#   Output: [1,6,15,20,15,6,1]
#
# Parameters
# ----------
# i : int
#   The row index of the row of Pascal's Triangle you are searching for
#
# Returns
# -------
# List[int]
#   Returns the i'th row of Pascal's Triangle as a list of ints
#

def pascals_triangle(i):
    pascals_line = [1]
    for j in range(0, i):
        pascals_line.append(pascals_line[j]*(i-j)/(j+1))
    return pascals_line

#print(pascals_triangle(2))
#print(pascals_triangle(6))

# Alive People
#
# Write a function that, given a list of strings representing a person's birth year: age of death,
# will return the year that had the most people alive (inclusive). If there are multiple years that tie, return the earliest.
# You can think of a birthdate and a deathdate as a range of years. Of all the birth years in the list, find the one where the highest
# amount of people in the list were still alive.
#
# Examples
# ----------
# Example 1:
#   Input: ["1920: 80", "1940: 22", "1961: 10"]
#   Output: 1961
#
# Example 2:
#   Input: ["2000: 46", "1990: 17", "1200: 97", "1995: 20"]
#   Output: 2000
#
# Parameters
# ----------
# people : List[string]
#   A list of strings each representing a birth year and final age
#
#
# Returns
# -------
# int
#   Returns earliest year with the most people alive
#

def alive_people(people):
    birth_year = []
    death_year = []
    ages = []
    for i in people:
        temp_one = i[0:4]
        temp_two = i[6:8]
        birth_year.append(int(temp_one))
        ages.append(int(temp_two))
    for i in range(0, len(people)):
        death_year.append(birth_year[i]+ages[i])
    people_alive = []
    birth_years = get_years(birth_year)
    for i in range(0, len(birth_years)):
        count = 0
        for j in range(0, len(birth_year)):
            if is_alive(birth_years[i], birth_year[j], death_year[j]) == True:
                count+=1
        people_alive.append(count)
    max_year = birth_years[people_alive.index(max(people_alive))]
    for i in range(0, len(birth_years)):
        if people_alive[i] == max(people_alive) and max_year > birth_year[i]:
            max_year = birth_year[i]
    return max_year

def get_years(years):
    births = []
    for i,j in enumerate(years):
        if j not in births:
            births.append(j)
    return births

def is_alive(year, birth, death):
    if year >= birth and year <= death:
        return True
    else:
        return False

#print(alive_people(["1920: 80", "1940: 22", "1961: 10"]))
#print(alive_people(["2000: 46", "1990: 17", "1200: 97", "1995: 20"]))
#print(alive_people(["2000: 46", "1990: 17", "1200: 97", "1993: 2", "1992: 8", "1993: 4", "1990: 8"]))


# String, My One True Love
#
# Your favorite course staff member really likes strings that have the same occurences of letters.
# This means the staff member likes "aabbcc" and "ccddee" and even strings like "abcabcabc"
#
# But the person who wrote all of your homewokrs wants to trick the staff with really long string,
# that either could be the string that the staff member likes, or something that becomes such a string
# when you remove a single character from the string.
#
# Your goal is to return True if it's a string that the homework creator made
# and False otherwise.
#
# Restrictions
# ------------
# Inputs are only given as lower case alphabets, without punctuation, spaces, etc.
# Your solution must run in O(n) time.
#
# Example(s)
# ----------
# Example 1:
#   Input: "abcbabcdcdda"
#   There is 3 a's, 3 b's, 3 c's, and 3 d's. That means it is a very likable string!
#   Output:
#   True
#
# Example 2:
#   Input: "aaabbbcccddde"
#   Again there are 3 a's, 3 b's, 3 c's, and 3 d's. However, we also have 1 e!
#   We can remove this string however, and it will become a likeable string, so this is valid.
#   Output:
#   True
#
# Example 3:
#   Input: "aaabbbcccdddeeffgg"
#   This string is similar to the other ones, except with 2 e's, f's and g's at the end.
#   To make this string likable, we need to remove the 2 e's, f's, and g's or we can remove
#   one a, b, c, and d. However all of these require more than one removal, so it becomes invalid.
#   Output:
#   False
#
# Parameters
# ----------
# the_string : str
#   The string to check whether it is likeable or not.
#
# Returns
# -------
# bool
#   True if the string is likable, or removing a single character makes it likable.
#   False if the string is not likeable, and we need to remove more than 1 character to become likable.

def string_my_one_true_love(the_string):
    letters = get_letters(the_string)
    counts = []
    for i in range(0, len(letters)):
        temp = the_string.count(letters[i])
        counts.append(temp)
    if len(set(counts)) > 2:
        return False
    if len(set(counts)) == 1:
        return True
    numbers = get_nums(counts)
    instances = [0, 0]
    for i,j in enumerate(counts):
        if j == numbers[0]:
            instances[0]+=1
        elif j == numbers[1]:
            instances[1]+=1
    if instances[0] > 1 and instances[1] > 1:
        return False
    else:
        return True

def get_letters(string):
    letters = []
    for i,j in enumerate(string):
        if j not in letters:
            letters.append(j)
    return letters

def get_nums(numbers):
    nums = []
    for i,j in enumerate(numbers):
        if j not in nums:
            nums.append(j)
    return nums 

#print(string_my_one_true_love("abcbabcdcdda"))
#print(string_my_one_true_love("aaabbbcccddde"))
#print(string_my_one_true_love("aaabbbcccdddeeffgg"))
#print(string_my_one_true_love("aaaahfiieeqwertyuioasdghjjojo"))
#print(string_my_one_true_love("aaaaaabbbbbbccccccdddffdddeeeeee"))
#print(string_my_one_true_love("aaaaaabbbbbbccccccdddfdddeeeeee"))
#print(string_my_one_true_love("sjfhefvbejfvkfsjfhkdscbrekvuievbcieucfegskcbdhkhecbhkscbhdkhscbheksceiecbfkshcbkdsfc"))
#print(string_my_one_true_love("qqqqqqqqqqhhhhhhhhhhhiiiiiiiiiiyyyyyyyyyy"))

# Longest Palindromic Substring
#
# Given a string, find the longest substring that is a palindrome. If
#
# Ideal runtime: o(n), but we will give full credit for o(n^2) solutions.
#
# RESTRICTIONS:
# There is guarunteed to be exactly 1 longest palindrome
#
# Example(s)
# ----------
# Example 1:
#   Input: "ABBAC"
#
#   Output:
#   "ABBA"
#
# Example 2:
#   Input: "A"
#
#   Output:
#   "A"
#
# Parameters
# ----------
# word: str
#   String input
#
# Returns
# -------
# String
#    Longest Palindrome substring
def longest_palindrome_substring(word):
    results = []
    if len(word) == 1:
        return word
    else:
        for i in range(0, len(word)):
            for j in range(0, i):
                sub_str = word[j:i+1]
                if sub_str == sub_str[::-1]:
                    results.append(sub_str)
        max_index = 0
        for i in range(1, len(results)):
            if len(results[i]) > len(results[max_index]):
                max_index = i
        return results[max_index]

#print(longest_palindrome_substring("ABBAC"))
#print(longest_palindrome_substring("A"))

# Longest Unique Substring
#
# Given a string, find the longest unique substring
#
# Ideal runtime: o(n). full credit only given for o(n).
# Do not consider case. Therefore, 'A' and 'a' are considered the same character
#
# RESTRICTIONS:
# There is guarunteed to be exactly 1 longest unique substring
#
# Example(s)
# ----------
# Example 1:
#   Input: "zzAabcdefFgg"
#
#   Output:
#   "abcdef"
#
# Example 2:
#   Input: "AA"
#
#   Output:
#   "A"
#
# Parameters
# ----------
# word: str
#   String input
#
# Returns
# -------
# String
#    Longest unique substring

def longest_unique_substring(word):
    max_len = 0
    longest = ""
    for i in range(0, len(word)):
        sub_str = word[i:].lower()
        chars = set()
        for j,c in enumerate(sub_str):
            if c in chars:
                break
            else:
                chars.add(c)
        else:
            j+=1
        if j > max_len:
            max_len = j
            longest = word[i:i+j]
    return longest

#print(longest_unique_substring("zzAabcdefFgg"))
#print(longest_unique_substring("AA"))
#print(longest_unique_substring("AWsefghyAasvevevfverv"))

# Three Sum
#
# Given an array S of n integers and constant 'target', are there elements a, b, c in S such that
# a+b+c = target? Find all unique triplets in the array which gives the sum of target.
# return a 2d list, where all inner lists are triplets. There may be more than
# one pair of triplets.
#
# Runtime: o(n^2) will get full credit.
#
#
# Example(s)
# ----------
# Example 1:
#   Input: [-1, 0, 1, 2, -1, -4], 0
#
#   Output:
#   [
#  [-1, 0, 1],
#  [-1, -1, 2]
#   ]
#
#
# Parameters
# ----------
# arr: array
#   array of numbers
#
# target: int
#   target integer
#
# Returns
# -------
# 2d array
#    2d list, inner lists are triplets that add up to target.

def three_sum(arr, target):
    new_arr = sorted(arr)
    final_arr = []
    for i in range(len(new_arr)):
        temp = target - new_arr[i]
        j = i+1
        k = len(new_arr)-1
        while j < k:
            s_sum = new_arr[j] + new_arr[k]
            if s_sum < temp:
                j+=1
            elif s_sum > temp:
                k-=1
            else:
                sum_arr = [new_arr[i], new_arr[j], new_arr[k]]
                if sum_arr not in final_arr:
                    final_arr.append(sum_arr)
                j+=1
                k-=1
    return final_arr

#print(three_sum([-1, 0, 1, 2, -1, -4], 0))

#print(three_sum([-1, 0, 1, 2, -1, -4], 0))
#print(three_sum([-1, 0, 1, 4, 0, 6, -1, 1], 5))

# Zero Sum
#
# Return True if a subarray (not any element) summed can create 0.
# Otherwise return False.
#
# Time Complexity
# ------------
# Optimal time complexity is O(n). You can assume the running time of updating a dictionary is O(1)
#
# You CANNOT assume the order given will be sorted.
#
# Example(s)
# ----------
# Example 1:
#   Input: zero_sum([0, 1, 2, 3, 4, 5])
#   We need to see if a subarray can create 0.
#   The first element gives us 0. So there is a subarray that can create 0.
#   Output:
#   True
#
# Example 2:
#   Input: zero_sum([10, 20, -20, 3, 21, 2, -6])
#   We need to see if a subarray can create 0.
#   The subarray [20, -20] can create zero.
#   Output:
#   True
#
# Parameters
# ----------
# arr: array
#   array of numbers

def zero_sum(arr):
    sums = {}
    total = 0
    for i in arr:
        total += i
        try:
            if i == 0 or total == 0 or sums[total] == 1:
                return True
            else:
                sums[total] = 1
        except:
            sums[total] = 1
    return False
    
    


#print(zero_sum([0, 1, 2, 3, 4, 5]))
#print(zero_sum([10, 20, -20, 3, 21, 2, -6]))
#print(zero_sum([1, 2, 3, 4, 5, 6]))
#print(zero_sum([1, 2, -2, 3, 4, 5, 1, 3, -9]))
#print(zero_sum([2, -6, 4, 1, 2, 3, 4, 5, 6]))



# Stair Stepping
#
# One day, Alice's power went out in her house.
# Because Alice is currently in 374, she decided to count how many distinct ways she can climb up her staircase (from the bottom to the last stair). Alice is able to skip some stairs because she has very long legs.
# Help Alice determine the number of distinct ways she can climb up the staircase given the number of stairs on the staircase (stairs) and the maximum number of stairs she can skip at each one of her steps (skip).
#
# Time Complexity
# ---------------
# Optimal time complexity is O(stairs).
# Example 1:
# stairs = 3
# skip = 0
#
#   #
#  ##
# ###
# 123
#
# Alice cannot skip any stairs, so there is only one way.
# BOTTOM -> 1 -> 2 -> 3
#
# Example 2:
# stairs = 3
# skip = 1
#
#   #
#  ##
# ###
# 123
#
# Alice can skip one stair at most, so there are 3 ways.
# BOTTOM -> 1 -> 2 -> 3
# BOTTOM -> 1 -> 3
# BOTTOM -> 2 -> 3
#
# Example 3:
# stairs = 5
# skip = 2
#
#     #
#    ##
#   ###
#  ####
# #####
# 12345
#
# Alice can skip two stairs at most, so there are 13 ways.
#
# BOTTOM -> 1 -> 2 -> 3 -> 4 -> 5
# BOTTOM -> 1 -> 2 -> 3 -> 5
# BOTTOM -> 1 -> 2 -> 4 -> 5
# BOTTOM -> 1 -> 3 -> 4 -> 5
# ...
# ...
# ...
# BOTTOM -> 3 -> 5
#
# Note that Alice must start at the "0th" step and finish exactly at the Nth step where N is the number of stairs.

def staircase_ways(stairs, skip):
    ways = [1] + [None] * stairs
    for i in range(1, stairs+1):
        ways[i] = sum(ways[max(0, i-(skip+1)):i])
    return ways[stairs]

#print(staircase_ways(3, 0))
#print(staircase_ways(3, 1))
#print(staircase_ways(5, 2))

# Odd One Out
#
# Given an array of 2n + 1 integers where each integer except one is duplicated, return the number that only appears once in the array.
#
# Time complexity
# ---------------
# Optimal time complexity is O(n). Try to only use O(1) space/memory.
#
# Example 1:
# arr = [10]
# Answer is 10.
#
# Example 2:
#
# arr = [3, 2, 1, 3, 2, 4, 4]
# Answer is 1.
#
#
# Example 3:
# arr = [-1, 1, 0, 5, 0, 2, 1, 2, 5]
# Answer is -1.

def odd_one_out(arr):
    for i in range(0, len(arr)):
        temp = arr[i]
        if arr.index(temp) == (len(arr) - arr[::-1].index(temp) - 1):
            return temp

#print(odd_one_out([10]))
#print(odd_one_out([3, 2, 1, 3, 2, 4, 4]))
#print(odd_one_out([-1, 1, 0, 5, 0, 2, 1, 2, 5]))
#print(odd_one_out([-1, 2, 3, 5, 5, 3, 2, -1, 4, 5,6,7,8,7,6,5,8,9,9,2,3,5,6,7,7,6]))

# Circular Shift
#
# Given an array (arr) and a shift value (k), shift the array to the
# right by k. If the rightmost element will become out of bounds, move
# it to the front of the array (hence circular shift).
#
# Time complexity
# ---------------
# Optimal complexity is O(len(arr)). Try using only O(1) space/memory
#
# Example 1:
# arr = [1, 2, 3, 4, 5]
# k = 1
# Returns [5, 1, 2, 3, 4]
#
# Example 2:
# arr = [1, 2, 3, 4, 5]
# k = 2
# Returns [4, 5, 1, 2, 3]
#
# Example 3:
# arr = [1, 2, 3]
# k = 10
# Returns [3, 1, 2]

def circular_shift(arr, k):
    r = k % len(arr)
    return arr[-r:] + arr[:-r]

#print(circular_shift([1, 2, 3, 4, 5], 1))
#print(circular_shift([1, 2, 3, 4, 5], 2))
#print(circular_shift([1, 2, 3], 10))

# Reverse Linked List
#
# Given a linked list, reverse it in-place
#
# Time Complexity
# ---------------
# Optimal time complexity is O(n). Try to use only O(1) memory.

class Node:
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node

def reverse_list(head):
    if head == None:
        return None
    current = head
    previous = None
    while current != None:
        tail = current.next_node
        current.next_node = previous
        previous = current
        current = tail
    return previous