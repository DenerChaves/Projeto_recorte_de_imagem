from ultralytics import YOLO
import cv2
import os


class inferencia:
    def __init__(self, img_convertida):
        self.img_convertida = img_convertida
        # Caminho do modelo
        self.model_path = 'detect/train4/weights/best.pt'
        #model_path = 'ProjetoRecorteCnh/Treinov10/runs/detect/train6/weights/best.pt'
        #model_path = 'runs/detect/train/weights/best.pt'

        # Verifica se o modelo existe
        if not os.path.exists(self.model_path):
            raise FileNotFoundError(f"Modelo não encontrado: {self.model_path}")
        
        # Carregar o modelo
        self.model = YOLO(self.model_path)

        # Verifica se a imagem existe
        if not os.path.exists(self.img_convertida):
            raise FileNotFoundError(f"Imagem não encontrada: {img_convertida}")

        # Realizar a predição e salvar resultados
        self.results = self.model.predict(source=self.img_convertida, save=True, save_txt=True)

        # Carregar a imagem original
        image = cv2.imread(self.img_convertida)

        # Criar diretório para salvar os recortes
        os.makedirs("pdf_uploads/recortes", exist_ok=True)

        # Processar os resultados
        for self.result in self.results:
            self.boxes = self.result.boxes  # Pegamos as bounding boxes detectadas

            for box in self.boxes:
                x1, y1, x2, y2 = map(int, box.xyxy[0])  # Coordenadas da bounding box
                conf = float(box.conf[0])  # Confiança da detecção
                cls = int(box.cls[0])  # Classe detectada

                # Nome da classe detectada
                class_name = self.model.names[cls] if hasattr(self.model, 'names') else f"classe_{cls}"
                label = f"{class_name}_{conf:.2f}"

                # Recortar o objeto detectado
                cropped_object = image[y1:y2, x1:x2]

                # limpar diretorio de recortes
            #caminho_arquivo = 'caminho/para/o/arquivo/recorte_cnh.jpg'
            #if os.path.exists(caminho_arquivo):
            #    os.remove(caminho_arquivo)
            #    print(f'Arquivo {caminho_arquivo} deletado com sucesso!')
            
            # Salvar a imagem recortada
            output_path = f"pdf_uploads/recortes/recorte_cnh.jpg"
            cv2.imwrite(output_path, cropped_object)
            print(f"Imagem salva em: {output_path}")
            #Mostrar a imagem recortada
            imagem_cinza = cv2.cvtColor(cropped_object, cv2.COLOR_BGR2GRAY)
            # 3. Aplicar threshold (binarização)
            imagem_pb = cv2.threshold(imagem_cinza, 127, 255, cv2.THRESH_BINARY)
            # Mostrar a imagem recortada
            #cv2.imshow(f"Recorte", cropped_object), cv2.waitKey(0), cv2.destroyAllWindows() 
            cv2.imshow(f"Recorte", imagem_cinza), cv2.waitKey(0), cv2.destroyAllWindows() 
                
                
            
            
    