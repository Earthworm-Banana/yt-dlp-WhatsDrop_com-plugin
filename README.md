# WhatsDrop.com YT-DLP Plugin 🛠️

## Introduction 📚

Welcome to the WhatsDrop.com YT-DLP Plugin. This tool enhances your video downloading experience from WhatsDrop.com, allowing you to grab individual videos or entire channels with ease.

> 📝 **Note**: This plugin and README were largely assisted by OpenAI's GPT-4 model.

## Features 🌟

- **Individual Video Downloads** 🎥  
  Grab videos one at a time.
  
- **Channel Downloads** 📺  
  Download an entire channel's video lineup.

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

- **Download an Individual Video** 🎥  
  ```bash
  yt-dlp "https://whatsdrop.com/example_video"
  ```
  
- **Download a Channel** 📺  
  ```bash
  yt-dlp "https://whatsdrop.com/@example_channel"
  ```
  
### Metadata Extraction 🔍

- 🏷️ Video Title
- 🔠 Video ID
- 📝 Description
- 🙋 Uploader Username
- 🖥️ Video Dimensions
- ⏱️ Video Duration
- 👁️ View Count
- 👍 Like Count
- 👎 Dislike Count
- 📅 Upload Date

### Limitations and Known Issues ❗

- 📉 **Video Quality**: The plugin is set to download the 'streaming' version of the video, which is what you typically watch on the site. A 'high-quality' download option is in the code but has been disabled (commented out) because it wasn't functioning properly. For most users, the quality difference is hardly noticeable.

- 🗨️ **Comments**: Downloading of comments is not supported at this time.

## Support and Contributions 🤝

For any issues or suggestions, feel free to [open an issue on GitHub](https://github.com/Earthworm-Banana/yt-dlp-WhatsDrop_com-plugin/issues).

Thank you for choosing the WhatsDrop.com YT-DLP Plugin. Happy downloading! 🎉
