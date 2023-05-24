# Zbuduj obraz bazowy na podstawie najnowszej wersji Pythona
FROM python:3.10-slim-buster

# Praca w katalogu /lab_6
WORKDIR /lab_6

# Skopiuj plik requirements.txt do obrazu
COPY requirements.txt .

# Zainstaluj wymagane zależności
RUN pip install --no-cache-dir -r requirements.txt

# Skopiuj resztę plików aplikacji do obrazu
COPY . /lab_6/

# Ustaw port, na którym będzie działać aplikacja
EXPOSE 5000

# Uruchom aplikację
CMD ["python", "app.py"]