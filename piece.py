class ChessPiece(object):

	def __init__(self, x, y):
		self.pos_x = x
		self.pos_y = y
	
	def move_options(self):
		pass
	
class Pawn(object):
	
	def __init__(self, piece, initial_y):
		self.piece = piece	
		self.initial_y = initial_y
		
	def move_options(self):
		moves = []
		if self.initial_y == 2:
			dir = 1
		else:
			dir = -1
			
		# move 1 forth
		moves.append((self.piece.pos_x,self.piece.pos_y + 1*dir))
		# move 2 forth from initial pos
		
		if self.piece.pos_y == self.initial_y:
			moves.append((self.piece.pos_x,self.piece.pos_y + 2*dir))
		
		# take piece on the right
		if self.piece.pos_x + 1 < 9:
			moves.append((self.piece.pos_x + 1, self.piece.pos_y + 1*dir))
			
		# take piece on the left
		if self.piece.pos_x - 1 < 0:
			moves.append((self.piece.pos_x - 1, self.piece.pos_y + 1*dir))
			
		return moves


class Rook(object):

	def __init__(self, piece):
		self.piece = piece

	def move_options(self):
		moves = []
		for i in range(1,9):
			moves.append((self.piece.pos_x, i))
			
		for i in range(1,9):
			moves.append((i, self.piece.pos_y))
			
		return moves
		

class Bishop(object):
	