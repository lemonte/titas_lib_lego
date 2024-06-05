# acoes_robo.py
from titas_lib.hub_base import HubType
from titas_lib.falar_erro import falar_erro

class AcaoFinalRobo:
    @falar_erro
    def executar(self):
        raise NotImplementedError("Este método deve ser sobrescrito por uma subclasse.")

class DeixarRodarLivre(AcaoFinalRobo):
    @falar_erro
    def executar(self):
        return HubType.__instance.getImports().getStop().COAST

class PararLentamente(AcaoFinalRobo):
    @falar_erro
    def executar(self):
        return HubType.__instance.getImports().getStop().BRAKE

class PararInstantaneamenteEMantenhaNoAngulo(AcaoFinalRobo):
    @falar_erro
    def executar(self):
        return HubType.__instance.getImports().getStop().HOLD
