# robo_motor.py
from titas_lib.hub_base import HubType
from titas_lib.acoes_robo import PararInstantaneamenteEMantenhaNoAngulo, __AcaoFinalRobo
from titas_lib.falar_erro import falar_erro

class RoboMotor:
    __motor = None

    @falar_erro
    def __init__(self, Port: str):
        print("#### RoboMotor ####")
        try:
            self.__motor = HubType.__instance.getImports().get_motor(port=Port)
        except Exception as _:
          raise TypeError("Não foi possivel iniciar o motor, verifique a porta: " + Port)
    
    @falar_erro
    def getMotor(self):
        """ Retorna o objeto do motor """
        if(self.__motor == None):
          raise TypeError("Motor não instanciado anteriormente")
        return self.__motor

    @falar_erro
    def getVelocidade(self):
        """ Retorna a velocidade do motor """
        return self.getMotor().speed()
    
    @falar_erro
    def getAngulo(self):
        """ Retorna o angulo do motor """
        return self.getMotor().angle()
    
    @falar_erro
    def resetarAngulo(self):
        """ Reseta o angulo do motor para 0 """
        return self.redefinirAngulo(angulo=0)
    
    @falar_erro
    def redefinirAngulo(self, angulo: int):
        """ Define o angulo atual do motor para o angulo desejado """
        return self.getMotor().reset_angle(angulo)
    
    @falar_erro
    def deixarMotorLivre(self):
        """ O motor para gradualmente devido ao atrito. """
        return self.getMotor().stop()
    
    @falar_erro
    def paraMotorLentamente(self):
        """ O motor para devido ao atrito, mais a tensão gerada enquanto o motor ainda está em movimento. """
        return self.getMotor().brake()
   
    @falar_erro
    def pararMotorInstantaneamente(self):
        """ Para o motor e o mantém travado no ângulo atual. """
        return self.getMotor().hold()

    @falar_erro
    def mover(self, velocidade: float = 0):
        """ Para o motor e o mantém travado no ângulo atual. """
        return self.getMotor().run(velocidade)
    

    @falar_erro
    def moverDuranteUmTempo(self, velocidade: float=0, tempo: int=0, aguardarAcaoFinalizar: bool =True, acaoAoFinalizar: __AcaoFinalRobo = PararInstantaneamenteEMantenhaNoAngulo()):
        """ Mover o motor durante um determinado tempo. """
        """ velocidade: Em graus/segundos """
        """ tempo: Em milisegundos """
        """ aguardarAcaoFinalizar: por padrao é true """
        """ acaoAoFinalizar: por padrao recebe AcaoFinalRobo.pararInstantaneamenteEMantenhaNoAngulo """

        return self.getMotor().run_time(velocidade, tempo, wait=aguardarAcaoFinalizar, then=acaoAoFinalizar.executar())

    @falar_erro
    def moverUmAngulo(self, velocidade: float, angulo: int, aguardarAcaoFinalizar: bool =True, acaoAoFinalizar: __AcaoFinalRobo = PararInstantaneamenteEMantenhaNoAngulo()):
        """ Mover o motor por um determinado angulo. """
        """ velocidade: Em graus/segundos """
        """ angulo: Em graus """
        """ aguardarAcaoFinalizar: por padrao é true """
        """ acaoAoFinalizar: por padrao recebe AcaoFinalRobo.pararInstantaneamenteEMantenhaNoAngulo """
        return self.getMotor().run_angle(velocidade, angulo, wait=aguardarAcaoFinalizar, then=acaoAoFinalizar.executar())
    
    
    @falar_erro
    def moverParaUmAnguloSuavemente(self, velocidade: float, anguloDestino: int, aguardarAcaoFinalizar: bool =True, acaoAoFinalizar: __AcaoFinalRobo = PararInstantaneamenteEMantenhaNoAngulo()):
        """ Mover o motor para um determinado angulo baseado na referencia 0 do motor. """
        """ velocidade: Em graus/segundos """
        """ anguloDestino: Baseado na referencia 0 do motor """
        """ aguardarAcaoFinalizar: por padrao é true """
        """ acaoAoFinalizar: por padrao recebe AcaoFinalRobo.pararInstantaneamenteEMantenhaNoAngulo """
        return self.getMotor().run_target(velocidade, anguloDestino, wait=aguardarAcaoFinalizar, then=acaoAoFinalizar.executar())

    @falar_erro
    def moverAteTravar(self, velocidade: float = 0, forcaLimite: int =100, acaoAoFinalizar: __AcaoFinalRobo = PararInstantaneamenteEMantenhaNoAngulo()):
        """ Mover o motor até que ele trave """
        """ velocidade: Em graus/segundos """
        """ forcaLimite: forca limite para considerar travado, sendo em porcentagem do torque total do motor 0 - 100% """
        """ acaoAoFinalizar: por padrao recebe AcaoFinalRobo.pararInstantaneamenteEMantenhaNoAngulo """
        return self.getMotor().run_until_stalled(velocidade, duty_limit=forcaLimite, then=acaoAoFinalizar.executar())

    @falar_erro
    def moverPorPotencia(self, potencia: float):
        """ Mover o motor baseado em sua potencia """
        """ potencia: - 100% até 100% da potencia do motor"""
        return self.getMotor().dc(potencia)
    

    @falar_erro
    def moverParaUmAnguloRapidamente(self, anguloDestino: int):
        """ Mover o motor baseado em sua potencia """
        """ potencia: - 100% até 100% da potencia do motor"""
        return self.getMotor().track_target(anguloDestino)

