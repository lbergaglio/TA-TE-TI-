"""
TA TE TI
"""
tateti=[[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]


def pantalla(tateti):
    print("     1   2   3  ")
    print("    ___________ ")
    print("   |   |   |   |")
    print(" 1 |",tateti[0][0],"|",tateti[0][1],"|",tateti[0][2],"|")
    print("   |   |   |   |")
    print("   |---|---|---|")
    print("   |   |   |   |")
    print(" 2 |",tateti[1][0],"|",tateti[1][1],"|",tateti[1][2],"|")
    print("   |   |   |   |")
    print("   |---|---|---|")
    print("   |   |   |   |")
    print(" 3 |",tateti[2][0],"|",tateti[2][1],"|",tateti[2][2],"|")
    print("   |   |   |   |")
    print("    ¯¯¯¯¯¯¯¯¯¯¯ ")
       
    
def hay_tateti(matriz):   
    for i in range(len(matriz)):
        if (matriz[i][0]==matriz[i][1]==matriz[i][2]) and (matriz[i][0]!=' '):
            print("TA TE TI!")
            if matriz[i][0]=='X':
                print("GANO EL JUGADOR 1")
            else:
                print("GANO EL JUGADOR 2")
            return True
        elif (matriz[0][i]==matriz[1][i]==matriz[2][i]) and (matriz[0][i]!=' '):
            print("TA TE TI!")
            if matriz[0][i]=='X':
                print("GANO EL JUGADOR 1")
            else:
                print("GANO EL JUGADOR 2")
            return True
        elif (matriz[0][0]==matriz[1][1]==matriz[2][2]) and (matriz[1][1]!=' '):
            print("TA TE TI!")
            if matriz[0][0]=='X':
                print("GANO EL JUGADOR 1")
            else:
                print("GANO EL JUGADOR 2")
            return True
        elif (matriz[0][2]==matriz[1][1]==matriz[2][0]) and (matriz[1][1]!=' '):
            print("TA TE TI!")
            if matriz[0][2]=='X':
                print("GANO EL JUGADOR 1")
            else:
                print("GANO EL JUGADOR 2")
            return True  
    return False

def validacion(numero1,numero2,limMenor,limMayor):
    if numero1<limMenor or numero1>limMayor or numero2<limMenor or numero2>limMayor:
        print("ERROR.Ingrese numeros nuevamente.")
        return False
    return True

def carga_de_datos(matriz,jugador,fila,columna):
    print(fila,columna)
    if jugador%2==0:
        matriz[fila][columna]='X'
    else:
        matriz[fila][columna]='0' 

pantalla(tateti)           
cont=0
while hay_tateti(tateti)!=True:   
    jugadaFila=int(input("Ingrese n° de fila: "))
    jugadaColumna=int(input("Ingrese n° de columna: "))
    senal=1
    while validacion(jugadaFila-1,jugadaColumna-1,0,2)==True and senal==1:
        senal=0
        if tateti[jugadaFila-1][jugadaColumna-1]==' ':
            carga_de_datos(tateti,cont,jugadaFila-1,jugadaColumna-1)
            cont+=1  
        else:
            senal=1
            jugadaFila=int(input("Ingrese n° de fila: "))
            jugadaColumna=int(input("Ingrese n° de columna: "))
    pantalla(tateti)        
    
