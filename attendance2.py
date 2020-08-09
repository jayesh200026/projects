import face_recognition
import os
import cv2
from datetime import datetime

KNOWN_FACES_DIR="known"
TOLERANCE=0.6
FRAME_THICKNESS=3
FONT_THICKNESS=2
MODEL="hog"

print("Loading known faces..")

known_faces =[]
known_name=[]


def markattandance(name):
	#time=now.strftime('%H:%M:%S')
	now = datetime.now()
	hour=now.strftime('%H')
	minute=now.strftime('%M')
	int_hour=int(hour)
	int_minute=int(minute)
	if(int_hour==9 and (int_minute>=0 and int_minute<55)):
		period="first"
	elif(int_hour==9 and int_minute>=55):
		period="second"
	elif(int_hour==10 and (int_minute>=0 and int_minute<50)):
		period="second"
	elif(int_hour==11 and (int_minute>=10 and int_minute<60)):
		period="Third"
	elif(int_hour==12 and int_minute<=5):
		period="Third"
	elif(int_hour==12 and int_minute>6 and int_minute<=59):
		period="fourth"
	elif(int_hour==13 and int_minute>=5):
		period="fifth"
	elif(int_hour==14 and int_minute<=50):
		period="fifth"
	elif(int_hour==14 and int_minute>=51):
		period="sixth"
	elif(int_hour==15 and int_minute<=40):
		period="sixth"
	elif(int_hour==16 and int_minute>=41):
		period="seventh"
	elif(int_hour==16 and int_minute<=30):
		period="seventh"
	elif(int_hour==19):
		period="eight"

		
	parent_dir='Date'
	dir=now.strftime('%d-%m-%Y')
	path=os.path.join(parent_dir,dir)
	if not os.path.exists(path):
		os.mkdir(path)

	else:
		pass


	filename='attendance_'+period+'.csv'
	mode='r+' if os.path.exists(f"{path}\{filename}") else 'w+'
	#print(mode)


	with open(f"{path}\{filename}",mode) as f:
		namelist=[]
		myDatalist=f.readlines()
		for line in myDatalist:
			entry=line.split(',')
			namelist.append(entry[0])

		
		if name!=None:
			if name not in namelist:
				now = datetime.now()
				datestr=now.strftime('%H:%M:%S')
				f.writelines(f'\n{name},{datestr}')




for name in os.listdir(KNOWN_FACES_DIR):
	for filename in os.listdir(f"{KNOWN_FACES_DIR}\{name}"):
		img=face_recognition.load_image_file(f"{KNOWN_FACES_DIR}\{name}\{filename}")
		encoding=face_recognition.face_encodings(img)[0]
		known_faces.append(encoding)
		known_name.append(name)


cap=cv2.VideoCapture(0)

while True:
	_,img=cap.read()
	img=cv2.cvtColor(img,cv2.COLOR_RGB2BGR)
	facescur=face_recognition.face_locations(img,model=MODEL)
	encodecur=face_recognition.face_encodings(img,facescur)

	for encodeface,faceloc in zip(encodecur,facescur):
		match=face_recognition.compare_faces(known_faces,encodeface,TOLERANCE)
		name=None

		if True in match:
			name=known_name[match.index(True)]
		y1,x2,y2,x1=faceloc
		cv2.rectangle(img,(x1,y1),(x2,y2),(0,255,0),FRAME_THICKNESS)
		cv2.rectangle(img,(x1,y2),(x2,y2+20),(0,255,0),cv2.FILLED)
		cv2.putText(img,name,(x1+10,y2+12),cv2.FONT_HERSHEY_SIMPLEX,0.5,(200,200,200),FONT_THICKNESS)
		markattandance(name)
	cv2.imshow("Camera",img)
	#cv2.waitKey(1000)

	if cv2.waitKey(1)== ord('q'):
		break


cap.release()
cv2.destroyAllWindows()
    


