import os
import whisper

def transcreverAudio(arquivoAudio):
   
    print(f"Transcrevendo: {arquivoAudio}")
    
    if not os.path.exists(arquivoAudio):
        raise FileNotFoundError(f"O arquivo não foi encontrado: {arquivoAudio}")
    modelo = whisper.load_model("base")
    resultado = modelo.transcribe(arquivoAudio)
    
    return resultado['text']
