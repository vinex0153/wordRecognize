from PIL import Image
import pytesseract

pytesseract.pytesseract.tesseract_cmd = 'C:\Program Files\Tesseract-OCR\\tesseract.exe'  
img = Image.open('bill3.jpg')
text = pytesseract.image_to_string(img,  config= '--psm 6 digits')
print(text)