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

- 📉 **Video Quality:**
  - **Default Streaming Quality**: Videos are downloaded in the standard 'streaming' quality.
  - **High-Quality Download**: A high-quality download option is coded but inactive due to it retrieving invalid files in trials. Although a visual comparison between both the standard and high-quality from the website (via a typical browser interaction) did not showcase a discernible quality difference, they can occasionally be provided in different media containers (e.g., streaming in .mp4 and download in .mov).

- 🗨️ **Comment Downloading:**
  - Comment downloading is not supported by the plugin.

- 🌐 **Selenium Dependency:**
  - To fully utilize features like downloading publicly viewable liked posts, search results, and popular media which require JavaScript rendering, Selenium is needed.

- ⏳ **Dynamic URL Challenges:**
  - Some URLs may expire during extensive download sessions, potentially causing 404 errors.
  - Workaround: The `--lazy-playlist` option can help navigate this issue, although it may not be as effective if the extractor utilizes Selenium.

- 🚫 **URL Validity Issue:**
  - A rare issue where the plugin might generate invalid URLs has been observed. This was noted in only one specific user account and affected a minimal amount of content (2 out of approximately 280 items).
  - Its impact is minimal, and given its scarcity, it is not an immediate concern but will be monitored and investigated if it emerges as a recurring or impactful problem. Users are encouraged to report such instances.
  - This does not affect the functionality of the plugin, as it only generates invalid URLs that causes a 404 error. Valid URLs are still downloaded.
## Support and Contributions 🤝

For any issues or suggestions, feel free to [open an issue on GitHub](https://github.com/Earthworm-Banana/yt-dlp-WhatsDrop_com-plugin/issues).

Thank you for choosing the WhatsDrop.com YT-DLP Plugin. Happy downloading! 🎉