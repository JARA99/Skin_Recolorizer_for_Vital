import tkinter.filedialog
import tkinter.colorchooser
import tkinter as tk
import math as math
import colorsys as colorsys

################################################ Global Const ##############################################

DEFAULT_PATH = '..'
DEFAULT_SKIN = './src/default.vitalskin'

#MAX_COLORS = 100
COLUMNS = 10
#MAX_ROWS = math.ceil(MAX_COLORS/COLUMNS) 

SORT_ITERATIONS = 1

############################################## Global Variables ############################################

global skin 
global col_set
global original_skin_list
global new_skin_list
global color_quant
#global button_created
# global button_list

skin = ''
col_set = set()
original_skin_list = []
new_skin_list = []
color_quant = 0
#button_created = False
# button_list = []

############################################## Functions ###################################################

def CreateButtons():
    global col_set
    global original_skin_list
    global new_skin_list
    global color_quant
    # global button_created
    # global button_list

    ROWS = int((COLUMNS + color_quant - color_quant%COLUMNS) / COLUMNS)
    # print('cant ',color_quant)
    # print('filas', ROWS)
    for r in range(ROWS):
        for c in range(COLUMNS):
            i = c+(10*r)
            # print(i)
            if i < color_quant:
                tk.Button(F1_ColorTable, width = 4, height = 3, background = new_skin_list[i][1], activebackground = original_skin_list[i][1], text = new_skin_list[i][1][1:], activeforeground = 'white', command = lambda a = i: ChangeColor(a)).grid(row = r, column = c)
    
    F1_ColorTable.pack()
    # print(button_list)
    
def UpdateColorButton(n):
    # global button_list
    global new_skin_list

    # c = n%COLUMNS
    # r = int((n-c)/COLUMNS)

    # button_list[n].destroy()
    # button = tk.Button(F1_ColorTable, width = 3, height = 2, background = new_skin_list[n][1], command = lambda a = n: ChangeColor(a)).grid(row = r, column = c)
    # button_list[n] = button

    # DestroyChildern(F1_ColorTable)

    # buttons_temp_list = []

    # print(F1_ColorTable.winfo_children())

    # for child in F1_ColorTable.winfo_children():
        # print(child)
        # buttons_temp_list.append[child]

    F1_ColorTable.winfo_children()[n].config(background = new_skin_list[n][1])
    # CreateButtons()


def ChangeColor(n):
        global skin 
        global col_set
        global original_skin_list
        global new_skin_list
        global color_quant
        global button_created
        # global button_list

        # print(original_skin_list[n][1])
        color = tkinter.colorchooser.askcolor(color=new_skin_list[n][1])
        if color != (None,None):
            # print(color)
            new_skin_list[n] = color
            UpdateColorButton(n)

def Step(r,g,b, repetitions=1):
    lum = math.sqrt( .241 * r + .691 * g + .068 * b )

    h, s, v = colorsys.rgb_to_hsv(r,g,b)

    h2 = int(h * repetitions)
    lum2 = int(lum * repetitions)
    v2 = int(v * repetitions)
    s2 = int(s * repetitions)

    return (lum, h2, s2, v2)

def ColorSort(lis):
    lis.sort(key = lambda rgb: Step(rgb[0],rgb[1],rgb[2],SORT_ITERATIONS)) 

def RgbToHex(rgb):
    return '%02x%02x%02x' % rgb

def LoadFile():
    global skin 
    global col_set
    global original_skin_list
    global new_skin_list
    global color_quant
    # global button_created

    # SkinSource = open('./src/default.vitalskin','r')
    SkinSource = tkinter.filedialog.askopenfile(mode = 'r', title = 'Load', initialfile = DEFAULT_SKIN)
    if SkinSource != None:
        DestroyChildern(F1_ColorTable)
        skin = ''
        col_set = set()
        original_skin_list = []
        new_skin_list = []
        color_quant = 0
        skin = SkinSource.read()
        SkinSource.close()
        # print(skin)

        i = 0

        while i != -1:
            i += 1
            i = skin.find(':"', i)
            j = skin.find('"', i+2)

            clr = str(skin[i+2:j])
            if len(clr) == 8:
                col_set.add(str(clr[2:8]))
        # print('\n Original ColorSet: ',col_set, '\n')
        
        hex_temp_list = list(col_set)
        color_quant = len(hex_temp_list)
        # print(color_quant)
        rgb_temp_list = []

        for i in range(color_quant):
            rgb_temp_list.append(tuple(int(hex_temp_list[i][j:j+2], 16) for j in (0, 2, 4)))

        # print(rgb_temp_list, '\n')
        ColorSort(rgb_temp_list)
        # print(rgb_temp_list, '\n')

        for i in range(color_quant):
            temp_item = [] 
            temp_item.append(rgb_temp_list[i])
            temp_item.append('#' + RgbToHex(rgb_temp_list[i]))
            original_skin_list.append(temp_item)

        # print(original_skin_list, '\n')
        new_skin_list = original_skin_list.copy()
        
        CreateButtons()
        # print('\n Creating buttons')
    return

def LoadFirst():
    global skin 
    global col_set
    global original_skin_list
    global new_skin_list
    global color_quant
    # global button_created

    # SkinSource = open('./src/default.vitalskin','r')
    SkinSource = open(DEFAULT_SKIN, 'r')
    if SkinSource != None:
        # F1_ColorTable.grid_forget()
        skin = ''
        col_set = set()
        original_skin_list = []
        new_skin_list = []
        color_quant = 0
        skin = SkinSource.read()
        SkinSource.close()
        # print(skin)

        i = 0

        while i != -1:
            i += 1
            i = skin.find(':"', i)
            j = skin.find('"', i+2)

            clr = str(skin[i+2:j])
            if len(clr) == 8:
                col_set.add(str(clr[2:8]))
        # print('\n Original ColorSet: ',col_set, '\n')
        
        hex_temp_list = list(col_set)
        color_quant = len(hex_temp_list)
        # print(color_quant)
        rgb_temp_list = []

        for i in range(color_quant):
            rgb_temp_list.append(tuple(int(hex_temp_list[i][j:j+2], 16) for j in (0, 2, 4)))

        # print(rgb_temp_list, '\n')
        ColorSort(rgb_temp_list)
        # print(rgb_temp_list, '\n')

        for i in range(color_quant):
            temp_item = [] 
            temp_item.append(rgb_temp_list[i])
            temp_item.append('#' + RgbToHex(rgb_temp_list[i]))
            original_skin_list.append(temp_item)

        # print(original_skin_list, '\n')
        new_skin_list = original_skin_list.copy()
        
        CreateButtons()
        # print('\n Creating buttons')
    return

def SaveFile():
    global skin 
    global col_set
    global original_skin_list
    global new_skin_list
    global color_quant
    # global button_created

    # SkinSource = open('./src/default.vitalskin','r')
        
    SkinSink = tkinter.filedialog.asksaveasfile(mode = 'w', title = 'Save as', initialdir = DEFAULT_PATH)
    if SkinSink != None:
        #print(skin)
        new_skin = str(skin)
        for j in range(color_quant): 
            new_skin = new_skin.replace(original_skin_list[j][1][1:]+'"', new_skin_list[j][1][1:]+'"')

        SkinSink.write(new_skin)
    return

def DestroyChildern(frame):
    for child in frame.winfo_children():
        # print(child)
        child.destroy()


################################################# GUI ######################################################

root = tk.Tk()
root.title('Theme recolorizer for Vital')
F1_ColorTable = tk.Frame()
F2_Buttons = tk.Frame()

load_bt = tk.Button(F2_Buttons, text = 'Load', command = LoadFile).pack(side = tk.RIGHT)
save_bt = tk.Button(F2_Buttons, text = 'Save', command = SaveFile).pack(side = tk.RIGHT)


############################################### Logic ######################################################

# LoadFile()
LoadFirst()
F2_Buttons.pack()

root.mainloop()