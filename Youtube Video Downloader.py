from tkinter import *
from tkinter import ttk
from tkinter import messagebox , filedialog
from pytube import YouTube
root = Tk()
root.geometry('545x800')
root.resizable(0,0)
root.configure(bg='black')
root.title("Easy youtube video downloader")


Label(root,text = 'Welcome to Youtube Video Downloader', font ='forte 20 bold',bg='#FF0000',fg='white').pack()




##enter link
video_Link = StringVar()
download_Path = StringVar()

Label(root, text = 'Paste Link of Video', font = 'forte 15 bold',fg='white', bg='red').place(x= 160 , y = 60)
link_enter = Entry(root, width = 70 ,textvariable = video_Link).place(x = 32, y = 90)


Label(root, text = 'Destination' , font = 'forte 15 bold', fg='white',bg='red').place(x=170 , y=140)
link_enter1 = Entry(root, width = 70,textvariable =download_Path).place(x = 35, y= 170)



#function to download video


def Browse():

    download_Directory = filedialog.askdirectory(initialdir = "your directory path")
    download_Path.set(download_Directory)

Button(root,text='Browse', font= 'forte 15 bold' ,bg ='#FF0000' ,fg ='white' ,padx =4, command = Browse).place(x=170,y=200)

Label(root, text = 'select quality' , font = 'forte 15 bold', fg='white',bg='red').place(x=170 , y=260)
choice=["720p","144p","only Audio"]
choice1=ttk.Combobox(root, values=choice)
choice1.place(x=170 , y=300)

def Downloader():
    c = choice1.get()
    Youtube_link = video_Link.get()
    download_Folder = download_Path.get()
    getVideo = YouTube(Youtube_link)

    if (c==choice[0]):
                    strm=getVideo.streams.get_highest_resolution()
    elif(c == choice[1]):
                    strm = getVideo.streams.get_lowest_resolution()
    elif(c == choice[2]):
                    strm = getVideo.streams.get_audio_only()
    strm.download(download_Folder)
    messagebox.showinfo('SUCCESSFULLY DONE' , 'DOWNLOADED AND SAVED IN\n'+download_Folder)



Button(root,text = 'DOWNLOAD', font = 'forte 15 bold' ,bg = '#FF0000', fg='white' , padx = 2, command = Downloader).place(x=170 ,y = 350)


root.mainloop()
