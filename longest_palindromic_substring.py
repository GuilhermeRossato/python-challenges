class Solution:
	def longestPalindrome(self, s: str) -> str:
		palindromes = []
		for i in range(len(s)):
			if (i + 1 < len(s) and s[i] == s[i+1]):
				palindromes.append(self.analyzeCenter(s, i, i + 1))
			palindromes.append(self.analyzeCenter(s, i, i))
		return max(palindromes, key=len)

	def analyzeCenter(self, s: str, index_start: int, index_end: int):
		if index_start == 0 or index_end + 1 >= len(s):
			return s[index_start : index_end + 1]
		if s[index_start - 1] == s[index_end + 1]:
			return self.analyzeCenter(s, index_start - 1, index_end + 1)
		return s[index_start : index_end + 1]
