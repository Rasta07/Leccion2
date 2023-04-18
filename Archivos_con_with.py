from ManejoArchivos import ManejoArchivos

#Manejo de contexto with: sintaxis simplificada, abre y cierra el  archivo
#with open("prueba.txt","r",encoding="utf8") as archivo:
 #   print(archivo.read())
#No hace falta  ni el try, nni el finally
# een el contexto de with lo que se ejecuta de manerra automatica
# utiliza diferentee metodos: __enter__ este es el que abre
#  ahora el siguiente metodo es el que cierra: __exit__

with ManejoArchivos("prueba.txt") as archivo:
    print(archivo.read())