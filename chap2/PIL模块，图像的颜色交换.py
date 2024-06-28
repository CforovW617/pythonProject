from PIL import Image
#加载图片
im=Image.open('C:\\Users\\lyw\\Desktop\\湘信院资料\\教学进度表.jpg')
#print(type(im),im)
#提取P图像的颜色通道，返回结果是图像的副本
r,g,b=im.split()
# print(r)
# print(g)
# print(b)
#合并通道
om=Image.merge(mode='RGB',bands=(g,b,r))
om.save('教学进度表.jpg')