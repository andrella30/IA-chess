import chess
import random
import time


def define_player(player):
    if player == chess.WHITE:
        return "White"
    else:
        return "Black"

def random_player(board):
    move = random.choice(list(board.legal_moves))
    return move.uci()

def random_game(player1, player2, board):
    while not board.is_game_over(claim_draw=True):
        if board.turn == chess.WHITE:
            uci = player1(board)
        else:
            uci = player2(board)
        board.push_uci(uci)
        print(board)
        print("---------------")
        print("A B C D E F G H")
    result = None
    if board.is_checkmate():
        msg = "Checkmate: " + define_player(not board.turn) + " ganhou!"
        result = not board.turn
    elif board.is_stalemate() or board.is_fivefold_repetition() or board.is_insufficient_material() or board.can_claim_draw():
        msg = "Empate"
    print("Resultado Final: " + msg + "\n")
    return (result, msg, board)

board = chess.Board()


def player(board):
    print("A B C D E F G H")
    print("---------------")
    print(board)
    print("---------------")
    print("A B C D E F G H")
    move = input("Enter move: ")
    move = chess.Move.from_uci(str(move))
    return move.uci()



board = chess.Board()
ans = True
while True:
    print("1. Jogar contra a máquina\n2. Simulação máquina contra máquina\n3. Sair")
    ans= input("Opção: ")
    if ans == "1":
        start = time.time()
        random_game(player, random_player, board)
        board.reset()
        end = time.time()
        tempoFinal = end - start
        print("Tempo: ", round(tempoFinal, 2))
    elif ans == "2":
        start = time.time()
        random_game(random_player, random_player, board)
        board.reset()
        end = time.time()
        tempoFinal = end - start
        print("Tempo: ", round(tempoFinal, 2))
    elif ans == "3":
        exit()
    else:
        print("Comando Inválido")
        exit()
