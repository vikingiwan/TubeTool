##########################################
# TubeTool - Download YouTube with ease! #
# By VikingIwan                          #
##########################################

from __future__ import unicode_literals
from ast import AsyncFunctionDef
from distutils.debug import DEBUG
from xml.etree.ElementTree import VERSION
import yt_dlp
import os
import time


def setup():
    global VERSION
    VERSION = '1.0.0'

    global DEBUG
    DEBUG = True

    global banner
    banner = '''
    ###########################################
    #  _______    _       _______          _  #
    # |__   __|  | |     |__   __|        | | #
    #    | |_   _| |__   ___| | ___   ___ | | #
    #    | | | | | '_ \ / _ \ |/ _ \ / _ \| | #
    #    | | |_| | |_) |  __/ | (_) | (_) | | #
    #    |_|\__,_|_.__/ \___|_|\___/ \___/|_| #
    #                                         #
    ###########################################
    
                By: VikingIwan

    '''


def cls():
    os.system('cls' if os.name == 'nt' else 'clear')


def debug(msg):
    if DEBUG == True:
        print("DEBUG: " + msg)


class TLogger(object):
    def debug(self, msg):
        pass

    def warning(self, msg):
        pass

    def error(self, msg):
        print(msg)


def Thook(d):
    if d['status'] == 'finished':
        print('Starting conversion ...')


def dlAudio(link):
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'outtmpl': 'Downloads/Audio/%(title)s.%(ext)s',
        'logger': TLogger(),
        'progress_hooks': [Thook],
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([link])


def dlVideo(link):
    ydl_opts = {
        'format': 'bestvideo*+bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegVideoConvertor',
            'preferedformat': 'mp4'
        }],
        'outtmpl': 'Downloads/Video/%(title)s.%(ext)s',
        'logger': TLogger(),
        'progress_hooks': [Thook],
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([link])


def main():
    cls()
    print(banner)

    link = input("Enter the Youtube link you would like to download: ")
    print("To download as Video, enter 1. To download as Audio, enter 2.")
    _c = input("Choice: ")
    mode = ""

    if _c == "1":
        mode = "video"
    elif _c == "2":
        mode = "audio"
    else:
        mode = "error"

    if mode == "error" or "":
        print("ERROR: UNKNOWN INPUT. PLEASE MAKE SURE YOU ENTER 1 OR 2.")
        print("Restarting application...")
        time.sleep(5)
        main()
    else:
        debug("Chosen mode: " + mode)
        print("")
        if mode == "video":
            print("Downloading as video (mp4). This may take some time.")
            dlVideo(link)
            print("Download complete.")
            if input("Would you like to download another? (y/n)") == "y":
                main()
            if os.name == 'nt':
                Folder = os.getcwd() + "\\Downloads\\Video"
                os.path.realpath(Folder)
                os.startfile(Folder)
        elif mode == "audio":
            print("Downloading as Audio (mp3). This may take some time.")
            dlAudio(link)
            print("Download complete.")
            if input("Would you like to download another? (y/n)") == "y":
                main()
            if os.name == 'nt':
                Folder = os.getcwd() + "\\Downloads\\Audio"
                os.path.realpath(Folder)
                os.startfile(Folder)


setup()
main()
