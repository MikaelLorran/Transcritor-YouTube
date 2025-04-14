import os
import yt_dlp
import uuid

def baixarAudio(url, pastaDestino = "downloads"):
    if not os.path.exists(pastaDestino):
        os.makedirs(pastaDestino)
    
    nomeArquivo = f"{uuid.uuid4()}"
    caminhoCompleto = os.path.join(pastaDestino, nomeArquivo)
    
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': caminhoCompleto,
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'ffmpeg_location': r'C:\ffmpeg\ffmpeg-7.1.1-full_build\bin\ffmpeg.exe',
        'quiet': False
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
    
    return caminhoCompleto + ".mp3"