from pytube import YouTube

link=input("Enter Youtube Video Link : ")
yt=YouTube(link)
video=yt.streams.all()
x=1
for i in video:
    print(str(x) + ".  " + str(i))
    x+=1

Rsolution=int(input("Enter the number which you want to download"))

finalVid=video[Rsolution-1]
finalVid.download('D:\\')  # you can add your own path
print("Dowloaded Succesfully")