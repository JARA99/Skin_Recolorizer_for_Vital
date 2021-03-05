import tkinter as tk
from tkinter import ttk
 

path = input('Skin source at: ')
if path == '':
    path = './src/default.vitalskin'
SkinSource = open(path,'r')
#SkinSource = open('./src/default.vitalskin','r')
skin = SkinSource.read()

colors = set()
data = 0
i = 0

while i != -1:
    i += 1
    i = skin.find(':"', i)
    j = skin.find('"', i+2)

    color = str(skin[i+2:j])
    if len(color) == 8:
        #print(color)
        colors.add(str(color[1:7]))

SkinColors = list(colors)
SkinColors.sort()

print()
print(SkinColors)
print()
print()
print('Este tema contiene ' + str(len(colors)) + ' colores distintos')

################################################## GUI ###############################################################

root = tk.Tk()

label = tk.Label(root, text="what's my favorite video?", background='#'+str(SkinColors[1]))
label.pack()
click_here = tk.Button(root, text="click here to find out", padx = 10, pady = 5)
click_here.pack()

root.mainloop()