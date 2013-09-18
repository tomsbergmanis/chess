import piece

EN_PASSANTLINE_W = 4
EN_PASSANTLINE_B = 3

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
		self.board[7][4] = ColoredChessPiece("B", piece.King(5,8,5,8))
		
		self.board[6][0] = ColoredChessPiece("B", piece.Pawn(1,7,7))
		self.board[6][1] = ColoredChessPiece("B", piece.Pawn(2,7,7))
		self.board[6][2] = ColoredChessPiece("B", piece.Pawn(3,7,7))
		self.board[6][3] = ColoredChessPiece("B", piece.Pawn(4,7,7))
		self.board[6][4] = ColoredChessPiece("B", piece.Pawn(5,7,7))
		self.board[6][5] = ColoredChessPiece("B", piece.Pawn(6,7,7))
		self.board[6][6] = ColoredChessPiece("B", piece.Pawn(7,7,7))
		self.board[6][7] = ColoredChessPiece("B", piece.Pawn(8,7,7))
		
		self.__white_king_moved__ = False
		self.__black_king_moved__ = False
		self.__white_a_rook_moved__ = False
		self.__white_e_rook_moved__ = False
		self.__black_a_rook_moved__ = False
		self.__black_e_rook_moved__ = False
		
		self.__en_passant_possible__ = -1
		
		
	def move_piece(self, old_i, old_j, new_i, new_j):
		if self.is_legal_move(old_i, old_j, new_i, new_j):
			#print old_i, old_j, new_i, new_j
			self.board[new_i][new_j] = self.board[old_i][old_j]
			#have to add one due to difference in representations
			self.board[new_i][new_j].decorated.move_piece( new_j+1, new_i+1) 
			self.board[old_i][old_j] = None
			self.__update_board__(old_i, old_j, new_i, new_j)
			
	def __place_piece__(self, old_i, old_j, new_i, new_j):
		self.board[new_i][new_j] = self.board[old_i][old_j]
		#have to add one due to difference in representations
		self.board[new_i][new_j].decorated.move_piece( new_j+1, new_i+1) 
		self.board[old_i][old_j] = None
		
	def remove_piece(self, i,j):
		self.board[i][j] = None
	
	def __update_board__(self, old_i, old_j, new_i, new_j):
		if self.board[new_i][new_j].decorated.__repr__() == "K":
			if self.board[new_i][new_j].colour == "W":
				self.__white_king_moved__ = True
			else:
				self.__black_king_moved__ = True
		elif self.board[new_i][new_j].decorated.__repr__() == "R":
			if self.board[new_i][new_j].colour == "W":
				if old_i == 0 and old_j == 0:
					self.__white_a_rook_moved__ = True
				elif old_i == 0  and old_j == 7:
					self.__white_e_rook_moved__ = True
			else:
				if old_i == 7 and old_j == 0:
					self.__black_a_rook_moved__ = True
				elif old_i == 7  and old_j == 7:
					self.__black_e_rook_moved__ = True
		elif self.board[new_i][new_j].decorated.__repr__() == "P":
			if old_i == 1 or old_i == 6:
				if new_i == 3 or new_i == 4:
					self.__en_passant_possible__ = new_j
		if not self.board[new_i][new_j].decorated.__repr__() == "P":
			self.__en_passant_possible__ = -1
	
	def is_legal_move(self, old_i, old_j, new_i, new_j):
		if self.board[old_i][old_j].decorated.__repr__() == "B":
			is_accessible = self.is_accessible_by_B(old_i, old_j, new_i, new_j)
		elif self.board[old_i][old_j].decorated.__repr__() == "R":
			is_accessible = self.is_accessible_by_R(old_i, old_j, new_i, new_j)
		elif self.board[old_i][old_j].decorated.__repr__() == "Q":
			is_accessible = self.is_accessible_by_Q(old_i, old_j, new_i, new_j)
		elif self.board[old_i][old_j].decorated.__repr__() == "K":
			is_accessible = self.is_accessible_by_K(old_i, old_j, new_i, new_j)
		elif self.board[old_i][old_j].decorated.__repr__() == "P":
			is_accessible = self.is_accessible_by_P(old_i, old_j, new_i, new_j)
		else:
			is_accessible = True
		
		return self.is_legal_move_by_piece(old_i, old_j, new_i, new_j) \
				and self.is_target_sq_occupiable(old_i, old_j, new_i, new_j) \
				and is_accessible
	
	def is_legal_move_by_piece(self, old_i, old_j, new_i, new_j):
		if old_i != new_i or old_j != new_j:
			#have to add one due to difference in representations
			move_to = (new_j+1, new_i+1)
			if not self.is_empty(old_i, old_j):
				if move_to in self.board[old_i][old_j].decorated.move_options():
					return True
				else:
					return False
			else:
				return False	
		else: 
			return False
			
	def is_target_sq_occupiable(self, old_i, old_j, new_i, new_j):
		if self.is_empty(new_i, new_j):
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
		
	def is_accessible_by_Q(self, old_i, old_j, new_i, new_j):
		if old_i == new_i or old_j == new_j:
			return self.is_accessible_by_R(old_i, old_j, new_i, new_j)
		else: 
			return self.is_accessible_by_B(old_i, old_j, new_i, new_j)
		
	def is_accessible_by_K(self, old_i, old_j, new_i, new_j):
	
		colour = self.board[old_i][old_j].colour
		if colour == "W":
			if old_j == new_j - 2:
				if self.__white_king_moved__ == False and \
					self.__white_e_rook_moved__ == False:
					op_colour = self.__other_colour__(old_i, old_j)
					self.__place_piece__(old_i, old_j, old_i, old_j + 1)
					answer1 =  not self.is_attacked(old_i, old_j + 1, op_colour)
					self.__place_piece__(old_i, old_j + 1, old_i, old_j + 2)
					answer2 =  not self.is_attacked(old_i, old_j + 2, op_colour)
					self.__place_piece__(old_i, old_j + 2, old_i, old_j)
					return answer1 and answer2
				else:
					return False
			if old_j == new_j + 2:
				if self.__white_king_moved__ == False and \
					self.__white_a_rook_moved__ == False:
					op_colour = self.__other_colour__(old_i, old_j)
					self.__place_piece__(old_i, old_j, old_i, old_j - 1)
					answer1 =  not self.is_attacked(old_i, old_j - 1, op_colour)
					self.__place_piece__(old_i, old_j - 1, old_i, old_j - 2)
					answer2 =  not self.is_attacked(old_i, old_j - 2, op_colour)
					self.__place_piece__(old_i, old_j - 2, old_i, old_j)
					return answer1 and answer2
				else:
					return False
		else:
			if old_j == new_j - 2:
				if self.__black_king_moved__ == False and \
					self.__black_e_rook_moved__ == False:
					op_colour = self.__other_colour__(old_i, old_j)
					self.__place_piece__(old_i, old_j, old_i, old_j + 1)
					answer1 =  not self.is_attacked(old_i, old_j + 1, op_colour)
					self.__place_piece__(old_i, old_j + 1, old_i, old_j + 2)
					answer2 =  not self.is_attacked(old_i, old_j + 2, op_colour)
					self.__place_piece__(old_i, old_j + 2, old_i, old_j)
					return answer1 and answer2
				else:
					return False
			if old_j == new_j + 2:
				if self.__black_king_moved__ == False and \
					self.__black_a_rook_moved__ == False:
					op_colour = self.__other_colour__(old_i, old_j)
					self.__place_piece__(old_i, old_j, old_i, old_j - 1)
					answer1 =  not self.is_attacked(old_i, old_j - 1, op_colour)
					self.__place_piece__(old_i, old_j - 1, old_i, old_j - 2)
					answer2 =  not self.is_attacked(old_i, old_j - 2, op_colour)
					self.__place_piece__(old_i, old_j - 2, old_i, old_j)
					return answer1 and answer2
				else:
					return False
			
		op_colour = self.__other_colour__(old_i, old_j)
		self.__place_piece__(old_i, old_j, new_i, new_j)
		answer =  not self.is_attacked(new_i, new_j, op_colour)
		self.__place_piece__( new_i, new_j, old_i, old_j)
		return answer
	
	def is_accessible_by_P(self, old_i, old_j, new_i, new_j):
		if old_j == new_j:
			if self.is_empty(new_i, new_j):
				return True
			else:
				return False
		else:
			if not self.is_empty(new_i, new_j):
				op = self.__other_colour__(old_i, old_j)
				if self.board[new_i][new_j].colour == op:
					return True
				else:
					return False
			elif self.__en_passant_possible__ >= 0:
				if self.board[old_i][old_j].colour == 'W':
					if old_i == EN_PASSANTLINE_W and \
						self.__en_passant_possible__ == new_j:
						return True
				else:
					if old_i == EN_PASSANTLINE_B and \
						self.__en_passant_possible__ == new_j:
						return True
			else:
				return False
	
	def is_attacked(self, sq_i, sq_j, op):
		
		for i in range(8):
			for j in range(8):
				if self.is_empty(i, j):
					continue
				else:
					if self.board[i][j].colour == op:
						if self.board[i][j].decorated.__repr__() == "K":
							#have to add one due to difference in representations
							if (sq_j + 1, sq_i + 1 ) in \
								self.board[i][j].decorated.move_options():
								return True
						else:
							if self.is_legal_move(i, j, sq_i, sq_j):
								return True
		return False
	
	def is_casteling(self, prev_i, prev_j, i, j):
		if self.board[i][j].decorated.__repr__() == "K":
			if abs(prev_j - j) == 2:
				return True
		else:
			return False
			
	def is_empasant(self, prev_i, prev_j, i, j):
		if self.board[prev_i][prev_j].decorated.__repr__() == "P":
			if abs(prev_j - j) == 1 and abs(prev_i - i) == 1 \
				and self.is_empty(i, j):
				return True
		else:
			return False
	
	def __other_colour__(self, i, j):
		colour = self.board[i][j].colour
		if colour == "W":
			return "B"
		else:
			return "W"
	def __is_square__(self, i, j):
		return i < 8 and i > -1 and j < 8 and j > -1
		
	def is_empty(self, i, j):
		return self.board[i][j].__repr__() == 'None'
	
	def set_rook_moved(self, colour, flank):
		if colour == 'W':
			if flank == 'e':
				self.__white_e_rook_moved=True
			else:
				self.__white_a_rook_moved = False
		else:
			if flank == 'e':
				self.__white_e_rook_moved=True
			else:
				self.__white_a_rook_moved = False
		