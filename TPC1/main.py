from typing import Dict, Tuple

def main():
    ficheiro = open("emd.csv")
    modalidades = []
    i = 0
    aptos = 0
    inaptos = 0
    escaloes: Dict[Tuple[int,int],int] = {}

    for linha in ficheiro:
        if i != 0:
            vl = linha.split(",")

            modalidades.append(vl[8])

            if vl[12] == "true\n":
                aptos += 1
            else:
                inaptos += 1

            idade = int(vl[5])
            escalaoIntervalo = (idade - (idade%5), idade - (idade%5)+ 4)
            escaloes[escalaoIntervalo] = escaloes.get(escalaoIntervalo,0) + 1

        i += 1
    
    verificaModalidades = list(set(modalidades))
    verificaModalidades.sort()

    total = aptos + inaptos

    print("Modalidades:")
    for m in verificaModalidades:
        print("-> " + m)

    print("\nAtletas Aptos: " + str((aptos/total)*100) + "%")
    print("Atletas Inaptos:" + str((inaptos/total)*100) + "%")

    print("\nEscalões:")
    for intervalo in sorted(escaloes.keys()):
        print(f"{intervalo[0]}-{intervalo[1]}: {escaloes[intervalo]}")

main()