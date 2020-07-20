import cv2
import face_recognition
from PIL import Image,ImageDraw


'''image_of_gautham=face_recognition.load_image_file('gautham.jpg')
gautham_encoding=face_recognition.face_encodings(image_of_gautham)[0]

image_of_jayesh=face_recognition.load_image_file('Jayesh.jpg')
jayesh_encoding=face_recognition.face_encodings(image_of_jayesh)[0]'''

'''image_of_kaushik=face_recognition.load_image_file('Kaushi.jpg')
kaushik_encoding=face_recognition.face_encodings(image_of_kaushik)[0]'''

'''image_of_darshan=face_recognition.load_image_file('Darshan2.jpg')
darshan_encoding=face_recognition.face_encodings(image_of_darshan)[0]'''

'''image_of_sailesh=face_recognition.load_image_file('Sailesh.jpg')
sailesh_encoding=face_recognition.face_encodings(image_of_sailesh)'''

image_of_pitt=face_recognition.load_image_file('Brad-pitt.jpg')
brad_encoding=face_recognition.face_encodings(image_of_pitt)[0]

known_face_encoding=[
	
	
	
	brad_encoding
	


]

known_face_name=[
 	
 	
 	
 	"Brad-pitt"
 	
 	]

test_img=face_recognition.load_image_file('Cris Pitt.jpeg')

face_locations=face_recognition.face_locations(test_img)
face_encodings=face_recognition.face_encodings(test_img,face_locations)

pil_img=Image.fromarray(test_img)


draw=ImageDraw.Draw(pil_img)

for(top,right,bottom,left),encoding in zip(face_locations,face_encodings):
 	matches=face_recognition.compare_faces(known_face_encoding,encoding)

 	name="Unknown"

 	if True in matches:
 		first_match_index=matches.index(True)
 		name=known_face_name[first_match_index]

 	draw.rectangle(((left,top),(right,bottom)),outline=(0,0,0))


 	text_width,text_height=draw.textsize(name)
 	draw.rectangle(((left,top+300),(right,bottom)),fill=(0,0,0),outline=(0,0,0))
 	draw.text((left+6,bottom+10),name,fill=(255,255,255,255))

del draw

pil_img.show()


