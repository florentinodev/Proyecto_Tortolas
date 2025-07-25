# Proyecto Tórtolas: Detección de Objetos con YOLOv8
*Detección de tuberías, camionetas y piezómetros en ortomosaicos mediante una app desplegada en AWS EC2.*

Introducción / Descripción del proyecto
Una solución para entrenar, inferir y desplegar modelos de detección de objetos usando YOLOv8. El sistema fue desarrollado con:
- Roboflow para etiquetado y exportación de dataset,
- entrenamiento local con Python,
- despliegue en AWS EC2 con interfaz web (Streamlit),
- todo sin APIs intermedias, permitiendo inferencia desde imágenes locales.

Características principales
- Etiquetado y formato YOLOv8 utilizando Roboflow.

- Entrenamiento eficiente según criterios definidos (data.yaml, YOLO.py).

- Inferencia en tiempo real desde interfaz Streamlit desplegada en EC2.

- Pruebas funcionales y de rendimiento documentadas (CPU, RAM, Disco, Red, monitoreo).

- Disponibilidad pública mediante IP de EC2 y puerto 8501.

Tecnologías usadas
- Python 3.x
- YOLOv8 (ultralytics)
- Roboflow
- Streamlit
- AWS EC2 / EBS
- Bash utilities: `nohup`, `top`, `dd`, etc.
- Git / GitHub

Instalación local
git clone https://github.com/florentinodev/Proyecto_Tortolas.git
cd Proyecto_Tortolas
python3 -m venv venv && source venv/bin/activate
pip install -r requirements.txt

Uso / Training
# Entrenamiento
python train/YOLO.py --data dataset/data.yaml --cfg yolov8.yaml --epochs 30

# Inferencia local
streamlit run app.py

Despliegue en AWS EC2
- Subir código y modelo `.pt` a instancia EC2.
- Ejecutar: nohup streamlit run app.py &
- Abrir navegador: http://<EC2_Public_IP>:8501

Pruebas y Rendimiento
Describe brevemente las pruebas ejecutadas:
Test CPU: cálculo de π (≈1.1 s)
Test RAM: matriz NumPy 10000×10000 (0 s)
Test Disco: lectura/escritura 1 GB (0 s)
Test Red: descarga 100 MB (0 s)
Monitoreo: uso de CPU ≤30% durante inferencia (usando top)


## 🎥 Demostración
[![Ver video en YouTube](https://img.youtube.com/vi/ID_DEL_VIDEO/0.jpg)](https://www.youtube.com/watch?v=Epf_IBGuYOg)
