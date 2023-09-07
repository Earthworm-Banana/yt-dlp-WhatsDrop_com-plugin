import rich
from yt_dlp.extractor.common import InfoExtractor
from yt_dlp.compat import compat_str
from bs4 import BeautifulSoup
import os
from datetime import datetime
from rich import print


class WhatsDropVideoIE(InfoExtractor):
    _VALID_URL = r'https?://(?:www\.)?whatsdrop\.com/(?P<id>[^/]+)'

    def _get_file_extension(self, url):
        # get the file extension from the url
        file_extension = os.path.splitext(url)[1]
        # remove the dot from the file extension
        file_extension = file_extension.replace('.', '')
        return file_extension

    def _real_extract(self, url):
        video_id = self._match_id(url)
        webpage = self._download_webpage(url, video_id)
        soup = BeautifulSoup(webpage, 'html.parser')

        # Extract title
        title_h1 = soup.find('h1', {'id': 'title'})
        title = title_h1.get_text() if title_h1 else None
        if not title:
            title_meta = soup.find('meta', {'itemprop': 'name'})
            title = title_meta['content'] if title_meta else None

        # Extract video dimensions and duration
        video_width = int(soup.find('meta', {'property': 'og:video:width'})['content']) if soup.find('meta', {
            'property': 'og:video:width'}) and soup.find('meta', {'property': 'og:video:width'})[
                                                                                               'content'].strip() else None
        video_height = int(soup.find('meta', {'property': 'og:video:height'})['content']) if soup.find('meta', {
            'property': 'og:video:height'}) and soup.find('meta', {'property': 'og:video:height'})[
                                                                                                 'content'].strip() else None
        video_duration = int(soup.find('meta', {'property': 'video:duration'})['content']) if soup.find('meta', {
            'property': 'video:duration'}) and soup.find('meta', {'property': 'video:duration'})[
                                                                                                  'content'].strip() else None

        # Extract description
        description_div = soup.find('div', {'id': 'description'})
        description = description_div.get_text() if description_div else None

        # Extract username
        username_div = soup.find('div', {'class': 'author'}).find('div', {'class': 'name'})
        username_tag = username_div.find('a') if username_div else None
        username = username_tag.text if username_tag else None

        # Extract thumbnail
        thumbnail = soup.find('link', {'itemprop': 'thumbnail'})['href'] if soup.find('link', {
            'itemprop': 'thumbnail'}) else None

        # Extract video formats
        formats = []

        # Extract lower quality video
        lower_quality_video = soup.find('link', {'itemprop': 'contentUrl'})['href'] if soup.find('link', {
            'itemprop': 'contentUrl'}) else None
        lower_quality_ext = self._get_file_extension(lower_quality_video)
        if lower_quality_video:
            formats.append({
                'url': lower_quality_video,
                'ext': lower_quality_ext,
                'quality': 1,
            })

        # Extract better quality video
        # BROKEN, Gives BROKEN DOWNLOAD LINK, Downloads 15kb file, which is a html file
        # better_quality_div = soup.find('div', {'class': 'rate'})
        # better_quality_video = better_quality_div.find('a', {'class': 'download'})['href'] if better_quality_div and better_quality_div.find('a', {'class': 'download'}) else None
        # better_quality_ext = self._get_file_extension(better_quality_video)
        # if better_quality_video:
        #    formats.append({
        #        'url': better_quality_video,
        #        'ext': better_quality_ext,
        #        'quality': 2,
        #    })

        # Extract views
        view_count = int(soup.find('div', {'id': 'vi'}).text) if soup.find('div', {'id': 'vi'}) and soup.find('div', {
            'id': 'vi'}).text.strip() else None

        # Extract likes
        like_count = int(soup.find('div', {'id': 'like'}).text) if soup.find('div', {'id': 'like'}) and soup.find('div',
                                                                                                                  {
                                                                                                                      'id': 'like'}).text.strip() else None

        # Extract dislikes
        dislike_count = int(soup.find('div', {'id': 'dislike'}).text) if soup.find('div',
                                                                                   {'id': 'dislike'}) and soup.find(
            'div', {'id': 'dislike'}).text.strip() else None

        # Extract upload date and format it
        upload_date_str = soup.find('meta', {'itemprop': 'uploadDate'})['content'] if soup.find('meta', {
            'itemprop': 'uploadDate'}) else None
        if upload_date_str:
            upload_date_dt = datetime.fromisoformat(upload_date_str.replace("Z", "+00:00"))
            upload_date = upload_date_dt.strftime('%Y%m%d')

        return {
            'id': compat_str(video_id),
            'title': title,
            'description': description,
            'uploader': username,
            'thumbnail': thumbnail,
            'width': video_width,
            'height': video_height,
            'duration': video_duration,
            'formats': formats,
            'upload_date': upload_date,
            'view_count': view_count,
            'like_count': like_count,
            'dislike_count': dislike_count,
        }


class WhatsDropChannelIE(InfoExtractor):
    _VALID_URL = r'https?://(?:www\.)?whatsdrop\.com/@(?P<id>[^/?&]+)'

    def _entries(self, channel_name):
        page_num = 1
        count_videos = 0
        while True:  # Loop to run indefinitely through every page
            url = f'https://whatsdrop.com/@{channel_name}?page={page_num}'
            print(f'[green]Checking page {page_num}[/green]: {url}')
            webpage = self._download_webpage(url, channel_name, note=f'Downloading page {page_num}')
            soup = BeautifulSoup(webpage, 'html.parser')

            # Find video URLs on the channel page based on your provided HTML sample
            video_containers = soup.find_all('a', {'class': 'boxpost tube'})

            # If no video containers are found, break the loop
            if not video_containers:
                print(f'[red]No videos found on page {page_num}[/red]')
                break

            for container in video_containers:
                count_videos += 1
                video_id = container['id']
                video_url = 'https://whatsdrop.com/' + video_id
                yield self.url_result(video_url, ie=WhatsDropVideoIE.ie_key())

            page_num += 1  # Increment the page number

        # Print amount of videos found
        print(f'[green]Found {count_videos} videos[/green]')

    def _real_extract(self, url):
        channel_id = self._match_id(url)
        entries = self._entries(channel_id)
        return self.playlist_result(entries, channel_id)
