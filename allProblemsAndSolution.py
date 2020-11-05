# QUESTION: 1
"""
---------
Question
---------
You will be supplied with two data files in CSV format. The  first file contains
statistics about various dinosaurs. The second file contains additional data.

Given the following formula,
-----
speed = ((STRIDE_LENGTH / LEG_LENGTH) - 1) * SQRT(LEG_LENGTH * g)
Where g = 9.8 m/s^2 (gravitational constant)
-----

Write a program to read in the data files from disk, it must then print the
names of only the bipedal dinosaurs from fastest to slowest. Do not print any
other information.


dataset1.csv
-----------
NAME,STRIDE_LENGTH,STANCE
Euoplocephalus,1.97,quadrupedal
Stegosaurus,1.70,quadrupedal
Tyrannosaurus Rex,4.76,bipedal
Hadrosaurus,1.3,bipedal
Deinonychus,1.11,bipedal
Struthiomimus,1.24,bipedal
Velociraptor,2.62,bipedal

dataset2.csv
------------
NAME,LEG_LENGTH,DIET
Hadrosaurus,1.4,herbivore
Struthiomimus,0.72,omnivore
Velociraptor,1.8,carnivore
Triceratops,0.47,herbivore
Euoplocephalus,2.6,herbivore
Stegosaurus,1.50,herbivore
Tyrannosaurus Rex,6.5,carnivor

"""

"""
Approach 1st
"""
from math import sqrt

fname1 = "dataset1.csv"
fname2 = "dataset2.csv"

g = 9.8

d1 = {}
d2 = {}

d3 = {}

with open(fname1, 'r') as file:
    next(file)
    for info in file:
        data = info.split(",")

        name = data[0]
        info1 = data[1]
        info2 = data[2][:-1]

        d1[data[0]] = [info1, info2]

with open(fname2, 'r') as file:
    next(file)
    for info in file:
        data = info.split(",")

        name = data[0]
        info1 = data[1]
        info2 = data[2][:-1]

        d2[data[0]] = [info1, info2]


for d in d1.keys():
    if d not in d2:
        continue

    if d2[d][1]!= "bipedal":
        continue

    leg = float(d1[d][0])
    stride = float(d2[d][0])
    speed = ((stride / leg) - 1) * sqrt(leg * g)
    d3[d] = speed

for name in sorted(d3.items(), key=lambda x:x[1], reverse=True):
    print (name)

"""
Approach 2nd
"""
import csv
from math import sqrt

filenames = ['dataset2.csv','dataset1.csv']
g = 9.8
dino_info = {}

for fname in filenames:
    with open(fname, 'r') as re:
        csv_data = csv.DictReader(re)

        for data in csv_data:
            name = data["NAME"]

            if "STANCE" in data:
                if data["STANCE"] == "bipedal":
                    if name not in dino_info:
                        dino_info[name] = data
                    else:
                        dino_info[name].update(data)
            else:
                if name in dino_info:

                    dino_info[name].update(data)
result = {}
for name, info in dino_info.items():
    if "LEG_LENGTH" not in info:
        continue

    print (name, info)
    STRIDE_LENGTH = float(info["STRIDE_LENGTH"])
    LEG_LENGTH = float(info["LEG_LENGTH"])

    speed = speed = ((STRIDE_LENGTH / LEG_LENGTH) - 1) * sqrt(LEG_LENGTH * g)
    result[name] = speed


for dino in sorted(result.items(), key=lambda x:x[1], reverse=True):
    print (dino)


#-----------------------------------------------------------------------------#
# QUESTION: 2
"""
Provided list of IPs and ports check if the host is accessible on that particular
port.

"""

import socket
import time

iplist = ["8.8.8.8","0.0.0.0","127.0.0.1"]
ports = [80, 443]

## efficient way
retry = 5
delay = 10
timeout = 3


def isOpen(ip, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(timeout)

    try:
        s.connect((ip, port))
        s.shutdown(socket.SHUT_RDWR)
        return True
    except:
        return False
    finally:
        s.close()


def vrfyHost():
    for ip in iplist:
        for port in ports:

            for i in range(retry):
                if isOpen(ip, port):
                    print (ip, port)
                else:
                    print (ip, "Ip is not able to connect to port ", port )
                    time.sleep(delay)



#-----------------------------------------------------------------------------#
# QUESTION: 3
"""
Take a paragraph as Input and output the top three most repeated words
"""
def topKFrequent(words, k):
    """
    :type words: List[str]
    :type k: int
    :rtype: List[str]
    """
    count = collections.Counter(words)
    candidates = count.keys()
    print candidates ,count
    candidates.sort(key = lambda w:(-count[w],w))


    #count[word] is the frequency of the word, so -count[word] means that sorting is reverse with the negative sign.
    #And, the word behind means that if their -count[word] are equal, they will compare their alphabetical orders, as
    #mentioned in the problem
    return candidates[:k]

    """
    #--- using heap ---
    count = collections.Counter(words)
    heap = [(-freq, word) for word, freq in count.items()]
    heapq.heapify(heap)
    return [heapq.heappop(heap)[1] for _ in xrange(k)
    """

#-----------------------------------------------------------------------------#
# QUESTION: 4
"""
Write a function to sort a list of integers that looks like this
[5,2,0,3,0,1,6,0] -> [1,2,3,5,6,0,0,0] in the most efficient way .
"""
def moveZeroes(nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        c = 0
        
        for i in range(len(nums)):
            if nums[i]!=0:
                nums[c] = nums[i]
                c +=1
                
        for i in range(c,len(nums)):
            nums[i]=0


#-----------------------------------------------------------------------------#
# QUESTION: 5
"""
One is translate English to «Goat Latin» language with a set of predefined rules. 

Given a sentence convert the sentence to the modified pig-latin language:
Words beginning with a vowel, remove the vowel letter and append the letter to the end.
All words append the letters ‘ni’ to the end.
All words incrementally append the letter ‘j’. i.e. ‘j’,’jj’,’jjj’, etc…
"""
class Solution(object):
    def toGoatLatin(self, S):
        """
        :type S: str
        :rtype: str
        """
        
        compare = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        result = ""
        c = 1
        for word in S.split():
            if word[0] in compare:
                result += word+"ma"+"a"*c+" "
            else:
                result += word[1:]+word[0]+"ma"+"a"*c+" "
            
            c +=1
        
        return result[:-1]
#-----------------------------------------------------------------------------#
# QUESTION: 6
"""
Given a list of integers, output all subsets of size three, which sum to zero.
"""
class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        n = len(nums)
        
        output = [[]]
        
        for num in nums:
            output += [curr + [num] for curr in output]
        
        for s in output:
            if len(s)==3 and sum(s) == 0:
                print s 
        
#-----------------------------------------------------------------------------#
# QUESTION: 7
"""
Given a list of integers which are sorted, but rotated ([4, 5, 6, 1, 2, 3]), 
search for a given integer in the list.
https://leetcode.com/problems/search-in-rotated-sorted-array/  
-------------------------
[ Binary Search ] [ IMP ]
-------------------------

"""
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        
        l = 0
        r = len(nums) - 1
        
        
        while l <= r:
            m = (l + r) // 2
            
            if nums[m] == target:
                return m
            
            if nums[m] >= nums[l]: # First part
                if nums[l] <= target and target < nums[m]:
                    r = m - 1
                else:
                    l = m + 1
            
            else: # second part, nums[m] < nums[l]
                if nums[m] < target and target <= nums[r]:
                    l = m + 1
                else:
                    r = m - 1
                    
        return -1

#-----------------------------------------------------------------------------#
# QUESTION: 8
"""
An array is monotonic if it is either monotone increasing or monotone decreasing.
An array A is monotone increasing if for all i <= j, A[i] <= A[j].  An array A is 
monotone decreasing if for all i <= j, A[i] >= A[j].
Return true if and only if the given array A is monotonic.

Example 1:
Input: [1,2,2,3]
Output: true

Example 2:
Input: [6,5,4,4]
Output: true
Example 3:

Input: [1,3,2]
Output: false

Example 4:
Input: [1,2,4,5]
Output: true

Example 5:
Input: [1,1,1]
Output: true
"""

class Solution(object):
    def isMonotonic(self, A):
        """
        :type A: List[int]
        :rtype: bool

        status1 = all(A[i] <= A[i+1] for i in range(len(A)-1))
        status2 = all(A[i] >= A[i+1] for i in range(len(A)-1))
        
        if status1 or status2:
            return True
        
        return False
        """
        temp = sorted(A)
        temp1 = temp[::-1]
        
        if temp == A or temp1 == A:
            return True
        return False 
        
#-----------------------------------------------------------------------------#
# QUESTION: 9
"""
Longest Substring Without Repeating Characters
Given a string s, find the length of the longest substring without repeating 
characters.

Example 1:
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

Example 2:
Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Example 3:
Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.Notice that the answer must be
a substring, "pwke" is a subsequence and not a substring.

Example 4:
Input: s = ""
Output: 0
"""
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        maxlen = 0
        
        track = set()
        
        i = 0
        j = 0
        
        while j < len(s):
            if s[j] not in track:
                track.add(s[j])
                j +=1
                maxlen = max(maxlen, j - i)
            else:
                track.remove(s[i])
                i +=1
                
        return maxlen

#-----------------------------------------------------------------------------#
# QUESTION: 10
"""
1. Given an array of numbers(ex [3 2 5]), find if its possible to split it into 2 
parts with equal sum without reordering (ex [3 2 ] and [5] ) and false if not possible!. 

2. Split array apart into two equal sums./ split array in such a way that their sum is same/Add 
each number in an array until the sum equals the rest of the array /Split an array and add up 
the numbers so that the first part of the array equals the sum of the second part of possible.. 

https://leetcode.com/discuss/interview-question/718692/Facebook-or-Training-or-Balanced-Split
https://leetcode.com/problems/partition-equal-subset-sum/
"""
def can_partition(num):
  s = sum(num)
  # if 's' is a an odd number, we can't have two subsets with equal sum
  if s % 2 != 0:
    return False

  return can_partition_recursive(num, s / 2, 0)

#---------------------
def can_partition_recursive(num, sum, currentIndex):
  # base check
  if sum == 0:
    return True

  n = len(num)
  if n == 0 or currentIndex >= n:
    return False

  # recursive call after choosing the number at the `currentIndex`
  # if the number at `currentIndex` exceeds the sum, we shouldn't process this
  if num[currentIndex] <= sum:
    if(can_partition_recursive(num, sum - num[currentIndex], currentIndex + 1)):
      return True

  # recursive call after excluding the number at the 'currentIndex'
  return can_partition_recursive(num, sum, currentIndex + 1)


def main():
  print("Can partition: " + str(can_partition([1, 2, 3, 4])))
  print("Can partition: " + str(can_partition([1, 1, 3, 4, 7])))
  print("Can partition: " + str(can_partition([2, 3, 4, 6])))


main()

#---------------------
def can_partition_recursive(dp, num, sum, currentIndex):
  # base check
  if sum == 0:
    return 1

  n = len(num)
  if n == 0 or currentIndex >= n:
    return 0

  # if we have not already processed a similar problem
  if dp[currentIndex][sum] == -1:
    # recursive call after choosing the number at the currentIndex
    # if the number at currentIndex exceeds the sum, we shouldn't process this
    if num[currentIndex] <= sum:
      if can_partition_recursive(dp, num, sum - num[currentIndex], currentIndex + 1) == 1:
        dp[currentIndex][sum] = 1
        return 1

    # recursive call after excluding the number at the currentIndex
    dp[currentIndex][sum] = can_partition_recursive(
      dp, num, sum, currentIndex + 1)

  return dp[currentIndex][sum]


def main():
  print("Can partition: " + str(can_partition([1, 2, 3, 4])))
  print("Can partition: " + str(can_partition([1, 1, 3, 4, 7])))
  print("Can partition: " + str(can_partition([2, 3, 4, 6])))


main()


#---------------------
def can_partition(num):
  s = sum(num)

  # if 's' is a an odd number, we can't have two subsets with same total
  if s % 2 != 0:
    return False

  # we are trying to find a subset of given numbers that has a total sum of 's/2'.
  s = int(s / 2)

  n = len(num)
  dp = [[False for x in range(s+1)] for y in range(n)]

  # populate the sum=0 column, as we can always have '0' sum without including 
  # any element
  for i in range(0, n):
    dp[i][0] = True

  # with only one number, we can form a subset only when the required sum is
  # equal to its value
  for j in range(1, s+1):
    dp[0][j] = num[0] == j

  # process all subsets for all sums
  for i in range(1, n):
    for j in range(1, s+1):
      # if we can get the sum 'j' without the number at index 'i'
      if dp[i - 1][j]:
        dp[i][j] = dp[i - 1][j]
      elif j >= num[i]:  # else if we can find a subset to get the remaining sum
        dp[i][j] = dp[i - 1][j - num[i]]

  # the bottom-right corner will have our answer.
  return dp[n - 1][s]


def main():
  print("Can partition: " + str(can_partition([1, 2, 3, 4])))
  print("Can partition: " + str(can_partition([1, 1, 3, 4, 7])))
  print("Can partition: " + str(can_partition([2, 3, 4, 6])))

main()
