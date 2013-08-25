
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
	
class Pawn(ChessPiece):
	
	def __init__(self, initial_y):
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
		if self.pos_x - 1 < BMIN:
			moves.append((self.pos_x - 1, self.pos_y + 1*dir))
			
		return moves


class Rook(ChessPiece):

	def move_options(self):
		moves = []
		for i in range(1,BMAX):
			moves.append((self.pos_x, i))
			
		for i in range(1, BMAX):
			moves.append((i, self.pos_y))
			
		return moves
		

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


class King(ChessPiece):
	
	def move_options(self):
		"""
		>>> King(5,5).move_options()
		[(4, 6), (6, 6), (5, 6), (4, 4), (6, 4), (5, 4), (6, 4), (6, 6), (6, 5), (4, 4), (4, 6), (4, 5)]
		"""
		moves = []
		x = self.pos_x
		y = self.pos_y
		if y + 1 < BMAX:
			if x - 1 > BMIN:
				moves.append((x - 1, y + 1))
			
			if x + 1 < BMAX:
				moves.append((x + 1, y + 1))
		
			moves.append((x, y + 1))
			
		if y - 1 > BMIN:
			if x - 1 > BMIN:
				moves.append((x - 1, y - 1))
			
			if x + 1 < BMAX:
				moves.append((x + 1, y - 1))		
			
			moves.append((x, y - 1))
				
		if x + 1 < BMAX:
			if y - 1 > BMIN:
				moves.append((x + 1, y - 1))
			
			if y + 1 < BMAX:
				moves.append((x + 1, y + 1))
		
			moves.append((x + 1, y))
			
		if x - 1 > BMIN:
			if y - 1 > BMIN:
				moves.append((x - 1, y - 1))
			
			if y + 1 < BMAX:
				moves.append((x - 1, y + 1))
						
			moves.append((x - 1, y))

		return moves
	
if __name__ == "__main__":
    import doctest
    doctest.testmod()