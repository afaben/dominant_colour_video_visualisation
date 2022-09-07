import pytest
import os

from app.url_getter import YoutubeVideoDownloader

class TestYoutubeVideoDownloader:

    test_url = 'https://www.youtube.com/watch?v=icPHcK_cCF4'
    # Test that 
    @pytest.mark.parametrize(
        # Input, # Output
        'test_url, expected_output',
        [
            (test_url, 'Countdown 5 seconds timer')
        ],
    )

    def test_get_video_title(self, test_url, expected_output):
        get_yt_video_title = YoutubeVideoDownloader(test_url)

        output = get_yt_video_title.get_video_title()

        assert type(output) == type(expected_output)
        assert output == expected_output

    @pytest.mark.parametrize(
        'file_location',
        [
            r'raw_videos/'
        ]
    )

    def test_get_youtube_video_download(self,):
        check_video_exists_in_folder = YoutubeVideoDownloader():

        check_video_exists_in_folder.get_downloaded_video(video_title)

        path = os.path.join(fname)
        assert os.path.exists