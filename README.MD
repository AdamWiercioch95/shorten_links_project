# Zadanie rekrutacyjne - CodersLab - kurs Python

## Wstęp
Prezentowane zadanie, jest okazją by zaprezentować Twoje dotychczasowe doświadczenie, Twój styl oraz Twój sposób pracy - i zaprezentować swoję umiejętności, wiedzę oraz znajomość narzędzi i technologii zdobytą w trakcie kursu.

W ramach prezentowanego zadania będziesz miał/miała okazję zaprezentować swoje umiejętności w następujących obszarach:

* HTML i CSS,
* Python,
* Bazy danych,
* Django,
* najlepsze praktyki.

## Wprowadzenie
Zadanie polega na stworzeniu, w oparciu o framework Django, systemu dającego możliwość skracania linków. Poniżej znajdziesz spis adresów, które twoja aplikacja powinna obsługiwać.

Screeny przedstawione poniżej są tylko poglądaowe - kwestie interfejsu użytkownika (UI) i związanych z nim doświadczeń zostawiamy tobie. Aplikacja nie będzie oceniana pod względem wyglądu.

### Rejestracja użytkowników: `/register/`

Rejestracja wymaga podania loginu, dwa razy hasła oraz adresu email. Formularz sprawdza czy login jest wolny, email jest wolny oraz czy hasła są takie same.

Po udanej rejestracji użytkownik powinien być od razu zalogowany, i przekierowany na stronę główną.

![Rejestracja](./images/register.png)

![Rejestracja - błędy](./images/register-errors.png)

### Strona logowania: `/login/`

Użytkownicy mogą się tutaj zalogować. Po udanym logowaniu powinni zostać przekierowani na stronę główną.

![Logowanie](./images/login.png)

W przypadku podania błędnych danych, odpowiedni komunikat powinien pojawić się ponad formularzem:

![Logowanie - błędy](./images/login-errors.png)

### Strona główna: `/`

Zawiera formularz do skracania linków (z walidacją poprawności adresu URL) oraz listę linków skróconych wcześniej, należących do obecnie zalogowanego użytkownika.

Jeśli użytkownik jest niezalogowany, powinien zostać przekierowany na adres `/login/`.

![Strona główna](./images/empty-index.png)

Dodanie nowego linku powinno zakończyć się przekierowaniem na stronę szczegółów linku: `/my-links/TUTAJ-WSTAW-ID-LINKU/`.

Po dodaniu kilku linków strona powinna wyglądać tak:

![Strona główna - z danymi](./images/filled-index.png)

Linki widoczne na obrazku powyżej nie prowadzą bezpośrednio do stron, które reprezentują - zamiast tego prowadzą na adres `http://localhost:8000/TUTAJ-WSTAW-ID-LINKU/`.

Przyciski "Usuń" pozwalają na usunięcie wpisu z bazy danych.

### Widok szczegółów linku: `/my-links/TUTAJ-WSTAW-ID-LINKU/`

Tutaj jest zaprezentowany link w swojej oryginalnej postaci oraz skróconej. Próba wejścia na stronę szczegółów nie swojego linku powinna skończyć się przekierowaniem na stronę główną.

![Szczegóły linku](./images/details.png)

### Widok przekierowania: `/TUTAJ-WSTAW-ID-LINKU/`

Ten widok nie posiada swojego szablonu. Jego rolą jest odczytanie z bazy adresu docelowego dla linku o wskazanym `pk` oraz przekierowanie przeglądarki na ten adres.

Jeśli link o podanym `pk` nie istnieje, przeglądarka powinna zostać przekierowana na stronę główną.


## Check-lista

### Zadania obowiązkowe

- [ ] Aplikacja oparta o `Django`.
- [ ] Struktura routingu, która umożliwia użytkownikowi swobodne przechodzenie pomiędzy widokami:
  * Strona główna (`/`),
  * Strona rejestracji (`/register/`),
  * Strona logowania (`/login/`),
  * Widok szczegółów linku (`/my-links/TUTAJ-WSTAW-ID-LINKU/`),
  * Widok przekierowania (`/TUTAJ-WSTAW-ID-LINKU/`),  
  * Strona logowania (`/login/`),
- [ ] Funkcjonalność umożliwiająca rejestrację oraz zalogowanie użytkownika,
- [ ] Funkcjonalność umożliwiająca zapisanie linku do bazy danych i wygenerowanie do niego unikatowego ID,
- [ ] Funkcjonalność umożliwiająca usuwanie stworzonych wcześniej linków,
- [ ] Funkcjonalność przekierowania do zapamiętanego adresu.

## Uwagi końcowe

- Możesz użyć pliku README do zapisania swoich uwag i spostrzeżeń dotyczących wykonywanego zadania. Możesz również wykorzystać ten plik do zaprezentowania swojego punktu widzenia dotyczącego procesu realizacji zadania.

- Upewnij się, że w Twoim kodzie nie ma błędów (generujących ostrzeżenia lub błędy w konsoli). Lepiej gdy, któryś z punktów nie zostanie dostarczony, aniżeli dostarczysz go zaimplementowanego nieprawidłowo.

# Dodatkowe informacje

Do stylowania strony zastosuj dowolny styl/framework z tej listy: [https://github.com/dbohdan/classless-css](https://github.com/dbohdan/classless-css). Styl z obrazków powyżej pochodzi z [https://github.com/kognise/water.css](https://github.com/kognise/water.css).


