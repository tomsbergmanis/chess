
UP = 1
DOWN = -1
RIGHT = 1
LEFT = -1

BMAX = 9
BMIN = 0


class ChessPiece(object):

	def __init__(self, x, y):
		self.pos_x = x
		self.pos_y = y
	
	def move_options(self):
		pass
		
	def move_piece(self, x, y):
		self.pos_x = x
		self.pos_y = y
	
	def __repr__(self):
		pass
	
	
class Pawn(ChessPiece):
	
	def __init__(self, x, y, initial_y):
		self.pos_x = x
		self.pos_y = y
		self.initial_y = initial_y
		
	def move_options(self):
		moves = []
		if self.initial_y == 2:
			dir = UP
		else:
			dir = DOWN
			
		# move 1 forth
		moves.append((self.pos_x,self.pos_y + 1*dir))
		
		# move 2 forth from initial pos
		if self.pos_y == self.initial_y:
			moves.append((self.pos_x,self.pos_y + 2*dir))
		
		# take piece on the right
		if self.pos_x + 1 <  BMAX:
			moves.append((self.pos_x + 1, self.pos_y + 1*dir))
			
		# take piece on the left
		if self.pos_x - 1 > BMIN:
			moves.append((self.pos_x - 1, self.pos_y + 1*dir))
			
		return moves

	def __repr__(self):
		return "P"


class Rook(ChessPiece):

	def move_options(self):
		moves = []
		for i in range(1,BMAX):
			if i != self.pos_y:
				moves.append((self.pos_x, i))
			
		for i in range(1, BMAX):
			if i != self.pos_x:
				moves.append((i, self.pos_y))
			
		return moves
	
	def __repr__(self):
		return "R"


class Bishop(ChessPiece):

	
	def move_options(self):
		moves = []

		moves.extend(self.__extend_diognal__(UP, RIGHT))
		moves.extend(self.__extend_diognal__(DOWN, LEFT))
		
		moves.extend(self.__extend_diognal__(UP, LEFT))
		moves.extend(self.__extend_diognal__(DOWN, RIGHT))

		return moves
		
	def __extend_diognal__(self, x_dir, y_dir):
		squares = []
		x = self.pos_x + x_dir
		y = self.pos_y + y_dir
		
		while x <  BMAX and y < BMAX and x > BMIN and y > BMIN:
			squares.append((x,y))
			x = x + x_dir
			y = y + y_dir

		return squares
	
	def __repr__(self):
		return "B"


class Knight(ChessPiece):
		
	def move_options(self):
		"""
		>>> Knight(1,1).move_options()
		[(2, 3), (3, 2)]
		
		>>> Knight(8,8).move_options()
		[(7, 6), (6, 7)]

		>>> Knight(1,8).move_options()
		[(2, 6), (3, 7)]
		
		>>> Knight(8,1).move_options()
		[(7, 3), (6, 2)]
		
		>>> Knight(5,5).move_options()
		[(4, 7), (6, 7), (4, 3), (6, 3), (7, 4), (7, 6), (3, 4), (3, 6)]
		
		"""
		moves = []
		x = self.pos_x
		y = self.pos_y
		if y + 2 < BMAX:
			if x - 1 > BMIN:
				moves.append((x - 1, y + 2))
			
			if x + 1 < BMAX:
				moves.append((x + 1, y + 2))

		if y - 2 > BMIN:
			if x - 1 > BMIN:
				moves.append((x - 1, y - 2))
			
			if x + 1 < BMAX:
				moves.append((x + 1, y - 2))
				
		if x + 2 < BMAX:
			if y - 1 > BMIN:
				moves.append((x + 2, y - 1))
			
			if y + 1 < BMAX:
				moves.append((x + 2, y + 1))

		if x - 2 > BMIN:
			if y - 1 > BMIN:
				moves.append((x - 2, y - 1))
			
			if y + 1 < BMAX:
				moves.append((x - 2, y + 1))

		return moves
	
	def __repr__(self):
		return "N"
		

class King(ChessPiece):
	
	def __init__(self, x, y, initial_x, initial_y):
		self.pos_x = x
		self.pos_y = y
		self.initial_y = initial_y
		self.initial_x = initial_x
		
	def move_options(self):
		"""
		>>> King(5,5,5,1).move_options() #doctest: +NORMALIZE_WHITESPACE
		[(4, 6), (6, 6), (5, 6), (4, 4), (6, 4), (5, 4), (6, 4), (6, 6), 
		(6, 5), (4, 4), (4, 6), (4, 5)]
		"""
		moves = []
		x = self.pos_x
		y = self.pos_y
		if y + 1 < BMAX:
			if x - 1 > BMIN:
				moves.append((x - 1, y + 1))  #up left 
			
			if x + 1 < BMAX:
				moves.append((x + 1, y + 1))  #up right 
		
			moves.append((x, y + 1)) #up
			
		if y - 1 > BMIN:
			if x - 1 > BMIN:
				moves.append((x - 1, y - 1)) #down left 
			
			if x + 1 < BMAX:
				moves.append((x + 1, y - 1)) #down rigt 
			
			moves.append((x, y - 1)) #down 
				
		if x + 1 < BMAX:
			if y - 1 > BMIN:
				moves.append((x + 1, y - 1)) #right down
			
			if y + 1 < BMAX:
				moves.append((x + 1, y + 1)) #right up
		
			moves.append((x + 1, y)) #right 
			
		if x - 1 > BMIN:
			if y - 1 > BMIN:
				moves.append((x - 1, y - 1)) #left down
			
			if y + 1 < BMAX:
				moves.append((x - 1, y + 1)) #left up
						
			moves.append((x - 1, y)) #left

		if x == self.initial_x and y == self.initial_y: 
			moves.append((x + 2, y)) #Castle Kingside
			moves.append((x - 2, y)) #Castle Queenside 
			
		return moves
		
	def __repr__(self):
		return "K"

	
	
class Queen(ChessPiece):

	def __init__(self, x, y):
		self.pos_x = x
		self.pos_y = y
		self.__rook = Rook(x, y)
		self.__bishop = Bishop(x, y)
		
	def move_piece(self, x, y):
		self.pos_x = x
		self.pos_y = y
		self.__rook.move_piece(x, y)
		self.__bishop.move_piece(x, y)
		
	def move_options(self):
		"""
		>>> Queen(1,1).move_options() #doctest: +NORMALIZE_WHITESPACE
		[(1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (1, 7), (1, 8), (2, 1),
		(3, 1), (4, 1), (5, 1), (6, 1), (7, 1), (8, 1), (2, 2), (3, 3),
		(4, 4), (5, 5), (6, 6), (7, 7), (8, 8)]
		"""
		moves = []
		moves.extend(self.__rook.move_options())
		moves.extend(self.__bishop.move_options())
		return moves

	def __repr__(self):
		return "Q"

		
if __name__ == "__main__":
    
	import doctest
	doctest.testmod()