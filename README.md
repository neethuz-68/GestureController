<p align="center">
  <img src="./img.png" alt="Project Banner" width="100%">
</p>

# AirGestures 🎯

## Basic Details

### Team Name: LadyBug

### Team Members
- Member 1: Devangana U - CET
- Member 2: V Navaneeta Saraswathy - CET

### Project Description
AirGestures is a cross-platform hand gesture control system that allows users to navigate presentations, scroll through documents, and zoom in/out without touching the keyboard or mouse. Using a live webcam feed and real-time hand tracking via MediaPipe, the system detects specific gestures—such as open palm, fist, one finger, or two fingers—and maps them to actions like scroll, zoom, or slide navigation. Users can toggle the feature on/off with a keyboard shortcut, enabling seamless control in PowerPoint, PDF viewers, and web documents, all while running in the background.

### The Problem statement
In presentations, meetings, or document navigation, users frequently need to interact with a computer via keyboard or mouse, which can be cumbersome, slow, and disrupt the flow of work. Traditional input methods are not intuitive for hands-free control, and there is no easy way to navigate slides, scroll documents, or zoom in/out without physically touching the device.

### The Solution
AirGestures leverages real-time hand tracking via a webcam to recognize simple gestures and map them to computer actions. With gestures like open palm, fist, or one/two fingers, users can scroll, zoom, or navigate slides without touching the keyboard or mouse. The system runs in the background and can be toggled on/off using a keyboard shortcut, providing an intuitive, touch-free, and efficient way to control presentations and documents across multiple platforms.
Key Advantages:
Hands-free control for presentations and documents.
Real-time gesture recognition using MediaPipe.
Hotkey toggle for quick activation/deactivation.
Cross-platform support with minimal setup.

## Technical Details
Gesture Detection:
Uses MediaPipe Hands to detect hand landmarks in real-time from a webcam feed.
Each finger’s position is analyzed to classify gestures like open palm, fist, 1 finger, 2 fingers.

Action Mapping:
Gestures are mapped to computer actions:
Open palm → Zoom In
Fist → Zoom Out
1 finger → Scroll Up
2 fingers → Scroll Down
PowerPoint specific: One additional gesture for Next Slide / Previous Slide.

Real-Time Control:
Runs a background thread for continuous hand detection.
Can be toggled on/off with a keyboard shortcut (Ctrl+Shift+G).
Optional hotkey to quit the application gracefully.

Platform Adaptation:
Detects the active window to apply slide navigation only when using PowerPoint or other target applications.
Cross-platform support for Windows, Mac, and Linux with platform-specific APIs.

User Feedback (UI):
Optional overlay on the webcam feed showing detected gesture in real-time for clarity during demos.

### Technologies/Components Used
-Languages used: Python 3.10+
-Frameworks used: None (lightweight, custom Python implementation)
-Libraries used: OpenCV, MediaPipe, PyAutoGUI, Keyboard, Pillow (PIL)
-Tools used: VS Code, Git, Python virtual environment, System APIs (win32gui for Windows, AppKit for Mac, subprocess for Linux)
---

## Features

List the key features of your project:
- Feature 1: Gesture-based navigation: scroll up/down, zoom in/out.
- Feature 2: Slide control: next/previous slide in PowerPoint
- Feature 3: Hotkey toggle for on/off control.
- Feature 4: Cross-platform support (Windows, macOS, Linux).
- Feature 5: Real-time feedback with optional on-screen overlay.

---

## Implementation

### For Software:

#### Installation
# 1. Clone the repository
git clone <https://github.com/neethuz-68/GestureController>
cd GestureController/src

# 2. Create a virtual environment (optional but recommended)
python -m venv venv
# Activate the virtual environment
# Windows
venv\Scripts\activate
# Mac/Linux
source venv/bin/activate

# 3. Manually install if no requirements file
pip install opencv-python mediapipe pyautogui keyboard

#### Run
# Run the main script in the background
python main.py

# Use Ctrl+Shift+G to toggle gesture control ON/OFF
# Use Ctrl+Shift+Q to quit the program

## Project Documentation

### For Software:

#### Screenshots (Add at least 3)

![Screenshot1]https://drive.google.com/file/d/1loBVtg8j2KcFKe3YVF_3yGxTpGtC0WJQ/view?usp=sharing

![Screenshot2]https://drive.google.com/file/d/15s7DHWn93J_MxAAaPTTxBvzPdcoDLrFH/view?usp=sharing

![Screenshot3]https://drive.google.com/file/d/1Y2O2rmH1estULS7HUh7X30pqw2xCOgiA/view?usp=sharing

#### Diagrams

**System Architecture:**
The system consists of three main components: Gesture Detection, Action Mapping, and System Control. These components interact to allow users to control software (e.g., PowerPoint, web browsers, PDF viewers) via hand gestures.
Components & Flow:
Webcam Input
Captures live video frames.
Feeds frames into the Gesture Detection module.
Gesture Detection (Controller + Mediapipe)
Uses Mediapipe Hands to detect hand landmarks.

Classifies gestures using GestureClassifier:
Open palm → Zoom in
Fist → Zoom out
1 finger → Scroll up
2 fingers → Scroll down
3 fingers → next slide
Index and pinky → previous slide

Action Mapping (ActionMapper)
Checks the active window to determine the context (PowerPoint, browser, etc.).
Maps gestures to appropriate system actions using pyautogui or keyboard:
Scroll, zoom, slide navigation.

System Control & Hotkeys
Background Python script listens for hotkeys:
Ctrl+Shift+G → Toggle gesture detection on/off
Ensures non-blocking execution so gestures can work alongside other applications.

[Webcam] → [GestureController] → [GestureClassifier] → [ActionMapper] → [System / Application]
                 ↑
                 │
        [Hotkey Toggle / Quit]


## Additional Documentation


### For Scripts/CLI Tools:

#### Command Reference

**Basic Usage:**
```bash
python main.py
```

**HotKeys**
Ctrl+Shift+G (Toggle on/off)

**Examples:**

# Start the controller
python main.py

# Toggle gestures ON
Press Ctrl+Shift+G

# Toggle gestures OFF
Press Ctrl+Shift+G again


#### Demo Output

**Example 1: Basic Processing**

**Input:**
```None```

**Command:**
```bash
python main.py
```

**Output:**
```
(venv) PS C:\Users\navan\GestureController\src> python main.py
INFO: Created TensorFlow Lite XNNPACK delegate for CPU.
Gesture Controller running in background. Press Ctrl+Shift+G to toggle.
Gesture ON
Gesture OFF
```

## Project Demo

### Video
https://drive.google.com/file/d/1JpBirrMMzV4xPBpIQGD0Qct5P4chm-be/view?usp=sharing

## AI Tools Used (Optional - For Transparency Bonus)

**Tool Used:** [ChatGPT]

**Purpose:** Assisted with:
Planning the project workflow and team responsibilities
Writing Python boilerplate code for gesture detection and mapping
Debugging issues with MediaPipe, OpenCV, and keyboard shortcuts
Suggesting improvements for code structure and repo organization
Drafting project documentation, problem statements, and technical descriptions

**Key Prompts Used:**
- "Create a Python class to classify hand gestures using MediaPipe"
- "Suggest a clean folder structure for a Python gesture control project"
- "Generate a project problem statement and technical details for documentation"

**Percentage of AI-generated code:** [Approximately 50%]

**Human Contributions:**
- Designing system architecture and workflow for gesture control
- Implementing gesture-to-action mapping logic (scroll, zoom, slide navigation)
- Integrating MediaPipe, OpenCV, pyautogui, and keyboard libraries
- Testing across platforms and handling live webcam input
- Version control management and merging contributions between team members

*Note: Proper documentation of AI usage demonstrates transparency and earns bonus points in evaluation!*

---

## Team Contributions

- [Navaneeta]: [Integrated gesture detection with the webcam using MediaPipe.
            Developed the GestureController class and main application logic.
            Implemented the hotkey toggle system for background gesture control.
            Tested the final system and handled demo execution.]
- [Devangana]: [Developed the ActionMapper to map gestures to scroll, zoom, and slide actions.
            Added PowerPoint-specific gestures for next/previous slide.
            Created gesture classifier logic (GestureClassifier class).
            Helped with debugging, documentation, and Git collaboration.]
---

## License

This project is licensed under the [LICENSE_NAME] License - see the [LICENSE](LICENSE) file for details.

**Common License Options:**
- MIT License (Permissive, widely used)
- Apache 2.0 (Permissive with patent grant)
- GPL v3 (Copyleft, requires derivative works to be open source)

---

Made with ❤️ at TinkerHub
