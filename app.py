# -*- coding: utf-8 -*-

from pytube import YouTube
from moviepy.editor import AudioFileClip
import os

def descargar_video_y_convertir_mp3(url, carpeta_salida="downloads"):
    # Crear carpeta de salida si no existe
    if not os.path.exists(carpeta_salida):
        os.makedirs(carpeta_salida)

    print("Descargando video...")
    yt = YouTube(url)
    video = yt.streams.filter(only_audio=True).first()

    archivo_video = video.download(output_path=carpeta_salida)
    print(f"Video descargado en: {archivo_video}")

    # Crear ruta del archivo MP3
    archivo_mp3 = os.path.splitext(archivo_video)[0] + ".mp3"

    print("Convirtiendo a MP3...")
    audio_clip = AudioFileClip(archivo_video)
    audio_clip.write_audiofile(archivo_mp3)
    audio_clip.close()

    # Opcional: eliminar el archivo de audio original (formato webm o mp4)
    os.remove(archivo_video)

    print(f"Archivo MP3 guardado en: {archivo_mp3}")

if __name__ == "__main__":
    url = input("Introduce la URL del video de YouTube: ").strip()
    descargar_video_y_convertir_mp3(url)
