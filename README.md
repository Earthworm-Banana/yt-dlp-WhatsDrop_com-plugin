# WhatsDrop.com YT-DLP Plugin 🛠️

## Introduction 📚

Welcome to the WhatsDrop.com YT-DLP Plugin, a tool designed to enhance your media downloading experience from WhatsDrop.com. This plugin allows you to effortlessly fetch individual videos, images, or entire uploader's content, as well as their publicly viewable liked posts, search results, and popular media.

> 📝 **Note**: This plugin and README were crafted with the assistance of OpenAI's GPT-4 model.

## Features 🌟

- **Individual Media Downloads** 🎥🖼️  
  Download videos or images individually.

- **Uploader Content Downloads** 📺  
  Download all media content from an entire uploader's page.

- **Support for Image Posts** 🖼️  
  Download image-only posts from WhatsDrop.com.

- **Publicly Viewable Liked Posts** 👍  
  Download media from publicly viewable liked posts of a user.

- **Search Results Download** 🔍  
  Download media based on search queries, supporting both the general and channel-specific URL patterns.
  > 📝 **Note**: For the channel-specific URL format, ensure that your search is conducted while viewing a specific channel on WhatsDrop.com and then copy the correct URL from the address bar.

- **Popular Media Downloads** 🎉  
  Download media content from the popular tab on WhatsDrop.com, making trending and widely-viewed content readily accessible.
  > 📝 **Note**: Ensure to use the specific URL format from the popular tab for this feature.

## Installation Guide 🖥️

> ⚠️ **Compatibility**: These installation steps are tailored for Windows 11 and have only been tested on this specific OS.

1. 🌐 Open your Command Prompt (`cmd`).
2. 🗂️ Navigate to your yt-dlp plugins directory:
    ```bash
    cd C:\Users\%username%\AppData\Roaming\yt-dlp\plugins
    ```
3. 🎬 Clone this repository:
    ```bash
    git clone https://github.com/Earthworm-Banana/yt-dlp-WhatsDrop_com-plugin.git
    ```
4. 🧰 Install necessary Python packages:
    ```bash
    pip install selenium
    pip install beautifulsoup4
    ```
   
> 📘 For more ways of installing plugins, visit [yt-dlp's plugin installation guide](https://github.com/yt-dlp/yt-dlp#installing-plugins).

## Usage Guidelines 📋

### Commands 📜

- **Download an Individual Video or Image** 🎥🖼️  
  ```bash
  yt-dlp "https://whatsdrop.com/example_media"
  ```
  
- **Download an Uploader's Content** 📺  
  ```bash
  yt-dlp "https://whatsdrop.com/@example_uploader"
  ```

- **Download Publicly Viewable Liked Posts** 👍  
  ```bash
  yt-dlp "https://whatsdrop.com/@example_uploader/liked"
  ```

- **Download Search Results** 🔍  
  Compatible with both general and channel-specific URL formats.
  - General search format:
    ```bash
    yt-dlp "https://whatsdrop.com/search?search=example_query&set=example_set"
    ```
  - Channel-specific search format:
    ```bash
    yt-dlp "https://whatsdrop.com/@example_uploader/search?search=example_query&set=example_set"
    ```

- **Download Popular Media** 🎉  
  ```bash
  yt-dlp "https://whatsdrop.com/p-example_popular_media"
  ```

### Metadata Extraction 🔍

- 🏷️ Title
- 🔠 ID
- 📝 Description
- 🙋 Uploader Username
- 🖥️ Dimensions (for videos)
- ⏱️ Duration (for videos)
- 👁️ View Count
- 👍 Like Count
- 👎 Dislike Count
- 📅 Upload Date

### Limitations and Known Issues ❗

- 📉 **Video Quality Limitation**: The plugin defaults to downloading the 'streaming' version of videos, which generally provides satisfactory viewing quality on the site. A 'high-quality' download option is coded but inactive (commented out) due to stability issues. This alternative option often retrieves the media in a different container, although whether it always offers superior quality remains undetermined, as an extensive, comparative evaluation hasn’t been undertaken. However, for the majority of users, the streaming version’s quality is likely to be sufficiently high.

- 🗨️ **Comment Downloading**: At this time, the plugin does not facilitate the downloading of comments.

- 🌐 **Selenium Dependency**: Selenium is required for downloading features like publicly viewable liked posts, search results, and popular media, as these pages need JavaScript for rendering. Ensure Selenium is installed and configured to fully exploit these features.

- ⏳ **Dynamic URL Challenges**: This issue pertains to the gradual expiration of URLs during an active download session, potentially leading to 404 errors after several minutes of downloading videos, particularly from large user profiles. This occurs because the site generates slightly dynamic URLs that time out after a certain duration. Utilizing the `--lazy-playlist` option can circumvent this, and retriggering the extraction fetches the refreshed URLs.

- 🚫 **URL Validity Issue**: Contrary to the dynamic URL issue, the URL validity concern arises when the plugin generates invalid URLs, which don’t correspond to any actual content. This isn’t a problem related to URL expiration but seems to be a peculiarity in URL generation, prominently observed on one specific user account and not a common or widespread issue. The plugin will access a 404 page but will not attempt to download non-existing content and will proceed as per usual. Given its rarity and low impact (affecting 2 out of about 280 media items in the noted account), this isn’t an actively pursued fix but will be revisited if it emerges as a pervasive or impactful problem. 

## Support and Contributions 🤝

For any issues or suggestions, feel free to [open an issue on GitHub](https://github.com/Earthworm-Banana/yt-dlp-WhatsDrop_com-plugin/issues).

Thank you for choosing the WhatsDrop.com YT-DLP Plugin. Happy downloading! 🎉