from yt_dlp import YoutubeDL

video_url = 'https://www.youtube.com/watch?v=fKB_bdxIbdI'

ydl_opts = {
    'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]',  # Choose the best video and audio format
    'merge_output_format': 'mp4',
    'outtmpl': '%(title)s.%(ext)s',
    'postprocessors': [{
        'key': 'FFmpegVideoConvertor',
        'preferedformat': 'mp4',
    }]
}

# Download the video
with YoutubeDL(ydl_opts) as ydl:
    ydl.download([video_url])

print("Download finish!")
