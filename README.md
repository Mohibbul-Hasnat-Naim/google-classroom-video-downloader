# Classroom Video Downloader

A simple tool for downloading Google Classroom videos that do not provide a normal **Download** option.

Sometimes in Google Classroom, videos can only be watched online and the download button is unavailable.
This project helps save those videos for personal study by using the video stream links from the browser.

It works by:

* Detecting the hidden video/audio stream links from the browser
* Cleaning the copied URLs automatically
* Opening the corrected links for download using browser or IDM
* Downloading both video and audio files
* Merging them into one final complete video using FFmpeg

This is useful for students who want offline access to lecture videos for personal learning.

---

# What This Project Does

Some Google Classroom videos are protected from direct download.

That means:

* no normal **Download** button
* only online viewing is allowed

But the browser still loads:

* one video stream (`.mp4`)
* one audio stream (`.m4a`)

This project helps capture those stream links and combine them into a proper downloadable video.

Without this process, users often get:

* video without sound
  or
* only audio

This tool solves that automatically.

---

# Features

## 1. Clipboard Watcher

This script watches copied links from your browser.

It will:

* detect copied `videoplayback` links
* remove unnecessary URL parts like:

  * `range=...`
  * `srfvp=1`
* convert:

```text id="0r0k6s"
&ump=1&srfvp=1
```

into:

```text id="u4v14v"
&ump
```

* match audio + video pair automatically
* open the cleaned links in browser / IDM

You only need to:

* copy the first link
* copy the second link

The script handles the rest.

---

## 2. Audio + Video Merger

After downloading finishes:

* it finds matching video + audio files
* merges them using FFmpeg
* saves the final video inside the OUTPUT folder

Example:

```text id="26rj6w"
videoplayback.mp4 + videoplayback.m4a
→ 1 "Thev_Machine".mp4
```

Fast merging:
usually only a few seconds per video

---

# Project Folder Structure

Keep your project like this:

```text id="yjlwmv"
Classroom-Video-Downloader/

│
├── clipboard_watcher.py
├── Audio + Video merge.py
├── requirements.txt
├── README.md
│
├── INPUT/
│   └── Put downloaded files here
│
└── OUTPUT/
    └── Final merged videos appear here
```

---

# Before First Use

You need only 3 things:

---

## 1. Python Installed

Install Python on your computer.

Download from:

### Very Important

During installation, check:

```text id="8kg6b8"
Add Python to PATH
```

before clicking Install.

---

## 2. FFmpeg Installed

FFmpeg is used for merging video + audio.

Download from:

After installing, FFmpeg must be added to your system PATH.

(You can easily find simple YouTube tutorials for this.)

---

## 3. Install Required Python Package

Open **Command Prompt (CMD)** and type:

```text id="p5k5uj"
pip install pyperclip
```

Then press Enter.

This is needed only once.

---

# How To Use

---

# Step 1 — Open Google Classroom Video

Open the lecture video in your browser.

Since download is blocked, we use browser tools to access the hidden stream links.

---

# Step 2 — Open Developer Tools

Press:

```text id="f2jrrt"
F12
```

or

```text id="2lplg6"
Right Click → Inspect
```

Then go to:

```text id="5s9hmp"
Network Tab
```

Search for:

```text id="k4xjsa"
videoplayback
```

You will usually find:

* one audio link
* one video link

---

# Step 3 — Run Clipboard Watcher

Open:

```text id="x5gzja"
clipboard_watcher.py
```

Now:

* copy the first link
* copy the second link

The script will:

* detect both links
* clean them automatically
* open them in browser / IDM

Now download both files into:

```text id="7rw95t"
INPUT
```

folder.

---

# Step 4 — Change Video Title

Open:

```text id="7r0dhw"
Audio + Video merge.py
```

Find:

```python id="rb7hbv"
TITLE = "Thev_Machine"
```

Change it to your lecture title.

Example:

```python id="1p0h3r"
TITLE = "Power System Lecture 03"
```

Save the file.

---

# Step 5 — Run Merge Script

Open:

```text id="5gs5eq"
Audio + Video merge.py
```

The script will:

* scan the INPUT folder
* merge matching files
* create final videos inside OUTPUT

Example output:

```text id="vdgwrn"
1 "Power System Lecture 03".mp4
2 "Power System Lecture 03".mp4
3 "Power System Lecture 03".mp4
```

Done.

---

# Important Notes

## INPUT Folder

Only keep downloaded Classroom files here.

Example:

```text id="cm6prp"
videoplayback.mp4
videoplayback.m4a
videoplayback_1.mp4
videoplayback_1.m4a
```

---

## OUTPUT Folder

Final merged videos will appear here automatically.

---

## If FFmpeg Error Appears

It usually means:

* FFmpeg is not installed
  or
* FFmpeg is not added to PATH

Please fix that first.

---

# Recommended Workflow

Best method:

### First

Download all videos

### Then

Run merge script once

This is faster and cleaner.

---

# Disclaimer

This project is made for personal educational use only.

Please respect copyright, platform policies, and course ownership.

Use responsibly.

---

# Author

Mohibbul Hasnat Naim
Bangladesh
