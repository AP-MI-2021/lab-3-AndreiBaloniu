def menu():
    print('1.Citire date')
    print('2.Determinare cea mai lunga subsecventa cu proprietatea ca toate numerele sunt palindroame')
    print('3.Determinarea cea mai lunga subsecventa cu proprietatea ca toate numerele se pot scrie ca x**k')
    print('4.Iesire din program')


def citire_lista():
    lista = []
    lista_str = input('Dati numerele separate prin spatiu: ')
    lista_str_split = lista_str.split(' ')
    for num_str in lista_str_split:
        lista.append(int(num_str))
    return lista


def get_palindrome(nr):
    # Determina palindromul unui numar dat
    inv = nr
    palindrome = 0
    while inv > 0:
        palindrome = palindrome * 10 + inv % 10
        inv = inv // 10
    if palindrome == nr:
        return 1
    return 0


def get_longest_all_palindromes(lst):
    # Determina cea mai lunga subsecventa cu proprietatea ca toate numerele sunt palindroame
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
    assert get_longest_all_palindromes([1221, 14, 123321, 12221, 131]) == [123321, 12221, 131]
    assert get_longest_all_palindromes([14, 15, 121, 414, 17, 19]) == [121, 414]


def get_power_of_k(nr: int, k: int):
    # Determina daca un numar se poate scrie ca x la puterea k
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
    # Determina cea mai lunga subsecventa cu proprietatea ca toate numerele se pot scrie ca x la puterea k
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
    assert get_longest_powers_of_k([8, 9, 16, 25, 121, 13, 412, 4, 49], 2) == [9, 16, 25, 121]
    assert get_longest_powers_of_k([1, 8, 27, 64, 8, 2, 27], 3) == [8, 27, 64, 8]


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
            break
        else:
            print('Optiune invalida.')


test_get_longest_all_palindromes()
test_get_longest_powers_of_k()
main()
