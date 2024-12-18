# sensores_robo.py
from titas_lib.hub_base import HubType
from titas_lib.hub_robo import RoboHub
from titas_lib.falar_erro import falar_erro
from titas_lib.robo_imports import *


class RoboGiroscopio:
    __giro = None

    @falar_erro
    def __init__(self, port: str):
        print("#### RoboGiroscopio ####")
        try:
            self.__giro = GyroSensor(port=HubType.definirPorta(port))
        except Exception as _:
          raise TypeError("Não foi possivel iniciar o sensor, verifique a porta: " + port)
    
    

    @falar_erro
    def getGiroscopio(self):
        """ Retorna o objeto do motor """
        if(self.__giro == None):
          raise TypeError("Giroscópio não instanciado anteriormente")
        return self.__giro
    

    @falar_erro
    def getVelocidadeAngular(self):
        """ Retorna a velocidade angular """
        return self.getGiroscopio().speed()
    
    @falar_erro
    def getAnguloAcumulado(self):
        """ Retorna o angulo acumulado """
        return self.getGiroscopio().angle()
    

    @falar_erro
    def redefinirAnguloAcumulado(self, angulo: float):
        """ Retorna o angulo acumulado """
        return self.getGiroscopio().reset_angle(angulo)
    

    @falar_erro
    def resetAnguloAcumulado(self):
        """ Reseta o angulo acumulado para 0"""
        return self.redefinirAnguloAcumulado(0)
       

class RoboCor:
    __sensor = None

    @falar_erro
    def __init__(self, port: str):
        try:
            print("#### RoboCor ####")
            self.__sensor = ColorSensor(port=HubType.definirPorta(port))
        except Exception as _:
          raise TypeError("Não foi possivel iniciar o sensor, verifique a porta: " + port)
            
    @falar_erro
    def pegarRGB(self):
        if(HubType.hub_type == RoboHub.SPIKEHUB):
          raise TypeError("O Spike não possui essa funcionalidade")
        return self.__sensor.rgb()

    @falar_erro
    def pegarCor(self):
        return self.__sensor.color()
    
    @falar_erro
    def pegarHsv(self):
        if(HubType.hub_type == RoboHub.EV3BRICK):
          raise TypeError("O EV3 não possui essa funcionalidade")
        return self.__sensor.hsv()
    
    @falar_erro
    def pegarReflexao(self):
        return self.__sensor.reflection()
    

class RoboUltrassonico:
    __sensor = None

    @falar_erro
    def __init__(self, port: str):
        print("#### RoboUltrassonico ####")
        try:
            self.__sensor = UltrasonicSensor(port=HubType.definirPorta(port=port))
        except Exception as _:
          raise TypeError("Não foi possivel iniciar o sensor, verifique a porta: " + port)
    
    @falar_erro
    def pegarDistancia(self):
        return self.__sensor.distance()
    
    @falar_erro
    def verificarSePossuiOutroUltrassonico(self):
        return self.__sensor.presence()