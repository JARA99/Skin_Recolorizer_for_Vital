import tkinter.filedialog
import tkinter as tk
import math as math
import colorsys as colorsys

################################################ Global Const ##############################################

DEFAULT_PATH = '.'
DEFAULT_SKIN = './src/default.vitalskin'

#MAX_COLORS = 100
COLUMNS = 10
#MAX_ROWS = math.ceil(MAX_COLORS/COLUMNS) 

SORT_ITERATIONS = 8

############################################## Global Variables ############################################

skin = ''
col_set = set()
original_skin_list = []

############################################## Functions ###################################################

# def CreateColorButton(n):
    
# def UpdateColorButton(n):


# def ChangeColor(n):

def Step(r,g,b, repetitions=1):
    lum = math.sqrt( .241 * r + .691 * g + .068 * b )

    h, s, v = colorsys.rgb_to_hsv(r,g,b)

    h2 = int(h * repetitions)
    lum2 = int(lum * repetitions)
    v2 = int(v * repetitions)

    return (h2, lum, v2)

def ColorSort(lis):
    lis.sort(key = lambda rgb: Step(rgb[0],rgb[1],rgb[2],SORT_ITERATIONS)) 

def LoadFile():
    SkinSource = tkinter.filedialog.askopenfile(mode = 'r', title = 'Load', initialfile = DEFAULT_SKIN)
    if SkinSource != None:
        col_set = set()
        skin = SkinSource.read()
        # print(skin)

        i = 0

        while i != -1:
            i += 1
            i = skin.find(':"', i)
            j = skin.find('"', i+2)

            clr = str(skin[i+2:j])
            if len(clr) == 8:
                col_set.add(str(clr[2:8]))
        print('\n Original ColorSet: ',col_set, '\n')
        
        hex_temp_list = list(col_set)

        # for i in range(len(temp_list)):
        #     temp_item = [] 
        #     temp_item.append(tuple(int(temp_list[i][j:j+2], 16) for j in (0, 2, 4)))
        #     temp_item.append('#' + temp_list[i])
        #     original_skin_list.append(temp_item)

        # print(original_skin_list, '\n')
        # ColorSort(original_skin_list)
        # print(original_skin_list, '\n')

        rgb_temp_list = []

        for i in range(len(hex_temp_list)):
            rgb_temp_list.append(tuple(int(hex_temp_list[i][j:j+2], 16) for j in (0, 2, 4)))
        
        print(rgb_temp_list, '\n')
        ColorSort(rgb_temp_list)
        print(rgb_temp_list, '\n')

        
        

    return


# def SaveFile():




################################################# GUI ######################################################




############################################### Logic ######################################################

LoadFile()

