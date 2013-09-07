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
		if self.is_legal_move(old_i, old_j, new_i, new_j):
			self.board[new_i][new_j] = self.board[old_i][old_j]
			#have to add one due to difference in representations
			self.board[new_i][new_j].decorated.move_piece( new_j+1, new_i+1) 
			self.board[old_i][old_j] = None
	
	def is_legal_move(self, old_i, old_j, new_i, new_j):
		if self.board[old_i][old_j].decorated.__repr__() == "B":
			is_accessible = self.is_accessible_by_B(old_i, old_j, new_i, new_j)
		elif self.board[old_i][old_j].decorated.__repr__() == "R":
			is_accessible = self.is_accessible_by_R(old_i, old_j, new_i, new_j)
		else:
			is_accessible = True
		return self.is_legal_move_by_piece(old_i, old_j, new_i, new_j) \
				and self.is_target_sq_occupiable(old_i, old_j, new_i, new_j) \
				and is_accessible
	
	def is_legal_move_by_piece(self, old_i, old_j, new_i, new_j):
		if old_i != new_i or old_j != new_j:
			#have to add one due to difference in representations
			move_to = (new_j+1, new_i+1)
			if self.board[old_i][old_j] != None:
				if move_to in self.board[old_i][old_j].decorated.move_options():
					return True
				else:
					return False
			else:
				return False	
		else: 
			return False
			
	def is_target_sq_occupiable(self, old_i, old_j, new_i, new_j):
		if self.board[new_i][new_j] == None:
			return True
		else:
			piece_colour = self.board[old_i][ old_j].colour
			target_colour = self.board[new_i][ new_j].colour
			if piece_colour != target_colour:
				return True
			else:
				return False
			
	def is_accessible_by_B(self, old_i, old_j, new_i, new_j):
		i, j = old_i + 1, old_j + 1
		while i < new_i and j < new_j:
			if self.is_empty(i, j):
				i += 1
				j += 1
				continue
			else: 
				return False
		i, j = old_i + 1, old_j - 1
		while i < new_i and j > new_j:
			if self.is_empty(i, j):
				i += 1
				j -= 1
				continue
			else:
				return False
		i, j = old_i - 1, old_j + 1
		while i > new_i and j < new_j:
			if self.is_empty(i, j):
				i -= 1
				j += 1
				continue
			else:
				return False
		i, j = old_i - 1, old_j - 1
		while i > new_i and j > new_j:
			if self.is_empty(i, j):
				i -= 1
				j -= 1
				continue
			else:
				return False
		return True
	
	def is_accessible_by_R(self, old_i, old_j, new_i, new_j):
		i, j = old_i + 1, old_j
		while i < new_i:
			if self.is_empty(i, j):
				i += 1
				continue
			else: 
				return False
		i, j = old_i,  old_j - 1
		while j > new_j:
			if self.is_empty(i, j):
				j -= 1
				continue
			else:
				return False
		i, j = old_i - 1, old_j
		while i > new_i:
			if self.is_empty(i, j):
				i -= 1
				continue
			else:
				return False
		i, j = old_i, old_j + 1
		while j < new_j:
			if self.is_empty(i, j):
				j += 1
				continue
			else:
				return False
		return True
		
	def is_empty(self, i, j):
		return self.board[i][j] == None 