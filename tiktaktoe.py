# Juego de Tic-Tac-Toe con palomita y zapato

# Definimos los símbolos para cada jugador
PLAYER1_SYMBOL = "✓"
PLAYER2_SYMBOL = "👞"

# Inicializamos el tablero como una matriz de 3x3 llena de guiones bajos
board = [["_", "_", "_"], ["_", "_", "_"], ["_", "_", "_"]]

# Función para mostrar el tablero
def display_board():
    for row in board:
        print(" | ".join(row))
    print()

# Función para verificar si un jugador ha ganado
def check_winner(symbol):
    # Verificación de filas
    for row in board:
        if all(cell == symbol for cell in row):
            return True

    # Verificación de columnas
    for col in range(3):
        if all(board[row][col] == symbol for row in range(3)):
            return True

    # Verificación de diagonales
    if all(board[i][i] == symbol for i in range(3)) or all(board[i][2 - i] == symbol for i in range(3)):
        return True

    return False

# Función para verificar si el tablero está lleno (empate)
def is_board_full():
    return all(cell != "_" for row in board for cell in row)

# Función principal del juego
def tic_tac_toe():
    print("¡Bienvenidos al juego de Tic-Tac-Toe!")
    print("Jugador 1 es la palomita (✓) y Jugador 2 es el zapato (👞).")
    print("Para hacer un movimiento, ingresa el número de fila y columna (0, 1, o 2).")
    print()

    current_player = 1  # El jugador 1 comienza

    while True:
        display_board()
        if current_player == 1:
            symbol = PLAYER1_SYMBOL
        else:
            symbol = PLAYER2_SYMBOL

        print(f"Turno del Jugador {current_player} ({symbol})")
        
        # Solicitar movimiento del jugador
        try:
            row = int(input("Ingresa el número de la fila (0, 1, o 2): "))
            col = int(input("Ingresa el número de la columna (0, 1, o 2): "))
        except ValueError:
            print("Por favor ingresa números válidos para la fila y columna.")
            continue

        # Verificar si la posición es válida
        if row not in range(3) or col not in range(3):
            print("Posición fuera del rango. Intenta de nuevo.")
            continue
        if board[row][col] != "_":
            print("Esa posición ya está ocupada. Intenta de nuevo.")
            continue

        # Colocar el símbolo en el tablero
        board[row][col] = symbol

        # Verificar si el jugador actual ha ganado
        if check_winner(symbol):
            display_board()
            print(f"¡Jugador {current_player} ({symbol}) ha ganado!")
            break

        # Verificar si el tablero está lleno (empate)
        if is_board_full():
            display_board()
            print("El juego ha terminado en empate.")
            break

        # Cambiar de jugador
        current_player = 2 if current_player == 1 else 1

# Iniciar el juego
tic_tac_toe()
