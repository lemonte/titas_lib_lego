# robo_brick.py
from titas_lib.hub_base import HubType
from titas_lib.robo_motor import RoboMotor
from titas_lib.falar_erro import falar_erro
from titas_lib.acoes_robo import PararInstantaneamenteEMantenhaNoAngulo


class RoboBase:
    __driveBase = None
    @falar_erro
    def __init__(self, 
            motorEsquerdo: RoboMotor,
            motorDireito: RoboMotor,
            diametroRoda: float,
            distanciaEntreAsRodas: int,
    ) -> None:
        print("#### RoboBase ####")
        self.__driveBase = HubType.__instance.getImports().getDriveBase(
            motorDireito=motorDireito, 
            motorEsquerdo=motorEsquerdo, 
            diametroRoda=diametroRoda, 
            distanciaEntreAsRodas=distanciaEntreAsRodas,
        )
        
    @falar_erro
    def virar90grausEsquerda(self):
        """ Virar 90 graus para esquerda  """
        return self.virarAngulo(90)
    
    @falar_erro
    def moverDistancia(self, distancia: float = 0):
        return self.__driveBase.straight(distancia)


    @falar_erro
    def moverSemParar(self, velocidade: float = 0, angulo_curvatura: float =0):
        """ Essa função faz com que o robo ande, até que outro comando chame a função de parar  """
        """ velocidade = "Velocidade que o robo irá se mover"  """
        """ angulo_curvatura = "Angulo que o robo ira fazer enquanto se move, exemplo: angulo_curvatura=0, ele seguirá reto"  """
        return self.__driveBase.drive(velocidade, turn_rate=angulo_curvatura)

    @falar_erro
    def virar90grausDireita(self):
        """ Virar 90 graus para direita  """
        return self.virarAngulo(-90)
    
    @falar_erro
    def virar180grausDireita(self):
        """ Virar 180 graus para direita  """
        return self.virarAngulo(-180)
    
    @falar_erro
    def pararMotores(self):
        return self.__driveBase.stop()

    @falar_erro
    def virar180grausEsquerda(self):
        """ Virar 180 graus para esquerda  """
        return self.virarAngulo(180)

    
    @falar_erro
    def virarAngulo(self, angulo: float = 0):
        """ Virar angulo definido  """
        return self.__driveBase.turn( angle=angulo)
    
