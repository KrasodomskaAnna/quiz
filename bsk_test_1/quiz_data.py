quiz_data = [
  {
    "question": "Czym jest atak ze znanym szyfrogramem? (What is an attack with a known ciphertext?) Wybierz jedną lub więcej: (slajd 35)",
    "choices": [
      {
        "answer": "Odtworzeniem tekstu jawnego na podstawie znajomości części klucza\n(Restoring of plaintext basing on the knowledge of the part of the key)",
        "correct": "false"
      },
      {
        "answer": "Odtworzeniem tekstu jawnego na podstawie przechwyconego szyfrogramu\n(Restoring of plaintext basing on the intercepted ciphertext)",
        "correct": "true"
      },
      {
        "answer": "Odtworzeniem tekstu jawnego na podstawie znajomości szyfrogramu i fragmentu tekstu jawnego\n(Restoring of plaintext basing on the knowledge of the ciphertext and a part of plaintext)",
        "correct": "false"
      },
      {
        "answer": "Odtworzeniem tekstu jawnego na podstawie liczby przesłanych szyfrogramów\n(Restoring of plaintext basing on the number of transmitted ciphertexts)",
        "correct": "false"
      }
    ]
  },
  {
    "question": "Funkcja skrótu umożliwia (Hash function allows...) Wybierz jedną lub więcej:",
    "choices": [
      {
        "answer": "Wytworzenie tzw skrótu wiadomości o stałej długości\n(to create the so-called hash of fixed length)",
        "correct": "true"
      },
      {
        "answer": "Zaszyfrowanie danych użytkownika (to encrypt the user data)",
        "correct": "true"
      },
      {
        "answer": "Wytworzenie tzw skrótu wiadomości o długości zgodnej z danymi wejściowymi\n(to create the so-called a hash of a length same as the length of the input data)",
        "correct": "false"
      },
      {
        "answer": "Uprzypadkowienie danych podczas transmisji strumieniowej\n(to randomize the data during the data streaming)",
        "correct": "false"
      }
    ]
  },
  {
    "question": "Jak potocznie nazywa się kolejne cykle obliczeń wykonywanych w algorytmie Rijndael? Wybierz jedną lub więcej: (slajd 75)",
    "choices": [
      {
        "answer": "Serie (Series)",
        "correct": "false"
      },
      {
        "answer": "Iteracje (Iterations)",
        "correct": "false"
      },
      {
        "answer": "Rundy (Rounds)",
        "correct": "true"
      },
      {
        "answer": "Cykle (Cycles)",
        "correct": "false"
      }
    ]
  },
  {
    "question": "Podpis cyfrowy umożliwia (Digital signature allows to) Wybierz jedną lub więcej (slajd 98)",
    "choices": [
      {
        "answer": "Wskazanie odbiorcy rodzaju dokumentu / pliku",
        "correct": "false"
      },
      {
        "answer": "Poświadczenie autentyczności dokumentu",
        "correct": "true"
      },
      {
        "answer": "Załączenie do dokumentu jego atrybutów",
        "correct": "false"
      },
      {
        "answer": "Zaszyfrowanie dokumentu o dowolnej długości",
        "correct": "false"
      }
    ]
  },
  {
    "question": "Wyciekiem danych nazywamy... (A data leak is a ...) Wybierz jedną lub więcej (slajd 226)",
    "choices": [
      {
        "answer": "Odtajnienie danych niejawnych",
        "correct": "false"
      },
      {
        "answer": "Ujawnienie pewnej ilości danych osobom innym niż administratorzy systemu",
        "correct": "false"
      },
      {
        "answer": "Niewykrywalny przepływ danych do osób nieuprawnionych",
        "correct": "true"
      },
      {
        "answer": "Bezpieczne przekazanie danych osobom trzecim, np w postaci zaszyfrowanej",
        "correct": "false"
      }
    ]
  },
  {
    "question": "Podczas analizy ryzyka i próbie zwiększenia bezpieczeństwa... (During the risk analysis and an attempt to increase safety ...) Wybierz jedną lub więcej: (slajd 136)",
    "choices": [
      {
        "answer": "Dąży się do minimalizacji parametru MTBF minimalizując liczbę krytycznych urządzeń",
        "correct": "false"
      },
      {
        "answer": "Poszukuje się optimum pomiędzy nakładem środków a minimalizacją ryzyka",
        "correct": "true"
      },
      {
        "answer": "Wybierane są rozwiązania o najniższym koszcie, aby zminimalizować koszty działalności",
        "correct": "false"
      },
      {
        "answer": "Podejmuje się próbę minimalizacji ryzyka za wszelką cenę",
        "correct": "false"
      }
    ]
  },
  {
    "question": "Jakie jest podstawowe założenie system detekcji intruzów? (What is the basic assumption of an intrusion detection system?) Wybierz jedną lub więcej: (slajd 250, 254)",
    "choices": [
      {
        "answer": "Możliwe jest wykrycie intruza",
        "correct": "true"
      },
      {
        "answer": "System detekcji intruzów zajmuje minimalną część zasobów systemu",
        "correct": "false"
      },
      {
        "answer": "System detekcji intruzów jest odporny na ataki typu Denial of Service",
        "correct": "true"
      },
      {
        "answer": "Włamania wykrywane są z prawdopodobieństwem bliskim 100%",
        "correct": "false"
      }
    ]
  },
  {
    "question": "Udzieleniem uprawnień do wykonania określonych działań nazywamy... (Granting permissions to perform specific activities is called...) Wybierz jedną lub więcej: (slajd 3)",
    "choices": [
      {
        "answer": "Zapewnienie prywatności",
        "correct": "false"
      },
      {
        "answer": "Zapewnienie poufności",
        "correct": "false"
      },
      {
        "answer": "Uwierzytelnienie",
        "correct": "false"
      },
      {
        "answer": "Autoryzację",
        "correct": "true"
      }
    ]
  },
  {
    "question": "Który z trybów szyfrowania nie zapewnia powiązania pomiędzy blokami szyfrogramu? (Which of the encryption modes does not provide a connection between the cipher blocks?) Wybierz jedną lub więcej: (slajd 43, 36)",
    "choices": [
      {
        "answer": "CFB",
        "correct": "false"
      },
      {
        "answer": "CBC",
        "correct": "false"
      },
      {
        "answer": "OFB",
        "correct": "false"
      },
      {
        "answer": "ECB",
        "correct": "true"
      }
    ]
  },
  {
    "question": "Detekcja sygnaturowa w systemach detekcji intruzów polega na: (The signature detection in the IDS systems is based on:) Wybierz jedną lub więcej: (slajd 257)",
    "choices": [
      {
        "answer": "Wykryciu anomalii w zwyczajnym działaniu systemu",
        "correct": "false"
      },
      {
        "answer": "Wykryciu stopniowej zmiany zachowań użytkowników",
        "correct": "false"
      },
      {
        "answer": "Wykryciu charakterystycznych zachowań w działaniu systemu",
        "correct": "true"
      },
      {
        "answer": "Wykryciu uruchomienia programu z innymi uprawnieniami",
        "correct": "false"
      }
    ]
  },
  {
    "question": "Jakie główne zagrożenie niesie powszechna dostępność narzędzi do przeprowadzenia ataków penetracyjnych?",
    "choices": [
      {
        "answer": "Możliwość niewykrycia wszystkich słabych punktów systemu z racji niedoskonałości oprogramowania",
        "correct": "false"
      },
      {
        "answer": "Umożliwienie przeprowadzenia prostych ataków na systemy informatyczne przez prawie każdą osobę",
        "correct": "true"
      },
      {
        "answer": "Możliwość testowania opracowywanych systemów informatycznych w celu sprawdzenia ich odporności na przykładowe ataki",
        "correct": "false"
      },
      {
        "answer": "Długi czas testów z użyciem gotowych narzędzi",
        "correct": "false"
      }
    ]
  },
  {
    "question": "Do jakiej grupy szyfrów należy algorytm Rijndael/AES?",
    "choices": [
      {
        "answer": "Szyfry blokowe symetryczne",
        "correct": "true"
      },
      {
        "answer": "Szyfry blokowe asymetryczne",
        "correct": "false"
      },
      {
        "answer": "Szyfry strumieniowe asymetryczne",
        "correct": "false"
      },
      {
        "answer": "Szyfry strumieniowe symetryczne",
        "correct": "false"
      }
    ]
  },
  {
    "question": "Na czym polega jednokierunkowość funkcji skrótu? (What is the principle of operation of the one-direction hash function?) Wybierz jedną lub więcej: (slajd 80)",
    "choices": [
      {
        "answer": "Niemożność odtworzenia danych na podstawie skrótu",
        "correct": "true"
      },
      {
        "answer": "Niemożność wykonania skrótu z wykonanego skrótu",
        "correct": "false"
      },
      {
        "answer": "Niemożność wykonania skrótu wiadomości o długości innej niż wytwarzany skrót",
        "correct": "false"
      },
      {
        "answer": "Niemożność wykonania skrótu przez osobę weryfikującą wytworzony skrót wiadomości",
        "correct": "false"
      }
    ]
  },
  {
    "question": "Protokół Kerberos jest... (Kerberos protocol is ...) Wybierz jedną lub więcej: (slajd 31)",
    "choices": [
      {
        "answer": "Protokołem negocjacji zabezpieczeń i ustalania szybkości szyfrowania",
        "correct": "false"
      },
      {
        "answer": "Protokołem uwierzytelnienia symetrycznego",
        "correct": "true"
      },
      {
        "answer": "Protokołem uwierzytelniania asymetrycznego",
        "correct": "false"
      },
      {
        "answer": "Protokołem stosowanym do szyfrowania transmisji danych strumieniowych",
        "correct": "false"
      }
    ]
  },
  {
    "question": "Jak nie należy chronić systemu przed atakami typu Denial of Service?",
    "choices": [
      {
        "answer": "Regularnie monitorować działanie systemu",
        "correct": "false"
      },
      {
        "answer": "Implementując rozwiązania zalecanych przez instytucje standaryzujące",
        "correct": "false"
      },
      {
        "answer": "Stosować śluzy ogniowe nieblokujące pakietów rozgłoszeniowych",
        "correct": "true"
      },
      {
        "answer": "Stosować hartowanie systemu",
        "correct": "false"
      }
    ]
  },
  {
    "question": "Które z elementów nie podlegają uwierzytelnieniu?",
    "choices": [
      {
        "answer": "Odbiorca dokumentów",
        "correct": "false"
      },
      {
        "answer": "Zawartość dokumentów",
        "correct": "false"
      },
      {
        "answer": "Źródło wirusów komputerowych",
        "correct": "true"
      },
      {
        "answer": "Osoba przesyłająca dokumenty",
        "correct": "false"
      }
    ]
  },
  {
    "question": "Wskaż cechę algorytmu RSA",
    "choices": [
      {
        "answer": "Nie jest używany w protokołach bezpiecznej wymiany danych",
        "correct": "false"
      },
      {
        "answer": "Jest on przeznaczony do szyfrowania danych strumieniowych",
        "correct": "false"
      },
      {
        "answer": "Jest wolniejszy niż algorytm Rijndael / AES",
        "correct": "true"
      },
      {
        "answer": "Można go użyć do uwierzytelniania użytkowników",
        "correct": "true"
      }
    ]
  },
  {
    "question": "Atak typu Man in the Middle w sieciach typu 802.11 polega na:",
    "choices": [
      {
        "answer": "Tworzeniu fałszywej stacji AP i pośredniczenie w komunikacji użytkowników",
        "correct": "true"
      },
      {
        "answer": "Wytworzenie fałszywej wiadomości, która będzie potraktowana jako rzeczywista",
        "correct": "false"
      },
      {
        "answer": "Wytworzeniu silnego sygnału zagłuszającego blokującego transmisję",
        "correct": "false"
      },
      {
        "answer": "Wysyłaniu pakietów rozgłoszeniowych do dwóch użytkowników",
        "correct": "false"
      }
    ]
  },
  {
    "question": "Wskaż typ audytu",
    "choices": [
      {
        "answer": "Finansowy",
        "correct": "true"
      },
      {
        "answer": "Operacyjny",
        "correct": "true"
      },
      {
        "answer": "Informatyczny",
        "correct": "true"
      },
      {
        "answer": "Moralny",
        "correct": "false"
      }
    ]
  },
  {
    "question": "Protokół SESAME umożliwia...",
    "choices": [
      {
        "answer": "Kontrolę dostępu do zasobów i usług opartych na uwierzytelnianiu",
        "correct": "false"
      },
      {
        "answer": "Pracę wyłącznie w rozproszonym środowisku heterogenicznym",
        "correct": "false"
      },
      {
        "answer": "Zapewnienia spójności i tajności przesyłanych danych",
        "correct": "true"
      },
      {
        "answer": "Unifikacji tylko użytkownika z punktu widzenia uprawnień",
        "correct": "false"
      }
    ]
  },
  {
    "question": "Jakie jest prawdopodobieństwo przechwycenia danych przez osobę nieuprawnioną w przypadku użycia dowodu o wiedzy zerowej?",
    "choices": [
      {
        "answer": "Prawdopodobieństwo jest bliskie zeru",
        "correct": "true"
      },
      {
        "answer": "Prawdopodobieństwo jest równe zero",
        "correct": "false"
      },
      {
        "answer": "Prawdopodobieństwo wynosi 1",
        "correct": "false"
      },
      {
        "answer": "Prawdopodobieństwo wynosi 0,5",
        "correct": "false"
      }
    ]
  },
  {
    "question": "Czym charakteryzują się klucze w kryptografii symetrycznej i asymetrycznej?",
    "choices": [
      {
        "answer": "W każdym przypadku te same klucze używane są do szyfrowania i deszyfrowania",
        "correct": "false"
      },
      {
        "answer": "Klucze są takiej samej długości",
        "correct": "false"
      },
      {
        "answer": "W kryptografii asymetrycznej jeden z kluczy jest jawny",
        "correct": "true"
      },
      {
        "answer": "Klucze nie mogą być wytwarzane przez użytkowników",
        "correct": "false"
      }
    ]
  },
  {
    "question": "Którą z linii przesyłowych da się podsłuchać?",
    "choices": [
      {
        "answer": "Linię przewodową typu RS-232/RS-485",
        "correct": "true"
      },
      {
        "answer": "Połączenie radiowe",
        "correct": "true"
      },
      {
        "answer": "Linię optyczną",
        "correct": "true"
      },
      {
        "answer": "Linię przewodową sieci Ethernet/Token Ring",
        "correct": "true"
      }
    ]
  },
  {
    "question": "Jaki rodzaj kryptografii stosowany jest w odniesieniu do kart inteligentnych?",
    "choices": [
      {
        "answer": "Symetryczna, np algorytm RSA",
        "correct": "false"
      },
      {
        "answer": "Asymetryczna, np algorytm RSA",
        "correct": "true"
      },
      {
        "answer": "Symetryczne klucze jednorazowe",
        "correct": "false"
      },
      {
        "answer": "Symetryczne funkcje skrótu",
        "correct": "false"
      }
    ]
  },
  {
    "question": "Gdzie nie spotyka się systemów detekcji intruzów?",
    "choices": [
      {
        "answer": "W obszarze sieci szkieletowej",
        "correct": "false"
      },
      {
        "answer": "Po stronie serwerów WWW",
        "correct": "false"
      },
      {
        "answer": "Wewnątrz sieci lokalnych",
        "correct": "false"
      },
      {
        "answer": "W obrębie sieci za zaporą ogniową",
        "correct": "false"
      }
    ]
  },
  {
    "question": "Który z modeli kontroli dostępu umożliwia zastosowanie dodatkowego modelu kontroli dostępu?",
    "choices": [
      {
        "answer": "TE",
        "correct": "false"
      },
      {
        "answer": "MAC",
        "correct": "true"
      },
      {
        "answer": "DAC",
        "correct": "true"
      },
      {
        "answer": "RBAC",
        "correct": "true"
      }
    ]
  },
  {
    "question": "Fałszywym odrzuceniem nazywamy",
    "choices": [
      {
        "answer": "Anulowanie działania w przypadku zaistnienia zdarzenia o wyższym priorytecie",
        "correct": "false"
      },
      {
        "answer": "Zaprzestanie działań prewencyjnych w trakcie usuwania zagrożenia",
        "correct": "false"
      },
      {
        "answer": "Odrzucenie zdarzenia będącego zagrożeniem",
        "correct": "false"
      },
      {
        "answer": "Odrzucenie zagrożenia niebędącym krytycznym zagrożeniem",
        "correct": "true"
      }
    ]
  },
  {
    "question": "Który ze standardów nie dotyczy sieci radiowych Wi-Fi/Bluetooth/WiMax?",
    "choices": [
      {
        "answer": "802.11i (Wiki: WPA2)",
        "correct": "false"
      },
      {
        "answer": "802.11.ax (Wiki: WiFi 6)",
        "correct": "false"
      },
      {
        "answer": "802.16e (dotyczy WiMax)",
        "correct": "false"
      },
      {
        "answer": "802.15.2",
        "correct": "true"
      }
    ]
  },
  {
    "question": "Atak typu sniffing polega na ...",
    "choices": [
      {
        "answer": "Podszyciu się pod innego użytkownika",
        "correct": "false"
      },
      {
        "answer": "Przechwytywaniu pakietów sieciowych",
        "correct": "true"
      },
      {
        "answer": "Przejęciu dostępnych zasobów sieciowych",
        "correct": "false"
      },
      {
        "answer": "Fałszowaniu kluczy uwierzytelniających",
        "correct": "false"
      }
    ]
  },
  {
    "question": "Który z rodzajów spoofingu jest prawdziwy?",
    "choices": [
      {
        "answer": "Spoofing APR",
        "correct": "true"
      },
      {
        "answer": "Spoofing TCP",
        "correct": "true"
      },
      {
        "answer": "Spoofing DNS",
        "correct": "true"
      },
      {
        "answer": "Spoofing SSL",
        "correct": "false"
      }
    ]
  },
  {
    "question": "Atak typu Denial of Service polega na:",
    "choices": [
      {
        "answer": "Zmniejszeniu prawdopodobieństwa wykrycia ataku",
        "correct": "false"
      },
      {
        "answer": "Wykradzeniu tajnych danych użytkownika",
        "correct": "false"
      },
      {
        "answer": "Uniemożliwieniu normalnego działania systemu",
        "correct": "true"
      },
      {
        "answer": "Usunięciu danych użytkownika",
        "correct": "false"
      }
    ]
  },
  {
    "question": "Jaki rodzaj ramek jest spotykany w sieci typu 802.11?",
    "choices": [
      {
        "answer": "Ramki danych",
        "correct": "false"
      },
      {
        "answer": "Ramki organizacyjne",
        "correct": "false"
      },
      {
        "answer": "Ramki szyfrujące",
        "correct": "true"
      },
      {
        "answer": "Ramki sterujące",
        "correct": "false"
      }
    ]
  },
  {
    "question": "Który rodzaj wirusa komputerowego dopisuje swój kod za kodem zasadniczym programu?",
    "choices": [
      {
        "answer": "Overwrite",
        "correct": "false"
      },
      {
        "answer": "Prepender",
        "correct": "false"
      },
      {
        "answer": "Appender",
        "correct": "true"
      },
      {
        "answer": "Apprepender",
        "correct": "false"
      }
    ]
  },
  {
    "question": "Obniżenie przepustowości sieci może być powodowane przez:",
    "choices": [
      {
        "answer": "Zastosowaniu systemu detekcji intruzów pochłaniającego zasoby systemu",
        "correct": "false"
      },
      {
        "answer": "Nieautoryzowanym zajęciu większości zasobów czasowo-częstotliwościowych sieci",
        "correct": "true"
      },
      {
        "answer": "Sporadycznym przesyłaniu pakietów IP ze zmodyfikowanym nagłówkiem",
        "correct": "false"
      },
      {
        "answer": "Celowym korzystaniu ze skomplikowanego algorytmu zabezpieczającego transmisję (algorytmu szyfrującego)",
        "correct": "false"
      }
    ]
  },
  {
    "question": "Czym jest transakcja?",
    "choices": [
      {
        "answer": "Procedura realizowana zawsze bez obecności TTP",
        "correct": "false"
      },
      {
        "answer": "Zestaw instrukcji przeznaczony do wykrywania nieautoryzowanego dostępu",
        "correct": "false"
      },
      {
        "answer": "Jest to element protokołu sieciowego TCP/IP",
        "correct": "false"
      },
      {
        "answer": "Unormowana procedura wykonywana przez dwie strony",
        "correct": "true"
      }
    ]
  },
  {
    "question": "Które z protokołów używane są w procesie uwierzytelnienia w sieci 802.11?",
    "choices": [
      {
        "answer": "802.1x, LEAP",
        "correct": "true"
      },
      {
        "answer": "Radius, PEAP",
        "correct": "true"
      },
      {
        "answer": "WPF, EAP-MD5",
        "correct": "false"
      },
      {
        "answer": "WAP, PEAP",
        "correct": "false"
      }
    ]
  },
  {
    "question": "Do procesu zarządzania transakcjami należy...",
    "choices": [
      {
        "answer": "Przeprowadzenie jedynie certyfikacji, bez konieczności weryfikacji poprawności transakcji",
        "correct": "false"
      },
      {
        "answer": "Rejestrowanie i unieważnienie transakcji",
        "correct": "true"
      },
      {
        "answer": "Archiwizowanie certyfikatów transakcji",
        "correct": "true"
      },
      {
        "answer": "Pominięcie procesu weryfikacji zaufanych klientów",
        "correct": "false"
      }
    ]
  },
  {
    "question": "Które z narzędzi nie jest wykorzystywane podczas realizowania transakcji internetowych?",
    "choices": [
      {
        "answer": "Algorytmy kryptograficzne",
        "correct": "false"
      },
      {
        "answer": "System detekcji intruzów",
        "correct": "true"
      },
      {
        "answer": "Generatory liczb pseudolosowych",
        "correct": "false"
      },
      {
        "answer": "Jednokierunkowe funkcje skrótu",
        "correct": "false"
      }
    ]
  },
  {
    "question": "Która z akcji nie jest przypisywana działaniu wirusów typu robak?",
    "choices": [
      {
        "answer": "Modyfikowanie programu gospodarza",
        "correct": "false"
      },
      {
        "answer": "Zajęcie dostępnych zasobów systemu operacyjnego",
        "correct": "false"
      },
      {
        "answer": "Usuwanie i niszczenie danych",
        "correct": "false"
      },
      {
        "answer": "Wykradzenie danych użytkownika",
        "correct": "true"
      }
    ]
  },
  {
    "question": "W sieciach radiowych zgodnych ze standardem Bluetooth...",
    "choices": [
      {
        "answer": "Wprowadzany numer PIN używany jest jako identyfikator użytkownika w danej sieci",
        "correct": "true"
      },
      {
        "answer": "Stosowana jest kryptografia symetryczna w procesie uwierzytelnienia oraz podczas szyfrowania przesyłanych danych",
        "correct": "true"
      },
      {
        "answer": "Możliwe jest przesyłanie danych pomiędzy dwoma użytkownikami na dystansie do 200 m",
        "correct": "false"
      },
      {
        "answer": "Nie stosuje się szyfrowania wzajemnego uwierzytelnienia",
        "correct": "false"
      }
    ]
  },
  {
    "question": "Które z zagrożeń/problemów nie dotyczy wektorów inicjujących?",
    "choices": [
      {
        "answer": "Licznikowy tryb wytwarzania wektorów inicjujących",
        "correct": "false"
      },
      {
        "answer": "Losowość generowanych wektorów inicjujących",
        "correct": "true"
      },
      {
        "answer": "Kolizja wektorów inicjujących",
        "correct": "false"
      },
      {
        "answer": "Znany początkowy stan generatora wektorów inicjujących",
        "correct": "false"
      }
    ]
  },
  {
    "question": "W procesie zabezpieczania systemu informatycznego udział biorą...",
    "choices": [
      {
        "answer": "Wyłącznie pracownicy firm zewnętrznych",
        "correct": "false"
      },
      {
        "answer": "Osoby na szczeblu kierowniczym",
        "correct": "true"
      },
      {
        "answer": "Osoby zarządzające oraz pracownicy firmy",
        "correct": "true"
      },
      {
        "answer": "Osoby zarządzające, pracownicy oraz użytkownicy",
        "correct": "false"
      }
    ]
  },
  {
    "question": "Jaka trudność występuje podczas implementacji modelu RBAC?",
    "choices": [
      {
        "answer": "Trudność w administrowaniu systemu",
        "correct": "false"
      },
      {
        "answer": "Trudność w dopasowaniu ról do struktury organizacji",
        "correct": "true"
      },
      {
        "answer": "Ograniczenie liczby możliwych ról",
        "correct": "false"
      },
      {
        "answer": "Brak dostępnego uniwersalnego rozwiązania",
        "correct": "true"
      }
    ]
  },
  {
    "question": "Która z technik umożliwia wykrycie nieznanego wirusa komputerowego?",
    "choices": [
      {
        "answer": "Niemożliwe jest wykrycie nieznanych wirusów",
        "correct": "false"
      },
      {
        "answer": "Kontrola spójności",
        "correct": "true"
      },
      {
        "answer": "Skanowanie plików",
        "correct": "false"
      },
      {
        "answer": "Blokowanie aktywności w systemie operacyjnym",
        "correct": "true"
      }
    ]
  },
  {
    "question": "Która z cech jest niepożądana w ujęciu bezpieczeństwa poczty elektronicznej?",
    "choices": [
      {
        "answer": "Zapewnienie poufności wiadomości",
        "correct": "false"
      },
      {
        "answer": "Możliwość wyparcia się treści",
        "correct": "true"
      },
      {
        "answer": "Weryfikacja tożsamości tylko nadawcy wiadomości",
        "correct": "true"
      },
      {
        "answer": "Kontrola spójności wiadomości",
        "correct": "false"
      }
    ]
  },
  {
    "question": "Ocenę systemów przeprowadza się w celu...",
    "choices": [
      {
        "answer": "Określenia czasu wystąpienia awarii systemu",
        "correct": "false"
      },
      {
        "answer": "Spełnienia wymogów prawnych producentów podzespołów bazowych serwerowni",
        "correct": "false"
      },
      {
        "answer": "Opracowania specyfikacji systemu",
        "correct": "false"
      },
      {
        "answer": "Okresowej oceny bezpieczeństwa systemu, znalezienia i poprawienia istniejących błędów",
        "correct": "true"
      }
    ]
  },
  {
    "question": "W jakim celu w tzw bezpiecznych stacjach roboczych stosowane jest silne ekranowanie elektromagnetyczne?",
    "choices": [
      {
        "answer": "W celu zwiększenia niezawodności stacji roboczych",
        "correct": "true"
      },
      {
        "answer": "W celu ochrony pracownika przed silnym polem elektromagnetycznym",
        "correct": "false"
      },
      {
        "answer": "W celu zachowania wysokiej kompatybilności elektromagnetycznej ze sprzętem komercyjnym",
        "correct": "true"
      },
      {
        "answer": "W celu uniemożliwienia wykrycia i przechwycenia emisji elektromagnetycznej",
        "correct": "false"
      }
    ]
  },
  {
    "question": "W jaki sposób sprzętowo zwiększa się bezpieczeństwo systemu informatycznego?",
    "choices": [
      {
        "answer": "Stosowane są dodatkowe linie zasilające oraz łącza telekomunikacyjne",
        "correct": "true"
      },
      {
        "answer": "Minimalizując liczbę serwerów w celu zmniejszenia prawdopodobieństwa awarii",
        "correct": "false"
      },
      {
        "answer": "Stosując sporadyczną wymianę przepracowanych podzespołów",
        "correct": "true"
      },
      {
        "answer": "Stosując nadmiarowe podzespoły bazowe w serwerach",
        "correct": "true"
      }
    ]
  },
  {
    "question": "W jakim celu stosowane jest tunelowanie SSL/TSL albo połączenia VPN?",
    "choices": [
      {
        "answer": "Zabezpieczenia transmisji w sieciach niezabezpieczonych",
        "correct": "false"
      },
      {
        "answer": "Wyeliminowania konieczności stosowania połączeń przewodowych",
        "correct": "true"
      },
      {
        "answer": "W celu eliminacji konieczności szyfrowania przesyłanych danych",
        "correct": "false"
      },
      {
        "answer": "W celu wyeliminowania konieczności uwierzytelnienia",
        "correct": "false"
      }
    ]
  },
  {
    "question": "Do jakiego umiejscowienia nie można przyporządkować zabezpieczeń serwera WWW?",
    "choices": [
      {
        "answer": "Zabezpieczenia po stronie serwera",
        "correct": "false"
      },
      {
        "answer": "Zabezpieczenia po stronie aplikacji WWW",
        "correct": "false"
      },
      {
        "answer": "Zabezpieczenia po stronie systemu",
        "correct": "false"
      },
      {
        "answer": "Zabezpieczenia po stronie dostawcy usługi sieciowej",
        "correct": "true"
      }
    ]
  },
  {
    "question": "Wskaż rolę sprzężenia zwrotnego w procesie ewaluacji systemu IT",
    "choices": [
      {
        "answer": "Umożliwia zlecenie ewaluacji firmie zewnętrznej",
        "correct": "false"
      },
      {
        "answer": "Zapewnienie przekazania danych o audycie do użytkownika końcowego",
        "correct": "false"
      },
      {
        "answer": "Zapewnia przepływ informacji pomiędzy kierownictwem a pracownikami",
        "correct": "false"
      },
      {
        "answer": "Możliwość wyeliminowania występujących w systemie błędów",
        "correct": "true"
      }
    ]
  },
  {
    "question": "Podczas analizy ryzyka zdarzeniem krytycznym określamy...",
    "choices": [
      {
        "answer": "Zdarzenie o niskim prawdopodobieństwie wystąpienia ale o wysokich konsekwencjach i kosztach naprawy",
        "correct": "true"
      },
      {
        "answer": "Zdarzenie o średnim prawdopodobieństwie i średnich konsekwencjach",
        "correct": "false"
      },
      {
        "answer": "Zdarzenie o wysokim prawdopodobieństwie wystąpienia i o wysokich konsekwencjach",
        "correct": "false"
      },
      {
        "answer": "Zdarzenie prawie niemożliwe o niskich konsekwencjach",
        "correct": "false"
      }
    ]
  },
  {
    "question": "Bezpieczeństwem systemu nazywamy",
    "choices": [
      {
        "answer": "Stan przed awarią systemu",
        "correct": "false"
      },
      {
        "answer": "Pożądany stan systemy",
        "correct": "true"
      },
      {
        "answer": "Stan, kiedy nikt nie może uzyskać dostępu do systemu",
        "correct": "false"
      },
      {
        "answer": "Stan podczas prac rozwojowych",
        "correct": "false"
      }
    ]
  },
  {
    "question": "Co opisuje norma ISO-9001-2015?",
    "choices": [
      {
        "answer": "System zarządzania jakością",
        "correct": "true"
      },
      {
        "answer": "System zarządzania bezpieczeństwem",
        "correct": "false"
      },
      {
        "answer": "System zarządzania jakością wytwarzanego oprogramowania",
        "correct": "false"
      },
      {
        "answer": "Sposób realizacji polityki bezpieczeństwa",
        "correct": "false"
      }
    ]
  },
  {
    "question": "Na czym polega ocena i doskonalenie polityki bezpieczeństwa?",
    "choices": [
      {
        "answer": "Periodyczne przeprowadzanie audytów polityki bezpieczeństwa",
        "correct": "false"
      },
      {
        "answer": "Wykrywaniu stopniowej zmiany postępowania użytkowników",
        "correct": "false"
      },
      {
        "answer": "Ciągłe monitorowanie i modyfikowanie polityki bezpieczeństwa",
        "correct": "false"
      },
      {
        "answer": "Ciągłe monitorowanie i rozszerzanie polityki bezpieczeństwa",
        "correct": "false"
      }
    ]
  },
  {
    "question": "O ile procent spada dostępna dla użytkownika przepływność, jeśli w interfejsie radiowym zastosowano szyfrowanie danych?",
    "choices": [
      {
        "answer": "Zależnie od kodowania, przeważnie ok. 20-30%",
        "correct": "true"
      },
      {
        "answer": "Około 50%",
        "correct": "false"
      },
      {
        "answer": "0%",
        "correct": "false"
      },
      {
        "answer": "Mniej niż 5%",
        "correct": "false"
      }
    ]
  }
]
