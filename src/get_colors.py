import tkinter as tk


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
        colors.add(str(color[2:8]))

SkinColors = list(colors)
SkinColors.sort()
SkCoLen = len(SkinColors)

print()
print(SkinColors)
print()
print()
print('Este tema contiene ' + str(len(colors)) + ' colores distintos')

################################################## GUI ###############################################################

root = tk.Tk()
root.title('Vital theme recolor')
label = []
entries = []

#scroll = tk.Scrollbar(root).pack(side = tk.RIGHT, fill = tk.Y)
 
for r in range(10):
    for c in range(10):
        i = c+(10*r)
        if i < len(SkinColors):
            tk.Label(root, text=str(SkinColors[i]), background='#'+str(SkinColors[i]), width = 9, height = 1).grid(row = 2*r, column = c)
            #entry = tk.Entry(root, width = 9).grid(row = 2*r+1, column = c)
            #entries[r][c] = entry


root.mainloop()