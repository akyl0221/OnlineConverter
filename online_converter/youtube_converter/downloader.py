import youtube_dl


def convert(video_url):
    ydl_opts = {
        'format': 'best',
        'outtmpl': 'media/%(title)s.%(ext)s',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        result = ydl.extract_info(video_url, download=False)
    url = result['url']
    return url
