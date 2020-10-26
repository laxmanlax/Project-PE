"""
Leetcode Link:
https://leetcode.com/discuss/interview-question/675445/facebook-interview-experiences-all-combined-from-lc-till-date-07-jun-2020

Coding Tips:
It is generally a great idea to come up with a few test cases (both normal and edge) before you write code.
--
You could do something like
Input | Expected Output
--
"""

 # QUESTION:  1
"""
Given a string s and a non-empty string p, find all the start indices of p's anagrams in s.
Strings consists of lowercase English letters only and the length of both strings s and p
will not be larger than 20,100. The order of output does not matter.

Example 1:
Input:
s: "cbaebabacd" p: "abc"

Output:
[0, 6]

Explanation:
The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".

Example 2:
Input:
s: "abab" p: "ab"

Output:
[0, 1, 2]

Explanation:
The substring with start index = 0 is "ab", which is an anagram of "ab".
The substring with start index = 1 is "ba", which is an anagram of "ab".
The substring with start index = 2 is "ab", which is an anagram of "ab".

"""
class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]

        Questions : Upper or Lower charter if not explind in the begining
        Think of the Edge cases: one "a":"a" , "":""
        Think of the test cases:

        # Brute force n(log(n))
        """

        l = len(p)
        t = "".join(sorted(p))
        res = []

        for i in range(len(s)):
            substr = "".join(sorted(s[i:l+i]))

            if substr == t:
                res.append(i)

        return res
       #---------------

        ns = len(s)
        np = len(p)

        if ns < np:
            return []

        output = []

        pCount = Counter(p)
        sCount = Counter()


        for i in range(ns):
            # add one more letter on the right side of the window

            sCount[s[i]] += 1

            # remove one letter on the left side of the window

            if i >= np:
                if sCount[s[i - np]] == 1:
                    del sCount[s[i - np]]
                else:
                    sCount[s[i - np]] -= 1


            if pCount == sCount:
                output.append(i - np+1)

        return output
        #--------------

        res = []
        pCount = Counter(p)
        sCount = Counter(s[:len(p) -1 ])

        for i in range(len(p)-1, len(s)):
            sCount[s[i]] +=1  # include a new character on the window

            if sCount == pCount: # This step is O(1), since there are at most 26 English letters
                res.append(i - len(p) +1) # appending the starting index


            sCount[s[i-len(p)+1]] -=1 # decrese the count of the char

            if sCount[s[i-len(p)+1]] == 0:
                del sCount[s[i-len(p)+1]]


        return res

# QUESTION:  2
# This is recursion and Dynamic programming Problem - DP
"""
Given a non-empty array nums containing only positive integers, find if the array
can be partitioned into two subsets such that the sum of elements in both subsets is equal.

Example 1:
Input: nums = [1,5,11,5]
Output: true
Explanation: The array can be partitioned as [1, 5, 5] and [11].

Example 2:
Input: nums = [1,2,3,5]
Output: false
Explanation: The array cannot be partitioned into equal sum subsets.
"""


# QUESTION:  3
"""
Given a non-empty string s, you may delete at most one character. Judge whether
you can make it a palindrome.

Example 1:

Input: "aba"
Output: True
Example 2:

Input: "abca"
Output: True
Explanation: You could delete the character 'c'.
"""

class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        """
        # Question -
        # 1 -  all charter are lower charter ?
        # 2 - Strign should be non-empty


        #Think for 10-20 second before jumpig on the solution
        # Brute Force Approach

        if s == s[::-1]:
            return True

        for i in range(len(s)):
            new_str = s[:i] + s[i+1:]
            if new_str == new_str[::-1]:
                return True

        return False
        # This is O(n) solution
        """

        l = len(s)  -1
        i = 0

        while i < l/2 and s[i] == s[-(i+1)]:
            i+=1

        s = s[i:len(s)-i]
        return s[1:]==s[1:][::-1] or s[:-1]==s[:-1][::-1]

        #Test cases


 # QUESTION:  4
"""
Given a list of non-negative numbers and a target integer k, write a function to
check if the array has a continuous subarray of size at least 2 that sums up to
a multiple of k, that is, sums up to n*k where n is also an integer.


Example 1:

Input: [23, 2, 4, 6, 7],  k=6
Output: True
Explanation: Because [2, 4] is a continuous subarray of size 2 and sums up to 6.
Example 2:

Input: [23, 2, 6, 4, 7],  k=6
Output: True
Explanation: Because [23, 2, 6, 4, 7] is an continuous subarray of size 5 and sums up to 42.
"""
class Solution(object):
    def checkSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool

        Trick y question :
        ask questions about : k == 0 or negative
        ask question about element in nums [0] or [-1]

        if k == 0:
            if len(set(nums)) == 1 and nums[0] == 0 and len(nums)>=2:
                return True

            return False

        if len(nums)>=2 and sum(nums)%2 == 0:
            return True

        s = 0
        for i in range(len(nums)-1):
            s += nums[i]
            if i >=2 and s%k==0:
                return True

        return False
        """
        seen = {0: -1}
        cur = 0

        for i,a in enumerate(nums):
            if k:
                cur = (cur+a)%abs(k)
            else:
                cur = cur + a

        if i - seen.setdefault(cur, i) > 1:
            return True

        return False


# Question-5
"""
In an alien language, surprisingly they also use english lowercase letters, but possibly in a different order.
The order of the alphabet is some permutation of lowercase letters.Given a sequence of words written in the alien
language, and the order of the alphabet, return true if and only if the given words are sorted lexicographicaly
in this alien language.



Example 1:
Input: words = ["hello","leetcode"], order = "hlabcdefgijkmnopqrstuvwxyz"
Output: true
Explanation: As 'h' comes before 'l' in this language, then the sequence is sorted.

Example 2:
Input: words = ["word","world","row"], order = "worldabcefghijkmnpqstuvxyz"
Output: false
Explanation: As 'd' comes after 'l' in this language, then words[0] > words[1], hence the sequence is unsorted.

Example 3:
Input: words = ["apple","app"], order = "abcdefghijklmnopqrstuvwxyz"
Output: false
Explanation: The first three characters "app" match, and the second string is shorter (in size.) According to
lexicographical rules "apple" > "app", because 'l' > '∅', where '∅' is defined as the blank character which is
less than any other character (More info).
"""
class Solution(object):
    def isAlienSorted(self, words, order):
        """
        :type words: List[str]
        :type order: str
        :rtype: bool
        """
        orderd_index = {c: i for i, c in enumerate(order)}
        print orderd_index

        for i in xrange(len(words) -1):
            word1 = words[i]
            word2 = words[i+1]

            for k in xrange(min(len(word1), len(word2))):

                if word1[k] != word2[k]:
                    if orderd_index[word1[k]] > orderd_index[word2[k]]:
                        return False
                    break
            else:

                if len(word1) > len(word2):
                    return False

        return True


 # QUESTION:  5
"""
Given a string s of '(' , ')' and lowercase English characters.
Your task is to remove the minimum number of parentheses ( '(' or ')', in any positions )
so that the resulting parentheses string is valid and return any valid string.

Formally, a parentheses string is valid if and only if:
It is the empty string, contains only lowercase characters, or
It can be written as AB (A concatenated with B), where A and B are valid strings, or
It can be written as (A), where A is a valid string.


Example 1:
Input: s = "lee(t(c)o)de)"
Output: "lee(t(c)o)de"
Explanation: "lee(t(co)de)" , "lee(t(c)ode)" would also be accepted.

Example 2:
Input: s = "a)b(c)d"
Output: "ab(c)d"
Example 3:

Input: s = "))(("
Output: ""
Explanation: An empty string is also valid.

Example 4:
Input: s = "(a(b(c)d)"
Output: "a(b(c)d)"
"""

class Solution(object):
    def minRemoveToMakeValid(self, s):
        """
        :type s: str
        :rtype: str

        Brute Force Approach
        """
        res = ""
        openb = 0

        for i in s:
            if i == "(":
                openb +=1
            elif i == ")":
                if openb == 0:
                    continue
                openb -=1

            res +=i

        print res,openb,res[::-1]

        result = ""
        for i in res[::-1]:
        #    print i
            if i == "(" and openb > 0:
                openb -=1

                continue
            result += i

        return result[::-1]


        #------- Using Stack -------

        stack = []
        res = ['']*len(s)

        for i, c in enumerate(s):
            if c == "(":
                stack.append(i)
            elif c == ")":
                if stack:
                    res[stack.pop()] = "("
                    res[i] = c
            else:
                res[i] = c

        return "".join(res)


# QUESTION:  6
"""
Given a string S of '(' and ')' parentheses, we add the minimum number of parentheses
( '(' or ')', and in any positions ) so that the resulting parentheses string is valid.

Formally, a parentheses string is valid if and only if:
It is the empty string, or
It can be written as AB (A concatenated with B), where A and B are valid strings, or
It can be written as (A), where A is a valid string.
Given a parentheses string, return the minimum number of parentheses we must add to
make the resulting string valid.


Example 1:
Input: "())"
Output: 1

Example 2:
Input: "((("
Output: 3

Example 3:
Input: "()"
Output: 0

Example 4:
Input: "()))(("
Output: 4
"""

class Solution(object):
    def minAddToMakeValid(self, S):
        """
        :type S: str
        :rtype: int
        """

        openb = 0
        closeb = 0

        for i in S:
            if i == "(":
                openb +=1
            elif i == ")":
                if openb > 0:
                    openb -=1

        print S[::-1]
        for j in S[::-1]:
            if j == ")":
                closeb +=1
            elif j == "(":
                if closeb > 0:
                    closeb -=1

        return openb+closeb

        ----
class Solution(object):
    def minAddToMakeValid(self, S):
        """
        :type S: str
        :rtype: int
        """
        ans = bal = 0

        for c in S:
            if c == "(":
                bal += 1
            else:
                bal -= 1

            if bal == -1:
                ans +=1
                bal +=1

        return ans + bal
        ---
class Solution(object):
    def minAddToMakeValid(self, S):
        left = right = 0

        for i in S:
            if right == 0 and i == ')':
                left += 1
            else:
                right += 1 if i == '(' else -1

        return left + right
