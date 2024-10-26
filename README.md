
# ![logo1](https://github.com/user-attachments/assets/e1a85956-8682-4dfd-ab1d-d6417ca665ec)

[![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)](https://www.python.org/)
[![MIT License](https://img.shields.io/badge/License-MIT-239120?style=for-the-badge&logoColor=white)](https://github.com/AlexRequiemd/CrimsonSimpleImageConverter?tab=MIT-1-ov-file)
![Status](https://img.shields.io/badge/Status-Complete-6600d9?style=for-the-badge&logoColor=white)
[![Author](https://img.shields.io/badge/By-Alex_S._A._Rocha_Filho-ffe200?style=for-the-badge&logoColor=white)](https://github.com/AlexRequiemd)

***YTtoAudio is an application for Downloading videos from Youtube.com and converts to a audio file. This project uses Python 3.11 and several libraries, including Pydub, Pytube and CustomTKinter.***

<img src="https://github.com/user-attachments/assets/5c19b8ba-9354-4971-a8f9-558fb7006195" style="height: 64px; width:64px;"/>

## Table of Contents 

- [Features](#features)
- [Architecture](#architecture)
- [Files and Folders](#files-and-folders)
- [Libraries](#libraries)
- [Supported Formats](#supported-formats)
- [Setup](#setup)
  - [Install Dependencies](#install-dependencies)
  - [Download FFMPEG](#download-ffmpeg)
  - [Folder Structure](#folder-structure)
  - [Windows Executable](#standalone-windows-executable)
- [Usage](#usage)
  - [User Interface](#user-interface)
- [Demonstration](#demonstration)
- [Screenshots](#screenshots)
- [Contributing](#contributing)
- [License](https://github.com/AlexRequiemd/YTtoAudio/tree/YTtoAUDIO?tab=License-1-ov-file)
- [Releases](https://github.com/AlexRequiemd/YTtoAudio/releases)

## Features

- Reading and recognizing video links from the Youtube website.
- Conversion into various audio formats.
- Adjustable settings, including options for handling existing files.
- Graphical user interface using customtkinter.

## Architecture

### Files and Folders

- `assets/`: Contains images and fonts files for the user interface.
- `conv.py`: Initializes conversion function.
- `main.py`: Main application file.

### Libraries

- **Pydub**: Used for audio manipulation and conversion.
- **customtkinter**: Provides custom widgets for the graphical interface.
- **Pytube**: Used for downloading YouTube videos or audio.

## Supported Formats

### Output Settings

- **Audio Format**: `.mp3`, `.wav`, `.ogg`.
- **Audio Bitrate**: `320kbps`, `256kbps`, `192kbps`, `160kbps`, `128kbps`.

## Setup

### Install Dependencies

#### Make sure you have the following libraries installed:
+ **Pydub:** A Python library for manipulating audio files, supporting editing, format conversion, and simple effects.
+ **CustomTkinter:** An extension of Tkinter with modern, customizable widgets for graphical interfaces.
+ **Pytube:** A Python library for downloading YouTube videos or audio with options for resolution and filtering.

```bash
pip install -r requirements.txt
```

### Download FFMPEG
***WARNING The absence of ffmpeg may affect the functioning of the software***

+ For the software to work properly and avoid errors, download ffmpeg from this link: [FFMPEG](https://github.com/BtbN/FFmpeg-Builds/releases/download/latest/ffmpeg-master-latest-win64-gpl.zip)
+ After downloading, extract the files, copy the files inside the path **'ffmpeg-master-latest-win64-gpl\bin\\'** and paste them into the project folder where the **main.py** file is located.

## Standalone Windows Executable
+ You can also download the application executable using the link provided in the [Releases](https://github.com/AlexRequiemd/YTtoAudio/releases) section of the repository. Download the executable from the latest release and follow the instructions for the software work properly.

## Folder Structure
### The project should have the following folder structure:

```plaintext
YTtoAudio/
├── temp/
├── assets/
│   ├── frame_bg.png
│   ├── icon.ico
│   ├── label2_bg.png
│   ├── logo.png
│   ├── logo_bg.png
│   ├── logo_nbg.png
│   ├── MinervaModern_Black.otf
│   ├── MinervaModern_Bold.otf
│   ├── MinervaModern_Regular.otf
│   └── root_bg.png
├── conv.py
├── ffmpeg.exe
├── ffplay.exe
├── ffprobe.exe
└── main.py
```



## Usage
### Start the Application
Run the main file to start the application:

```bash
python main.py
```

## User Interface
### Format:
+ Select the preferred format.
### Bitrate: 
+ Select the preferred bitrate.
### Output: 
+ Select the output folder location.
### Paste URL: 
+ Get the URL copied from the user's clipboard
### Download: 
+ Start download and conversion.

## Demonstration
### Check out the demonstration video of the application:

<a href="https://youtu.be/jYjmX5a1u80"> 
<img src="https://github.com/user-attachments/assets/abcaf86f-78f0-44f1-8366-b99c4689c0fe" style="height: 338px; width:603px;"/>
</a>


### Screenshots
+ Here are some screenshots of the application:

<img src="https://github.com/user-attachments/assets/26f6076d-a140-4007-b669-5471c85adcc0" style="height: 250px; width:427px;"/>

<img src="https://github.com/user-attachments/assets/b97186cd-c16b-4266-9267-cf1e231e9cd8" style="height: 250px; width:427px;"/>

## Contributing
### Contributions are welcome! If you would like to contribute to the project, please follow these steps:

+ Fork the repository.
+ Create a branch for your feature or fix: git checkout -b my-new-feature.
+ Commit your changes: git commit -am 'Add new feature'.
+ Push your branch to the remote repository: git push origin my-new-feature.
+ Open a Pull Request for review.

