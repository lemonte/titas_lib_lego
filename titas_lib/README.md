
# SEK - Sistema de Controle para Robôs

Este repositório contém funções úteis para controle de robôs utilizando o Pybricks e hubs compatíveis como o EV3. Inclui comandos para configuração, funções gerais, de movimento, sensores e controle de motores.

---

## 🚀 Comandos para Executar no VSCode

```bash
source ../tcc/.venv/bin/activate
pybricksdev run ble example.py
```

---

## 📜 Funções Gerais

```python
def executar(self):
    """
    Executa uma ação definida.
    """

def falar_erro(funcao):
    """
    Trata e exibe mensagens de erro de uma função.
    Parâmetros:
        funcao: Função que gerou o erro.
    """

def funcao_envolvida(*args, **kwargs):
    """
    Envolve outra função para tratá-la.
    """

def __init__(self, hub=RoboHub.EV3BRICK):
    """
    Inicializa o hub do robô.
    Parâmetros:
        hub: Tipo de hub (padrão: RoboHub.EV3BRICK).
    """
```

---

## 🚦 Funções de Movimento

```python
def moverSemParar(self, velocidade=0, angulo_curvatura=0):
    """
    Faz o robô andar continuamente.
    """

def moverDistancia(self, distancia=0):
    """
    Move o robô por uma distância específica.
    """

def virar90grausEsquerda(self):
    """
    Faz o robô virar 90 graus para a esquerda.
    """

def virar90grausDireita(self):
    """
    Faz o robô virar 90 graus para a direita.
    """

def virar180grausEsquerda(self):
    """
    Faz o robô virar 180 graus para a esquerda.
    """

def virar180grausDireita(self):
    """
    Faz o robô virar 180 graus para a direita.
    """

def virarAngulo(self, angulo=0):
    """
    Faz o robô virar para um ângulo específico.
    """

def pararMotores(self):
    """
    Para todos os motores do robô.
    """

def seguirLinhaPreta(self, cor_vermelha_esquerda, cor_vermelha_direta, motor_direito, motor_esquerdo, kp=1, kd=1, potencia_motores=70):
    """
    Faz o robô seguir uma linha preta.
    Parâmetros:
        cor_vermelha_esquerda: Leitura do sensor esquerdo.
        cor_vermelha_direta: Leitura do sensor direito.
        motor_direito: Motor do lado direito.
        motor_esquerdo: Motor do lado esquerdo.
        kp: Ganho proporcional.
        kd: Ganho derivativo.
        potencia_motores: Potência dos motores.
    """
```

---

## 📡 Funções de Sensores

```python
def pegarRGB(self):
    """
    Retorna os valores RGB detectados pelo sensor.
    """

def pegarCor(self):
    """
    Retorna a cor detectada pelo sensor.
    """

def pegarHsv(self):
    """
    Retorna os valores HSV da cor detectada.
    """

def pegarReflexao(self):
    """
    Retorna o valor de reflexão medido pelo sensor.
    """

def pegarDistancia(self):
    """
    Retorna a distância medida pelo sensor ultrassônico.
    """

def verificarSePossuiOutroUltrassonico(self):
    """
    Verifica se há outro sensor ultrassônico nas proximidades.
    """

def getGiroscopio(self):
    """
    Retorna o objeto do giroscópio.
    """

def getVelocidadeAngular(self):
    """
    Retorna a velocidade angular medida pelo giroscópio.
    """

def getAnguloAcumulado(self):
    """
    Retorna o ângulo acumulado pelo giroscópio.
    """

def redefinirAnguloAcumulado(self, angulo):
    """
    Redefine o ângulo acumulado do giroscópio para o valor especificado.
    """

def resetAnguloAcumulado(self):
    """
    Reseta o ângulo acumulado do giroscópio para 0.
    """
```

---

## ⚙️ Funções Específicas do Motor

```python
def getAngulo(self):
    """
    Retorna o ângulo atual do motor.
    """

def resetarAngulo(self):
    """
    Reseta o ângulo atual do motor para 0.
    """

def redefinirAngulo(self, angulo):
    """
    Define o ângulo atual do motor para um valor específico.
    """

def deixarMotorLivre(self):
    """
    Libera o motor, permitindo que ele gire livremente devido ao atrito.
    """

def paraMotorLentamente(self):
    """
    Para o motor gradualmente, utilizando o atrito.
    """

def pararMotorInstantaneamente(self):
    """
    Para o motor e o mantém travado no ângulo atual.
    """

def mover(self, velocidade=0):
    """
    Move o motor com uma velocidade específica.
    """

def moverDuranteUmTempo(self, velocidade=0, tempo=0, aguardarAcaoFinalizar=True, acaoAoFinalizar=PararInstantaneamenteEMantenhaNoAngulo()):
    """
    Move o motor por um tempo definido.
    Parâmetros:
        velocidade: Velocidade em graus por segundo.
        tempo: Duração do movimento, em milissegundos.
        aguardarAcaoFinalizar: Define se o movimento deve aguardar a conclusão.
        acaoAoFinalizar: Ação a ser executada ao final do movimento.
    """

def moverUmAngulo(self, velocidade, angulo, aguardarAcaoFinalizar=True, acaoAoFinalizar=PararInstantaneamenteEMantenhaNoAngulo()):
    """
    Move o motor até atingir um ângulo específico.
    """

def moverParaUmAnguloSuavemente(self, velocidade, anguloDestino, aguardarAcaoFinalizar=True, acaoAoFinalizar=PararInstantaneamenteEMantenhaNoAngulo()):
    """
    Move o motor suavemente para um ângulo de destino.
    """

def moverAteTravar(self, velocidade=0, forcaLimite=100, acaoAoFinalizar=PararInstantaneamenteEMantenhaNoAngulo()):
    """
    Move o motor até encontrar uma resistência acima de um limite especificado.
    """

def moverPorPotencia(self, potencia):
    """
    Move o motor baseado em uma potência específica.
    """

def moverParaUmAnguloRapidamente(self, anguloDestino):
    """
    Move o motor rapidamente até atingir um ângulo específico.
    """
```
