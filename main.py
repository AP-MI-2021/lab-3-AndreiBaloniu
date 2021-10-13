def menu():
    print('1.Citire date')
    print('2.Determinare cea mai lunga subsecventa cu proprietatea ca toate numerele sunt palindroame')
    print('3.Determinarea cea mai lunga subsecventa cu proprietatea ca toate numerele se pot scrie ca x**k')
    print('4.Determinare cea mai lunga subsecventa cu proprieteatea ca toate numerele sunt intr-o progresie aritmetica')
    print('5.Iesire din program')


def citire_lista():
    lista = []
    lista_str = input('Dati numerele separate prin spatiu: ')
    lista_str_split = lista_str.split(' ')
    for num_str in lista_str_split:
        lista.append(int(num_str))
    return lista


def get_palindrome(nr):
    """
    Determina daca un numar este palindrom
    :param nr: numar
    :return: 1 daca e palindrom, 0 in caz contrar
    """
    inv = nr
    palindrome = 0
    while inv > 0:
        palindrome = palindrome * 10 + inv % 10
        inv = inv // 10
    if palindrome == nr:
        return 1
    return 0


def get_longest_all_palindromes(lst):
    """
    Determina cea mai lunga subsecventa cu proprietatea ca toate numerele sunt palindroame
    :param lst: lista cu care lucram
    :return: rezultat -> cea mai lunga subsecventa cu proprietatea ca toate numerele sunt palindrome
    """
    # lungimea listei
    n = len(lst)
    rezultat = []
    for stanga in range(n):
        for dreapta in range(stanga, n):
            all_palindromes = True
            for num in lst[stanga:dreapta + 1]:
                if get_palindrome(num) == 0:
                    all_palindromes = False
                    break
            if all_palindromes:
                if dreapta - stanga + 1 > len(rezultat):
                    rezultat = lst[stanga:dreapta + 1]
    return rezultat


def test_get_longest_all_palindromes():
    # Aceasta functie verifica daca functia get_longest_all_palindromes returneaza corect cea mai lunga subsecventa de palindroame
    assert get_longest_all_palindromes([1221, 14, 123321, 12221, 131]) == [123321, 12221, 131]
    assert get_longest_all_palindromes([14, 15, 121, 414, 17, 19]) == [121, 414]


def get_power_of_k(nr: int, k: int):
    """
    Determina daca un numar se poate scrie ca x la puterea k
    :param nr: numar
    :param k: putere
    :return: 1 daca un nr se poate scrie ca x la puterea k, 0 in caz contrar
    """
    if nr == 1 and k == 0:
        return 1
    for i in range(2, nr):
        nou = 1
        putere = 0
        while nou < nr:
            nou = nou * i
            putere = putere + 1
        if nou == nr and putere == k:
            return 1
    return 0


def get_longest_powers_of_k(lst, k):
    """
    Determina cea mai lunga subsecventa cu proprietatea ca toate numerele se pot scrie ca x la puterea k
    :param lst: lista de numere cu care lucram
    :param k: puterea
    :return: rezultat -> cea mai mare subsecventa cu proprietatea ca toate numerele se pot scrie sub forma de x**k
    """
    n = len(lst)
    rezultat = []
    for stanga in range(n):
        for dreapta in range(stanga, n):
            all_powers_of_k = True
            for num in lst[stanga:dreapta + 1]:
                if get_power_of_k(num, k) == 0:
                    all_powers_of_k = False
                    break
            if all_powers_of_k:
                if dreapta - stanga + 1 > len(rezultat):
                    rezultat = lst[stanga:dreapta + 1]
    return rezultat


def test_get_longest_powers_of_k():
    # Aceasta functie verifica daca functia get_longest_powers_of_k returneaza corect cea mai lunga subsecventa denumere de forma x**k
    assert get_longest_powers_of_k([8, 9, 16, 25, 121, 13, 412, 4, 49], 2) == [9, 16, 25, 121]
    assert get_longest_powers_of_k([1, 8, 27, 64, 8, 2, 27], 3) == [8, 27, 64, 8]


def get_arithmetic_progression(lst):
    """
    Aceasta functie determina numerele ce sunt in progresie aritmetica
    :param lst: lista de numere cu care lucram
    :return: True daca numerele sunt in progresie aritmetica, False in caz contrar
    """
    ratie = 0
    if len(lst) > 1:
        # calculam ratia dintre 2 termeni consecutivi (r = a2 - a1)
        ratie = lst[1] - lst[0]
    for nr in range(2, len(lst)):
        # verificam daca ratia ramane aceeasi
        if lst[nr] - lst[nr - 1] != ratie:
            return False
    return True


def get_longest_arithmetic_progression(lst):
    """
    Aceasta functie returneaza cea mai lunga subsecventa de numere in progresie aritmetica
    :param lst: lista de numere cu care lucram
    :return: rezultat -> cea mai mare subsecventa de numere in progresie aritmetica
    """
    # lungimea listei
    n = len(lst)
    rezultat = []
    for stanga in range(n):
        for dreapta in range(stanga, n):
            if get_arithmetic_progression(lst[stanga:dreapta + 1]):
                if len(rezultat) < len(lst[stanga:dreapta + 1]):
                    rezultat = lst[stanga:dreapta + 1]
    return rezultat


def test_get_longest_arithmetic_progression():
    # Aceasta functie verifica daca functia get_longest_arithmetic_progression returneaza corect cea mai lunga subsecventa de numere in progresie aritmetica
    assert get_longest_arithmetic_progression([12, 15, 18, 2, 31, 45124, 2323]) == [12, 15, 18]
    assert get_longest_arithmetic_progression([2, 4, 6, 8, 5, 35, 65, 95, 125]) == [5, 35, 65, 95, 125]
    assert get_longest_arithmetic_progression([1, 2, 3, 4, 5, 6]) == [1, 2, 3, 4, 5, 6]


def main():
    lst = []
    while True:
        menu()
        opt = input('Optiunea: ')
        if opt == '1':
            lst = citire_lista()
        elif opt == '2':
            print(f'Cea mai lunga subsecventa de numere palindroame este: {get_longest_all_palindromes(lst)}.')
        elif opt == '3':
            putere = int(input('Dati valoarea lui k: '))
            print(f'Cea mai lunga subsecventa de numere sub forma x la k este: {get_longest_powers_of_k(lst, putere)}.')
        elif opt == '4':
            print(f'Cea mai lunga subsecventa de numere in progresie aritmetica: {get_longest_arithmetic_progression(lst)}')
        elif opt == '5':
            break
        else:
            print('Optiune invalida.')


test_get_longest_all_palindromes()
test_get_longest_powers_of_k()
test_get_longest_arithmetic_progression()
main()
