from downloader import baixarAudio
from transcriber import transcreverAudio

def main():
    
    url = input("Cole a URL do vídeo do YouTube: ").strip()
    print("Baixando audio...")
    caminho = baixarAudio(url)
    
    print("\nTranscrevendo o áudio...")
    texto = transcreverAudio(caminho)
    
    print("\n Transcrição completa:")
    print(texto)
    
if __name__ == "__main__":
    main()