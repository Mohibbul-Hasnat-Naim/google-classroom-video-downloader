# Audio + Video merge.py

import os
import re
import subprocess
import sys


def check_ffmpeg():
    """Check if FFmpeg is installed and available in system PATH."""
    try:
        subprocess.run(
            ["ffmpeg", "-version"],
            capture_output=True,
            check=True
        )
        return True
    except (subprocess.CalledProcessError, FileNotFoundError):
        return False


# ===== PRE-CHECK: FFmpeg =====
if not check_ffmpeg():
    print("❌ FFmpeg not found!")
    print("Please install FFmpeg and add it to your System PATH.")
    print("Download: https://ffmpeg.org/download.html")
    sys.exit(1)


# ===== CONFIG =====
INPUT_FOLDER = os.path.join(os.getcwd(), "INPUT")
OUTPUT_FOLDER = os.path.join(os.getcwd(), "OUTPUT")

# Create OUTPUT folder if missing
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

# Create INPUT folder if missing
if not os.path.exists(INPUT_FOLDER):
    os.makedirs(INPUT_FOLDER)
    print("📁 INPUT folder created.")
    print("Please place downloaded files inside INPUT folder and run again.")
    sys.exit(1)

TITLE = "Thev_Machine"  # Customize your title here

# Clean invalid Windows filename characters
TITLE = re.sub(r'[\\/*?:"<>|]', "", TITLE)


# ===== FUNCTIONS =====
def merge_av(video_file, audio_file, output_file):
    """Merge video + audio using FFmpeg."""

    # Wrap paths with quotes for Windows path safety
    video_file = f'"{video_file}"'
    audio_file = f'"{audio_file}"'
    output_file = f'"{output_file}"'

    subprocess.run(
        f'ffmpeg -i {video_file} -i {audio_file} '
        f'-c:v copy -c:a copy -shortest -y {output_file}',
        shell=True,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.STDOUT
    )


def extract_number(filename):
    """
    Extract numbering from:
    videoplayback.mp4 -> 0
    videoplayback_1.mp4 -> 1
    videoplayback_2.mp4 -> 2
    """

    match = re.search(r'_(\d+)', filename)
    if match:
        return int(match.group(1))

    if "videoplayback" in filename:
        return 0

    return -1


# ===== MERGE PROCESS =====
videos = [f for f in os.listdir(INPUT_FOLDER) if f.endswith(".mp4")]
audios = [f for f in os.listdir(INPUT_FOLDER) if f.endswith(".m4a")]

videos.sort(key=extract_number)
audios.sort(key=extract_number)

video_dict = {
    extract_number(v): os.path.join(INPUT_FOLDER, v)
    for v in videos
}

audio_dict = {
    extract_number(a): os.path.join(INPUT_FOLDER, a)
    for a in audios
}

counter = 1

for num in sorted(video_dict.keys()):
    if num in audio_dict:
        v_name = os.path.basename(video_dict[num])
        a_name = os.path.basename(audio_dict[num])

        output_name = f'{counter} "{TITLE}".mp4'
        output_path = os.path.join(OUTPUT_FOLDER, output_name)

        print(f"{v_name} + {a_name} --> {output_name}")

        merge_av(
            video_dict[num],
            audio_dict[num],
            output_path
        )

        counter += 1

    else:
        print(
            f"⚠ Skipping {os.path.basename(video_dict[num])} "
            f"→ no matching audio"
        )

print("\n✅ All existing pairs merged!")