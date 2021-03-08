import tkinter.filedialog
import tkinter.colorchooser
import tkinter as tk
import math as math
import colorsys as colorsys

################################################ Global Const ##############################################

DEFAULT_PATH = '..'
DEFAULT_SKIN = './src/default.vitalskin'

COLUMNS = 10

SORT_ITERATIONS = 1

############################################## Global Variables ############################################

global skin 
global col_set
global original_skin_list
global new_skin_list
global color_quant
#global button_created
# global button_list

skin = '{"Background":"ff262a2d","Body":"ff4c4f52","Body Heading Background":"ff3e4245","Body Rounding":4.0,"Body Text":"ffd3d6d6","Border":"8ffffff","Button Font Size":11.0,"Heading Text":"ffdfdfdf","Icon Button Off":"ff848789","Icon Button Off Hover":"ffaaacad","Icon Button Off Pressed":"ff848789","Icon Button On":"ffaa88ff","Icon Button On Hover":"ffbda3ff","Icon Button On Pressed":"ff906de9","Icon Selector Icon":"ff848789","Knob Arc Size":32.0,"Knob Arc Thickness":2.4000000953674316,"Knob Body Size":40.0,"Knob Handle Length":0.5,"Knob Mod Amount Arc Size":40.0,"Knob Mod Amount Arc Thickness":0.5,"Knob Mod Meter Arc Size":39.0,"Knob Mod Meter Arc Thickness":3.0,"Knob Offset":-7.0,"Knob Section Height":71.0,"Label Background":"ff3e4245","Label Background Height":18.0,"Label Connection":"393636","Label Height":11.0,"Label Offset":0.0,"Label Rounding":9.0,"Large Padding":10.0,"Lighten Screen":"22ffffff","Linear Slider":"ff848789","Linear Slider Disabled":"ff848686","Linear Slider Thumb":"ffffffff","Linear Slider Thumb Disabled":"ffffffff","Linear Slider Unselected":"ff262a2e","Modulation Button Dragging":"ffea1616","Modulation Button Selected":"ff4c4f52","Modulation Button Unselected":"ff2c3033","Modulation Button Width":68.0,"Modulation Font Size":11.0,"Modulation Meter":"ff1de9b6","Modulation Meter Control":"ff64ffda","Modulation Meter Left":"ff1de952","Modulation Meter Right":"ff1dc2e9","Overlay Screen":"22000000","Padding":4.0,"Popup Background":"ff1d2125","Popup Border":"ff000000","Popup Selector Background":"ff2c3033","Power Button Off":"ff606265","Power Button On":"ffaa88ff","Preset Text":"ffffffff","Rotary Arc":"ffaa88ff","Rotary Arc Disabled":"ff848789","Rotary Arc Unselected":"ff4c4f52","Rotary Arc Unselected Disabled":"ff4c4f52","Rotary Body":"ff262a2e","Rotary Body Border":"ff4c4f52","Rotary Hand":"ffffffff","Rotary Option Width":20.0,"Rotary Option X Offset":24.0,"Rotary Option Y Offset":4.0,"Shadow":"66000000","Slider Width":24.0,"Text Button Height":20.0,"Text Component Background":"ff2c3033","Text Component Font Size":15.0,"Text Component Height":43.0,"Text Component Label Offset":0.0,"Text Component Offset":-8.0,"Text Component Text":"ffffffff","Text Editor Background":"ff2c3033","Text Editor Border":"ffffff","Text Editor Caret":"ffaaacad","Text Editor Selection":"1faaabab","Title Width":32.0,"UI Action Button":"ffaa88ff","UI Action Button Hover":"ffba9fff","UI Action Button Press":"ff906de9","UI Button":"ff848789","UI Button Hover":"ff939699","UI Button Press":"ff606265","UI Button Text":"ff111111","Wavetable Draw Height":0.10000000149011612,"Wavetable Draw Width":0.7200000286102295,"Wavetable Horizontal Angle":-0.23999999463558197,"Wavetable Vertical Angle":1.2200000286102295,"Wavetable Y Offset":0.05000000074505806,"Widget Accent 1":"19aa88ff","Widget Accent 2":"19aa88ff","Widget Background":"ff1d2125","Widget Center Line":"ffffffff","Widget Fill Boost":1.600000023841858,"Widget Fill Center":0.0,"Widget Fill Fade":0.30000001192092896,"Widget Line Boost":1.0,"Widget Line Width":2.0,"Widget Margin":5.5,"Widget Primary 1":"ffaa88ff","Widget Primary 2":"ffaa88ff","Widget Primary Disabled":"ff4c4f52","Widget Rounded Corner":9.0,"Widget Secondary 1":"669f88ff","Widget Secondary 2":"669f88ff","Widget Secondary Disabled":"22666666","overrides":{"Advanced":{"Text Button Height":30.0,"Widget Line Width":1.2000000476837158,"Widget Primary 2":"64aa88ff"},"All":null,"All Effects":{"Power Button Off":"ff848686"},"Chorus":{"Widget Fill Center":-1.0},"Compressor":{"Power Button On":"ff1de9b6","Rotary Arc":"ff1de9b6","Widget Primary 1":"ff1de9b6","Widget Primary 2":"ffffffff","Widget Secondary 1":"ff10735b","Widget Secondary 2":"ff0b4039","Widget Secondary Disabled":"11ffffff"},"Delay":{"Power Button On":"ffff99e9","Rotary Arc":"ffff99e9","Widget Fill Center":-1.0,"Widget Primary 1":"ffff99e9","Widget Primary 2":"ffff99e9","Widget Secondary 1":"66ff99e9","Widget Secondary 2":"66ff99e9"},"Distortion":{"Power Button On":"ffff5252","Rotary Arc":"ffff5252","Widget Fill Center":-1.0,"Widget Primary 1":"ffff5252","Widget Primary 2":"ffff5252","Widget Primary Disabled":"ff666666","Widget Secondary 1":"66ff5252","Widget Secondary 2":"66ff5252"},"Effects Filter":{"Power Button On":"ffffb74d","Rotary Arc":"ffffb74d","Widget Fill Center":-1.0,"Widget Primary 1":"ffffb74d","Widget Primary 2":"ffff8180","Widget Secondary 1":"64ffb74d","Widget Secondary 2":"64ff8180","Widget Secondary Disabled":"ff4c4c4c"},"Envelope":{"Rotary Arc":"ff64ffda","Widget Accent 1":"bbffffff","Widget Accent 2":"11ffffff","Widget Center Line":"ff64ffda","Widget Fill Center":-1.0,"Widget Primary 1":"ff1de9b6","Widget Primary 2":"ff40c4ff","Widget Secondary 1":"361de9b6","Widget Secondary 2":"3640c4ff"},"Equalizer":{"Icon Button Off":"ff545454","Icon Button Off Hover":"ff6b6b6b","Icon Button On":"fffff6e1","Icon Button On Hover":"ffffffff","Icon Button On Pressed":"ffd1cab7","Power Button On":"fffff6e1","Rotary Arc":"fffff6e1","Text Component Height":30.0,"Text Component Text":"ff6b6b6b","Widget Primary 1":"fffff6e1","Widget Primary 2":"fffff6e1","Widget Primary Disabled":"ff666666","Widget Secondary 1":"33fff6e1","Widget Secondary 2":"33fff6e1","Widget Secondary Disabled":"ff4c4c4c"},"Filter":{"Body Heading Background":"0","Icon Button On":"ffffb74d","Icon Button On Hover":"fffdcf91","Icon Button On Pressed":"ffffb74d","Power Button On":"ffffb74d","Rotary Arc":"ffffb74d","Widget Fill Center":-1.0,"Widget Primary 1":"ffffb74d","Widget Primary 2":"ffff8180","Widget Secondary 1":"64ffb74d","Widget Secondary 2":"64ff8a80"},"Flanger":{"Power Button On":"ffffd740","Rotary Arc":"ffffd740","Widget Fill Center":-1.0,"Widget Primary 1":"ffffd740","Widget Primary 2":"ffffc900","Widget Primary Disabled":"ff666666","Widget Secondary 1":"66ffd740","Widget Secondary 2":"66ffc900","Widget Secondary Disabled":"ff4c4c4c"},"Header":{"Body":"333333","Body Heading Background":"0","Popup Selector Background":"ff14181b","Widget Accent 1":"ffff1744","Widget Accent 2":"ffff5252","Widget Background":"ff161718","Widget Line Width":1.2000000476837158,"Widget Primary 1":"ffaa88ff","Widget Primary 2":"64aa88ff","Widget Secondary 1":"ff1de9b6","Widget Secondary 2":"ff80d8ff"},"Keyboard":{"Widget Accent 1":"ff848789","Widget Accent 2":"32ffffff","Widget Primary 1":"ffaa88ff","Widget Rounded Corner":4.0,"Widget Secondary 1":"ff4c4f52","Widget Secondary 2":"ff262a2e"},"Lfo":{"Icon Button On":"ff64ffda","Icon Button On Hover":"ffb1ffec","Icon Button On Pressed":"ff32d6bf","Rotary Arc":"ff64ffda","Text Component Background":"ff2c3033","Widget Accent 1":"bbffffff","Widget Accent 2":"11ffffff","Widget Center Line":"ff64ffda","Widget Fill Center":-1.0,"Widget Primary 1":"ff1de9b6","Widget Primary 2":"ff40c4ff","Widget Secondary 1":"361de9b6","Widget Secondary 2":"3640c4ff"},"Logo":{"Body Heading Background":"0","Shadow":"ff000000","Widget Primary 1":"ffaa88ff","Widget Primary 2":"ff8464d2","Widget Secondary 1":"ffffffff","Widget Secondary 2":"ffeeeeee"},"Macro":{"Knob Offset":0.0,"Label Background":"0","Label Offset":19.0,"Rotary Option Width":22.0,"Rotary Option X Offset":25.0,"Rotary Option Y Offset":24.0},"Modulation Drag Drop":{"Label Rounding":4.0,"Lighten Screen":"5637beac","Widget Accent 1":"bbffffff","Widget Accent 2":"11ffffff","Widget Center Line":"ffb6e6e6","Widget Primary 1":"ff00e686","Widget Primary 2":"ff0086e6","Widget Secondary 1":"3500e686","Widget Secondary 2":"350086e6"},"Modulation Matrix":{"Button Font Size":14.0,"Icon Button On":"ff1de9b6","Icon Button On Hover":"ff64ffda","Icon Button On Pressed":"ff00bfa5","Widget Accent 1":"bbffffff","Widget Accent 2":"11ffffff","Widget Center Line":"ff64ffda","Widget Primary 1":"ff1de9b6","Widget Primary 2":"ff40c4ff","Widget Secondary 1":"361de9b6","Widget Secondary 2":"3640c4ff"},"Oscillator":{"Button Font Size":14.0,"Overlay Screen":"aa1d2125","Popup Selector Background":"0","Rotary Option Width":24.0,"Rotary Option X Offset":36.0,"Rotary Option Y Offset":1.0,"Text Button Height":30.0,"Text Component Font Size":13.0,"Text Component Height":30.0,"UI Action Button":"ff1de9b6","Wavetable Draw Width":0.7799999713897705},"Overlays":{"Body":"ff3e4245","Overlay Screen":"bb111111","Shadow":"ff000000","Widget Accent 1":"ff1de9b6","Widget Primary 1":"ffaa88ff","Widget Primary 2":"ff8464d2","Widget Secondary 1":"ffffffff","Widget Secondary 2":"ffeeeeee"},"Phaser":{"Power Button On":"ff40cfff","Rotary Arc":"ff40cfff","Widget Fill Center":-1.0,"Widget Primary 1":"ff40c4ff","Widget Primary 2":"ff00b0ff","Widget Primary Disabled":"ff666666","Widget Secondary 1":"6640c4ff","Widget Secondary 2":"6600b0ff","Widget Secondary Disabled":"ff4c4c4c"},"Popup Browser":{"Body":"ff1d2125","Border":"ff848789","Icon Button Off":"ffaaacad","Icon Button Off Hover":"ffd3d6d6","UI Action Button":"ff1de9b6","UI Action Button Hover":"ff64ffda","UI Action Button Press":"ff11cbb2","Widget Primary 1":"ff906de9"},"Preset Browser":{"Button Font Size":14.0,"UI Action Button":"ff1de9b6","UI Action Button Hover":"ff64ffda","UI Action Button Press":"ff11cbb2","Widget Rounded Corner":5.0},"RandomLfo":{"Icon Button On":"ff64ffda","Icon Button On Hover":"ffb1ffec","Icon Button On Pressed":"ff32d6bf","Popup Background":"ff2c2e2f","Rotary Arc":"ff64ffda","Widget Accent 1":"bbffffff","Widget Accent 2":"11ffffff","Widget Center Line":"ff64ffda","Widget Fill Center":-1.0,"Widget Primary 1":"ff1de9b6","Widget Primary 2":"ff40c4ff","Widget Secondary 1":"361de9b6","Widget Secondary 2":"3640c4ff"},"Reverb":{"Power Button On":"ff8fa0ff","Rotary Arc":"ff8fa0ff","Widget Primary 1":"ff9898ff","Widget Primary 2":"ff8fa0ff","Widget Secondary 1":"668fa0ff","Widget Secondary 2":"668fa0ff"},"Sample":{"Button Font Size":14.0,"Knob Section Height":70.0,"Popup Selector Background":"0","Text Button Height":30.0,"Text Component Font Size":13.0,"Text Component Height":30.0,"UI Action Button":"ff1de9b6","Widget Fill Boost":2.5},"Sub":{"Text Component Font Size":12.0,"Text Component Offset":0.0,"Widget Secondary Disabled":"ff4c4c4c"},"Voice":null,"Wavetable Editor":{"Label Rounding":12.0,"Lighten Screen":"19ffffff","Popup Selector Background":"ff14181b","Text Component Offset":0.0,"UI Button":"ff2c3033","UI Button Hover":"ff3e4245","UI Button Press":"ff1d2125","UI Button Text":"ff64ffda","Widget Accent 1":"bbffffff","Widget Accent 2":"11ffffff","Widget Center Line":"ffaa88ff","Widget Primary Disabled":"ff848789","Widget Secondary Disabled":"66848789"}},"synth_version":65541}'
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
            i = c+(COLUMNS*r)
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
    # SkinSource = open(DEFAULT_SKIN, 'r')
    # if SkinSource != None:
    #     # F1_ColorTable.grid_forget()
    #     skin = ''
    #     col_set = set()
    #     original_skin_list = []
    #     new_skin_list = []
    #     color_quant = 0
    #     skin = SkinSource.read()
    #     SkinSource.close()
    #     # print(skin)

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