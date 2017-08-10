kvmaps = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }


digits = '2234'
result = []
def digitToString(n, output):
	if n<0:
		result.append(output)
		return
	for ch in kvmaps[digits[n]]:
		digitToString(n-1,ch+output)

digitToString(3,'')
print result, len(result)

