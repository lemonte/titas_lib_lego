# sek
# comandos para executar no vscode
source ../tcc/.venv/bin/activate
pybricksdev run ble example.py

# ================================
# Funções Gerais
# ================================
def executar(self):
    """
    Executa uma ação definida.
    Parâmetros: Nenhum.
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
    Parâmetros:
        *args, **kwargs: Argumentos da função envolvida.
    """

def __init__(self, hub=RoboHub.EV3BRICK):
    """
    Inicializa o hub do robô.
    Parâmetros:
        hub: Tipo de hub (padrão: RoboHub.EV3BRICK).
    """

def getImports(self):
    """
    Retorna as importações usadas na biblioteca.
    Parâmetros: Nenhum.
    """

def beep(self):
    """
    Emite um sinal sonoro no robô.
    Parâmetros: Nenhum.
    """

def definirVolume(self, volume=100):
    """
    Define o volume do som do robô.
    Parâmetros:
        volume: Nível de volume (0 a 100).
    """

def falar(self, texto):
    """
    Faz o robô "falar" o texto especificado.
    Parâmetros:
        texto: Texto para o robô "falar".
    """

# ================================
# Funções de Movimento
# ================================
def moverSemParar(self, velocidade=0, angulo_curvatura=0):
    """
    Faz o robô andar continuamente.
    Parâmetros:
        velocidade: Velocidade de movimento.
        angulo_curvatura: Curvatura do movimento.
    """

def moverDistancia(self, distancia=0):
    """
    Move o robô por uma distância específica.
    Parâmetros:
        distancia: Distância a percorrer.
    """

def virar90grausEsquerda(self):
    """
    Faz o robô virar 90 graus para a esquerda.
    Parâmetros: Nenhum.
    """

def virar90grausDireita(self):
    """
    Faz o robô virar 90 graus para a direita.
    Parâmetros: Nenhum.
    """

def virar180grausEsquerda(self):
    """
    Faz o robô virar 180 graus para a esquerda.
    Parâmetros: Nenhum.
    """

def virar180grausDireita(self):
    """
    Faz o robô virar 180 graus para a direita.
    Parâmetros: Nenhum.
    """

def virarAngulo(self, angulo=0):
    """
    Faz o robô virar para um ângulo específico.
    Parâmetros:
        angulo: Ângulo desejado.
    """

def pararMotores(self):
    """
    Para todos os motores do robô.
    Parâmetros: Nenhum.
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

# ================================
# Funções de Sensores
# ================================
def pegarRGB(self):
    """
    Retorna os valores RGB detectados pelo sensor.
    Parâmetros: Nenhum.
    """

def pegarCor(self):
    """
    Retorna a cor detectada pelo sensor.
    Parâmetros: Nenhum.
    """

def pegarHsv(self):
    """
    Retorna os valores HSV da cor detectada.
    Parâmetros: Nenhum.
    """

def pegarReflexao(self):
    """
    Retorna o valor de reflexão medido pelo sensor.
    Parâmetros: Nenhum.
    """

def pegarDistancia(self):
    """
    Retorna a distância medida pelo sensor ultrassônico.
    Parâmetros: Nenhum.
    """

def verificarSePossuiOutroUltrassonico(self):
    """
    Verifica se há outro sensor ultrassônico nas proximidades.
    Parâmetros: Nenhum.
    """

def getGiroscopio(self):
    """
    Retorna o objeto do giroscópio.
    Parâmetros: Nenhum.
    """

def getVelocidadeAngular(self):
    """
    Retorna a velocidade angular medida pelo giroscópio.
    Parâmetros: Nenhum.
    """

def getAnguloAcumulado(self):
    """
    Retorna o ângulo acumulado pelo giroscópio.
    Parâmetros: Nenhum.
    """

def redefinirAnguloAcumulado(self, angulo):
    """
    Redefine o ângulo acumulado do giroscópio para o valor especificado.
    Parâmetros:
        angulo: Novo valor do ângulo acumulado.
    """

def resetAnguloAcumulado(self):
    """
    Reseta o ângulo acumulado do giroscópio para 0.
    Parâmetros: Nenhum.
    """

# ================================
# Funções Específicas do Motor
# ================================
def getAngulo(self):
    """
    Retorna o ângulo atual do motor.
    Parâmetros: Nenhum.
    """

def resetarAngulo(self):
    """
    Reseta o ângulo atual do motor para 0.
    Parâmetros: Nenhum.
    """

def redefinirAngulo(self, angulo):
    """
    Define o ângulo atual do motor para um valor específico.
    Parâmetros:
        angulo: Novo valor para o ângulo do motor.
    """

def deixarMotorLivre(self):
    """
    Libera o motor, permitindo que ele gire livremente devido ao atrito.
    Parâmetros: Nenhum.
    """

def paraMotorLentamente(self):
    """
    Para o motor gradualmente, utilizando o atrito.
    Parâmetros: Nenhum.
    """

def pararMotorInstantaneamente(self):
    """
    Para o motor e o mantém travado no ângulo atual.
    Parâmetros: Nenhum.
    """

def mover(self, velocidade=0):
    """
    Move o motor com uma velocidade específica.
    Parâmetros:
        velocidade: Velocidade em graus por segundo.
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
    Parâmetros:
        velocidade: Velocidade em graus por segundo.
        angulo: Ângulo a ser atingido pelo motor.
        aguardarAcaoFinalizar: Define se o movimento deve aguardar a conclusão.
        acaoAoFinalizar: Ação a ser executada ao final do movimento.
    """

def moverParaUmAnguloSuavemente(self, velocidade, anguloDestino, aguardarAcaoFinalizar=True, acaoAoFinalizar=PararInstantaneamenteEMantenhaNoAngulo()):
    """
    Move o motor suavemente para um ângulo de destino.
    Parâmetros:
        velocidade: Velocidade em graus por segundo.
        anguloDestino: Ângulo de destino.
        aguardarAcaoFinalizar: Define se o movimento deve aguardar a conclusão.
        acaoAoFinalizar: Ação a ser executada ao final do movimento.
    """

def moverAteTravar(self, velocidade=0, forcaLimite=100, acaoAoFinalizar=PararInstantaneamenteEMantenhaNoAngulo()):
    """
    Move o motor até encontrar uma resistência acima de um limite especificado.
    Parâmetros:
        velocidade: Velocidade em graus por segundo.
        forcaLimite: Força limite para considerar o motor travado (0 a 100%).
        acaoAoFinalizar: Ação a ser executada ao final do movimento.
    """

def moverPorPotencia(self, potencia):
    """
    Move o motor baseado em uma potência específica.
    Parâmetros:
        potencia: Percentual da potência do motor (-100% a 100%).
    """

def moverParaUmAnguloRapidamente(self, anguloDestino):
    """
    Move o motor rapidamente até atingir um ângulo específico.
    Parâmetros:
        anguloDestino: Ângulo de destino.
    """
