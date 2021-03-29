from tkinter import *
from tkinter import filedialog
from PIL import Image
import numpy

# 以上代码报错，表示相应的包未安装

def runLoop():
    inPix1 = str(num1Entry.get())
    inPix2 = str(num2Entry.get())
    inRGB = str(num3Entry.get())
    inDL = str(num4Entry.get())
    inLD = str(num5Entry.get())
    xx = str(num6Entry.get())
    yy = str(num7Entry.get())
    openFile = filedialog.askopenfilename(
        filetypes=[('以PNG和JPJ图片为准', '.png'), ('以PNG和JPJ图片为准', '.jpg'), ('别的格式不保证OK', '.*')]
    )
    img = numpy.array(Image.open(openFile))
    imgout = img
    numX, numY, null = img.shape
    print("Loading\n")
    if inPix1 == "":
        inPix1 = "*"
    if inPix2 == "":
        inPix2 = "*"
    if inDL == "":
        inDL = 128
    if inLD == "":
        inLD = 255
    if xx == "":
        xx = 13
    if yy == "":
        yy = 4
    if inRGB == "R" or inRGB == "r":
        RGB = 0
    elif inRGB == "G" or inRGB == "g":
        RGB = 1
    else:
        RGB = 2

    if int(inDL) < int(inLD):
        for i in range(numX):
            for j in range(numY):
                if img[i, j][RGB] >= int(inLD):
                    imgout[int(i / xx), int(j / yy)] = 255
                elif img[i, j][RGB] > int(inDL):
                    imgout[int(i / xx), int(j / yy)] = 128
                else:
                    imgout[int(i / xx), int(j / yy)] = 0
    elif int(inDL) > int(inLD):
        for i in range(numX):
            for j in range(numY):
                if img[i, j][RGB] >= int(inLD):
                    imgout[int(i / xx), int(j / yy)] = 0
                elif img[i, j][RGB] > int(inDL):
                    imgout[int(i / xx), int(j / yy)] = 128
                else:
                    imgout[int(i / xx), int(j / yy)] = 255
    else:
        print("error:wrong(4)and(5)")

    for i in range(int(numX / xx)):
        for j in range(int(numY / yy)):
            if imgout[i, j][0] == 255:
                print(str(inPix1), end="")
            if imgout[i, j][0] == 128:
                print(str(inPix2), end="")
            elif imgout[i, j][0] == 0:
                print(" ", end="")
        print("\n")

winX = 100
winY = 50
windowIn = Tk()
windowIn.title('Synthesis')
windowIn.minsize(winX, winY)
Label(windowIn, text="1)大色块字符(默认*)：").grid(row=0, column=0)
Label(windowIn, text="2)小色块字符(默认*)：").grid(row=2, column=0)
Label(windowIn, text="3)参考色(R/G/B)(默认B)：").grid(row=4, column=0)
Label(windowIn, text="4)阈值(0~255)(默认128)：").grid(row=6, column=0)
Label(windowIn, text="5)白极(0~255)(默认255)：").grid(row=8, column=0)
Label(windowIn, text="6)竖向缩放(默认13):").grid(row=10, column=0)
Label(windowIn, text="7)横向缩放(默认4):").grid(row=12, column=0)
Label(windowIn, text="注：若5)小于4)，则黑白反转").grid(row=15, column=0)
num1Entry = Entry(windowIn, textvariable=StringVar())
num2Entry = Entry(windowIn, textvariable=StringVar())
num3Entry = Entry(windowIn, textvariable=StringVar())
num4Entry = Entry(windowIn, textvariable=StringVar())
num5Entry = Entry(windowIn, textvariable=StringVar())
num6Entry = Entry(windowIn, textvariable=StringVar())
num7Entry = Entry(windowIn, textvariable=StringVar())
num1Entry.grid(row=1, column=0)
num2Entry.grid(row=3, column=0)
num3Entry.grid(row=5, column=0)
num4Entry.grid(row=7, column=0)
num5Entry.grid(row=9, column=0)
num6Entry.grid(row=11, column=0)
num7Entry.grid(row=13, column=0)
mainButton = Button(windowIn, bd=5, font='微软雅黑', padx=10, text=str("选取图片"), command=runLoop)
mainButton.grid(row=14, column=0, padx=winX/2, pady=winY/2)
windowIn.mainloop()






