import  cv2
data = cv2.QRCodeDetector()
value,_,_ = data.detectAndDecode(cv2.imread("/home/nzangi/PycharmProjects/My Projects/Analytica /nzangi.png"))
print("Dedoded data is:",value)