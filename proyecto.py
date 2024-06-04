compras = [];
price = [];

#variables pc
comp = ("Macbook pro 13.", "Macbook pro 14.", "Macbook pro 16.")
almcPC1y3 = ("256gb", "512gb", "1tb")
almcPC2 = ("512gb ssd ram 16gb.", "1tb ssd ram 32gb.")
#variables celulares
cel = ("Iphone 11.", "Iphone 13.", "Iphone 14.")
almcel1 = ("64 gb", "128 gb")
colr = ("Rojo", "Plata", "Negro espacial", "Negro", "Dorado", "Blanco")
colr1 = ("Rojo", "Plata", "Negro espacial", "Negro", "Dorado", "Blanco")
#variales ipads
ipads = ("Ipad de cuarta generacion pro.", "Ipad de novena generacion.", "Ipad de decima generaacion.")
#variables cargadores
charger = ("Cargador Macbook pro.", "Cargador Macbook air.", "Cable carga magnetica.", "Adaptador corriente usb.")
#variables airpods
airpds = ("Airpods segunda generacion.", "Airpods tercera generacion.", "Airpods witch charging case.")


#precios computadoras
compValue = (4999000, 9299000 ,12949000, 13500000,14100000, 13899000)

#precios celulares
celvalue = ()
almcelvalue = ()

op = 0;

while op != 6:
    print("*************Menu de tecnologia apple**********")
    print("1. Computadores")
    print("2. Celulares")
    print("3. Ipads")
    print("4. Cargadores")
    print("5. AirPods")
    print("6. Salir e imprimir factura")    
    
    op = int(input("Ingresar opcion: "))
    
    if op == 1:
        opc = 0;
        while opc != 4:
         print("1. ", comp[0])
         print("2. ", comp[1])
         print("3. ", comp[2])
         print("4. salir de computadoras")
         
         opc = int(input("Seleccione una opcion: "))
         
         if opc == 1:
             comp1 = 0;
             while  comp1 != 3:
              print("****Ingresar almacenamiento****")
              print("[1] ", almcPC[0])
              print("[2] ", almcPC[1])
              print("[3]. salir")
              comp1 = int(input("Seleccione una opcion: "))
              if comp1 == 1:
                  text = comp[0] + " " +almcPC[0];
                  compras.append(text);
                  
                  precioComp1 = compValue[0] + almcPCValue[0];
                  price.append(precioComp1);
                  
                  opc = 4;
                  comp1 = 3;
              elif comp1 == 2:
                  text2 = comp[0] + " " +almcPC[1];
                  compras.append(text2);
                  
                  precioComp2 = compValue[0] + almcPCValue[1];
                  price.append(precioComp2); 
                  
                  opc = 4;
                  comp1 = 3;
                  
                  
         elif opc == 2:
             comp2 = 0;
             while  comp2 != 3:
              print("****Ingresar almacenamiento****")
              print("[1] ", almcPC[0])
              print("[2] ", almcPC[1])
              print("[3]. salir")
              comp2 = input()
              if comp2 == 1:
                  text3 = cel[0] + " " +almcPC[0];
                  compras.append(text3);
                  
                  precioComp3 = compValue[1] + almcPCValue[0];
                  price.append(precioComp3);
                  
                  opc = 4;
                  comp2 = 3;
              elif comp2 == 2:
                  text4 = comp[1] + " " +almcPC[1];
                  compras.append(text4); 
                  
                  precioComp4 = compValue[1] + almcPCValue[1];
                  price.append(precioComp4); 

                  opc = 4;
                  comp2 = 3;
         elif opc == 3:
             comp3 = 0;
             while  comp3 != 3:
              print("****Ingresar almacenamiento****")
              print("[1] ", almcPC[0])
              print("[2] ", almcPC[1])
              print("[3]. salir")
              comp3 = input()
              if comp3 == 1:
                  text5 = comp[2] + " " +almcPC[0];
                  compras.append(text5);
                  
                  precioComp5 = compValue[2] + almcPCValue[0];
                  price.append(precioComp5);
                  
                  opc = 4;
                  comp3 = 3;
              elif comp3 == 2:
                  text6 = comp[2] + " " +almcPC[1];
                  compras.append(text6);
                  
                  precioComp6 = compValue[2] + almcPCValue[1];
                  price.append(precioComp6);
                  
                  opc = 4;
                  comp3 = 3;
    elif op == 2: #celulares
        opc2 = 0;
        while opc2 != 4:
         print("1.", cel[0])
         print("2.", cel[1])
         print("3.", cel[2])
         print("4. salir de celulares")
         
         opc2 = int(input("Seleccione una opcion: "))
         if opc2 == 1:
             cel1 = 0
             while cel1 != 3:
              print("****Ingresar almacenamiento****")
              print("1 ", almcel1[0])
              print("2 ", almcel1[1])
              print("3. salir")
              
              cel1 = int(input("Seleccione un color opcion: "))   
              if cel1 == 1:
                  celclr = 0
                  while celclr != 7:
                   print("1.", colr[0])
                   print("2.", colr[1])
                   print("3.", colr[2]) 
                   print("4.", colr[3])
                   print("5.", colr[4])
                   print("6.", colr[5]) 
                   print("7. salir")
                   
                   celcolr = int(input("Seleccione una opcion: "))
                   if celclr == 1:
                    text = comp[0] + " " +almcel1[0];
                    compras.append(text);
                  
                    precioComp1 = celvalue[0] + almcelvalue[0];
                    price.append(precioComp1);
                    
              elif cel1 == 2:
                    celclr2 = 0
                    while celclr2 != 7:
                     print("1.", colr1[0])
                     print("2.", colr1[1])
                     print("3.", colr1[2]) 
                     print("4.", colr1[3])
                     print("5.", colr1[4])
                     print("6.", colr1[5]) 
                     print("7. salir") 
                                                      
    elif op == 3: #ipad
        opc3 = 0;
        while opc3 != 4:
         print("1. ipad 11")
         print("2. ipad 12")
         print("3. ipad 13")
         print("4. salir de ipad")
         
         opc3 = input("Seleccione una opcion: ")
    elif op == 4: #Cargadores
        opc4 = 0;
        while opc4 != 4:
         print("1. Cargadores iphone 11")
         print("2. Cargadores iphone 12")
         print("3. Cargadores iphone 13")
         print("4. salir de Cargadores")
         
         opc4 = input("Seleccione una opcion: ")
    elif op == 5: #AirPods
        opc5 = 0;
        while opc5 != 4:
         print("1. AirPods 11")
         print("2. AirPods 12")
         print("3. AirPods 13")
         print("4. salir de AirPods")
         
         opc5 = input("Seleccione una opcion: ")
         
"""""""""""""""         
while op == 6:
    for i in compras:
        print("impresion de factura")
        print(f"{compras[i]}")
"""""""""      