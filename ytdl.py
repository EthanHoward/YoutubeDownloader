import os

os.system("color 0A")

def download(url):
    commandline = url
    os.system(("youtube-dl.exe " + commandline))

download(input("video url?\n"))
