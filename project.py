from tkinter import *
from yt_dlp import YoutubeDL
ء
def HighQuality():
    try:
        link = entry.get()
        ydl_opts={
            "fromat":"best",
            "outtmpl":"downloads%(titles)s.%(est)s"
        }
        with YoutubeDL(ydl_opts)as ydl:
            ydl.download([link])

            print("the vedio has been Download High Quality")
    
    except Exception as e:
        print("Error downloading")



def LowQuality():
    try:
        link = entry.get()
        ydl_opts={
            "fromat":"worst",
            "outtmpl":"downloads%(titles)s.%(est)s"
        }
        with YoutubeDL(ydl_opts)as ydl:
            ydl.download([link])

            print("the vedio has been Download Low Quality")
    
    except Exception as e:
        print("Error downloading")


def Audio():
    try:
        link = entry.get()
        ydl_opts={
            "fromat":"bestaudio",
            "outtmpl":"downloads%(titles)s.%(est)s"
        }
        with YoutubeDL(ydl_opts)as ydl:
            ydl.download([link])

            print("the vedio has been Download Audio Only")
    
    except Exception as e:
        print("Error downloading")





window=Tk()
window.title("Youtube")
window.geometry("600x400")
window.configure(bg="#EEDFCC")

labal=Label(window,text="add your youtube link here",font="bold",bg=window["bg"])
labal.place(x=200,y=30)

entry=Entry(window,width=50)
entry.place(x=150,y=100)

hight=Button(window,text="Hight Quality",command=HighQuality,font="bold",activeforeground="green")
hight.place(x=100,y=200)

low=Button(window,text="Low Quality",command=LowQuality,font="bold",activeforeground="green")
low.place(x=250,y=200)

audio=Button(window,text="Get Audio",command=Audio,font="bold",activeforeground="green")
audio.place(x=400,y=200)

window.mainloop()