from flask import Flask, render_template, request, send_file
from pytube import YouTube
from moviepy.editor import AudioFileClip
import os
import uuid

app = Flask(__name__)

DOWNLOAD_FOLDER = "downloads"
os.makedirs(DOWNLOAD_FOLDER, exist_ok=True)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        url = request.form["url"]
        try:
            yt = YouTube(url)
            video = yt.streams.filter(only_audio=True).first()
            temp_file = os.path.join(DOWNLOAD_FOLDER, f"{uuid.uuid4()}.mp4")
            video.download(filename=temp_file)

            mp3_file = temp_file.replace(".mp4", ".mp3")
            audio_clip = AudioFileClip(temp_file)
            audio_clip.write_audiofile(mp3_file)
            audio_clip.close()
            os.remove(temp_file)

            return send_file(mp3_file, as_attachment=True)
        except Exception as e:
            return render_template("index.html", error=str(e))
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
