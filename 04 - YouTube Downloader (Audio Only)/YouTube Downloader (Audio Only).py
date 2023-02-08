print("-" * 100 , "\n")
# --------------------------------------------------------------------
print("\n"*10)

from pytube import YouTube

l = input("Enter Video Link: ")
yt = YouTube(l)

print("\nTitle:", yt.title)
print("Views:", yt.views)
print("\nDownloading...\n")

d = yt.streams.get_audio_only()
d.download("C:\Downloads")

print("Download Successful")




























print("\n"*10)
# --------------------------------------------------------------------
print("-" * 100 , "\n")