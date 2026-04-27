# clipboard_watcher.py

import time
import webbrowser
import sys
from urllib.parse import urlparse, parse_qsl, urlunparse

try:
    import pyperclip
except ModuleNotFoundError:
    print("❌ pyperclip not installed!")
    print("Run this command in CMD:")
    print("pip install pyperclip")
    sys.exit(1)


last_clip = ""
stored_clip = None


def clean_video_url(original_url):
    """
    Clean Google Classroom video URL by:
    - removing range
    - removing srfvp
    - keeping only 'ump' instead of ump=1
    """

    parsed = urlparse(original_url)
    query_list = parse_qsl(
        parsed.query,
        keep_blank_values=True
    )

    new_query = []

    for key, value in query_list:
        if key in ["srfvp", "range"]:
            continue

        elif key == "ump":
            new_query.append((key, ""))  # keep only ump

        else:
            new_query.append((key, value))

    # Manual rebuild of query string
    query_parts = []

    for key, value in new_query:
        if value == "":
            query_parts.append(key)
        else:
            query_parts.append(f"{key}={value}")

    cleaned_query = "&".join(query_parts)

    cleaned_url = urlunparse(
        parsed._replace(query=cleaned_query)
    )

    return cleaned_url


print("📋 Clipboard watcher started.")
print("Copy video/audio links from Google Classroom...\n")


while True:
    clip = pyperclip.paste()

    if clip != last_clip and "videoplayback" in clip:
        last_clip = clip
        print("📥 Link detected")

        if stored_clip is None:
            stored_clip = clip
            print("🧠 Stored first link\n")

        else:
            # Match by Google Drive file ID
            id1 = dict(
                parse_qsl(urlparse(stored_clip).query)
            ).get("id")

            id2 = dict(
                parse_qsl(urlparse(clip).query)
            ).get("id")

            if id1 == id2:
                print("✅ Pair matched → opening in browser")
                print("Waiting for next link...\n")

                webbrowser.open_new_tab(
                    clean_video_url(stored_clip)
                )

                webbrowser.open_new_tab(
                    clean_video_url(clip)
                )

                stored_clip = None

            else:
                print("⚠ Replacing stored link\n")
                stored_clip = clip

    time.sleep(1)