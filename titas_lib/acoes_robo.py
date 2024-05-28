# acoes_robo.py
from titas_lib.hub_base import HubType
from titas_lib.falar_erro import falar_erro

class __AcaoFinalRobo:
    @falar_erro
    def executar(self):
        raise NotImplementedError("Este método deve ser sobrescrito por uma subclasse.")

class DeixarRodarLivre(__AcaoFinalRobo):
    @falar_erro
    def executar(self):
        return HubType.__instance.getImports().getStop().COAST

class PararLentamente(__AcaoFinalRobo):
    @falar_erro
    def executar(self):
        return HubType.__instance.getImports().getStop().BRAKE

class PararInstantaneamenteEMantenhaNoAngulo(__AcaoFinalRobo):
    @falar_erro
    def executar(self):
        return HubType.__instance.getImports().getStop().HOLD
