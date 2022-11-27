import tkinter as tk

root = tk.Tk()
vscrollbar = tk.Scrollbar(root)

canvas = tk.Canvas(
    root, width=1300, height=900, bg="white", yscrollcommand=vscrollbar.set
)
canvas.pack()

vscrollbar.config(command=canvas.yview)
vscrollbar.pack(side=tk.LEFT, fill=tk.Y)

f = tk.Frame(canvas)

canvas.pack(side="left", fill="both", expand=True)


canvas.create_window(0, 0, window=f, anchor="nw")
n = 1
w = 3


y1 = 0
y2 = 40000
for k in range(0, 200, 100):
    x1 = k
    x2 = k
    canvas.create_line(x1, y1, x2, y2, width=n, fill="white")

lis = [
[[0, 5], [4, -2.0], [-3, -1.5], [0, -2], [-1, 0.5]],
[[0, 7], [6, -3.0], [0, -5], [-4, -2.0], [-3, 1.5], [2, 1.0], [-1, 0.5]],
[[0, 7], [6, -3.0], [0, -5], [-4, -2.0], [-3, 1.5], [0, 2], [1, -0.5]],
]


count1 = 1
count2 = 1

x1 = 0
y1 = 100
x2 = 0
y2 = 100

for a in lis:
    if count1 == 1:
        x1 = 100
        x2 = 100
    elif count1 == 2:
        x1 = 300
        x2 = 300
    elif count1 == 3:
        x1 = 500
        x2 = 500
    elif count1 == 4:
        x1 = 700
        x2 = 700
    elif count1 == 5:
        x1 = 900
        x2 = 900
    elif count1 == 6:
        x1 = 1100
        x2 = 1100
    for p in a:
        if p[0] == 0 and p[1] > 0:
            canvas.create_line(
                x1, y1, x2 + (p[1] * 5), y2, width=n, fill="black")
            x2 += p[1] * 5
            x1 = x2
        elif p[0] == 0 and p[1] < 0:
            canvas.create_line(
                x1, y1, x2 + (p[1] * 5), y2, width=n, fill="black")
            x2 += p[1] * 5
            x1 = x2
        elif p[0] < 0 and p[1] > 0:
            canvas.create_line(
                x1, y1, x2 + (p[1] * 5), y2 - (p[0] * 5), width=n, fill="black"
            )
            x2 += p[1] * 5
            x1 = x2
            y2 -= p[0] * 5
            y1 = y2
        elif p[0] > 0 and p[1] < 0:
            canvas.create_line(
                x1, y1, x2 + (p[1] * 5), y2 - (p[0] * 5), width=n, fill="black"
            )
            x2 += p[1] * 5
            x1 = x2
            y2 -= p[0] * 5
            y1 = y2
        elif p[0] < 0 and p[1] < 0:
            canvas.create_line(
                x1, y1, x2 + (p[1] * 5), y2 - (p[0] * 5), width=n, fill="black"
            )
            x2 += p[1] * 5
            x1 = x2
            y2 -= p[0] * 5
            y1 = y2
        elif p[0] > 0 and p[1] > 0:
            canvas.create_line(
                x1, y1, x2 + (p[1] * 5), y2 - (p[0] * 5), width=n, fill="black"
            )
            x2 += p[1] * 5
            x1 = x2
            y2 -= p[0] * 5
            y1 = y2
    if count1 != 6:
        count1 += 1
        count2 += 1
    else:
        count1 = 1
        count2 = 1
        y1 += 240
        y2 = y1

root.update()
canvas.config(scrollregion=canvas.bbox("all"))


root.mainloop()
