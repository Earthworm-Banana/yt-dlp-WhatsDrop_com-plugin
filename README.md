# WhatsDrop.com YT-DLP Plugin 🛠️

## Introduction 📚

Welcome to the WhatsDrop.com YT-DLP Plugin, a tool designed to enhance your media downloading experience from WhatsDrop.com. This plugin allows you to effortlessly fetch individual videos, images, or entire uploader's content, as well as their publicly viewable liked posts and search results.

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

- 📉 **Video Quality**: The plugin is set to download the 'streaming' version of the video, which is what you typically watch on the site. A 'high-quality' download option is in the code but has been disabled (commented out) due to functionality issues. For most users, the quality difference is hardly noticeable.

- 🗨️ **Comments**: Downloading of comments is not supported at this time.

- 🌐 **Selenium Requirement**: The feature for downloading publicly viewable liked posts and search results requires Selenium due to the necessity of JavaScript for loading the pages.

- ⏳ **Dynamic URLs**: Extracting from large user profiles may result in 404 errors after a few minutes of downloading videos. This is because the site's URLs are slightly dynamic and expire after a certain amount of time. To mitigate this, you can use the `--lazy-playlist` option. Additionally, re-running the extraction will fetch the newer URLs.

## Support and Contributions 🤝

For any issues or suggestions, feel free to [open an issue on GitHub](https://github.com/Earthworm-Banana/yt-dlp-WhatsDrop_com-plugin/issues).

Thank you for choosing the WhatsDrop.com YT-DLP Plugin. Happy downloading! 🎉