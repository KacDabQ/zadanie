Aby obliczyć pierwiastek kwadratowy z danej liczby z zadaną dokładnością możemy posłużyć się następującą procedurą. Zauważamy, że pierwiastek kwadratowy z danej liczby to długość boku kwadratu o polu równym tej liczbie. Wobec tego wychodzimy od dowolnego prostokąta o polu równym zadanej liczby (oznaczmy go p) i ustalamy dowolnie jeden bok (b). Obliczamy długość drugiego boku (a) - stanowi to dla nas pierwsze przybliżenie pierwiastka. Następnie powtarzamy procedurę ustalając bok b jako średnią arytmetyczną boków z poprzedniego kroku. Kończymy iterować w momencie kiedy błąd (wyrażony przez wartość bezwzględną różnicy między bokami osiągnie założoną wartość (ε).

## ZADANIE:

Napisać program, który przyjmie na wejściu od użytkownika dwie liczby całkowite: liczbę do spierwiastkowania oraz ilość miejsc po przecinku, które mają być pewne, a następnie zwróci użytkownikowi wynik. Wszystkie elementy rozwiązania powinny być zaopatrzone w testy, powinny być również uwzględnione przypadki brzegowe.

### PRZYKŁADOWE WEJŚCIE:

4
2

### PRZYKŁADOWE WYJŚCIE:

2.0
