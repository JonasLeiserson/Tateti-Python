turnoX = True
tablero = [
    ["-", "-", "-"],
    ["-", "-", "-"],
    ["-", "-", "-"]
]
for i in range(9):

    while True:
        x = int(input("Elige fila "))
        y = int(input("Elige columna "))

        if tablero[x][y] == "-":
            break
        else: 
            print("Casilla ocupada")
        
    turnoX = not turnoX
    tablero[x][y] = "X" if turnoX else "O" 
    print(
        tablero[0], "\n",
        tablero[1], "\n",
        tablero[2], sep="")
    print("turno de X =", turnoX)
    
    for i in range(3):

        if tablero[i][0] == tablero[i][1] == tablero[i][2] != "-":
            print("Ganador", tablero[i][0])
            exit() 

        elif tablero[0][i] == tablero[1][i] == tablero[2][i] != "-":
            print("Ganador", tablero[0][i])
            exit()

        elif  tablero[0][0] == tablero[1][1] == tablero[2][2] != "-" or tablero[0][2] == tablero[1][1] == tablero[2][0] != "-":
            print("Ganador", tablero[1][1])
            exit()

print("empate")
turnoX = not turnoX
exit()

          