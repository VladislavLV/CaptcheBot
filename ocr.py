#!python3

def detectText(path):
    import pytesseract
    from PIL import Image
    pytesseract.pytesseract.tesseract_cmd = './utils/Tesseract-OCR/tesseract.exe'
    im = Image.open(path)
    im = im.convert('L')
    im = im.point(lambda x: 0 if x < 170 else 255)
    txt = pytesseract.image_to_string(im, lang="rus1+eng1")
    return txt