def day_of_the_week(day, n):
    week = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]
    index = 0
    for i, j in enumerate(week):
        if j == day:
            index = i
    index = (index + n)%7
    return week[index]

def is_palindrome(s):
    noNumbers = []
    for i in s:
        if i.isalpha() == True:
            noNumbers.append(i)
    result = ''.join(noNumbers)
    r = result.lower()
    if r[::-1] == r:
        return True
    else:
        return False

def find_missing_number(arr, n):
    sumTotal = (n + 1)*(n/2)
    arraySum = sum(arr)
    return sumTotal - arraySum

