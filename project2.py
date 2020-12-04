from tkinter import *
from tkinter import filedialog
from PIL import Image
import numpy
# （tkinter）生成启动窗口和输入框：
winX = 100
winY = 50
windowIn = Tk()
windowIn.title('Project2')
windowIn.minsize(winX, winY)
Label(windowIn, text="1)大字符(默认*)：").grid(row=0, column=0)
Label(windowIn, text="2)小字符(默认*)：").grid(row=2, column=0)
Label(windowIn, text="3)灰度模式(R/G/B)(默认B)：").grid(row=4, column=0)
Label(windowIn, text="4)灰度阈值(0~255)(默认128)：").grid(row=6, column=0)
Label(windowIn, text="5)亮极(0~255)(默认255)：").grid(row=8, column=0)
Label(windowIn, text="6)缩放(竖轴)(默认13):").grid(row=10, column=0)
Label(windowIn, text="7)缩放(横轴)(默认4):").grid(row=12, column=0)
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
# 由下方<mainButton>按钮触发的主体：
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
    # 导入图像：
    img = numpy.array(Image.open(openFile))
    imgout = img
    # numX, numY = img.shape 【ValueError: too many values to unpack (expected 2)】
    numX, numY, null = img.shape
        # <.shape>多维矩阵，对二维图像来说有三个维度：[0]长度尺寸，[1]宽度尺寸，[2]色彩通道数量
    print("Loading")
    # 是否使用默认值检测：
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
    # 通过img[i, j]，获取到像素值, print(img[i, j])结果为[R值，G值，B值，亮度值]
    # 利用for进行逐行扫描：
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
    # 利用for进行逐行打印：
    for i in range(int(numX / xx)):
        for j in range(int(numY / yy)):
            if imgout[i, j][0] == 255:
                print(str(inPix1), end="")
            if imgout[i, j][0] == 128:
                print(str(inPix2), end="")
            elif imgout[i, j][0] == 0:
                print(" ", end="")
        print("\n")
# （tkinter）按钮 用于在窗口中触发主体：
mainButton = Button(windowIn, bd=5, font='微软雅黑', padx=10, text=str("选取图片"), command=runLoop)
    # (<window>使用开头生成的窗口, <bd=5>体积块, <font='微软雅黑' & padx=10 & text=str("选取文件")>字体&大小&文本,
    # <command=runLoop>跳转至上方<def runloop>)
mainButton.grid(row=14, column=0, padx=winX/2, pady=winY/2)
windowIn.mainloop()






