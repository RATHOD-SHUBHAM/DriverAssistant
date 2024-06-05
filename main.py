# Importing all the required libraries
import cv2 as cv
import time
from dash import Dash
from drowsy import Drowsy
import pushover


def play_video(video_path, cam_path):
    dash = Dash(video_path)  # calling class Dash from dash.py
    drowsy_ = Drowsy()
    cap1 = cv.VideoCapture(video_path)
    cap2 = cv.VideoCapture(cam_path)

    pTime = 0
    if not cap1.isOpened():
        print("Error: Unable to open the dash cam.")
        return
    if not cap2.isOpened():
        print("Error: Unable to open the front cam.")
        return

    while True:
        cTime = time.time()
        ret1, frame1 = cap1.read()
        ret2, frame2 = cap2.read()

        if (not ret1) or (not ret2):
            break

        status, frame2 = drowsy_.dd(frame2)

        if status == "SLEEPING !!!":

            frame1, close, mod, far = dash.dash_detect(frame1)  # dash_detect method from Dash class

            if close:
                cv.putText(frame1, "nearest car:close", (3000, 170), cv.FONT_HERSHEY_PLAIN, 5,
                           (255, 0, 255), 5)
                cv.putText(frame1, "brake:100%", (3000, 250), cv.FONT_HERSHEY_PLAIN, 5,
                           (255, 0, 255), 5)

            elif mod:
                cv.putText(frame1, "nearest car:moderate", (3000, 170), cv.FONT_HERSHEY_PLAIN, 5,
                           (255, 0, 255), 5)
                cv.putText(frame1, "brake:70%", (3000, 250), cv.FONT_HERSHEY_PLAIN, 5,
                           (255, 0, 255), 5)

            elif far:
                cv.putText(frame1, "nearest car:far", (3000, 170), cv.FONT_HERSHEY_PLAIN, 5,
                           (255, 0, 255), 5)
                cv.putText(frame1, "brake:50%", (3000, 250), cv.FONT_HERSHEY_PLAIN, 5,
                           (255, 0, 255), 5)

            pushover.make_request_with_retry() # Send notification.

        fps = 1 / (cTime - pTime)
        pTime = cTime
        cv.putText(frame1, str(int(fps)), (10, 170), cv.FONT_HERSHEY_PLAIN, 5,
                   (255, 0, 255), 5)

        resized_frame = cv.resize(frame1, (1920, 1080))
        cv.imshow('dash_road', resized_frame)
        cv.imshow('dash_face', frame2)

        if cv.waitKey(1) & 0xFF == ord('q'):
            break

    cap1.release()
    cap2.release()
    cv.destroyAllWindows()


play_video("vid1.mp4", 0)  # input video and select camera




