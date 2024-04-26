from picamera import PiCamera
from time import sleep

camera =PiCamera()
camera.rotation=0
camera.start_preview(alpha=200)
for i in range(5):
    camera.annotate_text="hello world"
    sleep(5)
    camera.capture('/home/gcq/Desktop/New/image%s.jpg'%i)
    camera.capture('/home/gcq/Desktop/New/image%s.jpg')
    camera.stop_preview()
    
    
    
camera.start_preview()
camera.start_recording('/home/gcq/Desktop/New/video.h264')
sleep(25)
camera.stop_recording()
camera.stop_preview()
