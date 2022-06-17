##########################################
# TubeTool - Download YouTube with ease! #
# By VikingIwan                          #
##########################################

from __future__ import unicode_literals
import youtube_dl


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
    link = input("Enter the link: ")
    dlAudio(link)


main()
