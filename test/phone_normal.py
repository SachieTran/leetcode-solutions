kvmap = {
	"1":"abc",
	"2":"def",
	"3":"ght",
	"4":"jkl",
	"5":"mno",
	"6":"pqrs",
	"7":"tuv",
	"8":"wxyz"
}

def wordCombinations(number, result):
	if len(number)==0:
		print result
		return

	for c in kvmap[number[0]]:
		wordCombinations(number[1:], result+c)

wordCombinations("11","")
