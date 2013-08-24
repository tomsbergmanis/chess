UP = 1
DOWN = -1
RIGHT = 1
LEFT = -1

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
			dir = UP
		else:
			dir = DOWN
			
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
	
	def __init__(self, piece):
		self.piece = piece
	
	def move_options(self):
		moves = []

		moves.extend(self.__extend_diognal__(UP, RIGHT))
		moves.extend(self.__extend_diognal__(DOWN, LEFT))
		
		moves.extend(self.__extend_diognal__(UP, LEFT))
		moves.extend(self.__extend_diognal__(DOWN, RIGHT))

		return moves
		
	def __extend_diognal__(self,x_dir, y_dir):
		squares = []
		x = self.piece.pos_x + x_dir
		y = self.piece.pos_y + y_dir
		
		while x < 9 and y < 9 and x > 0 and y > 0:
			squares.append((x,y))
			x = x + x_dir
			y = y + y_dir

		return squares