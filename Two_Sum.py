class Solution:
    # @return a tuple, (index1, index2)
    def twoSum(self, num, target):
	
		# Brute force, O(n^2)
		'''
		for i in range(len(num)):
			for j in range(i+1,len(num)):
				if ((num[i] + num[j]) == target):
					return (i+1,j+1)
		'''			
	
		# Use dict
		# construct a dict, just use it for search value
		# it's said to be linear time in search, though I don't know why
		dict_num = dict()
		index = 0
		for i in num:
			dict_num[i] = 1
		
		# if (target-i) is in dict, find its index and return value
		for i in range(len(num)):
			if (target-num[i]) in dict_num:
				for j in range(i+1, len(num)):
					if num[i] + num[j] == target:
						return ( i+1, j+1)
	

	
if __name__ == "__main__":

	s = Solution()
	num = [3,2,4]
	target = 6

	print(s.twoSum(num, target))
