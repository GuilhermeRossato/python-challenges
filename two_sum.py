from typing import List

class Solution:
	def twoSum(self, nums: List[int], target: int) -> List[int]:
		nhash = {}
		for index, num in enumerate(nums):
			delta = target - num
			if delta in nhash:
				return [nhash[delta], index]
			nhash[num] = index
