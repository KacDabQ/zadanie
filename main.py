def liczby():
    try:
        p = input(int(("Proszę podać liczbe do zpierwiastkowania kwadratowego: ")))
        prec = input(int(("Proszę podać liczbe dokładności: ")))
        return p, prec
    except:
        return "Something went wrong"
    

def pierwiastek(p, prec):
    
    if p < 0:
        raise ValueError("Liczba musi być nieujemna.")
    
    ε = 10 ** (-prec)

    b = p / 2.0

    while True:
        a = p / b
        nowy_b = (a + b) / 2.0
        if abs(nowy_b - b) < ε:
            return nowy_b
        b = nowy_b

def main():
    a, b = liczby()
    if isinstance(a, int) and isinstance(b, int):
        return pierwiastek(a, b)

main()