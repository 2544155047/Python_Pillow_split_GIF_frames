import easygui as ui ###导入UI库
from PIL import Image ###图片处理库
import os ###导入系统库

def main(): ###主函数
    image_path = ui.fileopenbox(title="打开GIF文件") ###GIF文件路径
    image = Image.open(image_path) ###打开图片

    ###切割GIF图片的每一帧
    try:
        image.save(path+'/picFrame{:02d}.png'.format(image.tell())) ###保存图片
        while True:
            image.seek(image.tell()+1)
            image.save(path+'/picFrame{:02d}.png'.format(image.tell()))
    except:
        ui.msgbox("位于'"+image_path+"'的文件已分割帧完毕") ###信息框提示已经分割完毕


ynpath = ui.boolbox("您是否选择输出目录(不选择NO则在当前目录创建一个output文件夹以用来保存文件)")

if ynpath: ###如果是True则运行选择输出路径
    path = ui.diropenbox('请选择输出路径')
    print(path) ###输出文件路径
    try:
        os.mkdir("output") ###新建文件夹，如果已经存在则直接运行main
        main()
    except FileExistsError:
        main()
else: ###如果是False则新建output文件夹在当前目录上
    try:
        os.mkdir("output")
        main()
    except FileExistsError:
        main()