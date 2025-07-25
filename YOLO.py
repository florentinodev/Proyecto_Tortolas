from ultralytics import YOLO
import os
import torch

def entrenar_yolo():
    os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"

    print("🚀 Iniciando entrenamiento...")

    # Detectar si hay GPU disponible
    device = "cuda" if torch.cuda.is_available() else "cpu"
    print(f"💻 Dispositivo detectado: {device}")

    # Cargar modelo base (no uses best.pt para entrenar desde cero)
    model = YOLO('yolov8m-seg.pt')  # usa un modelo base, no uno ya entrenado

    model.train(
        data="data.yaml",           # Asegúrate que este archivo existe y tiene el formato correcto
        epochs=50,
        imgsz=640 if device == "cpu" else 1024,  # más liviano si estás en CPU
        batch=2 if device == "cpu" else 8,
        name="modelo_tortolas_v1_seg_desde_web",
        project="frontend/RUN",
        device=device,
        workers=0,
        patience=20,
        cache=False
    )

    print("✅ Entrenamiento completado con éxito.")
    return "✅ Entrenamiento completado con éxito."