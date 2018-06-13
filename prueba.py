tablero=[
    [0,0,0],
    [0,0,0],
    [0,0,0]
 ]
actions ={
    "1": [2, 0],
    "2": [2, 1],
    "3": [2, 2],
    "4": [1, 0],
    "5": [1, 1],
    "6": [1, 2],
    "7": [0, 0],
    "8": [0, 1],
    "9": [0, 2],
}




def isFinal(state):
    if((state[0][0]==-1 or state[0][0]==1)and state[0][0]==state[1][1] and state[1][1]==state[2][2]):return True
    if ((state[2][0]==-1 or state[2][0]==1)and state[2][ 0] == state[1][ 1] and state[1][ 1] == state[0][2]): return True

    for row in state:
        if( (row[0]==-1 or row[0]==1)and row[0]==row[1]and row[1]==row[2]): return True

    for i in range(3):

        if( (state[0][i]==-1 or state[0][i]==1)and state[0][i]==state[1][i]and state[1][i]==state[2][i]): return True

    for row in state:
        for n in row:

            if(n==0):return False

    return True



def valida(state):
    if((state[0][0]==-1 or state[0][0]==1)and state[0][0]==state[1][1] and state[1][1]==state[2][2]):
        if(state[0][0]==-1):return 1
        return -1
    if ( (state[2][0]==-1 or state[2][0]==1)and state[2][0] == state[1][ 1] and state[1][ 1] == state[0][2]):
        if(state[2][0]==-1):return 1
        return -1
    for row in state:
        if((row[0]==-1 or row[0]==1)and row[0]==row[1]and row[1]==row[2]):
            if(row[0]==-1):return 1
            return -1
    for i in range(3):
        if( (state[0][i]==-1 or state[0][i]==1)and state[0][i]==state[1][i]and state[1][i]==state[2][i]):
            if (state[0][ i] == -1): return 1
            return -1


    return 0



def minimax( n , state,actionn):
    num=1
    vp=0
    a = ""
    if (isFinal(state)): return [valida(state),""]
    for key, value in actionn.items():



        new_state=copy(state)
        new_state[value[0]][value[1]]=n
        actionnn=dict(actionn)
        del actionnn[key]
        vn=minimax(n*-1,new_state, actionnn)
        if(num==1):

            vp=[vn[0],key]
            num=0
        else:
            if(n==-1):
                if(vp[0]<vn[0]):

                    vp = [vn[0], key]

            else:
                if (vp[0] > vn[0]):

                    vp = [vn[0], key]

    return vp

def copy(old_list):
    new_list=[]
    for v in old_list:
        new_list.append(v[:])


    return new_list



def game_player1(s,a):

    while(True):
        print(s[0])
        print(s[1])
        print(s[2])
        valu=input("Tu turno: ")
        act=a[valu]
        s[act[0]][act[1]]=1
        del a[valu]
        if(isFinal(s)):
            if(valida(s)==0 ):print("empate")
            else: print("Ganaste")
            print(s)
            break
        valu=minimax(-1,copy(s),dict(a))[1]
        act = a[valu]
        s[act[0]][act[1]] = -1
        del a[valu]
        if (isFinal(s)):
            if (valida(s) == 0): print("empate")
            else: print("Perdiste")
            print(s)
            break


def game_player2(s,a):
    while(True):

        valu=minimax(-1,copy(s),dict(a))[1]
        act = a[valu]
        s[act[0]][act[1]] = -1
        del a[valu]
        if (isFinal(s)):
            if (valida(s) == 0): print("empate")
            else: print("Perdiste")
            print(s)
            break

        print(s[0])
        print(s[1])
        print(s[2])
        valu = input("Tu turno: ")
        act = a[valu]
        s[act[0]][act[1]] = 1
        del a[valu]
        if (isFinal(s)):
            if (valida(s) == 0): print("empate")
            else: print("Ganaste")
            print(s)
            break


def game():
    while(True):
        player=input("Quiere ser jugador 1 o 2 :")
        if(player=="1"):game_player1(copy(tablero),dict(actions))
        else:game_player2(copy(tablero),dict(actions))
game()