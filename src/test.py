# -*- coding: utf-8 -*- 
import cv2  
import numpy  
from PIL import Image, ImageDraw, ImageFont  
  
if __name__ == '__main__':  
  
    img_OpenCV = cv2.imread('test2.jpg')  
    # 图像从OpenCV格式转换成PIL格式  
    img_PIL = Image.fromarray(cv2.cvtColor(img_OpenCV, cv2.COLOR_BGR2RGB))  
  
    # 字体  字体*.ttc的存放路径一般是： /usr/share/fonts/opentype/n

    font = ImageFont.truetype('/root/Downloads/simsun.ttc', 20)  
    # 字体颜色  
    fillColor = (255,0,0)  
    rectFile=open("test2.rects", "r+")
    for line in rectFile:
        line=line.strip()
        line=line.split(",")
        x=int(line[0])
        y=int(line[1])
        # 文字输出位置  
        position = (x,y-20)  
        # 输出内容  
        str=line[4]
        # 需要先把输出的中文字符转换成Unicode编码形式  
        if not isinstance(str, unicode):  
           str = str.decode('utf8')  
    	   draw = ImageDraw.Draw(img_PIL)  
    	   draw.text(position, str, font=font, fill=fillColor)  
	    # 使用PIL中的save方法保存图片到本地  
	    # img_PIL.save('02.jpg', 'jpeg')  
  
    	   # 转换回OpenCV格式  
           img_OpenCV = cv2.cvtColor(numpy.asarray(img_PIL),cv2.COLOR_RGB2BGR)  
    cv2.imshow("print chinese to image",img_OpenCV)  
    cv2.waitKey()  
    cv2.imwrite('02.jpg',img_OpenCV)  

