import os

def salvarTranscricao(texto, nomeArquivo = "Transcrição.txt", pastaDestino = "exports"):
    if not os.path.exists(pastaDestino):
      os.makedirs(pastaDestino)
      
    caminhoCompleto = os.path.join(pastaDestino, nomeArquivo)
    with open(caminhoCompleto, "w", encoding="utf-8") as f:
      f.write(texto)
      
    print(f"Transcrição salva em: {caminhoCompleto}")