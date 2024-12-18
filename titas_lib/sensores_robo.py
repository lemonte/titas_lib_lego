# sensores_robo.py
from titas_lib.hub_base import HubType
from titas_lib.hub_robo import RoboHub
from titas_lib.falar_erro import falar_erro
from titas_lib.robo_imports import *


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