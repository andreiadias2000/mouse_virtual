import cv2
import mediapipe as mp
import pyautogui
import math # Nova biblioteca para calcular a distância

camera = cv2.VideoCapture(0)

detector_maos = mp.solutions.hands.Hands(max_num_hands=1)
desenho = mp.solutions.drawing_utils

tela_largura, tela_altura = pyautogui.size()

while True:
    sucesso, frame = camera.read()
    if not sucesso:
        break
        
    frame = cv2.flip(frame, 1)
    frame_altura, frame_largura, _ = frame.shape
    
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    
    resultado = detector_maos.process(rgb_frame)
    maos = resultado.multi_hand_landmarks
    
    if maos:
        for mao in maos:
            desenho.draw_landmarks(frame, mao)
            pontos = mao.landmark
            
            # Variavel para guardar a posição do dedão (4) e indicador (8)
            x_indicador, y_indicador = 0, 0
            x_dedao, y_dedao = 0, 0
            
            for id, ponto in enumerate(pontos):
                # Pega a posição do DEDO INDICADOR (Ponto 8) primeiro ponto é 0
                if id == 8:
                    x_indicador = int(ponto.x * frame_largura)
                    y_indicador = int(ponto.y * frame_altura)
                    cv2.circle(frame, (x_indicador, y_indicador), 10, (0, 255, 255), -1)
                    
                    # Move o mouse
                    x_tela = tela_largura / frame_largura * x_indicador
                    y_tela = tela_altura / frame_altura * y_indicador
                    pyautogui.moveTo(x_tela, y_tela)
                
                # Pega a posição do DEDÃO (Ponto 4)
                if id == 4:
                    x_dedao = int(ponto.x * frame_largura)
                    y_dedao = int(ponto.y * frame_altura)
                    cv2.circle(frame, (x_dedao, y_dedao), 10, (255, 0, 255), -1)

            # CLIQUE: Calcula a distância entre o dedão e o indicador
            distancia = math.hypot(x_indicador - x_dedao, y_indicador - y_dedao)
            
            # Se os dedos encostarem (distância menor que 20 pixels)
            if distancia < 20:
                # Muda a cor do círculo para verde para saber que clicou visualmente
                cv2.circle(frame, (x_indicador, y_indicador), 15, (0, 255, 0), -1)
                
                # Efetua o clique do trocinho
                pyautogui.click()

    cv2.imshow('Mouse Virtual via Webcam', frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

camera.release()
cv2.destroyAllWindows()