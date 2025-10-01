# Versión de Python
FROM python:3.12-slim

# Directorio de trabajo
WORKDIR /usr/src/app

# Se copia el archivo que
# contiene las dependencias
COPY requirements.txt .

# Instalar dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Extraer el código
COPY . .

# Puerto por donde sale la app
EXPOSE 2000

# Comando para iniciar la app
CMD ["python", "run.py"]