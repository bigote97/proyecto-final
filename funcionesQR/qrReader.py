import cv2

def scanQRCode():
  capture = cv2.VideoCapture(0, cv2.CAP_DSHOW)
  if not capture.isOpened():
    data = 'ErrorCode:01-No hay camara'
    
  while(capture.isOpened()):
    ret, frame = capture.read()

    if (cv2.waitKey(1) == ord('s')):
      cv2.destroyAllWindows()
      break

    qr_detector = cv2.QRCodeDetector()
    data, bbox, rectifiedImage = qr_detector.detectAndDecode(frame)

    if len(data) > 0:
      cv2.imshow('webCam', rectifiedImage)
      break
    else:
      cv2.imshow('webCam', frame)

  capture.release()
  cv2.destroyAllWindows()
  return data
