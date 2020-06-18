import cv2
import pytesseract
import numpy as np
import regex as re


def ocr_core(filename):
    # Load The Image-------------------------------------------------------------------
    img = cv2.imread(filename)
    # kernel = np.ones((5,5),np.uint8)

    #Convert it into Gray--------------------------------------------------------------
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Get The Thresold COnversion------------------------------------------------------
    thresh = cv2.threshold(gray, 128, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]

    # Median Blur----------------------------------------------------------------------
    # median = cv2.medianBlur(gray,3)

    # Image To Text Conversion---------------------------------------------------------
    text = pytesseract.image_to_string(thresh)

    # pattern = "[\d]+((-|\s)?[\d]+)+"
    # if re.search(pattern, text):
    #     atm_num = re.search(pattern, text)
    #     cv2.imshow("GrayScale", cv2.resize(gray,None,fx=0.8,fy=0.8))
    #     cv2.imshow("Threshold", cv2.resize(thresh,None,fx=0.8,fy=0.8))
    #     return atm_num.group()
    # else:


    cv2.imshow("GrayScale", cv2.resize(gray,None,fx=0.8,fy=0.8))
    cv2.imshow("Threshold", cv2.resize(thresh,None,fx=0.8,fy=0.8))    
    return text

if __name__ == "__main__":
    print(ocr_core('images/txt_1.jpeg'))
    cv2.waitKey(0)
    cv2.destroyAllWindows()
