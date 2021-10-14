import chess 
import time
import random

peaoValues = [
 0,  0,  0,  0,  0,  0,  0,  0,
 5, 10, 10,-20,-20, 10, 10,  5,
 5, -5,-10,  0,  0,-10, -5,  5,
 0,  0,  0, 20, 20,  0,  0,  0,
 5,  5, 10, 25, 25, 10,  5,  5,
10, 10, 20, 30, 30, 20, 10, 10,
50, 50, 50, 50, 50, 50, 50, 50,
 0,  0,  0,  0,  0,  0,  0,  0]


bispoValues = [
-20,-10,-10,-10,-10,-10,-10,-20,
-10,  5,  0,  0,  0,  0,  5,-10,
-10, 10, 10, 10, 10, 10, 10,-10,
-10,  0, 10, 10, 10, 10,  0,-10,
-10,  5,  5, 10, 10,  5,  5,-10,
-10,  0,  5, 10, 10,  5,  0,-10,
-10,  0,  0,  0,  0,  0,  0,-10,
-20,-10,-10,-10,-10,-10,-10,-20]


cavaloValues = [
-50,-40,-30,-30,-30,-30,-40,-50,
-40,-20,  0,  5,  5,  0,-20,-40,
-30,  5, 10, 15, 15, 10,  5,-30,
-30,  0, 15, 20, 20, 15,  0,-30,
-30,  5, 15, 20, 20, 15,  5,-30,
-30,  0, 10, 15, 15, 10,  0,-30,
-40,-20,  0,  0,  0,  0,-20,-40,
-50,-40,-30,-30,-30,-30,-40,-50]


torreValues = [
  0,  0,  0,  5,  5,  0,  0,  0,
 -5,  0,  0,  0,  0,  0,  0, -5,
 -5,  0,  0,  0,  0,  0,  0, -5,
 -5,  0,  0,  0,  0,  0,  0, -5,
 -5,  0,  0,  0,  0,  0,  0, -5,
 -5,  0,  0,  0,  0,  0,  0, -5,
  5, 10, 10, 10, 10, 10, 10,  5,
 0,  0,  0,  0,  0,  0,  0,  0]


rainhaValues = [
-20,-10,-10, -5, -5,-10,-10,-20,
-10,  0,  0,  0,  0,  0,  0,-10,
-10,  5,  5,  5,  5,  5,  0,-10,
  0,  0,  5,  5,  5,  5,  0, -5,
 -5,  0,  5,  5,  5,  5,  0, -5,
-10,  0,  5,  5,  5,  5,  0,-10,
-10,  0,  0,  0,  0,  0,  0,-10,
-20,-10,-10, -5, -5,-10,-10,-20]

reiValues = [
 20, 30, 10,  0,  0, 10, 30, 20,
 20, 20,  0,  0,  0,  0, 20, 20,
-10,-20,-20,-20,-20,-20,-20,-10,
-20,-30,-30,-40,-40,-30,-30,-20,
-30,-40,-40,-50,-50,-40,-40,-30,
-30,-40,-40,-50,-50,-40,-40,-30,
-30,-40,-40,-50,-50,-40,-40,-30,
-30,-40,-40,-50,-50,-40,-40,-30]


def define_player(player):
    if player == chess.WHITE:
        return "White"
    else:
        return "Black"

def init_board(board):

    if board.is_checkmate():
        if board.turn:            
            return -9999
        else:
            return 9999
    if board.is_stalemate():
        return 0
    if board.is_insufficient_material():
        return 0

    white_peao = len(board.pieces(chess.PAWN, chess.WHITE))
    black_peao = len(board.pieces(chess.PAWN, chess.BLACK))
    white_cavalo = len(board.pieces(chess.KNIGHT, chess.WHITE))
    black_cavalo = len(board.pieces(chess.KNIGHT, chess.BLACK))
    white_bispo =  len(board.pieces(chess.BISHOP, chess.WHITE))
    black_bispo = len(board.pieces(chess.BISHOP, chess.BLACK))
    white_torre = len(board.pieces(chess.ROOK, chess.WHITE))
    black_torre = len(board.pieces(chess.ROOK, chess.BLACK))
    white_rainha = len(board.pieces(chess.QUEEN, chess.WHITE))
    black_rainha = len(board.pieces(chess.QUEEN, chess.BLACK))

    material = 100*(white_peao - black_peao) + 320 * ( white_cavalo - black_cavalo ) + 330 * ( white_bispo - black_bispo ) + 500 * ( white_torre - black_torre ) + 900 * (white_rainha - black_rainha)

    peaosq = sum([peaoValues[i] for i in board.pieces(chess.PAWN, chess.WHITE)])
    
    peaosq= peaosq + sum([-peaoValues[chess.square_mirror(i)] 
                                    for i in board.pieces(chess.PAWN, chess.BLACK)])
    
    cavalosq = sum([cavaloValues[i] for i in board.pieces(chess.KNIGHT, chess.WHITE)])

    cavalosq = cavalosq + sum([-cavaloValues[chess.square_mirror(i)] 
                                    for i in board.pieces(chess.KNIGHT, chess.BLACK)])

    bisposq= sum([bispoValues[i] for i in board.pieces(chess.BISHOP, chess.WHITE)])

    bisposq= bisposq + sum([-bispoValues[chess.square_mirror(i)] 
                                    for i in board.pieces(chess.BISHOP, chess.BLACK)])

    torresq = sum([torreValues[i] for i in board.pieces(chess.ROOK, chess.WHITE)]) 
    torresq = torresq + sum([-torreValues[chess.square_mirror(i)] 
                                    for i in board.pieces(chess.ROOK, chess.BLACK)])

    rainhasq = sum([rainhaValues[i] for i in board.pieces(chess.QUEEN, chess.WHITE)]) 
    rainhasq = rainhasq + sum([-rainhaValues[chess.square_mirror(i)] 
                                    for i in board.pieces(chess.QUEEN, chess.BLACK)])
    reisq = sum([reiValues[i] for i in board.pieces(chess.KING, chess.WHITE)]) 

    reisq = reisq + sum([-reiValues[chess.square_mirror(i)] 
                                    for i in board.pieces(chess.KING, chess.BLACK)])
    
    eval = material + peaosq + cavalosq + bisposq+ torresq+ rainhasq + reisq
    
    if board.turn:
        return eval
    else:
        return -eval

def alphabetacut( alpha, beta, depthleft, board ):
    bestscore = -9999
    if( depthleft == 0 ):
        return eval( alpha, beta, board )
    for move in board.legal_moves:
        board.push(move)   
        score = -alphabetacut( -beta, -alpha, depthleft - 1, board )
        board.pop()
        if( score >= beta ):
            return score
        if( score > bestscore ):
            bestscore = score
        if( score > alpha ):
            alpha = score   
    return bestscore

def eval( alpha, beta, board):
    stand_pat = init_board(board)
    if( stand_pat >= beta ):
        return beta
    if( alpha < stand_pat ):
        alpha = stand_pat

    for move in board.legal_moves:
        if board.is_capture(move):
            board.push(move)        
            score = -eval( -beta, -alpha, board )
            board.pop()

            if( score >= beta ):
                return beta
            if( score > alpha ):
                alpha = score  
    return alpha


def selectmove(depth, board):
    bestMove = chess.Move.null()
    bestValue = -99999
    alpha = -100000
    beta = 100000
    for move in board.legal_moves:
        board.push(move)
        boardValue = -alphabetacut(-beta, -alpha, depth-1, board)
        if boardValue > bestValue:
            bestValue = boardValue
            bestMove = move
        if( boardValue > alpha ):
            alpha = boardValue
        board.pop()
    return bestMove

def random_player(board):
    move = random.choice(list(board.legal_moves))
    return move.uci()

def selfPlay(board):
    print(board)
    print("---------------")
    print("A B C D E F G H")
    while not board.is_game_over():
        if board.turn:
            move = input("Enter move: ")
            move = chess.Move.from_uci(str(move))
            board.push(move)
        else:
            print("Computers Turn:")
            move = selectmove(3,board)
            move = chess.Move.from_uci(str(move))
            board.push(move)
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

def simulation(board):
    print(board)
    print("---------------")
    print("A B C D E F G H")
    while not board.is_game_over():
        if board.turn:
            move = selectmove(3, board)
            board.push(move)       
        else:
            move = random_player(board)
            board.push_uci(move)
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


def main():
    board = chess.Board()
    ans = True
    while ans:
        print("1. Jogar contra a máquina\n2. Simulação máquina contra máquina\n3. Sair")
        ans= input("Opção: ")

        if ans == "1":
            start = time.time()
            selfPlay(board)
            end = time.time()
            tempoFinal = end - start
            print("Tempo: ", round(tempoFinal, 2))
            board.reset()

        elif ans == "2":
            start = time.time()
            simulation(board)
            end = time.time()
            tempoFinal = end - start
            print("Tempo: ", round(tempoFinal, 2))
            board.reset()
        elif ans == "3":
            exit()
        else:
            print("Comando Inválido")
            exit()



main()
