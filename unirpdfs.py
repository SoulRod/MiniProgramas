from PyPDF2 import PdfFileMerger
import os

os.chdir("C:/Users/Rodrigo Morales/Desktop/kk")     # Rodrigo : Le asigno un nuevo puesto de trabajo, en este caso una carpeta en el escritorio llamado kk 
print("Mi puesto de trabajo ", os.getcwd())         # Rodrigo : Lo dejo para saber donde me encuentro trabajando actualmente

pdfs = [archivo for archivo in os.listdir('./') if archivo.endswith(".pdf")]
nombre_archivo_salida = "ArchivoFinal.pdf"
fusionador = PdfFileMerger()

for pdf in pdfs:
    fusionador.append(open(pdf, 'rb'))

with open(nombre_archivo_salida, 'wb') as salida:
    fusionador.write(salida)