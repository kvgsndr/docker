# Kindulo allapot mi legyen:
FROM python:3.8-buster

# Munka konyvtar
WORKDIR /application

# Telepitjuk amit kell
COPY requirements.txt .
RUN pip install -r requirements.txt

# Telepitjuk a proginkat
COPY counter.py .

# Kontener inditasakor mi induljon el
CMD ["python", "counter.py"]


