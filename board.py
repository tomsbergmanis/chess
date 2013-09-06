import piece

class ColoredChessPiece():

	def __init__ (self, colour, decorated):
		self.colour = colour
		self.decorated = decorated

	def __repr__(self):
		return self.colour+self.decorated.__repr__()

class Board():
	def __init__ (self):
		self.board = [[None for _ in range(8)] for _ in range(8)]
		
		self.board[0][0] = ColoredChessPiece("W", piece.Rook(1,1))
		self.board[0][7] = ColoredChessPiece("W", piece.Rook(8,1))
		
		self.board[0][1] = ColoredChessPiece("W", piece.Knight(2,1))
		self.board[0][6] = ColoredChessPiece("W", piece.Knight(7,1))
		
		self.board[0][2] = ColoredChessPiece("W", piece.Bishop(3,1))
		self.board[0][5] = ColoredChessPiece("W", piece.Bishop(6,1))
				
		self.board[0][3] = ColoredChessPiece("W", piece.Queen(4,1))
		self.board[0][4] = ColoredChessPiece("W", piece.King(5,1,5,1))
		
		self.board[1][0] = ColoredChessPiece("W", piece.Pawn(1,2,2))
		self.board[1][1] = ColoredChessPiece("W", piece.Pawn(2,2,2))
		self.board[1][2] = ColoredChessPiece("W", piece.Pawn(3,2,2))
		self.board[1][3] = ColoredChessPiece("W", piece.Pawn(4,2,2))
		self.board[1][4] = ColoredChessPiece("W", piece.Pawn(5,2,2))
		self.board[1][5] = ColoredChessPiece("W", piece.Pawn(6,2,2))
		self.board[1][6] = ColoredChessPiece("W", piece.Pawn(7,2,2))
		self.board[1][7] = ColoredChessPiece("W", piece.Pawn(8,2,2))
		
		
		self.board[7][0] = ColoredChessPiece("B", piece.Rook(1,8))
		self.board[7][7] = ColoredChessPiece("B", piece.Rook(8,8))
		
		self.board[7][1] = ColoredChessPiece("B", piece.Knight(2,8))
		self.board[7][6] = ColoredChessPiece("B", piece.Knight(7,8))
		
		self.board[7][2] = ColoredChessPiece("B", piece.Bishop(3,8))
		self.board[7][5] = ColoredChessPiece("B", piece.Bishop(6,8))
				
		self.board[7][3] = ColoredChessPiece("B", piece.Queen(4,8))
		self.board[7][4] = ColoredChessPiece("B", piece.King(5,1,5,8))
		
		self.board[6][0] = ColoredChessPiece("B", piece.Pawn(1,7,7))
		self.board[6][1] = ColoredChessPiece("B", piece.Pawn(2,7,7))
		self.board[6][2] = ColoredChessPiece("B", piece.Pawn(3,7,7))
		self.board[6][3] = ColoredChessPiece("B", piece.Pawn(4,7,7))
		self.board[6][4] = ColoredChessPiece("B", piece.Pawn(5,7,7))
		self.board[6][5] = ColoredChessPiece("B", piece.Pawn(6,7,7))
		self.board[6][6] = ColoredChessPiece("B", piece.Pawn(7,7,7))
		self.board[6][7] = ColoredChessPiece("B", piece.Pawn(8,7,7))
		
	def move_piece(self, old_i, old_j, new_i, new_j):
		self.board[new_i][new_j] = self.board[old_i][old_j]
		if old_i != new_i or old_j != new_j:
			self.board[old_i][old_j] = None

	def is_empty(self, i, j):
		return self.board[i][j] == None 