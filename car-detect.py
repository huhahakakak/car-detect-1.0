import cv2
from tkSimpleStatusbar import *
import sys


master = Tk() #membuat window
master.title("Car Detect 1.0")
master.resizable(0,0) #menonaktifkan maximize
master.iconbitmap("icon/alert.ico")

#--------------------------------STATUS BAR--------------------------------------#
status = StatusBar(master)
status.pack(side=TOP, fill=X)
status.set("Selamat Datang...")

def openWebcam():
    status.set("Camera Open, Tekan q untuk keluar")
    cascadePath = 'cars.xml'
    video_src = 'dataset/cctvfootage.mp4'

    car_cascade = cv2.CascadeClassifier(cascadePath)
    cam = cv2.VideoCapture(video_src) # 1 untuk kamera eksternal bukan webcam & variable video_src untuk video dari dataset

    while True:
        _, img = cam.read()

        # TODO 1 : Menentukan variable
        if (type(img) == type(None)):
            break

        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        cars = car_cascade.detectMultiScale(gray, 1.1, 1)

        for (x, y, w, h) in cars:
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 2)

        cv2.imshow('CAM 1', img)

        if cv2.waitKey(10) & 0xFF == ord('q'):
            break

        status.set("Tekan q untuk keluar")

def openWebcam2():
    status.set("Camera Open, Tekan q untuk keluar")
    cascadePath = 'cars.xml'
    #video_src = "dataset/video1.avi"

    car_cascade = cv2.CascadeClassifier(cascadePath)
    cam = cv2.VideoCapture(0)  # 1 untuk kamera eksternal bukan webcam & variable video_src untuk video dari dataset

    while True:
        _, img = cam.read()
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        # TODO 1 : Menentukan variable
        if (type(img) == type(None)):
            break

        cars = car_cascade.detectMultiScale(gray, 1.1, 1)

        for (x, y, w, h) in cars:
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 2)

        cv2.imshow('CAM 1', img)

        if cv2.waitKey(10) & 0xFF == ord('q'):
            break

        status.set("Tekan q untuk keluar")

#def exitBtn():
    #sys.exit()


# --------------------------------MEMBUAT TOMBOL---------------------------------------#
img_webcam = PhotoImage(file="img/webcam.png").subsample(15, 15)
#img_exit = PhotoImage(file="img/exit.png").subsample(15, 15)

btn_cam1 = Button(master, image=img_webcam, compound=LEFT, command=openWebcam, text="CAM 1").pack(side=LEFT)
btn_cam2 = Button(master, image=img_webcam, compound=LEFT, command=openWebcam2, text="CAM 2").pack(side=LEFT)
#btn_exit = Button(master, image=img_exit, compound=LEFT, command=exitBtn(), text="Are You Sure ?").pack(side=LEFT)

master.mainloop() # penutup window agar tidak langsung keluar
master.quit() # keluar  dari window