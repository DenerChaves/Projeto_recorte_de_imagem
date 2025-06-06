from services.converterPdf_img import converter_Pdf
from services.inferencia_images import inferencia
from services.inserir_assinatura_doc import InserirAssinnatura



# Executa o código do arquivo  
with open("interface.py") as f:
   exec(f.read())   

img = converter_Pdf("pdf_uploads/pdf_enviado") 

# Criando obejto para receber o caminho do PDF
caminho_da_img = img.converter_img()

# Criando objeto que vai realizar o recorte da assinatura na CNH 
recorte = inferencia("pdf_uploads\pdf_enviado.png") 

# Criando objeto que vai inserir a assinatura no documento
inserir_assinatura = InserirAssinnatura()
inserir_assinatura.inserir_assinatura() 