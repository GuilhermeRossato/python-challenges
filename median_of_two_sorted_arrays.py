from typing import List

class Solution:
	def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
		merged = []
		i = j = 0
		size1 = len(nums1)
		size2 = len(nums2)
		while i < size1 or j < size2:
			if j >= size2 or (i < size1 and nums1[i] <= nums2[j]):
				merged.append(nums1[i])
				i += 1
			else:
				merged.append(nums2[j])
				j += 1
		total = size1 + size2
		mid = total // 2
		if (total % 2 == 1):
			return merged[mid]
		return (merged[mid] + merged[mid - 1]) / 2
