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
Asta = station(D, E, F, A)
Bsta = station(C, G, H, B)
Csta = station(B, I, J, C)
Dsta = station(A, K, L, D)
Esta = station(A, M, N, E)
Fsta = station(A, N, O, F)
Gsta = station(B, O, P, G)
Hsta = station(B, P, Q, H)
Ista = station(C, Q, R, I)
Jsta = station(C, R, S, J)
Ksta = station(D, S, T, K)
Lsta = station(D, T, M, L)
Msta = station(U, L, E, M)
Nsta = station(U, E, F, N)
Osta = station(V, F, G, O)
Psta = station(V, G, H, P)
Qsta = station(W, H, I, Q)
Rsta = station(W, I, J, R)
Ssta = station(X, J, K, S)
Tsta = station(X, K, L, T)
Usta = station(V, M, N, U)
Vsta = station(U, O, P, V)
Wsta = station(X, Q, R, W)
Xsta = station(W, S, T, X)

"""
Ask for the input: flip-flop stations
"""

#Add a list of flip-flop station
fifo = []

#Ask for current direction
current = "PV"
stafrom = current[0]
tempto = current[1]

#Ask for steps
bo = True
stato = None
#Access the stations
exec(f"stato = copy.deepcopy({tempto}sta)")
temp = None
i = 0

#loop for steps number of time
while True:
    #Access the destination station
    if i != 0:
        exec(f"stato = copy.deepcopy({temp}sta)")
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
            exec(f"{stato.name}sta.switch()")
    #if it enter from a curve route
    elif stafrom == stato.left or stafrom == stato.right:
        #Check if the station is a flip flop
        if not stato.name in fifo:
            #make the enter curve the avaliable curve
            if stafrom == stato.left:
                exec(f"{stato.name}sta.left_av = True")
                exec(f"{stato.name}sta.right_av = False")
            else:
                exec(f"{stato.name}sta.left_av = False")
                exec(f"{stato.name}sta.right_av = True")
        #Make the stationto be the next station from and save the next station to
        stafrom = stato.name
        temp = stato.st
    else:
        print("Stopped")
    print(stafrom, end=" ")
    if stafrom == P:
        break
    i+=1