class Solution:
	# @param s, a string
	# @return a boolean
	def isPalindrome(self, s):
		'''
		Return true if Palindrome
		1. remove space and special character
		2. convert all character to lower case
		3. if string length is zero -> return true
		4. compare s[i] and s[-(i=1)], see if a Palindrome
		'''
		# Convert string to lower case
		s = s.lower()
		# list to store stripped string
		l = list()
		# remove characters other than 0-9 a-z
		for i in range(len(s)):
			if (s[i] >= 'a' and s[i] <= 'z'):
				l.append(s[i])
			elif (s[i] >= '0' and s[i] <= '9'):
				l.append(s[i])
	
		# Set flag as True for initial
		flag = True
		# check if Palindrome
		# In Python division, int/int will be int
		# The middle character of a odd-length string will not be checked
		# Zero length string will also be judged as True
		for i in range(len(l)/2):
			if (l[i] != l[-(i+1)]):
				flag = False
				
		return flag
	
if __name__ == "__main__":

	solution = Solution()
	s = "1a2"

	print(solution.isPalindrome(s))
