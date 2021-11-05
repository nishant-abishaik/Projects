import face_recognition
import opencv
import json
import requests
import time

url = 'http://34.100.200.14/api'
currentname = "unknown"
while True:

    success, img = cap.read()
    frame = cv2.resize(img, (0, 0), None, 0.25, 0.25)
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    boxes = face_recognition.face_locations(frame)
    # compute the facial embeddings for each face bounding box
    Listencodings = face_recognition.face_encodings(frame, boxes)

    if len(Listencodings) > 0:
        encodings = face_recognition.face_encodings(frame, boxes)[0]
    #print(type(encodings))
        payload= encodings.tolist()
    # print(payload)
        final = json.dumps({'encodings': [payload]})
    # print(type(final))
        r = requests.post(url, time.sleep(1),json=final)

        print(r.text)

    else:
        time.sleep(2)
        print("No faces found in the Frame!")
        #quit()



    cv2.destroyAllWindows()