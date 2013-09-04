import Tkinter as tk
import board as b
from PIL import Image, ImageTk 

board = b.Board().board

counter = 0
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



def on_click(i,j,event):
	pass
	
for i,row in enumerate(board):
    for j,column in enumerate(row):
		color = "white" if (i+j)%2 else "gray55"
		if board[i][j].__repr__() == "WP":
			L = tk.Label(root,  image=wp, bg=color)
		elif board[i][j].__repr__() == "BP":
			L = tk.Label(root,  image=bp, bg=color)
		elif board[i][j].__repr__() == "WB":
			L = tk.Label(root,  image=wb, bg=color)
		elif board[i][j].__repr__() == "BB":
			L = tk.Label(root,  image=bb, bg=color)
		elif board[i][j].__repr__() == "WN":
			L = tk.Label(root,  image=wn, bg=color)
		elif board[i][j].__repr__() == "BN":
			L = tk.Label(root,  image=bn, bg=color)
		elif board[i][j].__repr__() == "WR":
			L = tk.Label(root,  image=wr, bg=color)
		elif board[i][j].__repr__() == "BR":
			L = tk.Label(root,  image=br, bg=color)
		elif board[i][j].__repr__() == "WK":
			L = tk.Label(root,  image=wk, bg=color)			
		elif board[i][j].__repr__() == "BK":
			L = tk.Label(root,  image=bk, bg=color)
		elif board[i][j].__repr__() == "WQ":
			L = tk.Label(root,  image=wq, bg=color)
		elif board[i][j].__repr__() == "BQ":
			L = tk.Label(root,  image=bq, bg=color)
		else:
			L = tk.Label(root, image=empty, bg=color)
		L.grid(row=7-i,column=j)
		L.bind('<Button-1>',lambda e,i=i,j=j: on_click(i,j,e))

root.mainloop()