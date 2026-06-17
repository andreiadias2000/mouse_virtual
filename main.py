import cv2
import mediapipe as mp
import pyautogui
import math

camera = cv2.VideoCapture(0)

detector_maos = mp.solutions.hands.Hands(max_num_hands=2)
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
        # 1. Conta quantas mãos estão sendo detectadas neste exato momento
        quantidade_maos = len(maos)
        
        for mao in maos:
            desenho.draw_landmarks(frame, mao, mp.solutions.hands.HAND_CONNECTIONS)
            pontos = mao.landmark
            
            x_indicador, y_indicador = 0, 0
            x_dedao, y_dedao = 0, 0
            
            for id, ponto in enumerate(pontos):
                # Pega a posição do DEDO INDICADOR (Ponto 8)q
                if id == 8:
                    x_indicador = int(ponto.x * frame_largura)
                    y_indicador = int(ponto.y * frame_altura)
                    cv2.circle(frame, (x_indicador, y_indicador), 10, (0, 255, 255), -1)
                    
                    # 2. O mouse SÓ se move se houver EXATAMENTE 1 mão visível
                    if quantidade_maos == 1:
                        x_tela = tela_largura / frame_largura * x_indicador
                        y_tela = tela_altura / frame_altura * y_indicador
                        pyautogui.moveTo(x_tela, y_tela)
                
                # Pega a posição do DEDÃO (Ponto 4)
                if id == 4:
                    x_dedao = int(ponto.x * frame_largura)
                    y_dedao = int(ponto.y * frame_altura)
                    cv2.circle(frame, (x_dedao, y_dedao), 10, (255, 0, 255), -1)

            # 3. O clique também SÓ é liberado se houver 1 mão visível
            if quantidade_maos == 1:
                distancia = math.hypot(x_indicador - x_dedao, y_indicador - y_dedao)
                
                if distancia < 20:
                    cv2.circle(frame, (x_indicador, y_indicador), 15, (0, 255, 0), -1)
                    pyautogui.click()

    cv2.imshow('Mouse Virtual via Webcam', frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

camera.release()
cv2.destroyAllWindows()