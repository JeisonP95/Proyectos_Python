#Venta tecnologia apple desde la tienda fisica
#Programa para el asesor comercial de ventas

#Listas
compras = []
price = []
op = 0
#tuplas
#computadores
comp = (
    "Macbook pro 13 256gb ssd" ,
    "Macbook pro 13 512gb ssd" ,
    "Macbook pro 14 512gb ssd, 16gb ram" ,
    "Macbook pro 14 1tb ssd, 32gb ram" ,
    "Macbook pro 16 512gb ssd" ,
    "Macbook pro 16 1tb ssd" ,
)
compValue = (
    4999000,
    9299000,
    12949000,
    13500000,
    14100000,
    13899000
)
#celulares
cel = (
    "Iphone 11 de 64gb", 
    "Iphone 11 de 128gb", 
    "Iphone 13 de 128gb", 
    "Iphone 13 de 256gb", 
    "Iphone 14 de 128gb", 
    "Iphone 14 de 256gb", 
    )
celvalue = (
    2279000, 
    2579000, 
    3669000, 
    4269000, 
    4949000, 
    5569000
    )
colr = (
    "rojo",
    "plata", 
    "negro espacial", 
    "negro", 
    "dorado", 
    "blanco"
    )
#ipads
ipds = ("Ipad cuarta generacion 256gb", 
        "Ipad cuarta generacion 512gb", 
        "Ipad novena generacion 64gb", 
        "Ipad novena generacion 256gb", 
        "Ipad decima generacion 64gb", 
        "Ipad decima generacion 256gb" 
    )
ipdsvalue = (5719000, 
             6889000, 
             2039000, 
             2899000, 
             2639000, 
             3499000,
    )
colrip = ("rosa", 
          "plata", 
          "gris espacial", 
          "amarillo", 
          "azul", 
          "blanco estrella"
    )
#cargadores
charger = (
    "Cargador Macbook pro.",
    "Cargador Macbook air.",
    "Cable carga magnetica.", 
    "Adaptador corriente usb."
) 
changerValue= (
    519000,
    499000,
    159000,
    429000
)
#airpds
airpds = (
    "Airpods segunda generacion.",
    "Airpods tercera generacion.",
    "Airpods witch charging case."
)
airpdsValue = (
    1389000,
    999000,
    749000
)
#Menu principal
while op != 6:
    print("Menu de tecnologia apple")
    print("1. Computadores")
    print("2. Celulares")
    print("3. Ipads")
    print("4. Cargadores")
    print("5. AirPods")
    print("6. Salir e imprimir factura")    
    #
    try:
        op = int(input("Ingrese la opción disponible: ")) 
    except ValueError:
        print(" !Ingrese la opción disponible¡ ")
    #computadores
    if op == 1:
        opc = 0
        while opc != 7:
         print("1. ", comp[0], "su valor es:", compValue[0])
         print("2. ", comp[1], "su valor es:", compValue[1])
         print("3. ", comp[2], "su valor es:", compValue[2])
         print("4. ", comp[3], "su valor es:", compValue[3])
         print("5. ", comp[4], "su valor es:", compValue[4])
         print("6. ", comp[5], "su valor es:", compValue[5])
         print("7. Salir de computadoras")
         try:
            opc = int(input("Ingrese la opción disponible: ")) 
         except ValueError:
            print(" !Ingrese la opción disponible¡ ")
         
         if opc == 1:
             showComp1 = comp[0] + "su precio es:" + str(compValue[0])
             compras.append(showComp1)
             price.append(compValue[0])
             opc = 7
         elif opc == 2:
             showComp2 = comp[1] + "su precio es:" + str(compValue[1])
             compras.append(showComp2)
             price.append(compValue[1])
             opc = 7
         elif opc == 3:
             showComp3 = comp[2] + "su precio es:" + str(compValue[2])
             compras.append(showComp3)
             price.append(compValue[2])
             opc = 7
         elif opc == 4:
             showComp4 = comp[3] + "su precio es:" + str(compValue[3])
             compras.append(showComp4)
             price.append(compValue[3])
             opc = 7
         elif opc == 5:
             showComp5 = comp[4] + "su precio es:" + str(compValue[4])
             compras.append(showComp5)
             price.append(compValue[4])
             opc = 7
         elif opc == 6:
             showComp6 = comp[5] + "su precio es:" + str(compValue[5])
             compras.append(showComp6)
             price.append(compValue[5])
             opc = 7
    #celulares         
    elif op == 2:
        opc2 = 0
        while opc2 != 7:
         print("1.", cel[0], "su precio es:", celvalue[0])
         print("2.", cel[1], "su precio es:", celvalue[1])
         print("3.", cel[2], "su precio es:", celvalue[2])
         print("4.", cel[3], "su precio es:", celvalue[3])
         print("5.", cel[4], "su precio es:", celvalue[4])
         print("6.", cel[5], "su precio es:", celvalue[5])
         print("7. Salir de celulares")
         try:
            opc2 = int(input("Ingrese la opción disponible: ")) 
         except ValueError:
            print(" !Ingrese la opción disponible¡ ")
         #Iphone 11 de 64gb.
         if opc2 == 1:
          opCel1 = 0
          while opCel1 != 7:
              print("1", colr[0])
              print("2", colr[1])
              print("3", colr[2])
              print("4", colr[3])
              print("5", colr[4])
              print("6", colr[5])
              print("7 Salir")
              try:
               opCel1 = int(input("Ingrese la opción disponible: ")) 
              except ValueError:
               print(" !Ingrese la opción disponible¡ ")
              #Color Iphone 11 de 64gb.
              if opCel1 == 1:
                  showCel1 = cel[0] + " con color "+ colr[0] +" su precio es: " + str(celvalue[0])
                  compras.append(showCel1)
                  price.append(celvalue[0])
                  opCel1 = 7
                  opc2 = 7 
              elif opCel1 == 2:
                  showCel2 = cel[0] + " con color "+ colr[1] +" su precio es: " + str(celvalue[0])
                  compras.append(showCel2)
                  price.append(celvalue[0])
                  opCel1 = 7
                  opc2 = 7 
              elif opCel1 == 3:
                  showCel3 = cel[0] + " con color "+ colr[2] +" su precio es: " + str(celvalue[0])
                  compras.append(showCel3)
                  price.append(celvalue[0])
                  opCel1 = 7
                  opc2 = 7 
              elif opCel1 == 4:
                  showCel4 = cel[0] + " con color "+ colr[3] +" su precio es: " + str(celvalue[0])
                  compras.append(showCel4)
                  price.append(celvalue[0])
                  opCel1 = 7
                  opc2 = 7 
              elif opCel1 == 5:                  
                  showCel5 = cel[0] + " con color "+ colr[4] +" su precio es: " + str(celvalue[0])
                  compras.append(showCel5)
                  price.append(celvalue[0]) 
                  opCel1 = 7
                  opc2 = 7
              elif opCel1 == 6:
                  showCel6 = cel[0] + " con color "+ colr[5] +" su precio es: " + str(celvalue[0])
                  compras.append(showCel6)
                  price.append(celvalue[0]) 
                  opCel1 = 7
                  opc2 = 7
          
         #Iphone 11 de 128gb.         
         elif opc2 == 2:
          opCel2 = 0
          while opCel2 != 7:
              print("1.", colr[0])
              print("2.", colr[1])
              print("3.", colr[2])
              print("4.", colr[3])
              print("5.", colr[4])
              print("6.", colr[5])
              print("7. Salir")
              try:
               opCel2 = int(input("Ingrese la opción disponible: ")) 
              except ValueError:
               print(" !Ingrese la opción disponible¡ ")
              #Color Iphone 11 de 128gb.
              if opCel2 == 1:
                  shoCell1 = cel[1] + " Con color: " + colr[0] + " Su precio es: " + str(celvalue[1])
                  compras.append(shoCell1)
                  price.append(celvalue[1])
                  opCel2 = 7
                  opc2 = 7
              elif opCel2 == 2:
                  shoCell2 = cel[1] + " Con color: " + colr[1] + " Su precio es: " + str(celvalue[1])
                  compras.append(shoCell2)
                  price.append(celvalue[1])
                  opCel2 = 7
                  opc2 = 7
              elif opCel2 == 3:
                  shoCell3 = cel[1] + " Con color: " + colr[2] + " Su precio es: " + str(celvalue[1])
                  compras.append(shoCell3)
                  price.append(celvalue[1])
                  opCel2 = 7
                  opc2 = 7
              elif opCel2 == 4:
                  shoCell4 = cel[1] + " Con color: " + colr[3] + " Su precio es: " + str(celvalue[1])
                  compras.append(shoCell4)
                  price.append(celvalue[1])
                  opCel2 = 7
                  opc2 = 7    
              elif opCel2 == 5:
                  shoCell5 = cel[1] + " Con color: " + colr[4] + " Su precio es: " + str(celvalue[1])
                  compras.append(shoCell5)
                  price.append(celvalue[1])
                  opCel2 = 7
                  opc2 = 7 
              elif opCel2 == 6:
                  shoCell6 = cel[1] + " Con color: " + colr[5] + " Su precio es: " + str(celvalue[1])
                  compras.append(shoCell6)
                  price.append(celvalue[1])
                  opCel2 = 7
                  opc2 = 7 
         #Iphone 13 de 128gb.        
         elif opc2 == 3:
             opCel3 = 0
             while opCel3 != 7:
                 print("1.", colr[0])
                 print("2.", colr[1])
                 print("3.", colr[2])
                 print("4.", colr[3])
                 print("5.", colr[4])
                 print("6.", colr[5])
                 print("7. Salir")
                 try:
                  opCel3 = int(input("Ingrese la opción disponible: ")) 
                 except ValueError:
                    print(" !Ingrese la opción disponible¡ ")
                 if opCel3 == 1:
                     shoCelll1 = cel[2] + " Con color: " + colr[0] + " Su precio es: " + str(celvalue[2])
                     compras.append(shoCelll1)
                     price.append(celvalue[2])
                     opCel3 = 7
                     opc2 = 7
                 elif opCel3 == 2:
                     shoCelll2 = cel[2] + " Con color: " + colr[1] + " Su precio es: " + str(celvalue[2])
                     compras.append(shoCelll2)
                     price.append(celvalue[2])
                     opCel3 = 7
                     opc2 = 7
                 elif opCel3 == 3:
                     shoCelll3 = cel[2] + " Con color: " + colr[2] + " Su precio es: " + str(celvalue[2])
                     compras.append(shoCelll3)
                     price.append(celvalue[2])
                     opCel3 = 7
                     opc2 = 7
                 elif opCel3 == 4:
                     shoCelll4 = cel[2] + " Con color: " + colr[3] + " Su precio es: " + str(celvalue[2])
                     compras.append(shoCelll4)
                     price.append(celvalue[2])
                     opCel3 = 7
                     opc2 = 7  
                 elif opCel3 == 5:
                     shoCelll5 = cel[2] + " Con color: " + colr[4] + " Su precio es: " + str(celvalue[2])
                     compras.append(shoCelll5)
                     price.append(celvalue[2])
                     opCel3 = 7
                     opc2 = 7
                 elif opCel3 == 6:
                     shoCelll6 = cel[2] + " Con color: " + colr[5] + " Su precio es: " + str(celvalue[2])
                     compras.append(shoCelll6)
                     price.append(celvalue[2])
                     opCel3 = 7
                     opc2 = 7 
         #Iphone 13 de 256gb.                     
         elif opc2 == 4:
             opCel4 = 0;
             while opCel4 != 7:
                 print("1.", colr[0])
                 print("2.", colr[1])
                 print("3.", colr[2])
                 print("4.", colr[3])
                 print("5.", colr[4])
                 print("6.", colr[5])
                 print("7. Salir")
                 try:
                  opCel4 = int(input("Ingrese la opción disponible: ")) 
                 except ValueError:
                  print(" !Ingrese la opción disponible¡ ")
                #Iphone 13 de 256gb.
                 if opCel4 == 1:
                     shoCeelll1 = cel[3] + " Con color: " + colr[0] + " Su precio es: " + str(celvalue[3])
                     compras.append(shoCeelll1)
                     price.append(celvalue[3])
                     opCel4 = 7
                     opc2 = 7
                 elif opCel4 == 2:
                     shoCeelll2 = cel[3] + " Con color: " + colr[1] + " Su precio es: " + str(celvalue[3])
                     compras.append(shoCeelll2)
                     price.append(celvalue[3])
                     opCel4 = 7
                     opc2 = 7
                 elif opCel4 == 3:
                     shoCeelll3 = cel[3] + " Con color: " + colr[2] + " Su precio es: " + str(celvalue[3])
                     compras.append(shoCeelll3)
                     price.append(celvalue[3])
                     opCel4 = 7
                     opc2 = 7
                 elif opCel4 == 4:
                     shoCeelll4 = cel[3] + " Con color: " + colr[3] + " Su precio es: " + str(celvalue[3])
                     compras.append(shoCeelll4)
                     price.append(celvalue[3])
                     opCel4 = 7
                     opc2 = 7  
                 elif opCel4 == 5:
                     shoCeelll5 = cel[3] + " Con color: " + colr[4] + " Su precio es: " + str(celvalue[3])
                     compras.append(shoCeelll5)
                     price.append(celvalue[3])
                     opCel4 = 7
                     opc2 = 7
                 elif opCel4 == 6:
                     shoCeelll6 = cel[3] + " Con color: " + colr[5] + " Su precio es: " + str(celvalue[3])
                     compras.append(shoCeelll6)
                     price.append(celvalue[3])
                     opCel4 = 7
                     opc2 = 7 
         #Iphone 14 de 128gb. 
         elif opc2 == 5:
             opCel5 = 0;
             while opCel5 != 7:
                 print("1.", colr[0])
                 print("2.", colr[1])
                 print("3.", colr[2])
                 print("4.", colr[3])
                 print("5.", colr[4])
                 print("6.", colr[5])
                 print("7. Salir")
                 try:
                  opCel5 = int(input("Ingrese la opción disponible: ")) 
                 except ValueError:
                  print(" !Ingrese la opción disponible¡ ")
                 #Color Iphone 14 de 128gb.
                 if opCel5 == 1:
                     shooCeelll1 = cel[4] + " Con color: " + colr[0] + " Su precio es: " + str(celvalue[4])
                     compras.append(shooCeelll1)
                     price.append(celvalue[4])
                     opCel5 = 7
                     opc2 = 7
                 elif opCel5 == 2:
                     shooCeelll2 = cel[4] + " Con color: " + colr[1] + " Su precio es: " + str(celvalue[4])
                     compras.append(shooCeelll2)
                     price.append(celvalue[4])
                     opCel5 = 7
                     opc2 = 7
                 elif opCel5 == 3:
                     shooCeelll3 = cel[4] + " Con color: " + colr[2] + " Su precio es: " + str(celvalue[4])
                     compras.append(shooCeelll3)
                     price.append(celvalue[4])
                     opCel5 = 7
                     opc2 = 7
                 elif opCel5 == 4:
                     shooCeelll4 = cel[4] + " Con color: " + colr[3] + " Su precio es: " + str(celvalue[4])
                     compras.append(shooCeelll4)
                     price.append(celvalue[4])
                     opCel5 = 7
                     opc2 = 7  
                 elif opCel5 == 5:
                     shooCeelll5 = cel[4] + " Con color: " + colr[4] + " Su precio es: " + str(celvalue[4])
                     compras.append(shooCeelll5)
                     price.append(celvalue[4])
                     opCel5 = 7
                     opc2 = 7
                 elif opCel5 == 6:
                     shooCeelll6 = cel[4] + " Con color: " + colr[5] + " Su precio es: " + str(celvalue[4])
                     compras.append(shooCeelll6)
                     price.append(celvalue[4])
                     opCel5= 7
                     opc2 = 7 
         #Iphone 14 de 256gb. 
         elif opc2 == 6:
             opCel6 = 0;  
             while opCel6 != 7:
                 print("1.", colr[0])
                 print("2.", colr[1])
                 print("3.", colr[2])
                 print("4.", colr[3])
                 print("5.", colr[4])
                 print("6.", colr[5])
                 print("7. Salir")
                 try:
                  opCel6 = int(input("Ingrese la opción disponible: ")) 
                 except ValueError:
                  print(" !Ingrese la opción disponible¡ ")
                 #Color Iphone 14 de 256gb.
                 if opCel6 == 1:
                     shhoCeelll1 = cel[5] + " Con color: " + colr[0] + " Su precio es: " + str(celvalue[5])
                     compras.append(shhoCeelll1)
                     price.append(celvalue[5])
                     opCel6 = 7
                     opc2 = 7
                 elif opCel6 == 2:
                     shhoCeelll2 = cel[5] + " Con color: " + colr[1] + " Su precio es: " + str(celvalue[5])
                     compras.append(shhoCeelll2)
                     price.append(celvalue[5])
                     opCel6 = 7
                     opc2 = 7
                 elif opCel6 == 3:
                     shhoCeelll3 = cel[5] + " Con color: " + colr[2] + " Su precio es: " + str(celvalue[5])
                     compras.append(shhoCeelll3)
                     price.append(celvalue[5])
                     opCel6 = 7
                     opc2 = 7
                 elif opCel6 == 4:
                     shhoeelll4 = cel[5] + " Con color: " + colr[3] + " Su precio es: " + str(celvalue[5])
                     compras.append(shhoeelll4)
                     price.append(celvalue[5])
                     opCel6 = 7
                     opc2 = 7  
                 elif opCel6 == 5:
                     shhoCeelll5 = cel[5] + " Con color: " + colr[4] + " Su precio es: " + str(celvalue[5])
                     compras.append(shhoCeelll5)
                     price.append(celvalue[5])
                     opCel6 = 7
                     opc2 = 7
                 elif opCel6 == 6:
                     shhoCeelll6 = cel[5] + " Con color: " + colr[5] + " Su precio es: " + str(celvalue[5])
                     compras.append(shhoCeelll6)
                     price.append(celvalue[5])
                     opCel6 = 7
                     opc2 = 7         
    #ipads        
    elif op == 3: 
        opc3 = 0
        while opc3 != 7:
           print("1.", ipds[0], " Su precio es:", ipdsvalue[0])
           print("2.", ipds[1], " Su precio es:", ipdsvalue[1])
           print("3.", ipds[2], " Su precio es:", ipdsvalue[2])
           print("4.", ipds[3], " Su precio es:", ipdsvalue[3])
           print("5.", ipds[4], " Su precio es:", ipdsvalue[4])
           print("6.", ipds[5], " Su precio es:", ipdsvalue[5])
           print("7. Salir de IpadS") 
           try:
               opc3 = int(input("Ingrese la opción disponible: ")) 
           except ValueError:
               print(" !Ingrese la opción disponible¡ ")
           #Ipad cuarta generacion 256gb.
           if opc3 == 1:
            opIpds1 = 0
            while opIpds1 != 7:
              print("1.", colrip[0])
              print("2.", colrip[1])
              print("3.", colrip[2])
              print("4.", colrip[3])
              print("5.", colrip[4])
              print("6.", colrip[5])
              print("7. Salir ")
              try:
               opIpds1 = int(input("Ingrese la opción disponible: ")) 
              except ValueError:
               print(" !Ingrese la opción disponible¡ ")
              #Colores Ipad cuarta generacion 256gb
              if opIpds1 == 1:
                  showipds1 = ipds[0] + " Con color " + colrip[0] + "Su precio es " + str(ipdsvalue[0])
                  compras.append(showipds1)
                  price.append(ipdsvalue[0])
                  opIpds1 = 7
                  opc3 = 7
              elif opIpds1 == 2:
                  showipds2 = ipds[0] + " Con color " + colrip[1] + "Su precio es " + str(ipdsvalue[0])
                  compras.append(showipds2)
                  price.append(ipdsvalue[0])
                  opIpds1 = 7
                  opc3 = 7               
              elif opIpds1 == 3:
                  showipds3 = ipds[0] + " Con color " + colrip[2] + "Su precio es " + str(ipdsvalue[0])
                  compras.append(showipds3)
                  price.append(ipdsvalue[0])
                  opIpds1 = 7
                  opc3 = 7
              elif opIpds1 == 4:
                  showipds4 = ipds[0] + " Con color " + colrip[3] + "Su precio es " + str(ipdsvalue[0])
                  compras.append(showipds4)
                  price.append(ipdsvalue[0])
                  opIpds1 = 7
                  opc3 = 7
              elif opIpds1 == 5:
                  showipds5 = ipds[0] + " Con color " + colrip[4] + "Su precio es " + str(ipdsvalue[0])
                  compras.append(showipds5)
                  price.append(ipdsvalue[0])
                  opIpds1 = 7
                  opc3 = 7
              elif opIpds1 == 6:
                  showipds6 = ipds[0] + " Con color " + colrip[5] + "Su precio es " + str(ipdsvalue[0])
                  compras.append(showipds6)
                  price.append(ipdsvalue[0])
                  opIpds1 = 7
                  opc3 = 7
           # Ipad cuarta generacion 512gb.        
           elif opc3 == 2:
            opIpdss1 = 0
            while opIpdss1 != 7:
              print("1.", colrip[0])
              print("2.", colrip[1])
              print("3.", colrip[2])
              print("4.", colrip[3])
              print("5.", colrip[4])
              print("6.", colrip[5])
              print("7. Salir ")
              try:
               opIpdss1 = int(input("Ingrese la opción disponible: ")) 
              except ValueError:
               print(" !Ingrese la opción disponible¡ ")
              #Colores Ipad cuarta generacion 512gb
              if opIpdss1 == 1:
                  showipdss1 = ipds[1] + " Con color " + colrip[0] + " Su precio es " + str(ipdsvalue[1])
                  compras.append(showipdss1)
                  price.append(ipdsvalue[1])
                  opIpdss1 = 7
                  opc3 = 7
              elif opIpdss1 == 2:
                  showipdss2 = ipds[1] + " Con color " + colrip[1] + " Su precio es " + str(ipdsvalue[1])
                  compras.append(showipdss2)
                  price.append(ipdsvalue[1])
                  opIpdss1 = 7
                  opc3 = 7       
              elif opIpdss1 == 3:
                  showipdss3 = ipds[1] + " Con color " + colrip[2] + " Su precio es " + str(ipdsvalue[1])
                  compras.append(showipdss3)
                  price.append(ipdsvalue[1])
                  opIpdss1 = 7
                  opc3 = 7
              elif opIpdss1 == 4:
                  showipdss4 = ipds[1] + " Con color " + colrip[3] + " Su precio es " + str(ipdsvalue[1])
                  compras.append(showipdss4)
                  price.append(ipdsvalue[1])
                  opIpdss1 = 7
                  opc3 = 7
              elif opIpdss1 == 5:
                  showipdss5 = ipds[1] + " Con color " + colrip[4] + " Su precio es " + str(ipdsvalue[1])
                  compras.append(showipdss5)
                  price.append(ipdsvalue[1])
                  opIpdss1 = 7
                  opc3 = 7
              elif opIpdss1 == 6:
                  showipdss6 = ipds[1] + " Con color " + colrip[5] + " Su precio es " + str(ipdsvalue[1])
                  compras.append(showipdss6)
                  price.append(ipdsvalue[1])
                  opIpdss1 = 7
                  opc3 = 7
           #Ipad novena generacion 64gb.
           elif opc3 == 3:
            opIpdsss1 = 0
            while opIpdsss1 != 7:
              print("1.", colrip[0])
              print("2.", colrip[1])
              print("3.", colrip[2])
              print("4.", colrip[3])
              print("5.", colrip[4])
              print("6.", colrip[5])
              print("7. Salir ")
              try:
               opIpdsss1 = int(input("Ingrese la opción disponible: ")) 
              except ValueError:
               print(" !Ingrese la opción disponible¡ ")
              #Colores Ipad novena generacion 64gb.
              if opIpdsss1 == 1:
                  showipdsss1 = ipds[2] + " Con color " + colrip[0] + " Su precio es " + str(ipdsvalue[2])
                  compras.append(showipdsss1)
                  price.append(ipdsvalue[2])
                  opIpdsss1 = 7
                  opc3 = 7
              elif opIpdsss1 == 2:
                  showipdsss2 = ipds[2] + " Con color " + colrip[1] + " Su precio es " + str(ipdsvalue[2])
                  compras.append(showipdsss2)
                  price.append(ipdsvalue[2])
                  opIpdsss1 = 7
                  opc3 = 7  
              elif opIpdsss1 == 3:
                  showipdsss3 = ipds[2] + " Con color " + colrip[2] + " Su precio es " + str(ipdsvalue[2])
                  compras.append(showipdsss3)
                  price.append(ipdsvalue[2])
                  opIpdsss1 = 7
                  opc3 = 7
              elif opIpdsss1 == 4:
                  showipdsss4 = ipds[2] + " Con color " + colrip[3] + " Su precio es " + str(ipdsvalue[2])
                  compras.append(showipdsss4)
                  price.append(ipdsvalue[2])
                  opIpdsss1 = 7
                  opc3 = 7
              elif opIpdsss1 == 5:
                  showipdsss5 = ipds[2] + " Con color " + colrip[4] + " Su precio es " + str(ipdsvalue[2])
                  compras.append(showipdsss5)
                  price.append(ipdsvalue[2])
                  opIpdsss1 = 7
                  opc3 = 7
              elif opIpdsss1 == 6:
                  showipdsss6 = ipds[2] + " Con color " + colrip[5] + "Su precio es " + str(ipdsvalue[2])
                  compras.append(showipdsss6)
                  price.append(ipdsvalue[2])
                  opIpdsss1 = 7
                  opc3 = 7
           #Ipad novena generacion 256gb. 
           elif opc3 == 4:
            opIpdssss1 = 0
            while opIpdssss1 != 7:
              print("1.", colrip[0])
              print("2.", colrip[1])
              print("3.", colrip[2])
              print("4.", colrip[3])
              print("5.", colrip[4])
              print("6.", colrip[5])
              print("7. Salir ")
              try:
               opIpdssss1 = int(input("Ingrese la opción disponible: ")) 
              except ValueError:
               print(" !Ingrese la opción disponible¡ ")
              #Colores Ipad novena generacion 256gb.
              if opIpdssss1 == 1:
                  showipdssss1 = ipds[3] + " Con color " + colrip[0] + " Su precio es " + str(ipdsvalue[3])
                  compras.append(showipdssss1)
                  price.append(ipdsvalue[3])
                  opIpdssss1 = 7
                  opc3 = 7
              elif opIpdssss1 == 2:
                  showipdssss2 = ipds[3] + " Con color " + colrip[1] + " Su precio es " + str(ipdsvalue[3])
                  compras.append(showipdssss2)
                  price.append(ipdsvalue[3])
                  opIpdssss1 = 7
                  opc3 = 7
              elif opIpdssss1 == 3:
                  showipdssss3 = ipds[3] + " Con color " + colrip[2] + " Su precio es " + str(ipdsvalue[3])
                  compras.append(showipdssss3)
                  price.append(ipdsvalue[3])
                  opIpdssss1 = 7
                  opc3 = 7
              elif opIpdssss1 == 4:
                  showipdssss4 = ipds[3] + " Con color " + colrip[3] + " Su precio es " + str(ipdsvalue[3])
                  compras.append(showipdssss4)
                  price.append(ipdsvalue[3])
                  opIpdssss1 = 7
                  opc3 = 7
              elif opIpdssss1 == 5:
                  showipdssss5 = ipds[3] + " Con color " + colrip[4] + " Su precio es " + str(ipdsvalue[3])
                  compras.append(showipdssss5)
                  price.append(ipdsvalue[3])
                  opIpdssss1 = 7
                  opc3 = 7
              elif opIpdssss1 == 6:
                  showipdssss6 = ipds[3] + " Con color " + colrip[5] + "Su precio es " + str(ipdsvalue[3])
                  compras.append(showipdssss6)
                  price.append(ipdsvalue[3])
                  opIpdssss1 = 7
                  opc3 = 7
           #Ipad decima generacion 64gb.
           elif opc3 == 5:
            opIpddssss1 = 0
            while opIpddssss1 != 7:
              print("1.", colrip[0])
              print("2.", colrip[1])
              print("3.", colrip[2])
              print("4.", colrip[3])
              print("5.", colrip[4])
              print("6.", colrip[5])
              print("7. Salir ")
              try:
               opIpddssss1 = int(input("Ingrese la opción disponible: ")) 
              except ValueError:
               print(" !Ingrese la opción disponible¡ ")
              #Colores Ipad decima generacion 64gb.
              if opIpddssss1 == 1:
                  showipddssss1 = ipds[4] + " Con color " + colrip[0] + " Su precio es " + str(ipdsvalue[4])
                  compras.append(showipddssss1)
                  price.append(ipdsvalue[4])
                  opIpddssss1 = 7
                  opc3 = 7
              elif opIpddssss1 == 2:
                  showipddssss2 = ipds[4] + " Con color " + colrip[1] + " Su precio es " + str(ipdsvalue[4])
                  compras.append(showipddssss2)
                  price.append(ipdsvalue[4])
                  opIpddssss1 = 7
                  opc3 = 7
              elif opIpddssss1 == 3:
                  showipddssss3 = ipds[4] + " Con color " + colrip[2] + " Su precio es " + str(ipdsvalue[4])
                  compras.append(showipddssss3)
                  price.append(ipdsvalue[4])
                  opIpddssss1 = 7
                  opc3 = 7
              elif opIpddssss1 == 4:
                  showipddssss4 = ipds[4] + " Con color " + colrip[3] + " Su precio es " + str(ipdsvalue[4])
                  compras.append(showipddssss4)
                  price.append(ipdsvalue[4])
                  opIpddssss1 = 7
                  opc3 = 7
              elif opIpddssss1 == 5:
                  showipddssss5 = ipds[4] + " Con color " + colrip[4] + " Su precio es " + str(ipdsvalue[4])
                  compras.append(showipddssss5)
                  price.append(ipdsvalue[4])
                  opIpddssss1 = 7
                  opc3 = 7
              elif opIpddssss1 == 6:
                  showipddssss6 = ipds[4] + " Con color " + colrip[5] + "Su precio es " + str(ipdsvalue[4])
                  compras.append(showipddssss6)
                  price.append(ipdsvalue[4])
                  opIpddssss1 = 7
                  opc3 = 7 
           #Ipad decima generacion 256gb. 
           elif opc3 == 6:
            opIpdddssss1 = 0
            while opIpdddssss1 != 7:
              print("1.", colrip[0])
              print("2.", colrip[1])
              print("3.", colrip[2])
              print("4.", colrip[3])
              print("5.", colrip[4])
              print("6.", colrip[5])
              print("7. Salir ")
              try:
               opIpdddssss1 = int(input("Ingrese la opción disponible: ")) 
              except ValueError:
               print(" !Ingrese la opción disponible¡ ")
              #Colores Ipad decima generacion 256gb.
              if opIpdddssss1 == 1:
                  showipdddssss1 = ipds[5] + " Con color " + colrip[0] + " Su precio es " + str(ipdsvalue[5])
                  compras.append(showipdddssss1)
                  price.append(ipdsvalue[5])
                  opIpdddssss1 = 7
                  opc3 = 7
              elif opIpdddssss1 == 2:
                  showipdddssss2 = ipds[5] + " Con color " + colrip[1] + " Su precio es " + str(ipdsvalue[5])
                  compras.append(showipdddssss2)
                  price.append(ipdsvalue[5])
                  opIpdddssss1 = 7
                  opc3 = 7
              elif opIpdddssss1 == 3:
                  showipdddssss3 = ipds[5] + " Con color " + colrip[2] + " Su precio es " + str(ipdsvalue[5])
                  compras.append(showipdddssss3)
                  price.append(ipdsvalue[5])
                  opIpdddssss1 = 7
                  opc3 = 7
              elif opIpdddssss1 == 4:
                  showipdddssss4 = ipds[5] + " Con color " + colrip[3] + " Su precio es " + str(ipdsvalue[5])
                  compras.append(showipdddssss4)
                  price.append(ipdsvalue[5])
                  opIpdddssss1 = 7
                  opc3 = 7
              elif opIpdddssss1 == 5:
                  showipdddssss5 = ipds[5] + " Con color " + colrip[4] + " Su precio es " + str(ipdsvalue[5])
                  compras.append(showipdddssss5)
                  price.append(ipdsvalue[5])
                  opIpdddssss1 = 7
                  opc3 = 7
              elif opIpdddssss1 == 6:
                  showipdddssss6 = ipds[5] + " Con color " + colrip[5] + "Su precio es " + str(ipdsvalue[5])
                  compras.append(showipdddssss6)
                  price.append(ipdsvalue[5])
                  opIpdddssss1 = 7
                  opc3 = 7                                                  
    #Cargadores        
    elif op == 4:
        opc4 = 0
        while opc4 != 5:
         print("1.", charger[0], "su valor es:", changerValue[0])
         print("2.", charger[1], "su valor es:", changerValue[1])
         print("3.", charger[2], "su valor es:", changerValue[2])
         print("4.", charger[3], "su valor es:", changerValue[3])
         print("5. Salir de cargadores")
         try:
           opc4 = int(input("Ingrese la opción disponible: ")) 
         except ValueError:
               print(" !Ingrese la opción disponible¡ ")
         if opc4 == 1:
             showCharger1 = charger[0] + "su valor es:" + str(changerValue[0])
             compras.append(showCharger1)
             price.append(changerValue[0])
             opc4 = 5
         elif opc4 == 2:
             showCharger2 = charger[1] + "su valor es:" + str(changerValue[1])
             compras.append(showCharger2)
             price.append(changerValue[1])
             opc4 = 5
         elif opc4 == 3:
             showCharger3 = charger[2] + "su valor es:" + str(changerValue[2])
             compras.append(showCharger3)
             price.append(changerValue[2])
             opc4 = 5
         elif opc4 == 4:
             showCharger4 = charger[3] + "su valor es:" + str(changerValue[3])
             compras.append(showCharger4)
             price.append(changerValue[3])
             opc4 = 5
    #AirPods         
    elif op == 5: 
        opc5 = 0
        while opc5 != 4:
          print("1.", airpds[0], "su valor es:", airpdsValue[0])
          print("2.", airpds[1], "su valor es:", airpdsValue[1])
          print("3.", airpds[2], "su valor es:", airpdsValue[2])
          print("4. Salir de AirPods")
          try:
           opc5 = int(input("Ingrese la opción disponible: ")) 
          except ValueError:
               print(" !Ingrese la opción disponible¡ ")
          
          if opc5 == 1:
             showAirpds1 = airpds[0] + "su valor es:" + str(airpdsValue[0])
             compras.append(showAirpds1)
             price.append(airpdsValue[0])
             opc5 = 4
          elif opc5 == 2:
             showAirpds2 = airpds[1] + "su valor es:" + str(airpdsValue[1])
             compras.append(showAirpds2)
             price.append(airpdsValue[1])
             opc5 = 4
          elif opc5 == 3:
             showAirpds3 = airpds[2] + "su valor es:" + str(airpdsValue[2])
             compras.append(showAirpds3)
             price.append(airpdsValue[2])
             opc5 = 4
#Facturacion                 
if op == 6:
   listar = compras
   compras = []
   suma = sum(price) 
   
   print("****Factura*****")

   for i in listar:
       print(i)

   print("El valor TOTAL a pagar es: ", suma)
   print("Proceda pasar a la caja, y realice su respectivo pago")
   
       

       