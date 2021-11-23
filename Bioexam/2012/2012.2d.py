import copy

A = "A"
B = "B"
C = "C"
D = "D"
E = "E"
F = "F"
G = "G"
H = "H"
I = "I"
J = "J"
K = "K"
L = "L"
M = "M"
N = "N"
O = "O"
P = "P"
Q = "Q"
R = "R"
S = "S"
T = "T"
U = "U"
V = "V"
W = "W"
X ="X"
Y = "Y"
Z = "Z"

"""
Set up station type which include station name, left route, right route, left right avalibility and a 
switch() function to switch between left and right avalibility
"""
class station():

    def __init__(self, st, left, right, name):
        self.name = self
        self.st = st
        self.left = left
        self.right = right
        self.left_av = True
        self.right_av = False
        self.name = name

    def switch(self):
        if self.left_av:
            self.right_av = True
            self.left_av = False
        else:
            self.left_av = True
            self.right_av = False
"""
setup every station
"""
ASTA= station(D, E, F, A)
BSTA= station(C, G, H, B)
CSTA= station(B, I, J, C)
DSTA= station(A, K, L, D)
ESTA= station(A, M, N, E)
FSTA= station(A, N, O, F)
GSTA= station(B, O, P, G)
HSTA= station(B, P, Q, H)
ISTA= station(C, Q, R, I)
JSTA= station(C, R, S, J)
KSTA= station(D, S, T, K)
LSTA= station(D, T, M, L)
MSTA= station(U, L, E, M)
NSTA= station(U, E, F, N)
OSTA= station(V, F, G, O)
PSTA= station(V, G, H, P)
QSTA= station(W, H, I, Q)
RSTA= station(W, I, J, R)
SSTA= station(X, J, K, S)
TSTA= station(X, K, L, T)
USTA= station(V, M, N, U)
VSTA= station(U, O, P, V)
WSTA= station(X, Q, R, W)
XSTA= station(W, S, T, X)

def find(ans1, current,steps):
    """
    Ask for the input: flip-flop stations
    """

    #Add a list of flip-flop station
    fifo = []
    for char in ans1:
        fifo.append(char)

    #Ask for current direction
    stafrom = current[0]
    tempto = current[1]

    #Ask for steps
    bo = True
    stato = None
    #Access the stations
    exec(f"stato = copy.deepcopy({tempto}STA)")
    temp = None

    #loop for steps number of time
    for i in range(steps):
        #Access the destination station
        if i != 0:
            exec(f"stato = copy.deepcopy({temp}STA)")
        #If it enter from a stright route
        if stafrom == stato.st:
            #Make stationfrom be the current destination station and save the next destination station
            if stato.left_av:
                stafrom = stato.name
                temp = stato.left
            elif stato.right_av:
                stafrom = stato.name
                temp = stato.right
            #If the destination station is flip-flop, switch the curve route avalibility
            if stato.name in fifo:
                exec(f"{stato.name}STA.switch()")
        #if it enter from a curve route
        elif stafrom == stato.left or stafrom == stato.right:
            #Check if the station is a flip flop
            if not stato.name in fifo:
                #make the enter curve the avaliable curve
                if stafrom == stato.left:
                    exec(f"{stato.name}STA.left_av = True")
                    exec(f"{stato.name}STA.right_av = False")
                else:
                    exec(f"{stato.name}STA.left_av = False")
                    exec(f"{stato.name}STA.right_av = True")
            #Make the stationto be the next station from and save the next station to
            stafrom = stato.name
            temp = stato.st
        else:
            print("Stopped")
    print(stafrom+temp)

def main():
    stations = [A, B, C, D, E, F, G, H, I, J, K, L, M, N, O, P, Q, R, S, T, U, V, W, X]
    





if __name__ == "__main__":
    main()