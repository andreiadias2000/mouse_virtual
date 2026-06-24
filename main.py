

import cv2
import mediapipe as mp
import pyautogui
import math

# ---------------------------------------------------------
# CONFIGURAÇÕES INICIAIS
# ---------------------------------------------------------
camera = cv2.VideoCapture(0)

detector_maos = mp.solutions.hands.Hands(max_num_hands=2)
desenho = mp.solutions.drawing_utils

tela_largura, tela_altura = pyautogui.size()
distancia_anterior = None

# --- NOVAS VARIÁVEIS PARA SUAVIZAÇÃO DO RATO ---
suavizacao = 5 # Quanto maior o número, mais suave (mas mais lento a reagir). 5 ou 7 são ideais.
plocX, plocY = 0, 0 # Posição Anterior (Previous Location)
clocX, clocY = 0, 0 # Posição Atual (Current Location)

# ---------------------------------------------------------
# LOOP PRINCIPAL DO PROGRAMA
# ---------------------------------------------------------
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
        quantidade_maos = len(maos)
        indicadores = []
        
        for mao in maos:
            desenho.draw_landmarks(frame, mao, mp.solutions.hands.HAND_CONNECTIONS)
            pontos = mao.landmark
            
            x_indicador, y_indicador = 0, 0
            x_dedao, y_dedao = 0, 0
            x_medio, y_medio = 0, 0
            x_anelar, y_anelar = 0, 0
            
            for id, ponto in enumerate(pontos):
                px = int(ponto.x * frame_largura)
                py = int(ponto.y * frame_altura)
                
                # --- PONTO 8: DEDO INDICADOR ---
                if id == 8:
                    x_indicador, y_indicador = px, py
                    cv2.circle(frame, (px, py), 10, (0, 255, 255), -1) 
                    indicadores.append((px, py))
                    
                    # 1. MOVER O RATO (Apenas 1 mão na tela)
                    if quantidade_maos == 1:
                        # 1.1 Calcula onde o rato DEVERIA estar
                        x_alvo = tela_largura / frame_largura * px
                        y_alvo = tela_altura / frame_altura * py
                        
                        # 1.2 Aplica o cálculo matemático de suavização para não tremer
                        clocX = plocX + (x_alvo - plocX) / suavizacao
                        clocY = plocY + (y_alvo - plocY) / suavizacao
                        
                        # 1.3 Move o rato para a coordenada suavizada
                        pyautogui.moveTo(clocX, clocY)
                        
                        # 1.4 Atualiza a posição anterior para o ciclo seguinte
                        plocX, plocY = clocX, clocY
                
                # --- PONTO 4: DEDÃO ---
                elif id == 4:
                    x_dedao, y_dedao = px, py
                    cv2.circle(frame, (px, py), 10, (255, 0, 255), -1) 
                    
                # --- PONTO 12: DEDO MÉDIO ---
                elif id == 12:
                    x_medio, y_medio = px, py
                    
                # --- PONTO 16: DEDO ANELAR ---
                elif id == 16:
                    x_anelar, y_anelar = px, py

            # ---------------------------------------------------------
            # 2. COMANDOS DE UMA MÃO (Clique e Scroll)
            # ---------------------------------------------------------
            if quantidade_maos == 1:
                
                # CLIQUE (Dedão + Indicador)
                if math.hypot(x_indicador - x_dedao, y_indicador - y_dedao) < 20:
                    cv2.circle(frame, (x_indicador, y_indicador), 15, (0, 255, 0), -1) 
                    pyautogui.click()
                    
                # SCROLL PARA CIMA (Dedão + Médio)
                elif math.hypot(x_medio - x_dedao, y_medio - y_dedao) < 20:
                    cv2.circle(frame, (x_medio, y_medio), 15, (255, 0, 0), -1) 
                    pyautogui.scroll(150) 
                    
                # SCROLL PARA BAIXO (Dedão + Anelar)
                elif math.hypot(x_anelar - x_dedao, y_anelar - y_dedao) < 20:
                    cv2.circle(frame, (x_anelar, y_anelar), 15, (0, 0, 255), -1) 
                    pyautogui.scroll(-150) 
                    
        # ---------------------------------------------------------
        # 3. COMANDOS DE DUAS MÃOS (Zoom In e Zoom Out)
        # ---------------------------------------------------------
        if quantidade_maos == 2 and len(indicadores) == 2:
            x1, y1 = indicadores[0] 
            x2, y2 = indicadores[1] 
            
            cv2.line(frame, (x1, y1), (x2, y2), (255, 0, 0), 3)
            distancia_atual = math.hypot(x2 - x1, y2 - y1)
            
            if distancia_anterior is not None:
                diferenca = distancia_atual - distancia_anterior
                
                if diferenca > 15:
                    pyautogui.hotkey('ctrl', '+')
                    distancia_anterior = distancia_atual 
                    
                elif diferenca < -15:
                    pyautogui.hotkey('ctrl', '-')
                    distancia_anterior = distancia_atual
            else:
                distancia_anterior = distancia_atual
    else:
        distancia_anterior = None

    cv2.imshow('Mouse Virtual via Webcam', frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

camera.release()
cv2.destroyAllWindows()



# import cv2
# import mediapipe as mp
# import pyautogui
# import math

# camera = cv2.VideoCapture(0)

# detector_maos = mp.solutions.hands.Hands(max_num_hands=2)
# desenho = mp.solutions.drawing_utils

# tela_largura, tela_altura = pyautogui.size()

# while True:
#     sucesso, frame = camera.read()
#     if not sucesso:
#         break
        
#     frame = cv2.flip(frame, 1)
#     frame_altura, frame_largura, _ = frame.shape
    
#     rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    
#     resultado = detector_maos.process(rgb_frame)
#     maos = resultado.multi_hand_landmarks
    
#     if maos:
#         # 1. Conta quantas mãos estão sendo detectadas neste exato momento
#         quantidade_maos = len(maos)
        
#         for mao in maos:
#             desenho.draw_landmarks(frame, mao, mp.solutions.hands.HAND_CONNECTIONS)
#             pontos = mao.landmark
            
#             x_indicador, y_indicador = 0, 0
#             x_dedao, y_dedao = 0, 0
            
#             for id, ponto in enumerate(pontos):
#                 # Pega a posição do DEDO INDICADOR (Ponto 8)q
#                 if id == 8:
#                     x_indicador = int(ponto.x * frame_largura)
#                     y_indicador = int(ponto.y * frame_altura)
#                     cv2.circle(frame, (x_indicador, y_indicador), 10, (0, 255, 255), -1)
                    
#                     # 2. O mouse SÓ se move se houver EXATAMENTE 1 mão visível
#                     if quantidade_maos == 1:
#                         x_tela = tela_largura / frame_largura * x_indicador
#                         y_tela = tela_altura / frame_altura * y_indicador
#                         pyautogui.moveTo(x_tela, y_tela)
                
#                 # Pega a posição do DEDÃO (Ponto 4)
#                 if id == 4:
#                     x_dedao = int(ponto.x * frame_largura)
#                     y_dedao = int(ponto.y * frame_altura)
#                     cv2.circle(frame, (x_dedao, y_dedao), 10, (255, 0, 255), -1)

#             # 3. O clique também SÓ é liberado se houver 1 mão visível
#             if quantidade_maos == 1:
#                 distancia = math.hypot(x_indicador - x_dedao, y_indicador - y_dedao)
                
#                 if distancia < 20:
#                     cv2.circle(frame, (x_indicador, y_indicador), 15, (0, 255, 0), -1)
#                     pyautogui.click()

#     cv2.imshow('Mouse Virtual via Webcam', frame)
    
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

# camera.release()
# cv2.destroyAllWindows()