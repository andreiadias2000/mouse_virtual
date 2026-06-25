# 🖱️ Mouse Virtual com Webcam

Este projeto utiliza visão computacional (OpenCV e MediaPipe) para controlar o cursor do mouse e executar comandos de sistema utilizando apenas a câmera do computador e os movimentos das mãos em tempo real. Conta com um sistema de suavização matemática para garantir que o cursor deslize perfeitamente pela tela sem trepidações.

## ⚠️ Pré-requisito Muito Importante
Para que a biblioteca de visão computacional funcione corretamente, você **precisa ter o Python 3.10 ou 3.11** instalado na sua máquina (versões mais novas, como a 3.13 ou 3.14, podem dar erro de módulo não encontrado no MediaPipe).
* Durante a instalação do Python, **NÃO ESQUEÇA** de marcar a caixa **"Add python.exe to PATH"** na primeira tela.

## 🚀 Como rodar o projeto na sua máquina

**1. Clone o repositório e entre na pasta**
Abra o terminal do seu VS Code e rode:
`git clone https://github.com/andreiadias2000/mouse_virtual.git`
`cd mouse_virtual`

**2. Crie o ambiente virtual isolado**
Para não misturar versões com os seus outros projetos, rode no terminal:
* No Windows (PowerShell): `py -3.10 -m venv venv`
* No Mac/Linux: `python3.10 -m venv venv`

**3. Ative o ambiente virtual**
* No Windows: `.\venv\Scripts\activate`
* No Mac/Linux: `source venv/bin/activate`
*(Você saberá que deu certo quando aparecer um `(venv)` no começo da linha do terminal).*

**4. Instale as bibliotecas necessárias**
Com o ambiente ativado, rode este comando para baixar tudo automaticamente:
`pip install -r requirements.txt`

**5. Rode a aplicação**
`python main.py`

## 🖐️ Guia de Comandos e Gestos

### Comandos com 1 Mão (Navegação)
*(Certifique-se de que apenas uma mão está visível na câmera)*

* 🖱️ **Mover o Mouse:** Aponte o **dedo indicador** para a câmera e mova a mão. Uma marcação amarela seguirá o seu dedo com movimento suavizado.
* 🖱️ **Clique Simples:** Faça um movimento de pinça rápido, juntando a ponta do **dedão** com a ponta do **dedo indicador**. A marcação ficará verde ao clicar.
* ⬆️ **Rolar para Cima (Scroll Up):** Junte a ponta do **dedão** com a ponta do **dedo médio**. A marcação ficará azul.
* ⬇️ **Rolar para Baixo (Scroll Down):** Junte a ponta do **dedão** com a ponta do **dedo anelar**. A marcação ficará vermelha.

### Comandos com 2 Mãos (Controle de Tela)
*(As duas mãos devem estar visíveis na câmera simultaneamente)*

* 🔍 **Ativar Modo Zoom:** Levante as duas mãos apontando os dois **dedos indicadores**. O sistema conectará os dedos com uma linha azul na tela.
* ➕ **Aumentar Tela (Zoom In):** Com a linha azul ativa, **afaste** os dedos indicadores um do outro. O sistema executará o atalho do teclado para dar zoom.
* ➖ **Diminuir Tela (Zoom Out):** Com a linha azul ativa, **aproxime** os dedos indicadores um do outro.

### Comando de Segurança
* 🛑 **Encerrar o Programa:** Clique na janela de vídeo da câmera ("Mouse Virtual via Webcam") e aperte a tecla **Q** no teclado para fechar a aplicação com segurança.
