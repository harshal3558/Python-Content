from pytube import YouTube

link = input("Enter the youtube link: ")
yt = YouTube(link)

downloader = yt.streams.get_highest_resolution()
print('Downloading...')

downloader.download(filename="Viddeo_Download.mp4")
print("Finished Downloading")