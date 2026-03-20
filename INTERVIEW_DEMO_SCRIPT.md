# Interview Demo Script (60-90 Seconds)

## 1) Opening (10-15s)

"This is my Smart Gesture-Controlled HCI System, a real-time computer vision application that lets users control a computer touch-free using hand gestures. I built it in Python with OpenCV and MediaPipe, with a CustomTkinter desktop UI and MongoDB Atlas for persistent user configuration."

## 2) Technical Snapshot (15-20s)

"The app tracks hand landmarks in real time, maps left-hand gestures to control modes, and uses right-hand gestures for actions like mouse control, media/volume, app launching, and virtual keyboard interaction. The architecture is modular, and I added stability/debounce logic for practical usability."

## 3) Live Demo Flow (25-35s)

1. Launch `SmartGestureHCI.exe`.
2. Click `Activate` and show webcam feed.
3. Demonstrate one mode switch with left hand.
4. Demonstrate one action with right hand (example: cursor move + click).
5. Open `Customize Gestures`, save one custom mapping.
6. Mention that settings persist (MongoDB + local runtime file).

Suggested narration:
"You can see the current mode and action feedback updating in real time. I can also customize gestures and save them. This packaging is production-style: users run a packaged EXE without installing Python."

## 4) Deployment/Engineering Highlight (10-15s)

"For deployment, I created a PyInstaller build pipeline, automated Windows release packaging in GitHub Actions, and published a tagged release with a portable zip artifact for easy download and execution."

## 5) Closing (5-10s)

"This project demonstrates end-to-end ownership: ML integration, desktop UX, system automation, cloud persistence, and release engineering for real users."

## Backup Plan (if live demo fails)

- Show a 60-90 second pre-recorded walkthrough.
- Open release page and show downloadable artifact.
- Explain runtime requirements: webcam permissions and `.env` MongoDB URI.
