# Usamos una imagen oficial y ligera de Python
FROM python:3.10-slim

# Directorio de trabajo dentro del contenedor
WORKDIR /app

# Copiamos los archivos de requerimientos y el código
COPY requirements.txt .
COPY bot.py .

# Instalamos las dependencias necesarias
RUN pip install --no-cache-dir -r requirements.txt

# Comando para ejecutar el bot de forma permanente
CMD ["python", "bot.py"]