# acoes_robo.py
from titas_lib.robo_imports import Stop
from titas_lib.falar_erro import falar_erro

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
