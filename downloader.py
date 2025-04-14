import yt_dlp

def baixarAudio(url):
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': 'output/audio.%(ext)s',
        'noplaylist': True,
        'quiet': False,
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
            print("Áudio baixado com sucesso.")
    except Exception as e:
        print(f"Erro ao baixar o vídeo: {e}")
