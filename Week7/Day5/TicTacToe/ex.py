# Mini-Project - Tic Tac Toe

board = [
	[' ', ' ', ' '],
	[' ', ' ', ' '],
	[' ', ' ', ' ']
]

def display_board():
	print(f"{board[0][0]} | {board[0][1]} | {board[0][2]}")
	print("--+---+--")
	print(f"{board[1][0]} | {board[1][1]} | {board[1][2]}")
	print("--+---+--")
	print(f"{board[2][0]} | {board[2][1]} | {board[2][2]}")
display_board()