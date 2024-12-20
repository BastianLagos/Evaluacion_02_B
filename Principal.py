from Remedio import Remedio

class Principal():
    __rem= Remedio()
    __lista=[]

    def __init__(self):
        pass

    def menu(self):
        try:
            system("cls")
            print("-----MENU-----")
            print("1.-Agregar.")
            print("2.-Listar Todos.")
            print("3.-Listar Solo Bayer.")
            print("4.-Listar Solo Chile.")
            print("5.-Buscar.")
            print("6.-Eliminar.")
            print("7.-Estadistica.")
            print("8.-Salir Del Programa.")
            op = int(input("Digite Una Opcion : "))
            if op==1:
                self.__agregar()
            elif op==2:
                self.__listarTodos()
            elif op==3:
                self.__listarSoloBayer()
            elif op==4:
                self.__listarSoloChile()
            elif op==5:
                self.__buscar()
            elif op==6:
                self.__eliminar()
            elif op==7:
                self.__estadistica()
            elif op==8:
                self.__salir()
                os._exit(1)
            else:
                self.__errorOpcion()

        except:
            print("\n---Error Al Intentar Almacenar La Opcion!! ---")
            system("pause")
            self.menu()
#-------------------------------------------------------------------------------------
    def __agregar(self):
        while True:
            try:
                system("cls")
                cod = int(input("Digite El Codigo Del Remedio ("+str(len(self.__lista)+1)+") : "))
                if cod<1 or cod>99999:
                    print("\n--- El Codigo Debe Tener Hasta 5 Digitos!! ---")
                    system("pause")
                else:
                    res = False
                    for x in self.__lista:
                        if cod==x.getCodigo():
                            res = True
                    
                    if res==True:
                        print("\n-----------------------------------")
                        print("--- El Codigo",cod,"Ya Existe!! ---")
                        print("-----------------------------------")
                        system("pause")
                    else:
                        break
            except:
                print("\n---Error Al intentar Almacenar El Codigo!! ---")
                system("pause")

        while True:
            try:
                system("cls")
                nom = input("Digite El Nombre Del Remedio ("+str(len(self.__lista)+1)+") : ")
                if len(nom.strip())<1 or len(nom.strip())>20:
                    print("\n--- El Nombre Debe Tener Hasta 20 Caracteres!! ---")
                    system("pause")
                else:
                    break
            except:
                print("\n---Error Al intentar Almacenar El Nombre!! ---")
                system("pause")

        while True:
            try:
                system("cls")
                print("---LABORATORIOS---")
                print("1.Laboratorio Bayer")
                print("2.Laboratorio Chile")
                lab = int(input("Digite El Laboratorio Del Remedio ("+str(len(self.__lista)+1)+") : "))
                if lab!=1 and lab!=2:
                    print("\n--- Error En La Opcion Del Laboratorio!! ---")
                    system("pause")
                else:
                    break
            except:
                print("\n---Error Al intentar Almacenar El Laboratorio!! ---")
                system("pause")

        while True:
            try:
                system("cls")
                pre = int(input("Digite El Precio Del Remedio ("+str(len(self.__lista)+1)+") : "))
                if pre<1000 or pre>250000:
                    print("\n--- El Precio Debe Estar Entre $1000 y $250000!! ---")
                    system("pause")
                else:
                    break
            except:
                print("\n---Error Al intentar Almacenar El Precio!! ---")
                system("pause")

        while True:
            try:
                system("cls")
                des = input("Digite La Descripcion Del Remedio ("+str(len(self.__lista)+1)+") : ")
                if len(des.strip())<1 or len(des.strip())>30:
                    print("\n--- La Descripcion Debe Tener Entre 1 y 30 Caracteres!! ---")
                    system("pause")
                else:
                    break
            except:
                print("\n---Error Al intentar Almacenar La Descripcion!! ---")
                system("pause")

        self.__rem = Remedio()
        self.__rem.setCodigo(cod)
        self.__rem.setNombre(nom)
        self.__rem.setLaboratorio(lab)
        self.__rem.setPrecio(pre)
        self.__rem.setDescripcion(des)
        self.__lista.append(self.__rem)
        self.menu()
#--------------------------------------------------------------------------------------
    def __listarTodos(self):
        if len(self.__lista)==0:
            system("cls")
            print("---------------------------------------------------")
            print("--- No Hay Registros De Remedios Para Listar!! ---")
            print("---------------------------------------------------")
            system("pause")
            self.menu()
        else:
            system("cls")
            print("---------------")
            print("--- LISTADO ---")
            print("---------------")
            for x in self.__lista:
                print("CODIGO : ",x.getCodigo())
                print("NOMBRE : ",x.getNombre())
                if x.getLaboratorio()==1:
                    print("LABORATORIO : Bayer")
                else:
                    print("LABORATORIO : Chile")
                print("PRECIO : ",x.getPrecio())
                print("DESCRIPCION : ",x.getDescripcion())
                print("----------------")
                print("----------------")

            system("pause")
            self.menu()
#--------------------------------------------------------------------------------------
    def __listarSoloBayer(self):
        if len(self.__lista)==0:
            system("cls")
            print("--------------------------------------------------------")
            print("--- No Hay Registros De Remedios Bayer Para Listar!! ---")
            print("--------------------------------------------------------")
            system("pause")
            self.menu()
        else:
            system("cls")
            print("---------------------")
            print("--- LISTADO BAYER ---")
            print("---------------------")
            for x in self.__lista:
                if x.getLaboratorio()==1:
                    print("CODIGO : ",x.getCodigo())
                    print("NOMBRE : ",x.getNombre())
                    print("LABORATORIO : Bayer")
                    print("PRECIO : ",x.getPrecio())
                    print("DESCRIPCION : ",x.getDescripcion())
                    print("---------------------")
                    print("---------------------")

            system("pause")
            self.menu()
#--------------------------------------------------------------------------------------
    def __listarSoloChile(self):
        if len(self.__lista)==0:
            system("cls")
            print("--------------------------------------------------------")
            print("--- No Hay Registros De Remedios Chile Para Listar!! ---")
            print("--------------------------------------------------------")
            system("pause")
            self.menu()
        else:
            system("cls")
            print("---------------------")
            print("--- LISTADO CHILE ---")
            print("---------------------")
            for x in self.__lista:
                if x.getLaboratorio()==2:
                    print("CODIGO : ",x.getCodigo())
                    print("NOMBRE : ",x.getNombre())
                    print("LABORATORIO : Chile")
                    print("PRECIO : ",x.getPrecio())
                    print("DESCRIPCION : ",x.getDescripcion())
                    print("---------------------")
                    print("---------------------")

            system("pause")
            self.menu()
#---------------------------------------------------------------------------------------
    def __buscar(self):
        if len(self.__lista)==0:
            system("cls")
            print("---------------------------------------------------")
            print("--- No Hay Registros De Remedios Para Buscar!! ---")
            print("---------------------------------------------------")
            system("pause")
            self.menu()
        else:
            while True:
                try:
                    system("cls")
                    cod = int(input("Digite El Codigo Del Remedio a Buscar : "))
                    res = False
                    for x in self.__lista:
                        if cod==x.getCodigo():
                            res = True
                            system("cls")
                            print("--------------------------")
                            print("----REMEDIO ENCONTRADO----")
                            print("--------------------------")
                            print("CODIGO : ",x.getCodigo())
                            print("NOMBRE : ",x.getNombre())
                            if x.getLaboratorio()==1:
                                print("LABORATORIO : Bayer")
                            else:
                                print("LABORATORIO : Chile")
                            print("PRECIO : ",x.getPrecio())
                            print("DESCRIPCION : ",x.getDescripcion())
                            print("----------------")
                            print("----------------")
                            system("pause")
                            self.menu()

                    if res==False:
                        print("\n-----------------------------------------")
                        print("--- El Codigo Buscado",cod,"No Existe!! ---")
                        print("-------------------------------------------")
                        system("pause")
                        self.menu()
                except:
                    print("\n---Error Al intentar Almacenar El Codigo Buscado!! ---")
                    system("pause")
                    self.menu()
#---------------------------------------------------------------------------------------
    def __eliminar(self):
        if len(self.__lista)==0:
            system("cls")
            print("-----------------------------------------------------")
            print("--- No Hay Registros De Remedios Para Eliminar!! ---")
            print("-----------------------------------------------------")
            system("pause")
            self.menu()
        else:
            while True:
                try:
                    system("cls")
                    cod = int(input("Digite El Codigo Del Remedio a Eliminar : "))
                    res = False
                    for x in self.__lista:
                        if cod==x.getCodigo():
                            res = True
                            self.__lista.remove(x)
                            system("cls")
                            print("------------------------")
                            print("---REMEDIO ELIMINADO---")
                            print("------------------------")
                            system("pause")
                            self.menu()

                    if res==False:
                        print("\n-----------------------------------------")
                        print("--- El Codigo Buscado",cod,"No Existe!! ---")
                        print("--------------------------------------------")
                        system("pause")
                        self.menu()
                except:
                    print("\n---Error Al intentar Almacenar El Codigo a Eliminar!! ---")
                    system("pause")
                    self.menu()
#----------------------------------------------------------------------------------------
    def __estadistica(self):
        if len(self.__lista)==0:
            system("cls")
            print("-----------------------------------------------------")
            print("--- No Hay Registros Para Generar La Estadistica ---")
            print("-----------------------------------------------------")
            system("pause")
            self.menu()
        else:
            con=0; sum=0; 
            for x in self.__lista:
                if x.getLaboratorio()==1:
                    con +=1
                    sum += x.getPrecio()
                else:
                    con += 1
                    sum += x.getPrecio()
                pro = int((sum/con))

            system("cls")
            print("--------------------")
            print("--- ESTADISTICA ---")
            print("--------------------")
            print("CANTIDAD GENERAL DE REMEDIOS")
            print("   Cantidad De Remedios       :  ",con)
            print("SUMA GENERAL DE REMEDIOS")
            print("   Suma De Remedios           : $",sum)
            print("PROMEDIO GENERAL DE REMEDIOS")
            print("   Promedio De Remedios       : $",pro)
            system("pause")
            self.menu()
#-----------------------------------------------------------------------------------------
    def __salir(self):
        print("\n----------------------------")
        print("---Adios, Vuelva Pronto!! ---")
        print("------------------------------")
        system("pause")
#------------------------------------------------------------------------------------------
    def __errorOpcion(self):
        print("\n--------------------------")
        print("--- Error De Opcion!! ---")
        print("----------------------------")
        system("pause")
        self.menu()
#------------------------------------------------------------------------------------------

from os import system
import os 
p=Principal()
p.menu()