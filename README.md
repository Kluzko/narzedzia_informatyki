# Aktywacja,instalacja i urchomienie programu

### Aktywacja Wirtualnego Środowiska (venv):

- **Windows**:

```
venv\Scripts\activate
```

- **MacOS**:

```
source venv/bin/activate
```

### Instalaja paczek

```
python3 -m pip install -r requirements.txt
```

### Uruchomienie Programu:

Użyj tej komendy w terminalu po aktywowaniu wirtualnego środowiska:

```bash
streamlit run sciezka/do/app.py
```

Upewnij się, że zastąpisz "sciezka/do/app.py" właściwą ścieżką do pliku app.py w Twoim projekcie.

Aplikacja będzie dostępna pod adresem: http://localhost:8501

# O Programie:

Program jest narzędziem do wizualizacji danych dotyczących zgonów według przyczyn w roku 2020, wykorzystującym Pythona oraz biblioteki Streamlit, Pandas i Plotly Express.

Projekt dodatkowo zawiera przykład implementacji bazy danych SQLite przy użyciu SQLAlchemy oraz pokazuje, jak można zaimportować dane z pliku XLSX do bazy danych za pomocą funkcji import_sheet_to_db().

### Screeny z Programu:

![Screen 1](static/screen_01.png)
![Screen 2](static/screen_02.png)
