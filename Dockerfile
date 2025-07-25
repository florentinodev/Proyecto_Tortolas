<<<<<<< HEAD
FROM python:3.9

RUN apt-get update && apt-get install -y libgl1-mesa-glx
=======
FROM python:3.9-slim
>>>>>>> cf1eec9 (Estructura reorganizada con app.py y utils.py en raíz del proyecto)

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

<<<<<<< HEAD
CMD ["python", "app.py"]
=======
CMD ["python", "app.py"]
>>>>>>> cf1eec9 (Estructura reorganizada con app.py y utils.py en raíz del proyecto)
