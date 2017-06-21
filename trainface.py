import cv2 #######Kuldeep Paul positive dataset generator########

cap = cv2.VideoCapture(0)

#trained face detection xml classifier

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface.xml')
pic_no = 171

while True:

    print 'Picture Taken '+ str(pic_no)+'.jpg'

    ret, frames = cap.read()
    gray=cv2.cvtColor(frames, cv2.COLOR_BGR2GRAY)

    #detect faces in input image
    faces = face_cascade.detectMultiScale(gray, 1.3, 1)

    for (x,y,w,h) in faces:

        crop_img = frames[y:y+h, x:x+w]
        cropped_img = cv2.resize(crop_img, (50,50))
        cv2.imwrite('pos/pos_'+str(pic_no)+'.jpg', cropped_img)
        print('pos_'+str(pic_no)+'.jpg has been created')

    pic_no+=1

    # Wait for Esc key to stop
    if cv2.waitKey(33)==27:
        break

cv2.DestroyAllWindows()
