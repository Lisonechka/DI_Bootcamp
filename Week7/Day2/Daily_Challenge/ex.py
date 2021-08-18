# Solve The Matrix
matrix_text = [
    ['7', 'i', '3'],
    ['T', 's', 'i'],
    ['h', '%', 'x'],
    ['i', ' ' , '#'],
    ['s', 'M', ' '],
    ['$', 'a', ' '],
    ['#', 't', '%'],
    ['^', 'r', '!']
    ]
result = ''
num_of_column = len(matrix_text[0])
num_of_rows = len(matrix_text)
for i in range(num_of_column):
	for j in range(num_of_rows):
		# scan the column
		if matrix_text[j][i].isalpha():
			result += matrix_text[j][i]
		elif result and result[-1] != ' ':  # result is not an empty string and the last item is not a space
			result += ' '

print(result)
