# Function params => s: string
# Data type that the function returns => int
def lengthOfLongestSubstring(s):
    charSet = set()
    leftPointer = 0
    result = 0
    for rightPointer in range(len(s)):
        while s[rightPointer] in charSet:
            charSet.remove(s[leftPointer])
            leftPointer += 1
        charSet.add(s[rightPointer])
        result = max(result, rightPointer - leftPointer + 1)
    return result
