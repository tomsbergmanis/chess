import Tkinter as tk
import board as b
from PIL import Image, ImageTk 



root = tk.Tk()

path = "art\\"
wp = ImageTk.PhotoImage(Image.open(path+"wp.png"))
wk = ImageTk.PhotoImage(Image.open(path+"wk.png"))
wq = ImageTk.PhotoImage(Image.open(path+"wq.png"))
wr = ImageTk.PhotoImage(Image.open(path+"wr.png"))
wb = ImageTk.PhotoImage(Image.open(path+"wb.png"))
wn = ImageTk.PhotoImage(Image.open(path+"wn.png"))

bp = ImageTk.PhotoImage(Image.open(path+"bp.png"))
bk = ImageTk.PhotoImage(Image.open(path+"bk.png"))
bq = ImageTk.PhotoImage(Image.open(path+"bq.png"))
br = ImageTk.PhotoImage(Image.open(path+"br.png"))
bb = ImageTk.PhotoImage(Image.open(path+"bb.png"))
bn = ImageTk.PhotoImage(Image.open(path+"bn.png"))

empty = ImageTk.PhotoImage(Image.open(path+"empty.png"))




def getArt(piece, i, j):
	color = "white" if (i+j)%2 else "gray55"
	if piece.__repr__() == "WP":
		return tk.Label(root,  image=wp, bg=color)
	elif piece.__repr__() == "BP":
		return tk.Label(root,  image=bp, bg=color)
	elif piece.__repr__() == "WB":
		return tk.Label(root,  image=wb, bg=color)
	elif piece.__repr__() == "BB":
		return tk.Label(root,  image=bb, bg=color)
	elif piece.__repr__() == "WN":
		return tk.Label(root,  image=wn, bg=color)
	elif piece.__repr__() == "BN":
		return tk.Label(root,  image=bn, bg=color)
	elif piece.__repr__() == "WR":
		return tk.Label(root,  image=wr, bg=color)
	elif piece.__repr__() == "BR":
		return tk.Label(root,  image=br, bg=color)
	elif piece.__repr__() == "WK":
		return tk.Label(root,  image=wk, bg=color)			
	elif piece.__repr__() == "BK":
		return tk.Label(root,  image=bk, bg=color)
	elif piece.__repr__() == "WQ":
		return tk.Label(root,  image=wq, bg=color)
	elif piece.__repr__() == "BQ":
		return tk.Label(root,  image=bq, bg=color)
	else:		
		return tk.Label(root, image=empty, bg=color)

def on_click(i,j,event):
	global prev_i
	global prev_j
	if prev_i == -1 and prev_j == -1:
		if not board.is_empty(i,j):
			prev_i = i
			prev_j = j
	else:
		is_empasant = board.is_empasant(prev_i, prev_j, i, j)
		if board.is_legal_move(prev_i, prev_j, i, j):
			color = "white" if (i+j)%2 else "gray55"
			L = getArt(board.board[prev_i][prev_j], i, j)
			L.grid(row=7-i,column=j)
			L.bind('<Button-1>', lambda e, i = i, j = j: on_click(i, j, e))
			board.move_piece(prev_i, prev_j, i, j)
			
			if i != prev_i or j != prev_j:
				color = "white" if (prev_i + prev_j) % 2 else "gray55"
				L1 = getArt(board.board[prev_i][prev_j], prev_i, prev_j)
				L1.grid(row = 7 - prev_i, column = prev_j)
				L1.bind('<Button-1>',lambda e, prev_i = prev_i, prev_j = prev_j: \
						on_click(prev_i, prev_j, e))
			
			if board.is_casteling(prev_i, prev_j, i, j):
				if prev_j - j == -2:
					board.set_rook_moved(board.board[i][j].colour, 'e')
					prev_i = i
					prev_j = j + 1
					i = i
					j = j - 1
					
				else:
					board.set_rook_moved(board.board[i][j].colour, 'a')
					prev_i = i
					prev_j = j -2
					i = i
					j = j + 1
				color = "white" if (i+j)%2 else "gray55"
				L3 = getArt(board.board[prev_i][prev_j], i, j)
				L3.grid(row=7-i,column=j)
				L3.bind('<Button-1>', lambda e, i = i, j = j: on_click(i, j, e))
				board.__place_piece__(prev_i, prev_j, i, j)
			
				color = "white" if (prev_i + prev_j) % 2 else "gray55"
				L4 = getArt(board.board[prev_i][prev_j], prev_i, prev_j)
				L4.grid(row = 7 - prev_i, column = prev_j)
				L4.bind('<Button-1>',lambda e, prev_i = prev_i, prev_j = prev_j: \
							on_click(prev_i, prev_j, e))
			
			if is_empasant:
				i = prev_i
				j = j
				color = "white" if (i+j)%2 else "gray55"
				L3 = tk.Label(root, image=empty, bg=color)
				L3.grid(row=7-i,column=j)
				L3.bind('<Button-1>', lambda e, i = i, j = j: on_click(i, j, e))
				board.remove_piece(i,j)
							
		prev_i = -1
		prev_j = -1
		
			
		
if __name__ == "__main__":
	global prev_i 
	prev_i = -1	
	global prev_j 
	prev_j = -1
	global board
	board = b.Board()
	for i,row in enumerate(board.board):
		for j,column in enumerate(row):
			color = "white" if (i+j)%2 else "gray55"
			L = getArt(board.board[i][j], i, j)
			L.grid(row=7-i,column=j)
			L.bind('<Button-1>',lambda e,i=i,j=j: on_click(i,j,e))
			
	root.mainloop()


