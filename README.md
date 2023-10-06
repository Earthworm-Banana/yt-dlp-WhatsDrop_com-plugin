# WhatsDrop.com YT-DLP Plugin 🛠️

## Introduction 📚

Welcome to the WhatsDrop.com YT-DLP Plugin, a tool designed to enhance your media downloading experience from WhatsDrop.com by enabling you to effortlessly fetch individual videos, images, or entire uploader's content.

> 📝 **Note**: This plugin and README were crafted with the assistance of OpenAI's GPT-4 model.

## Features 🌟

- **Individual Media Downloads** 🎥🖼️  
  Download videos or images individually.
  
- **Uploader Content Downloads** 📺  
  Download all media content from an entire uploader's page.

- **Support for Image Posts** 🖼️  
  Download image-only posts from WhatsDrop.com.

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

## Support and Contributions 🤝

For any issues or suggestions, feel free to [open an issue on GitHub](https://github.com/Earthworm-Banana/yt-dlp-WhatsDrop_com-plugin/issues).

Thank you for choosing the WhatsDrop.com YT-DLP Plugin. Happy downloading! 🎉