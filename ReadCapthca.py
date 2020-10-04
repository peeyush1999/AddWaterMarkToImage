#this script can read text from image using ocr


from PIL import Image
from pytesseract import image_to_string
img = Image.open('1.png')
print img
print image_to_string(img)
print image_to_string(Image.open('C:\Users\SahuTronics\Desktop\1.png'), lang='eng')
