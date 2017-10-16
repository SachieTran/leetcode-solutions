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

number = "223"

def possible_word(number, result):
	if number=="":
		print result
		return
	else:
		for c in kvmaps[number[0]]:
			possible_word(number[1:], result+c)

possible_word(number, "")
