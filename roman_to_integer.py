class Solution(object):
    def intToRoman(self, s):
		self.map = {1:'I',	5:'V', 10:'X', 50:'L', 100:'C', 500:'D', 1000:'M', 4:'IV', 9:'IX', 40:'XL', 90:'XC', 400:'CD', 900:'CM'}
		result = ''
		while(s>0):
			if s>=1000:
				result+=self.map[1000]*(s/1000)
				s%=1000
			elif s>=900:
				result+=self.map[900]*(s/900)
				s%=900
			elif s>=500:
				result+=self.map[500]*(s/500)
				s%=500
			elif s>=400:
				result+=self.map[400]*(s/400)
				s%=400	
			elif s>=100:
				result+=self.map[100]*(s/100)
				s%=100
			elif s>=90:
				result+=self.map[90]*(s/90)
				s%=90
			elif s>=50:
				result+=self.map[50]*(s/50)
				s%=50
			elif s>=40:
				result+=self.map[40]*(s/40)
				s%=40
			elif s>=10:
				result+=self.map[10]*(s/10)
				s%=10
			elif s>=9:
				result+=self.map[9]*(s/9)
				s%=9
			elif s>=5:
				result+=self.map[5]*(s/5)
				s%=5
			elif s>=4:
				result+=self.map[4]*(s/4)
				s%=4
			else:
				result+=self.map[1]*s
				s%=1

		return result


p = Solution()
print p.intToRoman(5)

