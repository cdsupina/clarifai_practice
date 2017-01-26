import cv2
import time
import os

#make directories for storing videos and frames if not created already
session_time = time.strftime('%d-%m-%Y')

if not os.path.exists('frames'):
    os.makedirs('frames')

if not os.path.exists('frames/' + session_time):
    os.makedirs('frames/' + session_time)

if not os.path.exists('video_log'):
    os.makedirs('video_log')

cap = cv2.VideoCapture(0)

#initialize the videowriter
fourcc = cv2.VideoWriter_fourcc(*'XVID')

#set the session time equal to te current date and time

out = cv2.VideoWriter('video_log/'+session_time+'.avi',fourcc,20.0,(640,480))

fps = 6
log_time = 5
clip_time = 0
frame_index = 0
current_time = time.time()

while True:
    ret,frame = cap.read()
    out.write(frame)
    cv2.imshow('frame',frame)
    new_time = time.time()

    if(new_time-current_time >= 1/fps):
        new_time_str = str(new_time).replace('.',',')
        cv2.imwrite('frames/' + session_time + '/' + str(frame_index) + '.png', frame)
        current_time = time.time()
        frame_index += 1

    k = cv2.waitKey(1)&0xFF
    if k == ord('q'):
        break

cap.release()
out.release()
cv2.destroyAllWindows()
