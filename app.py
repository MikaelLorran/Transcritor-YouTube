import tkinter as tk
from tkinter import messagebox, ttk
from downloader import baixarAudio
from transcriber import transcreverAudio
from exporter import salvarTranscricao

def inicioProcessamento():
    url = entrada_url.get()
    if not url:
        messagebox.showwarning("Atenção", "Por favor, insira a URL do vídeo.")
        return
    
    try:
        progresso['value'] = 0
        label_status.config(text="Baixando áudio...")
        janela.update()

        caminho = baixarAudio(url)
        progresso['value'] = 33
        janela.update()

        label_status.config(text="Transcrevendo áudio...")
        janela.update()

        texto = transcreverAudio(caminho)
        progresso['value'] = 66
        janela.update()

        salvarTranscricao(texto)
        progresso['value'] = 100

        label_status.config(text = "Concluído!")
        messagebox.showinfo("Sucesso", "Transcrição concluída e salva com sucesso.")
    except Exception as e:
        messagebox.showerror("Erro", f"Ocorreu um erro: {str(e)}")

janela = tk.Tk()
janela.title("Transcritor de Vídeos do YouTube")
janela.geometry("500x200")

titulo = tk.Label(janela, text="Insira a URL do vídeo do YouTube:", font=("Arial", 12))
titulo.pack(pady=10)

entrada_url = tk.Entry(janela, width=60)
entrada_url.pack()

botao_processar = tk.Button(janela, text="Baixar e Transcrever", command=inicioProcessamento)
botao_processar.pack(pady=10)

progresso = ttk.Progressbar(janela, length=400, mode='determinate')
progresso.pack(pady=5)

label_status = tk.Label(janela, text="", font=("Arial", 10), fg="green")
label_status.pack()

janela.mainloop()