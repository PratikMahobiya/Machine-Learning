import cv2
import pytesseract

cam = cv2.VideoCapture(0)

cv2.namedWindow("test")

img_counter = 0

while True:
    ret, frame = cam.read()
    if not ret:
        print("failed to capture an image")
        break
    cv2.imshow("test", frame)

    k = cv2.waitKey(1)
    if k%256 == 27:
        # ESC pressed
        print("Escape hit, closing...")
        break
    elif k%256 == 32:
        # img_name = "opencv_frame_{}.png".format(img_counter)
        # cv2.imwrite(img_name, frame)
        # print("{} written!".format(img_name))
        # img_counter += 1

        # SPACE pressed
        ret, frame = cam.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Get The Thresold COnversion------------------------------------------------------
        thresh = cv2.threshold(gray, 128, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]

        # Image To Text Conversion---------------------------------------------------------
        text = pytesseract.image_to_string(thresh)
        print ('Text_Found: ',text + "\n" +"Length of the text:- ",len(text))
        
cam.release()
cv2.destroyAllWindows()