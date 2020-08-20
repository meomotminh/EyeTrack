from PIL import Image
from matplotlib import image
from matplotlib import pyplot
from numpy import asarray

"""image = Image.open('Sydney-Opera-House.jpg')
data = asarray(image)
print(data.shape)
image2 = Image.fromarray(data)

print(image2.format)
print(image2.mode)
print(image2.size)

image2.show()"""

"""image = Image.open('Sydney-Opera-House.jpg')
print(image.format)
print(image.mode)
print(image.size)
image.show()"""

# load and display with Matplotlib

"""data = image.imread('Sydney-Opera-House.jpg')
print(data.dtype)
print(data.shape)
pyplot.imshow(data)
pyplot.show()"""

"""image = Image.open('Sydney-Opera-House.jpg')
image.save('opera-house.png',format='PNG')
image2 = Image.open('opera-house.png')
print(image2.format)"""

"""image = Image.open('Sydney-Opera-House.jpg')
gs_image = image.convert(mode='L')
gs_image.save('opera-house-grayscale.jpg')
image2 = Image.open('opera-house-grayscale.jpg')
image2.show();"""

"""image = Image.open('Sydney-Opera-House.jpg')
print(image.size)
image.thumbnail((100,50))
print(image.size)"""

image = Image.open('Sydney-Opera-House.jpg')
"""print(image.size)
image_resized = image.resize((200,200))
print(image_resized.size)
#image_resized.show();

hoz_flip = image.transpose(Image.FLIP_LEFT_RIGHT)

ver_flip = image.transpose(Image.FLIP_TOP_BOTTOM)
pyplot.subplot(311)
pyplot.imshow(image)
pyplot.subplot(312)
pyplot.imshow(image.rotate(45))
pyplot.subplot(313)
pyplot.imshow(image.rotate(90))
pyplot.show()"""
cropped = image.crop((100,100,200,200))
cropped.show()



