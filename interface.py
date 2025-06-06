import tkinter as tk
from tkinter import filedialog
import shutil
import os

# Função para selecionar o arquivo PDF
def selecionar_pdf():
    # Abrir o diálogo de arquivos para selecionar apenas PDFs
    file_path = filedialog.askopenfilename(filetypes=[("All Files", "*.*"), ("PDF Files", "*.pdf")])
    
    if file_path:
        # Exibir o caminho do arquivo selecionado
        label_status.config(text=f"PDF selecionado: {file_path}")
        global pdf_selecionado  # Tornar o PDF selecionado global para usar em outras funções
        pdf_selecionado = file_path

# Função para enviar o PDF para a pasta da aplicação
def enviar_pdf():
    if pdf_selecionado:
        # Definir o diretório de destino (pasta dentro da aplicação)
        pasta_destino = "pdf_uploads"
        
        # Verificar se a pasta existe, caso contrário, cria a pasta
        if not os.path.exists(pasta_destino):
            os.makedirs(pasta_destino)  
        
        # Definir o nome do arquivo destino (podemos manter o nome original ou mudar)
        nome_arquivo_destino = os.path.join(pasta_destino, "pdf_enviado" + os.path.splitext(pdf_selecionado)[1])
        
        # Mover o arquivo para a pasta de destino
        shutil.copy(pdf_selecionado, nome_arquivo_destino)
        
        # Atualizar o status na interface
        label_status.config(text=f"PDF enviado para: {nome_arquivo_destino}")
    else:
        label_status.config(text="Nenhum PDF selecionado.")
    
    # Fechar a janela após enviar o PDF
    root.quit()

# Criar a janela principal
root = tk.Tk()
root.title("Upload de Imagem")
root.geometry("400x200")

# Label de status para mostrar mensagens
label_status = tk.Label(root, text="Nenhum Imagem selecionado.")
label_status.pack(pady=10)

# Botão para selecionar o Imagem
button_selecionar = tk.Button(root, text="Seleciona Imagem", command=selecionar_pdf)
button_selecionar.pack(pady=10)

# Botão para enviar o Imagem para a pasta
button_enviar = tk.Button(root, text="Enviar Imagem", command=enviar_pdf)
button_enviar.pack(pady=10)

# Variável global para armazenar o caminho do Imagem selecionado
pdf_selecionado = ""

# Rodar a interface
root.mainloop()
