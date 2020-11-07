import tkinter as tk
from tkinter import messagebox
import tkinter.font as font
from tkinter import simpledialog


# Función para calcular la fila según un índice.
# @index    int [Índice de posición en el arreglo]
# Return    int [Posicion Y]
def getYfromIndex(index):
    arrayIndex = index - 1
    positionY = int((arrayIndex - arrayIndex%len(ticTacToe.board))/len(ticTacToe.board))
    return positionY


# Función para calcular la columna según un índice.
# @index    int [Índice de posición en el arreglo]
# Return    int [Posicion X]
def getXfromIndex(index):
    arrayIndex = index - 1
    positionX = int(arrayIndex%3)
    return positionX


# Función para comparar tres valores no nulos.
# @array    int[] [Valores a comparar]
# Return    bool  [Resultado de la evaluación]
def tripleMatch(array):
    if array[0] == array[1] and array[0] == array[2] and not (array[0]==""):
        print("Victoria!")
        accion1.configure(state='disabled')
        accion2.configure(state='disabled')
        accion3.configure(state='disabled')
        accion4.configure(state='disabled')
        accion5.configure(state='disabled')
        accion6.configure(state='disabled')
        accion7.configure(state='disabled')
        accion8.configure(state='disabled')
        accion9.configure(state='disabled')
        return True
    else:
        return False


#
# Clase Jugador
# @setName
# @getName
# @setMark
# @setMark
class Player():
    name = ""
    mark = ""

    def setName(self, name):
        self.name = name

    def getName(self):
        return self.name

    def setMark(self, mark):
        self.mark = mark

    def getMark(self):
        return self.mark


#
# Clase TicTacToe
# @restartTurn
# @increaseTurn
# @getTurn
# @currentPlayer
# @makeMove
# @updateValue
# @evaluateVictory
# @printPlayers
# @clearBoard
# @printBoard
class TicTacToe():
    firstPlayer = Player()
    secondPlayer = Player()
    activePlayer = None
    turn = 0
    board = [
            ["","",""], ["","",""], ["","",""],
        ]

    def restartTurn(self):
        self.turn = 0
        self.activePlayer = self.firstPlayer

    def increaseTurn(self):
        self.turn += 1

        if self.turn % 2 == 0:
            self.activePlayer = self.firstPlayer

        else:
            self.activePlayer = self.secondPlayer


    def getTurn(self):
        return self.turn

    def currentPlayer(self):
        return self.activePlayer

    def makeMove(self, index):
        positionY = getYfromIndex(index)
        positionX = getXfromIndex(index)

        updated = self.updateValue(positionY, positionX)

        return updated


    def updateValue(self, positionY, positionX):

        if self.board[positionY][positionX] == "" :
            self.board[positionY][positionX] = self.activePlayer.getMark()
            return True
        else:
            return False

    def evaluateVictory(self, index):
        positionY = getYfromIndex(index)
        positionX = getXfromIndex(index)
        victory = False

        temporalArray = []

        #VALIDACIÓN DE COLUMNA
        if not victory:
            temporalArray = []
            temporalArray.append(self.board[((positionY+0)%3)][positionX])
            temporalArray.append(self.board[((positionY+1)%3)][positionX])
            temporalArray.append(self.board[((positionY+2)%3)][positionX])
            print(temporalArray)
            victory = tripleMatch(temporalArray)

            if victory:
                if positionX == 0:
                    accion1.configure(state='normal', bg='#0f0', fg='#000')
                    accion4.configure(state='normal', bg='#0f0', fg='#000')
                    accion7.configure(state='normal', bg='#0f0', fg='#000')
                elif positionX == 1:
                    accion2.configure(state='normal', bg='#0f0', fg='#000')
                    accion5.configure(state='normal', bg='#0f0', fg='#000')
                    accion8.configure(state='normal', bg='#0f0', fg='#000')
                elif positionX == 2:
                    accion3.configure(state='normal', bg='#0f0', fg='#000')
                    accion6.configure(state='normal', bg='#0f0', fg='#000')
                    accion9.configure(state='normal', bg='#0f0', fg='#000')

                messagebox.showinfo(message=("Victoria de {0}!".format(ticTacToe.activePlayer.getName().upper())), title="El juego ha terminado")
                return True

        #VALIDACIÓN DE FILA
        if not victory:
            temporalArray = []
            temporalArray.append(self.board[((positionY)%3)][((positionX+0)%3)])
            temporalArray.append(self.board[((positionY)%3)][((positionX+1)%3)])
            temporalArray.append(self.board[((positionY)%3)][((positionX+2)%3)])
            print(temporalArray)
            victory = tripleMatch(temporalArray)

            if victory:
                if positionY == 0:
                    accion1.configure(state='normal', bg='#0f0', fg='#000')
                    accion2.configure(state='normal', bg='#0f0', fg='#000')
                    accion3.configure(state='normal', bg='#0f0', fg='#000')
                elif positionY == 1:
                    accion4.configure(state='normal', bg='#0f0', fg='#000')
                    accion5.configure(state='normal', bg='#0f0', fg='#000')
                    accion6.configure(state='normal', bg='#0f0', fg='#000')
                elif positionY == 2:
                    accion7.configure(state='normal', bg='#0f0', fg='#000')
                    accion8.configure(state='normal', bg='#0f0', fg='#000')
                    accion9.configure(state='normal', bg='#0f0', fg='#000')

                messagebox.showinfo(message=("Victoria de {0}!".format(ticTacToe.activePlayer.getName().upper())), title="El juego ha terminado")
                return True

        #VALIDACIÓN DE DIAGONAL
        if not victory:
            temporalArray = []
            temporalArray.append(self.board[0][0])
            temporalArray.append(self.board[1][1])
            temporalArray.append(self.board[2][2])
            print(temporalArray)
            victory = tripleMatch(temporalArray)

            if victory:

                accion1.configure(state='normal', bg='#0f0', fg='#000')
                accion5.configure(state='normal', bg='#0f0', fg='#000')
                accion9.configure(state='normal', bg='#0f0', fg='#000')

                messagebox.showinfo(message=("Victoria de {0}!".format(ticTacToe.activePlayer.getName().upper())), title="El juego ha terminado")
                return True

        #VALIDACIÓN DE DIAGONAL INVERSA
        if not victory:
            temporalArray = []
            temporalArray.append(self.board[0][2])
            temporalArray.append(self.board[1][1])
            temporalArray.append(self.board[2][0])
            print(temporalArray)
            victory = tripleMatch(temporalArray)

            if victory:

                accion3.configure(state='normal', bg='#0f0', fg='#000')
                accion5.configure(state='normal', bg='#0f0', fg='#000')
                accion7.configure(state='normal', bg='#0f0', fg='#000')

                messagebox.showinfo(message=("Victoria de {0}!".format(ticTacToe.activePlayer.getName().upper())), title="El juego ha terminado")
                return True

        return False


    def printPlayers(self):
        print("Jugador #1: {0}".format(self.firstPlayer.getName()))
        print("Jugador #2: {0}".format(self.secondPlayer.getName()))

    def clearBoard(self):
        self.board = [
            ["","",""], ["","",""], ["","",""],
        ]

    def printBoard(self):
        print (self.board)


# Función para realizar la actualización de las etiquetas de turno.
# @turno    int[] [Valores a comparar]
# Return    bool  [Resultado de la evaluación]
def drawTurn(turn):
    if (turn%2) == 0:
        firstCharacterTurnLabel.configure(bg='#0f0', text="TURNO ACTIVO")
        secondCharacterTurnLabel.configure(bg='#ccc', text="TURNO INACTIVO")
    else:
        firstCharacterTurnLabel.configure(bg='#ccc', text="TURNO INACTIVO")
        secondCharacterTurnLabel.configure(bg='#0f0', text="TURNO ACTIVO")


# Función para realizar la "Tirada" del jugador.
# @option   int     [Input del usuario]
# @button   Object  [Componente que activó el click.]
#
def makeMove(option, button):
    currentMark = ticTacToe.currentPlayer().getMark()

    validMove = ticTacToe.makeMove(option)
    if(validMove):
        button.configure(state='normal', bg='#424251', text=currentMark)
        result = ticTacToe.evaluateVictory(option)
        if ticTacToe.getTurn() == 8 and not result:
            messagebox.showinfo(message=("Empate!"), title="El juego ha terminado")

        elif not result:
            ticTacToe.increaseTurn()
            drawTurn(ticTacToe.getTurn())



# Función reiniciar los valores a nulos y los efectos visuales
# al estado inicial.
#
def startGame():
    print("Iniciando el juego")

    firstCharacterName = ""
    secondCharacterName = ""

    #Habilitar los botones
    accion1.configure(state='normal', bg='#424251', fg='#FFF', text="")
    accion2.configure(state='normal', bg='#424251', fg='#FFF', text="")
    accion3.configure(state='normal', bg='#424251', fg='#FFF', text="")
    accion4.configure(state='normal', bg='#424251', fg='#FFF', text="")
    accion5.configure(state='normal', bg='#424251', fg='#FFF', text="")
    accion6.configure(state='normal', bg='#424251', fg='#FFF', text="")
    accion7.configure(state='normal', bg='#424251', fg='#FFF', text="")
    accion8.configure(state='normal', bg='#424251', fg='#FFF', text="")
    accion9.configure(state='normal', bg='#424251', fg='#FFF', text="")
    firstCharacterTurnLabel.configure(text="TURNO INACTIVO", bg='#ccc')
    secondCharacterTurnLabel.configure(text="TURNO INACTIVO", bg='#ccc')
    firstCharacterNameLabel.configure(text="", bg='#424251')
    secondCharacterNameLabel.configure(text="", bg='#424251')

    while firstCharacterName == "":
        firstCharacterName = simpledialog.askstring("Input", "Jugador #1, ¿Cuál es tu nombre?",
                                    parent=root)
        if not (firstCharacterName==""):
            ticTacToe.firstPlayer.setName(firstCharacterName)
            ticTacToe.firstPlayer.setMark("X")

    while secondCharacterName == "":
        secondCharacterName = simpledialog.askstring("Input", "Jugador #2, ¿Cuál es tu nombre?",
                                    parent=root)

        if not (secondCharacterName==""):
            ticTacToe.secondPlayer.setName(secondCharacterName)
            ticTacToe.secondPlayer.setMark("O")

    ticTacToe.printPlayers()
    firstCharacterNameLabel.configure(text = ("JUGADOR #1 ( {0} )".format(ticTacToe.firstPlayer.getName().upper())) )
    secondCharacterNameLabel.configure(text = ("JUGADOR #2 ( {0} )".format(ticTacToe.secondPlayer.getName().upper())) )

    ticTacToe.restartTurn()
    ticTacToe.clearBoard()
    ticTacToe.printBoard()

    drawTurn(ticTacToe.getTurn())




heigh = 500
width = 700

root = tk.Tk()
root.config(width=width, height=heigh, bg='white')

#NOMBRE DE LOS JUGADORES
nombreJugador1 = ""
nombreJugador2 = ""

playerName = "JUGADOR #1 ( {0} )".format(nombreJugador1.upper())
firstCharacterNameLabel = tk.Label(root, text=playerName, width=20, heigh=1, bg='#424251', fg='white')
firstCharacterNameLabel.place(x=(width/2-310), y= 100)

myFont = font.Font(size=80, weight='bold')
firstCharacterTurn = tk.Label(root, text="X", width=2, heigh=1, bg='#424251', fg='white')
firstCharacterTurn.place(x=(width/2-307), y= 140)
firstCharacterTurn['font'] = myFont

playerStatusTurn = "Inactivo"
playerOneTurn = "TURNO {0}".format(playerStatusTurn.upper())
firstCharacterTurnLabel = tk.Label(root, text=playerOneTurn, width=20, heigh=1, bg='#ccc', fg='black')
firstCharacterTurnLabel.place(x=(width/2-310), y= 290)


playerName = "JUGADOR #2 ( {0} )".format(nombreJugador2.upper())
secondCharacterNameLabel = tk.Label(root, text=playerName, width=20, heigh=1, bg='#424251', fg='white')
secondCharacterNameLabel.place(x=(width/2+160), y= 100)

secondCharacterTurn = tk.Label(root, text="O", width=2, heigh=1, bg='#424251', fg='white')
secondCharacterTurn.place(x=(width/2+162), y= 140)
secondCharacterTurn['font'] = myFont

playerStatusTurn = "Inactivo"
playerOneTurn = "TURNO {0}".format(playerStatusTurn.upper())
secondCharacterTurnLabel = tk.Label(root, text=playerOneTurn, width=20, heigh=1, bg='#ccc', fg='black')
secondCharacterTurnLabel.place(x=(width/2+162), y= 290)


#Botones del tablero de gato
startButton = tk.Button(root, bg='#FFF', fg='#000', text="INICIAR JUEGO NUEVO",
    command=lambda: startGame())
startButton.place(x=(width/2+10-80), y=25)

accion1 = tk.Button(root, bg='#ccc', fg='white', state="disabled", height = 5, width = 10, text="",
    command=lambda: makeMove(1, accion1))
accion1.place(x=(width/2+10-150), y=80)

accion2 = tk.Button(root, bg='#ccc', fg='white', state="disabled", height = 5, width = 10, text="",
    command=lambda: makeMove(2, accion2))
accion2.place(x=(width/2+10-50), y=80)

accion3 = tk.Button(root, bg='#ccc', fg='white', state="disabled", height = 5, width = 10, text="",
    command=lambda: makeMove(3, accion3))
accion3.place(x=(width/2+10+50), y=80)

accion4 = tk.Button(root, bg='#ccc', fg='white', state="disabled", height = 5, width = 10, text="",
    command=lambda: makeMove(4, accion4))
accion4.place(x=(width/2+10-150), y=180)

accion5 = tk.Button(root, bg='#ccc', fg='white', state="disabled", height = 5, width = 10, text="",
    command=lambda: makeMove(5, accion5))
accion5.place(x=(width/2+10-50), y=180)

accion6 = tk.Button(root, bg='#ccc', fg='white', state="disabled", height = 5, width = 10, text="",
    command=lambda: makeMove(6, accion6))
accion6.place(x=(width/2+10+50), y=180)

accion7 = tk.Button(root, bg='#ccc', fg='white', state="disabled", height = 5, width = 10, text="",
    command=lambda: makeMove(7, accion7))
accion7.place(x=(width/2+10-150), y=280)

accion8 = tk.Button(root, bg='#ccc', fg='white', state="disabled", height = 5, width = 10, text="",
    command=lambda: makeMove(8, accion8))
accion8.place(x=(width/2+10-50), y=280)

accion9 = tk.Button(root, bg='#ccc', fg='white', state="disabled", height = 5, width = 10, text="",
    command=lambda: makeMove(9, accion9))
accion9.place(x=(width/2+10+50), y=280)


ticTacToe = TicTacToe()


root.mainloop()