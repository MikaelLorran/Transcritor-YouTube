import os
import whisper

def transcreverAudio(arquivoAudio):
    
    if not os.path.exists(arquivoAudio):
        print(f"Erro: O arquivo {arquivoAudio} não foi encontrado.")
        return None
    
    model = whisper.load_model("base")
    print("Transcrevendo o áudio...")
    
    result = model.transcribe(arquivoAudio)
    print("Transcrição concluída!")
    
    return result['text']

if __name__ == "__main__":
    audioArquivo = "output/audio.webm"
    texto = transcreverAudio(audioArquivo)
    print(f"Texto transcrito: {texto}")
