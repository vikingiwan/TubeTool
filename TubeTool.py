##########################################
# TubeTool - Download YouTube with ease! #
# By VikingIwan                          #
##########################################

from __future__ import unicode_literals
from ast import AsyncFunctionDef
from xml.etree.ElementTree import VERSION
import youtube_dl


def setup():
    global VERSION
    VERSION = '1.0.0'
    global author
    author = "VikingIwan"
    global banner
    banner = '''
    ##########################################
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


class TLogger(object):
    def debug(self, msg):
        pass

    def warning(self, msg):
        pass

    def error(self, msg):
        print(msg)


def Thook(d):
    if d['status'] == 'finished':
        print('Download complete. Starting conversion ...')


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
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([link])


def main():
    print(banner)

    link = input("Enter the link: ")
    dlAudio(link)


main()
