print("Bienvenido a la carniceria La estrella \n Celebrando el dia internacional de la mujer "
      "tenemos los siguientes decuentos esta semana\n Tras realizar la compras de productos que superen el peso de tres libras "
      "se le otorgara los siguientes decuentos \n De 3.1 a 4 libras usted contara con un 5% de descuento "
      "\n De 4.1 a 5 libras usted contrara con un decuento de 10% de descuento \n De 5 a 10 libras usted contara"
      "con un descuento de 15% de descuento")


Elementos = {"1. Costillas de cerdo" : 164 , "2. Costillas de res": 140, "3. alas de pollo" : 110,
             "4. longaniza de cerdo" : 100, "5. filete de pechuga de pollo" : 150 }



print(Elementos)



art = int(input("Coloque el articulo que desea: "))


descuento = ()

if  art ==1:
        art = Elementos["1. Costillas de cerdo"]

if art == 2:
    art = Elementos["2. Costillas de res"]

if art == 3:
    art = Elementos["3. alas de pollo"]

if art ==4:
    art = Elementos["4. longaniza de cerdo"]

if art ==5:
    art = ["5. filete de pechuga de pollo"]


libras = input("¿Cuantas libras desea? ")

if "." in libras:
    libras = float(libras)
else:
    libras = int(libras)


if libras > 3.0 and libras < 4.1:
    descuento = art*5/100
    print("Aplicando el descuento usted paga", art-descuento)

elif libras > 4.0 and libras < 5.1:
    descuento = art*10/100
    print("Aplicando el descuento usted paga", art-descuento)

elif libras > 5.0:
    descuento = art*15/100
    print("Aplicando el descuento usted paga", art-descuento)

else:
    print("Usted paga", art)

    