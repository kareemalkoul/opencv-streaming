import cv2

#get this ip from ipweb cam
address = "http://192.168.1.102:8080"

address = f"{address}/video"
cap = cv2.VideoCapture(address)

while True:
    ret, frame = cap.read()
    frame = cv2.resize(frame, (600, 400))
    if not ret:
        break
    cv2.imshow("frame", frame)
    key = cv2.waitKey(1)
    if key == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
