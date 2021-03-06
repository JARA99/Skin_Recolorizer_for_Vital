import tkinter as tk

################################################# Functions ################################################

def ChangeColor(n,col):
    NewSkinColors[n] = str(col)

def GetInput():
    n = int(OriginalColor.get())
    col = NewColor.get()
    ChangeColor(n,col)
    print(NewSkinColors)
    ColorTable.update()

    c = n%10
    r = int((n-c)/10)

    if NewSkinColors[n][::2].isdigit() == False:
        tk.Label(ColorTable, background='#'+str(NewSkinColors[n]), width = 1, height = 1).grid(row = 2*r, column = 3*c)
        tk.Label(ColorTable, background='#'+str(NewSkinColors[n]), width = 1, height = 1).grid(row = 2*r+1, column = 3*c)

        tk.Label(ColorTable, text='('+str(n)+') ', background='#'+str(NewSkinColors[n]), width = 12, height = 1).grid(row = 2*r, column = 3*c+2)
        tk.Label(ColorTable, text=str(NewSkinColors[n]), background='#'+str(NewSkinColors[n]), width = 12, height = 1).grid(row = 2*r+1, column = 3*c+2)
        
    else:
        tk.Label(ColorTable, background='#'+str(NewSkinColors[n]), width = 1, height = 1).grid(row = 2*r, column = 3*c)
        tk.Label(ColorTable, background='#'+str(NewSkinColors[n]), width = 1, height = 1).grid(row = 2*r+1, column = 3*c)

        tk.Label(ColorTable, text='('+str(n)+') ', background='#'+str(NewSkinColors[n]), width = 12, height = 1, fg = 'white').grid(row = 2*r, column = 3*c+2)
        tk.Label(ColorTable, text=str(NewSkinColors[n]), background='#'+str(NewSkinColors[n]), width = 12, height = 1, fg = 'white').grid(row = 2*r+1, column = 3*c+2)

    ColorTable.pack()

def SaveTheme():
    Savepath = input('Save to: ')
    if Savepath == '':
        Savepath = './out.vitalskin'
    SkinSink = open(Savepath,'w')
    #print(skin)
    new_skin = str(skin)
    for j in range(len(NewSkinColors)): 
        new_skin = new_skin.replace(SkinColors[j]+'"', NewSkinColors[j]+'"')
        print(SkinColors[j]+'"', 'y', NewSkinColors[j]+'"')

    #new_skin.replace('"Background"', 'ptaaaaa')

    SkinSink.write(new_skin)
    print(new_skin)
    return


################################################# Logic ####################################################


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
#NewSkinColors = list(colors)
NewSkinColors = SkinColors.copy()

print()
print(SkinColors)
print()
print()
print('Este tema contiene ' + str(len(colors)) + ' colores distintos')
print('lista nueva: ', NewSkinColors)


################################################## GUI ###############################################################

root = tk.Tk()
root.title('Theme recolorizer for Vital')
ColorTable = tk.Frame()
ColorChange = tk.Frame()

################################################# Color Table ########################################################

#scroll = tk.Scrollbar(root).pack(side = tk.RIGHT, fill = tk.Y)
 
for r in range(10):
    for c in range(10):
        i = c+(10*r)
        if i < len(SkinColors):
            if NewSkinColors[i][::2].isdigit() == False:
                tk.Label(ColorTable, background='#'+str(NewSkinColors[i]), width = 1, height = 1).grid(row = 2*r, column = 3*c)
                tk.Label(ColorTable, background='#'+str(NewSkinColors[i]), width = 1, height = 1).grid(row = 2*r+1, column = 3*c)

                tk.Label(ColorTable, background='#'+str(SkinColors[i]), width = 1, height = 1).grid(row = 2*r, column = 3*c+1)
                tk.Label(ColorTable, background='#'+str(SkinColors[i]), width = 1, height = 1).grid(row = 2*r+1, column = 3*c+1)

                tk.Label(ColorTable, text='('+str(i)+') ', background='#'+str(NewSkinColors[i]), width = 12, height = 1).grid(row = 2*r, column = 3*c+2)
                tk.Label(ColorTable, text=str(NewSkinColors[i]), background='#'+str(NewSkinColors[i]), width = 12, height = 1).grid(row = 2*r+1, column = 3*c+2)

                
            else:
                tk.Label(ColorTable, background='#'+str(NewSkinColors[i]), width = 1, height = 1).grid(row = 2*r, column = 3*c)
                tk.Label(ColorTable, background='#'+str(NewSkinColors[i]), width = 1, height = 1).grid(row = 2*r+1, column = 3*c)

                tk.Label(ColorTable, background='#'+str(SkinColors[i]), width = 1, height = 1).grid(row = 2*r, column = 3*c+1)
                tk.Label(ColorTable, background='#'+str(SkinColors[i]), width = 1, height = 1).grid(row = 2*r+1, column = 3*c+1)

                tk.Label(ColorTable, text='('+str(i)+') ', background='#'+str(NewSkinColors[i]), width = 12, height = 1, fg = 'white').grid(row = 2*r, column = 3*c+2)
                tk.Label(ColorTable, text=str(NewSkinColors[i]), background='#'+str(NewSkinColors[i]), width = 12, height = 1, fg = 'white').grid(row = 2*r+1, column = 3*c+2)


                #tk.Label(ColorTable, background='#'+str(NewSkinColors[i]), width = 1, height = 1).grid(row = 2*r, column = 2*c)
                #tk.Label(ColorTable, text='('+str(i)+') ', background = '#'+str(NewSkinColors[i]), fg = 'white',  width = 12, height = 1).grid(row = 2*r, column = 2*c+1)
                #print('nel')
                #tk.Label(ColorTable, background='#'+str(SkinColors[i]), width = 1, height = 1).grid(row = 2*r+1, column = 2*c)
                #tk.Label(ColorTable, text=str(NewSkinColors[i]), background = '#'+str(NewSkinColors[i]), fg = 'white',  width = 12, height = 1).grid(row = 2*r+1, column = 2*c+1)
    #tk.Label(ColorTable, text=str(r), width = 9, height = 1).grid(row = 2*r, column = 11)


#n = SkinColors.index(entrada)
#NewSkinColors[n] = salida

ColorTable.pack()

################################################## ColorChange ###############################################################

OriginalColorLabel = tk.Label(ColorChange, text = 'Change: ')
OriginalColorLabel.grid(row = 1, column = 0)

OriginalColor = tk.Entry(ColorChange, width = 5)
OriginalColor.grid(row = 1, column = 1)
#OriginalColor.bind('<Return>', on_change)

Paint = tk.Button(ColorChange, height = 1, text = 'to:', command = GetInput)
Paint.grid(row = 1, column = 2)

NewColor = tk.Entry(ColorChange, width = 15)
NewColor.grid(row = 1, column = 3)
#OriginalColor.bind('<Return>', on_change)


ColorChange.pack()

Save = tk.Button(root, text = 'Save', command = SaveTheme)
Save.pack(side = tk.RIGHT)

#root.send
root.mainloop()     





