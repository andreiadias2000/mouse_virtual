# 🖱️ Mouse Virtual com Webcam

Este projeto usa visão computacional (OpenCV e MediaPipe) para controlar o cursor do mouse usando apenas a câmera do computador e movimentos da mão.

## ⚠️ Pré-requisito Muito Importante
Para que a biblioteca de visão computacional funcione corretamente, você **precisa ter o Python 3.10 ou 3.11** instalado na sua máquina (versões mais novas, como a 3.13 ou 3.14, podem dar erro de módulo não encontrado no MediaPipe).
* Durante a instalação do Python, **NÃO ESQUEÇA** de marcar a caixa **"Add python.exe to PATH"** na primeira tela.

## 🚀 Como rodar o projeto na sua máquina

**1. Clone o repositório e entre na pasta**
Abra o terminal do seu VS Code e rode:
`git clone [COLOQUE_AQUI_O_LINK_DO_SEU_REPOSITORIO_GITHUB]`
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

## 🖐️ Como usar
* Levante a mão de frente para a câmera.
* Use a ponta do **dedo indicador** para mover o mouse pela tela.
* Para **clicar**, faça um movimento de pinça, juntando a ponta do dedo indicador com a ponta do dedão.
* Clique na janela da câmera e aperte a tecla **Q** no teclado para encerrar o programa com segurança.