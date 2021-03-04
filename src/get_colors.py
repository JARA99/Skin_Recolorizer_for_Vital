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

print()
print(list(colors))
print()
print()
print('Este tema contiene ' + str(len(colors)) + ' colores distintos')

SkinColors = list(colors)

