import fitz
from pdf2image import convert_from_path

class InserirAssinnatura:
   def __init__(self):
      pass
   def inserir_assinatura(self):
      pdf = fitz.open("doc_real_infrator\Termo_Real_Infrator.pdf")
      pagina = pdf[0]
      imagem = "pdf_uploads/recortes/recorte_cnh.jpg"
      retangulo = fitz.Rect(72, 337, 300, 357)
      pagina.insert_image(retangulo, filename=imagem)
      
      # Salva o PDF editado
      pdf.save("documento_editado.pdf")
      pdf.close()
      caminho_pdf = 'C:/Users/dener/Documents/vscode/Programas _Python/aplicacao/documento_editado.pdf'
      paginas = convert_from_path(caminho_pdf, dpi=200)
      paginas[0].show()
      