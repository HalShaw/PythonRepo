class Solution(object):
	def grayCode(self, n):
		if n==0:
			return [0]
		gc=self.grayCode(n-1)
		return gc+[(1<<(n-1))^i for i in reversed(gc)]#左移、异或
if __name__ == '__main__':
	s=Solution()
	print(s.grayCode(4))

