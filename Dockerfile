# Usamos una imagen base de Python 3.11-slim para mantener la imagen ligera
FROM python:3.11-slim

# Actualiza el sistema e instala Chromium y el driver de Chromium
RUN apt-get update && apt-get install -y \
    chromium \
    chromium-driver \
    && rm -rf /var/lib/apt/lists/*

# Establece variables de entorno para que Selenium sepa dónde está Chromium
ENV CHROME_BIN=/usr/bin/chromium
ENV CHROMEDRIVER_BIN=/usr/bin/chromedriver

# Establece el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copia el archivo de requerimientos e instala las dependencias de Python
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copia el resto del código de la aplicación
COPY . .

# Asegura que el script de inicio tenga permisos de ejecución
RUN chmod +x start.sh

# Expone el puerto (Render se encargará de pasar el puerto a través de la variable $PORT)
EXPOSE 10000

# Comando de inicio
CMD ["bash", "start.sh"]
