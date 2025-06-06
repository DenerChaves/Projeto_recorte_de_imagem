from pdf2image import convert_from_path
import os

class converter_Pdf:
    def __init__(self, img):
        self.img = img
        #self.images = convert_from_path(self.img, dpi=300) 

    def converter_img(self):
    # Caminho do seu PDF
        #pdf_path = "images_para_converter/cnh (1).pdf"
    
        # Verifica se o arquivo existe
        if not os.path.exists(self.img):
            print(f"Arquivo {self.img} não encontrado.")
            return
        else:
            # Converter o PDF para imagens (dpi alto para manter a qualidade)
            if self.img.endswith('.pdf'):
                self.imag= convert_from_path(self.img, dpi=300)

            # Salvar as imagens em arquivos separados
            os.makedirs("pdf_uploads/pdf_convertido", exist_ok=True)
            for i, image in enumerate(self.img):
                image.save(f"pdf_uploads/pdf_convertido/pdf_enviado.png", "PNG")

                print("Conversão concluída!")

        return f"pdf_uploads/pdf_convertido/pdf_enviado.png"
