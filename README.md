# Transcriber YouTube

Este projeto é um transcritor de vídeos do YouTube utilizando Python. O objetivo é baixar o áudio de um vídeo do YouTube e gerar uma transcrição do áudio em formato de texto. O projeto utiliza as bibliotecas `yt-dlp` para o download do áudio e o modelo `whisper` da OpenAI para a transcrição.

## Descrição

O **Transcriber YouTube** permite que você baixe o áudio de vídeos do YouTube e converta-o automaticamente em texto, útil para legendas, transcrições e outras aplicações.

## Funcionalidades

- Baixar áudio de vídeos do YouTube (suporta formatos `webm`).
- Transcrever áudio utilizando o modelo Whisper da OpenAI.
- Fácil de configurar e usar.

## Tecnologias Usadas

- **Python**: Linguagem de programação principal.
- **yt-dlp**: Biblioteca para baixar vídeos e áudios do YouTube.
- **Whisper**: Modelo de transcrição de áudio para texto da OpenAI.
- **ffmpeg**: Utilizado pelo Whisper para processar o áudio.

## Pré-requisitos

- Python 3.7 ou superior.
- ffmpeg instalado e configurado no PATH do sistema.

## Instalação

### Passo 1: Clonar o repositório

No terminal, execute o seguinte comando para clonar o repositório:

git clone https://github.com/seu-usuario/youtube-transcriber.git
cd youtube-transcriber

### Passo 2: Criar e ativar um ambiente virtual (opcional, mas recomendado)

Crie um ambiente virtual para instalar as dependências:

python -m venv venv
Ative o ambiente virtual:

Windows: venv\Scripts\activate

Linux/Mac: source venv/bin/activate

### Passo 3: Instalar as dependências

Com o ambiente virtual ativado, instale as dependências necessárias:

pip install -r requirements.txt
As dependências são:

yt-dlp: Para baixar o áudio do YouTube.

whisper: Para transcrever o áudio.

ffmpeg: Para processar arquivos de áudio.

### Passo 4: Instalar o FFmpeg

O FFmpeg é necessário para processar o áudio. Siga os passos abaixo para instalá-lo:

Baixe o FFmpeg em https://ffmpeg.org/download.html.

Extraia o conteúdo do arquivo ZIP.

Adicione o caminho da pasta bin do FFmpeg ao PATH do sistema.

### Passo 5: Rodar o programa

Após instalar as dependências, você pode rodar o programa. No terminal, execute o seguinte comando:

python transcriber.py <URL do vídeo do YouTube>
Exemplo:

python transcriber.py https://www.youtube.com/watch?v=dQw4w9WgXcQ
O programa fará o seguinte:

Baixará o áudio do vídeo em formato .webm.

Usará o Whisper para transcrever o áudio em texto.

Exibirá a transcrição no terminal.

### Passo 6: Verifique a transcrição

A transcrição será exibida diretamente no terminal, ou você pode modificá-lo para salvar a transcrição em um arquivo .txt caso prefira.
