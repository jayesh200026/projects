import face_recognition
import os
import cv2
KNOWN_FACES_DIR="known"
UNKNOWN_FACES_DIR="unknown"
TOLERANCE=0.6
FRAME_THICKNESS=3
FONT_THICKNESS=2
MODEL="hog"

print("Loading known faces..")

known_faces =[]
known_name=[]

for name in os.listdir(KNOWN_FACES_DIR):
	for filename in os.listdir(f"{KNOWN_FACES_DIR}\{name}"):
		img=face_recognition.load_image_file(f"{KNOWN_FACES_DIR}\{name}\{filename}")
		encoding=face_recognition.face_encodings(img)[0]
		known_faces.append(encoding)
		known_name.append(name)

print("Processing unknown faces")

for filename in os.listdir(UNKNOWN_FACES_DIR):
	print(filename)
	img=face_recognition.load_image_file(f"{UNKNOWN_FACES_DIR}\{filename}")
	locations=face_recognition.face_locations(img,model=MODEL)
	encodings=face_recognition.face_encodings(img,locations)
	img=cv2.cvtColor(img,cv2.COLOR_RGB2BGR)

	for face_encoding,face_location in zip(encodings,locations):
		result=face_recognition.compare_faces(known_faces,face_encoding,TOLERANCE)
		match="Unknown"

		if True in result:
			match=known_name[result.index(True)]
			print(f"MAtch found {match}")
		top_left=(face_location[3],face_location[0])
		bottom_right=(face_location[1],face_location[2])

		color=[0,255,0]

		cv2.rectangle(img,top_left,bottom_right,color,FRAME_THICKNESS)

		top_left=(face_location[3],face_location[2])
		bottom_right=(face_location[1],face_location[2]+20)

		cv2.rectangle(img,top_left,bottom_right,color,cv2.FILLED)
		cv2.putText(img,match,(face_location[3]+10,face_location[2]+15),cv2.FONT_HERSHEY_SIMPLEX,0.5,(200,200,200),FONT_THICKNESS)
	cv2.imshow(filename,img)
	cv2.waitKey(10000)




