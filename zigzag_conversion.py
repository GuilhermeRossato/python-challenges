class Solution:
	def convert(self, s: str, numRows: int) -> str:
		if (numRows == 1):
			return s
		lines = {}
		x = 0
		y = 0
		returning = False
		for c in s:
			if not y in lines:
				lines[y] = c
			else:
				lines[y] += c
			if not returning:
				if (y + 1 == numRows):
					returning = True
					x += 1
					y -= 1
				else:
					y += 1
			elif (returning):
				if (y == 0):
					returning = False
					y += 1
				else:
					x += 1
					y -= 1
		return ''.join(lines.values())