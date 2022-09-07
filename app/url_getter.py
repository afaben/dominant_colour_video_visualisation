import youtube_dl as yt

class YoutubeVideoDownloader():
    def __init__(self, yt_url, ydl_opts={
       'outtmpl': 'raw_videos/%(title)s.%(ext)s', 
    }):
        self.yt_url = yt_url
        self.ydl_opts = ydl_opts
    
    def get_video_title(self):
        # Get the video title 
        with yt.YoutubeDL(self.ydl_opts) as ydl:
            meta_info = ydl.extract_info(
                self.yt_url, download=False
            )
        video_filename = '%s' %(meta_info['title'])
        print("Video name here", video_filename)
        return video_filename

    def get_youtube_video_download(self, video_title):
        # Download the video
        with yt.YoutubeDL(self.ydl_opts) as ydl:
            print("Attempting to Download:", video_title)

            ydl.download([self.yt_url])
            print("Successfully Downloaded:", video_title)
    
    def get_downloaded_video(self):
        video_title = self.get_video_title()
        downloaded_video = self.get_youtube_video_download(video_title)
        return downloaded_video

if __name__ == '__main__':
    # This will only execute if the program is ran here and not in main.py
    yt_url = 'https://www.youtube.com/watch?v=H9154xIoYTA'
    test_attempt = YoutubeVideoDownloader(yt_url)
    test_attempt.get_video_title()