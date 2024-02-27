def main():
    import sys
    while True:
        try:
            print(f"New Entry:")
            g, p = map(int, sys.stdin.readline().strip().split())
            if not g and not p:
                break
            
            corrida = [[int(x) for x in sys.stdin.readline().strip().split()] for _ in range(g)]
            print() 
            
            s = int(sys.stdin.readline().strip())
            print() 
            for _ in range(s):
                k = int(sys.stdin.readline().strip())
                lista_mezclada = [0]
                sistema = [int(x) for x in sys.stdin.readline().strip().split()]
                if k < p:
                    for f in range(k, p):
                        lista_mezclada  = sistema + [0]
                        sistema = lista_mezclada
                ponto = [0] * p  
                for i in range(g):
                    for j in range(p):
                        ponto[j] += sistema[corrida[i][j]-1]
                m = max(ponto)
                winners = [i + 1 for i, points in enumerate(ponto) if points == m]
                if winners:
                    print(f"Winner {winners}")
                print() 
        except ValueError:
            print("Invalid input", file=sys.stderr)
            sys.exit(1)

if __name__ == "__main__":
    main()
