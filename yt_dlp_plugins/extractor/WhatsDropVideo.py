# import rich
from selenium.common.exceptions import TimeoutException
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from yt_dlp.extractor.common import InfoExtractor
from bs4 import BeautifulSoup
import os
from datetime import datetime


# from rich import print


class WhatsDropVideoIE(InfoExtractor):
    # _VALID_URL = r'https?://(?:www\.)?whatsdrop\.com/(?P<id>[^/]+)'
    # id changes to unknownID_videoID from videoID
    _VALID_URL = r'https?://(?:www\.)?whatsdrop\.com/(?P<some_unknown_id>[^/]+)_(?P<id>[^/]+)'

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

        # Extract image only post
        image_div = soup.find('div', {'class': 'getfile__image'})
        image_tag = image_div.find('img') if image_div else None
        image_url = image_tag['src'] if image_tag else None
        if image_url:
            formats.append({
                'url': image_url,
                'ext': 'jpg',
                'quality': 1,
            })

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

        if image_url:
            return {
                'id': video_id,
                'title': title,
                'description': description,
                'uploader': username,
                'width': video_width,
                'height': video_height,
                'duration': video_duration,
                'formats': formats,
                'upload_date': upload_date,
                'view_count': view_count,
                'like_count': like_count,
                'dislike_count': dislike_count,
            }
        else:
            return {
                'id': video_id,
                'title': title,
                'thumbnail': thumbnail,
                'description': description,
                'uploader': username,
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
    # Make a better one to ensure not conflict with other IE (etc LikedIE)
    # _VALID_URL = r'https?://(?:www\.)?whatsdrop\.com/@(?P<id>[^/?&]+)'
    _VALID_URL = r'https?://(?:www\.)?whatsdrop\.com/@(?P<id>[^/?&]+)(?:/(?![^/]*liked))?$'

    def _entries(self, channel_name):
        page_num = 1
        count_videos = 0
        while True:  # Loop to run indefinitely through every page
            url = f'https://whatsdrop.com/@{channel_name}?page={page_num}'
            # print(f'[green]Checking page {page_num}[/green]: {url}')
            webpage = self._download_webpage(url, channel_name, note=f'Downloading page {page_num}')
            soup = BeautifulSoup(webpage, 'html.parser')

            # Find video URLs on the channel page based on your provided HTML sample
            video_containers = soup.find_all('a', {'class': 'boxpost tube'})
            image_containers = soup.find_all('a', {'class': 'boxpost image'})

            media_containers = video_containers + image_containers

            # media_containers = soup.find_all('a', {'class': 'boxpost tube'}) and soup.find_all('a', {'class': 'boxpost image'})

            # If no media containers are found, break the loop
            if not media_containers:
                # print(f'[red]No media found on page {page_num}[/red]')
                break

            for container in media_containers:
                count_videos += 1
                video_id = container['href']
                video_url = 'https://whatsdrop.com' + video_id
                yield self.url_result(video_url, ie=WhatsDropVideoIE.ie_key())

            page_num += 1  # Increment the page number

        # Print amount of videos found
        # print(f'[green]Found {count_videos} videos[/green]')

    def _real_extract(self, url):
        channel_id = self._match_id(url)
        entries = self._entries(channel_id)
        return self.playlist_result(entries, channel_id)


class WhatsDropSearchIE(InfoExtractor):
    _VALID_URL = r'https?://(?:www\.)?whatsdrop\.com/search\?search=(?P<query>[^&]+)&set=(?P<set>[^&]+)'

    def _get_file_extension(self, url):
        file_extension = os.path.splitext(url)[1]
        file_extension = file_extension.replace('.', '')
        return file_extension

    def _entries(self, search_query, search_set):
        options = webdriver.FirefoxOptions()
        #options.add_argument('--headless')
        driver = webdriver.Firefox(options=options)
        driver.get(f'https://whatsdrop.com/search?search={search_query}&set={search_set}')
        scroll_page(driver, 2, 100)
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        driver.quit()
        media_containers = soup.find_all('a', {'class': 'boxpost'})
        for container in media_containers:
            video_id = container['href']
            video_url = 'https://whatsdrop.com' + video_id
            yield self.url_result(video_url, ie=WhatsDropVideoIE.ie_key())

    def _real_extract(self, url):
        mobj = self._match_valid_url(url)
        search_query = mobj.group('query')
        search_set = mobj.group('set')
        entries = self._entries(search_query, search_set)
        return self.playlist_result(entries, search_query)




class WhatsDropChannelLikedIE(InfoExtractor):
    _VALID_URL = r'https?://(?:www\.)?whatsdrop\.com/@(?P<id>[^/?&]+)\/liked'

    def _entries(self, channel_name):
        options = webdriver.FirefoxOptions()
        # options.add_argument('--headless')
        driver = webdriver.Firefox(options=options)
        media_containers = self.get_media_containers(driver, channel_name)
        while not media_containers:
            media_containers = self.get_media_containers(driver, channel_name)
        driver.quit()
        for container in media_containers:
            video_id = container['href']
            video_url = 'https://whatsdrop.com' + video_id
            yield self.url_result(video_url, ie=WhatsDropVideoIE.ie_key())

    def _real_extract(self, url):
        channel_id = self._match_id(url)
        entries = self._entries(channel_id)
        return self.playlist_result(entries, channel_id)

    def get_media_containers(self, driver, channel_name):
        driver.get(f'https://whatsdrop.com/@{channel_name}/liked')
        if not wait_for_element(driver, 10, By.CSS_SELECTOR, "a.boxpost.tube") and not wait_for_element(driver, 10, By.CSS_SELECTOR, "a.boxpost.image"):
            return []
        scroll_page(driver, 6, 100, 3)
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        video_containers = soup.find_all('a', {'class': 'boxpost tube'})
        image_containers = soup.find_all('a', {'class': 'boxpost image'})
        return video_containers + image_containers




def scroll_page(driver, pause_time, max_scrolls, max_no_change=3):
    # print("Scrolling page...")
    last_height = driver.execute_script("return document.body.scrollHeight")
    num_scrolls = 0
    no_change_count = 0
    while num_scrolls < max_scrolls:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(pause_time)
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            no_change_count += 1
            if no_change_count >= max_no_change:
                break
        else:
            no_change_count = 0
        last_height = new_height
        num_scrolls += 1


def wait_for_element(driver, timeout, by, value):
    try:
        WebDriverWait(driver, timeout).until(
            EC.presence_of_element_located((by, value))
        )
    except TimeoutException:
        return False
    return True