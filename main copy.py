hracie_pole = [
    [" ", 1,2,3,4],
    [1, " ", " ", " ", " "],
    [2, " ", " ", " ", " "],
    [3, " ", " ", " ", " "],
    [4, " ", " ", " ", " "],
]

kriz = "x"
gula = "o"
def usporiadanie(hracie_pole):
    for riadok in hracie_pole:
        for policko in riadok:
            print(policko, end="")
        print()

while True:
    usporiadanie(hracie_pole)
    print("Prvy ide s krizikmi")
    stav1 = int(input("Zadaj stplec:"))
    stav2 = int(input("Zadaj riadok:"))
    davanie = hracie_pole[stav1][stav2] = "x"

    usporiadanie(hracie_pole)
    print("Prvy ide s gulami")
    stav1 = int(input("Zadaj stlpec:"))
    stav2 = int(input("Zadaj riadok:"))
    davanie = hracie_pole[stav1][stav2] = "o"

    



