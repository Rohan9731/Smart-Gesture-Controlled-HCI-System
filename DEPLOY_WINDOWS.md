# Windows Desktop Deployment Guide (Interview Showcase)

This guide packages the project as a Windows desktop app (EXE) using PyInstaller.

## 1. One-time prerequisites

- Windows 10/11 (64-bit)
- Python 3.11 installed (py launcher available)
- Git
- Webcam working locally
- MongoDB Atlas connection string ready

Verify Python versions recognized by launcher:

- py -0p

If 3.11 is missing, install Python 3.11 before building.

## 2. Build locally

From project root:

1. Open PowerShell
2. Run:
   ./build_windows.ps1

If script execution is blocked in the current terminal, run this once per shell:

- Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass

After build completes, output is in:

- dist/SmartGestureHCI

## 3. Configure runtime environment

Inside dist/SmartGestureHCI:

1. Copy .env.example to .env
2. Edit .env and set MONGODB.URI

Expected app data location after first launch:

- %APPDATA%/SmartGestureHCI/user_defined_data.json

## 4. Quick smoke test before sharing

1. Launch SmartGestureHCI.exe
2. Click Activate
3. Confirm webcam feed appears
4. Test one gesture in Mouse mode
5. Open Customize Gestures and save one mapping
6. Restart app and confirm saved mapping persists

## 5. Create a portable release zip

From project root:

- Compress dist/SmartGestureHCI as SmartGestureHCI-Windows-x64.zip

Ship this zip for interviews. The reviewer only needs to unzip and run SmartGestureHCI.exe.

## 6. Publish on GitHub Releases

1. Create a new tag (example: v1.0.1-showcase)
2. Push tag
3. In GitHub Releases, attach SmartGestureHCI-Windows-x64.zip
4. Add short notes:
   - Built for Windows 10/11 x64
   - Requires webcam permission
   - Add .env with MONGODB.URI before first run

## 7. Interview demo fallback plan

Keep these ready in case of venue/network issues:

- Local demo video (60-90 seconds)
- Prepared .env file on your demo machine
- A second zip copy on USB/cloud
- Screen recording of gesture controls in action
