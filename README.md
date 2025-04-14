# 🎙️ Transcritor de Vídeos do YouTube

Este projeto permite baixar o áudio de vídeos do YouTube e transcrevê-los automaticamente utilizando Python. A transcrição é salva em um arquivo `.txt`.

## ✅ Funcionalidades

- Baixar o áudio de vídeos do YouTube em MP3
- Transcrever o áudio automaticamente usando inteligência artificial
- Salvar a transcrição em um arquivo `.txt`
- Interface gráfica simples com barra de progresso

## 🧰 Tecnologias utilizadas

- Python 3.11+
- [yt-dlp](https://github.com/yt-dlp/yt-dlp)
- [Whisper](https://github.com/openai/whisper)
- FFmpeg
- Tkinter (interface gráfica)

## 🧠 Como usar

1. Clone este repositório:

   ```
   git clone https://github.com/seu-usuario/transcritor-youtube.git
   cd transcritor-youtube
   ```

2. Instale as dependências:

   ```
   pip install -r requirements.txt
   ```

3. Verifique se o FFmpeg está instalado e adicionado ao PATH. Ou indique manualmente o caminho no arquivo `downloader.py`.

4. Execute o aplicativo:

   ```
   python app.py
   ```

## 📁 Estrutura do projeto

```
transcritor-youtube/
│
├── app.py                # Interface gráfica
├── downloader.py         # Função de download do YouTube
├── transcriber.py        # Transcrição com Whisper
├── exporter.py           # Salvamento da transcrição em .txt
├── requirements.txt      # Dependências do projeto
└── downloads/            # Áudios baixados
└── exports/              # Transcrições geradas
```

## 📦 Exemplo de uso

1. Insira a URL de um vídeo do YouTube.
2. Clique em **"Baixar e Transcrever"**.
3. A transcrição será salva automaticamente na pasta `exports/`.
