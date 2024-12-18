# Consolidated Imports
from pybricks.ev3devices import Motor
from pybricks.ev3devices import UltrasonicSensor, ColorSensor, GyroSensor
from pybricks.parameters import *

# Consolidated Code

# Código de falar_erro.py

def falar_erro(funcao):
    def funcao_envolvida(*args, **kwargs):
        try:
            return funcao(*args, **kwargs)
        except Exception as e:
            robo_brick = RoboBrick()
            mensagem_de_erro = str(e)
            print(mensagem_de_erro)
            robo_brick.beepErro()
            robo_brick.falar(mensagem_de_erro)
            raise 

    return funcao_envolvida
# Código de robo_imports.py
# robo_imports.py

# Motor = None
# UltrasonicSensor = None
# ColorSensor = None
# GyroSensor = None
LUMPDevice = None
DCMotor = None
EV3Brick = None
PrimeHub = None

def load_hub(hub_type):
    global Motor, UltrasonicSensor, ColorSensor, GyroSensor, LUMPDevice, DCMotor, EV3Brick, PrimeHub
    if hub_type == RoboHub.EV3BRICK:
        print("Carregando EV3BRICK")
        from pybricks.ev3devices import Motor, UltrasonicSensor, ColorSensor, GyroSensor
        from pybricks.iodevices import LUMPDevice, DCMotor
        from pybricks.hubs import EV3Brick
    elif hub_type == RoboHub.SPIKEHUB:
        from pybricks.pupdevices import Motor, ColorSensor, ColorDistanceSensor, UltrasonicSensor, ForceSensor
        from pybricks.hubs import PrimeHub
    else:
        raise ValueError("Tipo de hub não suportado.")

class RoboImports:
    brick = None
    hub_type = None

    def __init__(self, hub_type):
        self.hub_type = hub_type
        load_hub(hub_type)
        self.brick = self.__get_hub()

    def __get_hub(self):
        if self.hub_type == RoboHub.EV3BRICK:
            return EV3Brick()
        elif self.hub_type == RoboHub.SPIKEHUB:
            return PrimeHub()
        else:
            raise ValueError("Tipo de hub não suportado.")

    @staticmethod
    def definirPorta(port: str):
        porta_map = {
            "A": Port.A, "B": Port.B, "C": Port.C, "D": Port.D,
            "1": Port.S1, "2": Port.S2, "3": Port.S3, "4": Port.S4,
        }
        try:
            return porta_map[port.upper()]
        except KeyError:
            raise TypeError("Porta não encontrada")


# Código de acoes_robo.py
# acoes_robo.py

class AcaoFinalRobo:
    @falar_erro
    def executar(self):
        raise NotImplementedError("Este método deve ser sobrescrito por uma subclasse.")

class DeixarRodarLivre(AcaoFinalRobo):
    @falar_erro
    def executar(self):
        return Stop.COAST

class PararLentamente(AcaoFinalRobo):
    @falar_erro
    def executar(self):
        return Stop.BRAKE

class PararInstantaneamenteEMantenhaNoAngulo(AcaoFinalRobo):
    @falar_erro
    def executar(self):
        return Stop.HOLD

# Código de cor_robo.py

class CorRobor(Color):
    def __init__(self):
        super().__init__()



# Código de hub_robo.py
class RoboHub:
    EV3BRICK = 1
    SPIKEHUB = 2

# Código de hub_base.py
# hub_base.py

class HubType(RoboImports):
    __instance = None  

    def __new__(cls, hub=RoboHub.EV3BRICK):  
        if cls.__instance is None:
            print("#### Inicializando HubType ####")
            cls.__instance = super(HubType, cls).__new__(cls)
        return cls.__instance

    def __init__(self, hub=RoboHub.EV3BRICK):
        if not hasattr(self, "_initialized"): 
            super().__init__(hub_type=hub)  
            self._initialized = True 
# Código de robo_motor.py
# robo_motor.py

class RoboMotor(Motor):
    def __init__(self, port: str, reverse:bool = False):
        try:
            direction = Direction.CLOCKWISE
            if(reverse):
                direction = Direction.COUNTERCLOCKWISE
            super().__init__(port=HubType.definirPorta(port), positive_direction=direction)
        except Exception as e:
            raise TypeError(f"Não foi possível iniciar o motor. Verifique a porta: {port}") from e

    @falar_erro
    def getVelocidade(self):
        """ Retorna a velocidade do motor """
        return self.speed()
    
    @falar_erro
    def getAngulo(self):
        """ Retorna o angulo do motor """
        return self.angle()
    
    @falar_erro
    def resetarAngulo(self):
        """ Reseta o angulo do motor para 0 """
        return self.redefinirAngulo(angulo=0)
    
    @falar_erro
    def redefinirAngulo(self, angulo: int):
        """ Define o angulo atual do motor para o angulo desejado """
        return self.reset_angle(angulo)
    
    @falar_erro
    def deixarMotorLivre(self):
        """ O motor para gradualmente devido ao atrito. """
        return self.stop()
    
    @falar_erro
    def paraMotorLentamente(self):
        """ O motor para devido ao atrito, mais a tensão gerada enquanto o motor ainda está em movimento. """
        return self.brake()
   
    @falar_erro
    def pararMotorInstantaneamente(self):
        """ Para o motor e o mantém travado no ângulo atual. """
        return self.hold()

    @falar_erro
    def mover(self, velocidade: float = 0):
        """ Para o motor e o mantém travado no ângulo atual. """
        return self.run(velocidade)
    

    @falar_erro
    def moverDuranteUmTempo(self, velocidade: float=0, tempo: int=0, aguardarAcaoFinalizar: bool =True, acaoAoFinalizar: AcaoFinalRobo = PararInstantaneamenteEMantenhaNoAngulo()):
        """ Mover o motor durante um determinado tempo. """
        """ velocidade: Em graus/segundos """
        """ tempo: Em milisegundos """
        """ aguardarAcaoFinalizar: por padrao é true """
        """ acaoAoFinalizar: por padrao recebe AcaoFinalRobo.pararInstantaneamenteEMantenhaNoAngulo """

        return self.run_time(velocidade, tempo, wait=aguardarAcaoFinalizar, then=acaoAoFinalizar.executar())

    @falar_erro
    def moverUmAngulo(self, velocidade: float, angulo: int, aguardarAcaoFinalizar: bool =True, acaoAoFinalizar: AcaoFinalRobo = PararInstantaneamenteEMantenhaNoAngulo()):
        """ Mover o motor por um determinado angulo. """
        """ velocidade: Em graus/segundos """
        """ angulo: Em graus """
        """ aguardarAcaoFinalizar: por padrao é true """
        """ acaoAoFinalizar: por padrao recebe AcaoFinalRobo.pararInstantaneamenteEMantenhaNoAngulo """
        return self.run_angle(velocidade, angulo, wait=aguardarAcaoFinalizar, then=acaoAoFinalizar.executar())
    
    
    @falar_erro
    def moverParaUmAnguloSuavemente(self, velocidade: float, anguloDestino: int, aguardarAcaoFinalizar: bool =True, acaoAoFinalizar: AcaoFinalRobo = PararInstantaneamenteEMantenhaNoAngulo()):
        """ Mover o motor para um determinado angulo baseado na referencia 0 do motor. """
        """ velocidade: Em graus/segundos """
        """ anguloDestino: Baseado na referencia 0 do motor """
        """ aguardarAcaoFinalizar: por padrao é true """
        """ acaoAoFinalizar: por padrao recebe AcaoFinalRobo.pararInstantaneamenteEMantenhaNoAngulo """
        return self.run_target(velocidade, anguloDestino, wait=aguardarAcaoFinalizar, then=acaoAoFinalizar.executar())

    @falar_erro
    def moverAteTravar(self, velocidade: float = 0, forcaLimite: int =100, acaoAoFinalizar: AcaoFinalRobo = PararInstantaneamenteEMantenhaNoAngulo()):
        """ Mover o motor até que ele trave """
        """ velocidade: Em graus/segundos """
        """ forcaLimite: forca limite para considerar travado, sendo em porcentagem do torque total do motor 0 - 100% """
        """ acaoAoFinalizar: por padrao recebe AcaoFinalRobo.pararInstantaneamenteEMantenhaNoAngulo """
        return self.run_until_stalled(velocidade, duty_limit=forcaLimite, then=acaoAoFinalizar.executar())

    @falar_erro
    def moverPorPotencia(self, potencia: float):
        """ Mover o motor baseado em sua potencia """
        """ potencia: - 100% até 100% da potencia do motor"""
        return self.dc(potencia)
    

    @falar_erro
    def moverParaUmAnguloRapidamente(self, anguloDestino: int):
        """ Mover o motor baseado em sua potencia """
        """ potencia: - 100% até 100% da potencia do motor"""
        return self.track_target(anguloDestino)


# Código de robo_brick.py

class RoboBrick:
   """ Traz funções do brick """
   __hubBase = None
    
   def __init__(self) -> None:
      self.__hubBase = HubType.brick

  
   def beep(self,
   frequencia: int = 500,
   duracao: int = 100):
      """ Emite som """
      self.definirVolume(100)
      self.__hubBase.speaker.beep(frequency=frequencia, duration=duracao)


   def definirVolume(self, volume: int = 100):
      """ Define volume do alto falante """
      if(HubType.hub_type == RoboHub.EV3BRICK):
         self.__hubBase.speaker.set_volume(volume)
      if(HubType.hub_type == RoboHub.SPIKEHUB):
         self.__hubBase.speaker.volume(volume)

   def beepErro(self):
      """ Sinaliza erro """
      self.definirVolume(100)
      self.beep(frequencia=100, duracao=500)

   def falar(self, texto: str):
      """ Fala o texto """
      self.definirVolume(100)
      if(HubType.hub_type == RoboHub.EV3BRICK):
         self.__hubBase.speaker.set_speech_options(language='pt-br', voice='m3', speed=120)
         self.__hubBase.speaker.say(text=texto)
# Código de seguidor.py

    # Variáveis de estado do seguidor de linha

class PIDController:

    __erroAnterior = 0    

    def __calcularErro(self, leitura_sensor_esquerdo, leitura_sensor_direito):
        return leitura_sensor_esquerdo - leitura_sensor_direito

    def __calcularPotencia(self, kp, kd, erro, erroAnterior):
        return (erro * kp) + kd * (erro - erroAnterior)

    def __excedenteMotores(self, potenciaCalculada, potencia_maxima):
        if abs(potenciaCalculada) < potencia_maxima:
            return 0
        if potenciaCalculada < 0:
            return potencia_maxima - abs(potenciaCalculada)
        return potenciaCalculada - potencia_maxima


    def calculoPID(
        self,
        valor_referencia_1: int, 
        valor_referencia_2: int, 
        kp: float = 1, 
        kd: float = 1, 
        valor_maximo_permitido: int = 70
    ):

        if valor_referencia_1 is None or valor_referencia_2 is None:
            raise TypeError("#### Verifique se os valores RGB foram passados corretamente #####")

        # Calcula o erro
        erro = self.__calcularErro(valor_referencia_1, valor_referencia_2)
        potencia = self.__calcularPotencia(kp, kd, erro, self.__erroAnterior)
        self.__erroAnterior = erro

        # Calcula potência para cada motor
        potencia_esquerdo = valor_maximo_permitido + potencia
        potencia_direito = valor_maximo_permitido - potencia

        diferenca_d = self.__excedenteMotores(potencia_direito, valor_maximo_permitido)
        diferenca_e = self.__excedenteMotores(potencia_esquerdo, valor_maximo_permitido)

        potencia_direito -= diferenca_e
        potencia_esquerdo -= diferenca_d

        potencia_esquerdo = max(-valor_maximo_permitido, min(potencia_esquerdo, valor_maximo_permitido))
        potencia_direito = max(-valor_maximo_permitido, min(potencia_direito, valor_maximo_permitido))

        # Mover motores
        return [potencia_esquerdo, potencia_direito]



    def seguirLinha(
        self,
        cor_vermelha_esquerda: int, 
        cor_vermelha_direita: int, 
        motor_direito: RoboMotor, 
        motor_esquerdo: RoboMotor, 
        kp: float = 1, 
        kd: float = 1, 
        potencia_motores: int = 70
    ):

        if motor_direito is None or motor_esquerdo is None:
            print("#### Verifique se os motores foram passados corretamente #####")
            raise TypeError("#### Verifique se os motores foram passados corretamente #####")

        potencia_esquerdo, potencia_direito = self.calculoPID(
            cor_vermelha_esquerda,
            cor_vermelha_direita,
            kp,
            kd,
            potencia_motores,
        )
        motor_direito.moverPorPotencia(potencia_direito)
        motor_esquerdo.moverPorPotencia(potencia_esquerdo)

# Código de sensores_robo.py
# sensores_robo.py
# from titas_lib.robo_imports import *


class RoboGiroscopio(GyroSensor):
    def __init__(self, port: str):
        try:
            super().__init__(port=HubType.definirPorta(port))
        except Exception as e:
            raise TypeError(f"Não foi possível iniciar o sensor. Verifique a porta: {port}") from e
    

    @falar_erro
    def getVelocidadeAngular(self):
        """ Retorna a velocidade angular """
        return self.speed()
    
    @falar_erro
    def getAnguloAcumulado(self):
        """ Retorna o angulo acumulado """
        return self.angle()
    

    @falar_erro
    def redefinirAnguloAcumulado(self, angulo: float):
        """ Retorna o angulo acumulado """
        return self.reset_angle(angulo)
    

    @falar_erro
    def resetAnguloAcumulado(self):
        """ Reseta o angulo acumulado para 0"""
        return self.redefinirAnguloAcumulado(0)
       
class RoboCor(ColorSensor):  

    def __init__(self, port: str):
        try:
            super().__init__(port=HubType.definirPorta(port))
        except Exception as e:
            raise TypeError(f"Não foi possível iniciar o sensor. Verifique a porta: {port}") from e


    @falar_erro
    def pegarRGB(self):
        if(HubType.hub_type == RoboHub.SPIKEHUB):
          raise TypeError("O Spike não possui essa funcionalidade")
        return self.rgb()

    @falar_erro
    def pegarCor(self):
        return self.color()
    
    @falar_erro
    def pegarHsv(self):
        if(HubType.hub_type == RoboHub.EV3BRICK):
          raise TypeError("O EV3 não possui essa funcionalidade")
        return self.hsv()
    
    @falar_erro
    def pegarReflexao(self):
        return self.reflection()
    

class RoboUltrassonico(UltrasonicSensor):

    def __init__(self, port: str):
        try:
            super().__init__(port=HubType.definirPorta(port))
        except Exception as e:
            raise TypeError(f"Não foi possível iniciar o sensor. Verifique a porta: {port}") from e

    @falar_erro
    def pegarDistancia(self):
        return self.distance()
    
    @falar_erro
    def verificarSePossuiOutroUltrassonico(self):
        return self.presence()
# Código de static_property.py
# static_property.py

class StaticProperty:
    def __init__(self, getter):
        self.getter = getter
    
    def __get__(self, obj, objtype=None):
        return self.getter()
