import easygui as ui
from PIL import Image
import os

def main():
    image_path = ui.fileopenbox(title="打开GIF文件")
    image = Image.open(image_path)

    try:
        image.save(path+'/picFrame{:02d}.png'.format(image.tell()))
        while True:
            image.seek(image.tell()+1)
            image.save(path+'/picFrame{:02d}.png'.format(image.tell()))
    except:
        ui.msgbox("位于'"+image_path+"'的文件已分割帧完毕")


ynpath = ui.boolbox("您是否选择输出目录(不选择NO则在当前目录创建一个output文件夹以用来保存文件)")

if ynpath:
    path = ui.diropenbox('请选择输出路径')
    print(path)
    try:
        os.mkdir("output")
        main()
    except FileExistsError:
        main()
else:
    try:
        os.mkdir("output")
        main()
    except FileExistsError:
        main()