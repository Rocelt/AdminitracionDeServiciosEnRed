import re
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas

def export_to_pdf(tabla,sistema, nombre, contacto, ubicacion, numInterfaces):
    c = canvas.Canvas(nombre+".pdf", pagesize=A4)
    text = c.beginText(50,800)
    text.setFont("Times-Roman", 20)
    text.textLine("ADMINISTRACIÓN DE SERVICION EN RED")
    text.textLine("Práctica 1")
    text.textLine("Andrés Vanegas García    4CM14")
    #text.setFont("Times-Roman",'', 14)
    text.setFont("Times-Roman", 14)
    text.textLine("Sistema :")
    #text.setFont("Times-Roman", 10)
    print(sistema)
    text.textLine(sistema)
    #text.setFont("Times-Roman",'', 14)
    text.textLine("Nombre Dispositivo :")
    #text.setFont("Times-Roman", 14)
    text.textLine(nombre)
    #text.setFont("Times-Roman",'', 14)
    text.textLine("Contacto :")
    #text.setFont("Times-Roman", 14)
    text.textLine(contacto)
    #text.setFont("Times-Roman",'', 14)
    text.textLine("Ubicacion :")
    #text.setFont("Times-Roman", 14)
    text.textLine(ubicacion)
    text.textLine("Numero de Interfaces")
    #text.setFont("Times-Roman", 14)
    text.textLine(str(numInterfaces))
    #text.setFont("Times-Roman",'', 16)
    text.textLine("")
    text.textLine("Interfaz - Estado")
    #text.setFont("Times-Roman", 14)
    for i in range(0,len(tabla)):
        text.textLine(tabla[i][0]+'  -  '+str(tabla[i][1]))
    c.drawText(text)
    if re.search('Windows',sistema):

        c.drawImage("windows.png", 400, 500, width=180, height=180)
    else:
        c.drawImage("ubuntu.png", 400, 500, width=180, height=180)
    c.save()
    print('Pdf generado')

    

#export_to_pdf('hola','soy el sistema','2','3','3','5')
