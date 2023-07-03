import cv2
import mediapipe as mp
import os

#----------------------------------------------------------------Almacenar Entrenamiento
nombre = 'letra_A'
direccion = 'D:/Universidades/UNJBG/MAESTRIA/TESIS 2/ProyectoLS/Fotos/Validacion'
carpeta = direccion + '/' + nombre

if not os.path.exists(carpeta):
    print('carpeta creada',carpeta)
    os.makedirs(carpeta)

#Asignamos contador para nombre de las fotos
cont=0

#Leemos la camara
cap = cv2.VideoCapture(0)

#Creamos objeto que va a almacenar la deteccion y seguimiento de manos
clase_manos = mp.solutions.hands
manos = clase_manos.Hands()

#Metodo para dibujar las manos
dibujo=mp.solutions.drawing_utils #Con este metodo se dibuja 21 puntos

while (1):
    ret_frame = cap.read()
    color = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
    copia = frame.copy()
    resultado = manos.process(color)
    posiciones = [] # Almacenar coordenas de los puntos
    #pirnt(resultado.multi_hand_landmarks) #si queremos ver si existe deteccion

    if resultado.multi_hand_landmarks: 


