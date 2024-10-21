
# Blind Assist 
The main goal of this device is to empower and assist visually impaired individuals in performing daily activities within indoor environments. The device comprises three key subsystems: Object Detection, Text Localization, and Path Guidance. These features enable users to navigate their surroundings, identify objects, and read text effectively.

The device utilizes voice commands for user interaction and incorporates a camera to engage with the environment. 

To operate the device, users are required to wear a Raspberry Pi V3, which serves as a controller. This wearable device communicates with a central server via a network for data processing and analysis


## Features

#### Objet Detection
Identifies and locates objects within the user’s vicinity
#### Text Localization
Recognizes and reads text aloud, facilitating reading and comprehension
#### Path Guidance
Provides auditory directions to help users navigate safely through indoor spaces
#### Voice Command Interface
Allows for hands-free interaction, enhancing usability and accessibility




## Architecture

![App Screenshot](https://github.com/Immortal-Pi/doc_chat_bot/blob/main/resources/1.png)

## Useage

![App Screenshot](https://github.com/Immortal-Pi/doc_chat_bot/blob/main/resources/1.png)

![App Screenshot](https://github.com/Immortal-Pi/doc_chat_bot/blob/main/resources/2.png)

![App Screenshot](https://github.com/Immortal-Pi/doc_chat_bot/blob/main/resources/3.png)

![App Screenshot](https://github.com/Immortal-Pi/doc_chat_bot/blob/main/resources/4.png)


## Key Highlights

compared different CNN algorithms and choose the best algoritm for optimum results. YOLO detection had quite hugh accuracy compared to the other convolutional neural network based algorithms. YOLO could run recognition upto 91 frames per second.

![App Screenshot](https://github.com/Immortal-Pi/doc_chat_bot/blob/main/resources/1.png)


YOLO could deliver around 8 frames per second, but using the conventional algorithms will allow only 0.5 frames to be processed

![App Screenshot](https://github.com/Immortal-Pi/doc_chat_bot/blob/main/resources/1.png)
## Tech Stack

**Hardware:** Raspberry Pi (with camera module)

**Computer Vision:** YOLO (for real-time object detection)

**OCR:** Tesseract (for text recognition)

**Audio Output:** Text-to-Speech technology (for audible feedback)

**Programming Language:** Python



## Conclusion
The problem we aimed to solve is to simplify the day-to-day activities of visually impaired individuals. The expected outcome of our efforts is to reach a point where visually impaired people can confidently handle their tasks just like anyone else. Our goal is to bridge the gap between them and sighted individuals.

This is just one drop in an ocean of efforts aimed at improving lives. Several decades down the line, we envision a future where the disability quota for the blind is completely eliminated.

Using commodity hardware makes the device more accessible and affordable. Currently, the software is in a rough form, which can be further smoothed and refined to meet industrial standards.