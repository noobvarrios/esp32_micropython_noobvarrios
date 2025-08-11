from PIL import Image
import os

def convertir_pbm(ruta,size=(128,32)): 
    if not os.path.exists(ruta): 
        print("Archivo no encontrado: ",ruta)
        return

    img = Image.open(ruta).convert('1')
    img.thumbnail(size)

    img.save("neva_imagen.pbm", "PPM")

#!ejecucion 
if __name__ == "__main__": 
    ruta = "BlackBoxD1.bmp"
    convertir_pbm(ruta)