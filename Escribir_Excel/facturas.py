# Escribir en Hojas de Calculo Excel
# @docto_python
import xlsxwriter

def datos_usuario():
    print ("Itroducir los datos para facturar:")
    Nom = input ("Nombres:")
    ID  = int (input ("RUC/Cedula:"))
    Tel = int(input ("Telefono:"))
    Dir = input ("Direccion:")
    datos=(Nom, ID, Tel, Dir)
    return datos

def generar_archivo(datos):
    workbook = xlsxwriter.Workbook('datos.xlsx')
    worksheet = workbook.add_worksheet()
    worksheet.write('A1', 'Nombre:')
    worksheet.write('B1', datos[0])
    worksheet.write('A2', 'Cedula:')
    worksheet.write('B2', datos[1])
    worksheet.write('A3', 'Telefono:')
    worksheet.write('B3', datos[2])
    worksheet.write('A4', 'Direccion:')
    worksheet.write('B4', datos[3])
    workbook.close()

datos = datos_usuario()
generar_archivo(datos)
