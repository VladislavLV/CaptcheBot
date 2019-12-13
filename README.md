# CaptcheBot

This project was designed to host a bot for easy text conversion from image to text. The bot uses Telegram API to get image and to provide response. The response you get is just a text that bot managed to detect on the image. Bot has two modes - number OCR and text OCR. It differs by detection method, the first one detects each number as object, while the second one detects the whole sentence as object.  
**You should always provide number of mode you want to use for detection ("1" for number detection, "2" for text detection)**

## Getting Started

### Requirements

* Windows/Linux
* OpenCV >= 3.0
* CUDA 10.0 in case GPU usage
* cuDNN >= 7.0 for CUDA 10.0
* GPU with CC >= 3.0
* Python >= 3.5(64bit)
* Python libraries: Pillow, pyTesseract, python-telegram-bot.  
Any of this libraries can be installed by typing:  
`pip install <library name>`

### Installing

1. Download current git repository.
2. Unzip archive.
3. Install OpenCV3 to the **C:/OpenCV_3.0/opencv/**.
4. Compile Yolo library from [this repository](https://github.com/AlexeyAB/darknet) using ways, provided in ReadMe.
5. Put **yolo_cpp_dll.dll** or **libdarknet.so** near .py files.
6. Find files **opencv_world347.dll** and **opencv_ffmpeg347_64.dll** in **C:\opencv_3.0\opencv\build\x64\vc14\bin** and put it into the same folder.
8. Edit bot.py file, [line 54](https://github.com/VladislavLV/CaptcheBot/blob/c276dd9bb532bdb955045adc68f135cf3df2ae33/bot.py#L54) by adding Telegram token.
9. Run project from command promt (for Windows) or terminal (for Linux) by using command python bot.py.

### Requirements for image:
For numberOCR there are some requirements for number to be correctly detected. Neural network was trained to **detect images with resolution from 150x150 to 400x400**, you can provide any other images, but numbers on it **should be clearly seen in 224x244 resolution**.
Text OCR doesn't have such requirements, but for best detection performance it's recommended to have bright background and dark text on it.

### Demonstration

![](https://sun9-64.userapi.com/c857124/v857124869/69078/imDkDjAUoEI.jpg)
![](https://sun9-16.userapi.com/c857124/v857124869/69068/zSppIqgJ4wg.jpg)
