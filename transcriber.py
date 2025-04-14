import whisper

def transcreverAudio(arquivoAudio):
      
    modelo = whisper.load_model("base")
    resultado = modelo.transcribe(arquivoAudio)
    
    return resultado['text']
