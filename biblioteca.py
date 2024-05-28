
#!/usr/bin/env pybricks-micropython


class StaticProperty:
    def __init__(self, getter):
        self.getter = getter
    
    def __get__(self, obj, objtype=None):
        return self.getter()


class HubRobo:

    @StaticProperty
    def EV3BRICK():
       return 1
    
    @StaticProperty
    def PRIMEHUB():
       return 2


class HubBase:
    __instance = None
    __imports = None


    def __init__(self,
            hub=HubRobo.EV3BRICK,    
        ):
        if HubBase.__instance is None:
            print("#### RoboImports ####")
            self.__imports = RoboImports(hub_type=hub)
            HubBase.__instance = self

    def getImports(self):
        if(self.__imports == None):
          raise TypeError("RoboBase não instanciado anteriormente")
        return self.__imports
    



class StaticProperty:
    def __init__(self, getter):
        self.getter = getter
    
    def __get__(self, obj, objtype=None):
        return self.getter()





class __AcaoFinalRobo:
    def executar(self):
        raise NotImplementedError("Este método deve ser sobrescrito por uma subclasse.")


class DeixarRodarLivre(__AcaoFinalRobo):
    def executar(self):
        return HubBase.__instance.getImports().getStop().COAST

class PararLentamente(__AcaoFinalRobo):
    def executar(self):
        return HubBase.__instance.getImports().getStop().BRAKE

class PararInstantaneamenteEMantenhaNoAngulo(__AcaoFinalRobo):
    def executar(self):
        return HubBase.__instance.getImports().getStop().HOLD


   
class RoboGiroscopio:
    __giro = None
    def __init__(self, Port: str):
        self.__giro = HubBase.__instance.getImports().getGiroscopico(Port=Port)
    

    def getGiroscopio(self):
        """ Retorna o objeto do motor """
        if(self.__giro == None):
          raise TypeError("Giroscópio não instanciado anteriormente")
        return self.__giro
    

    def getVelocidadeAngular(self):
        """ Retorna a velocidade angular """
        return self.getGiroscopio().speed()
    
    def getAnguloAcumulado(self):
        """ Retorna o angulo acumulado """
        return self.getGiroscopio().angle()
    

    def redefinirAnguloAcumulado(self, angulo: float):
        """ Retorna o angulo acumulado """
        return self.getGiroscopio().reset_angle(angulo)
    

    def resetAnguloAcumulado(self):
        """ Reseta o angulo acumulado para 0"""
        return self.redefinirAnguloAcumulado(0)
       

   
class RoboCor:
    __sensor = None
    def __init__(self, Port: str):
        print("#### RoboMotor ####")
        self.__sensor = HubBase.__instance.getImports().getColorSensor(Port=Port)
    
    def pegarCor(self):
        return self.__sensor.color()
    
    def pegarHsv(self):
        return self.__sensor.hsv()
    
    def pegarReflexao(self):
        return self.__sensor.reflection()


class RoboUltrassonico:
    __sensor = None
    def __init__(self, Port: str):
        print("#### RoboMotor ####")
        self.__sensor = HubBase.__instance.getImports().getUltrasonicSensor(Port=Port)
    
    def pegarDistancia(self):
        return self.__sensor.distance()
    
    def verificarSePossuiOutroUltrassonico(self):
        return self.__sensor.presence()
    


class RoboMotor:
    __motor = None
    def __init__(self, Port: str):
        print("#### RoboMotor ####")
        self.__motor = HubBase.__instance.getImports().get_motor(port=Port)
    
    def getMotor(self):
        """ Retorna o objeto do motor """
        if(self.__motor == None):
          raise TypeError("Motor não instanciado anteriormente")
        return self.__motor

    def getVelocidade(self):
        """ Retorna a velocidade do motor """
        return self.getMotor().speed()
    
    def getAngulo(self):
        """ Retorna o angulo do motor """
        return self.getMotor().angle()
    
    def resetarAngulo(self):
        """ Reseta o angulo do motor para 0 """
        return self.redefinirAngulo(angulo=0)
    
    def redefinirAngulo(self, angulo: int):
        """ Define o angulo atual do motor para o angulo desejado """
        return self.getMotor().reset_angle(angulo)
    
    def deixarMotorLivre(self):
        """ O motor para gradualmente devido ao atrito. """
        return self.getMotor().stop()
    
    def paraMotorLentamente(self):
        """ O motor para devido ao atrito, mais a tensão gerada enquanto o motor ainda está em movimento. """
        return self.getMotor().brake()
   
    def pararMotorInstantaneamente(self):
        """ Para o motor e o mantém travado no ângulo atual. """
        return self.getMotor().hold()

    def mover(self, velocidade: float = 0):
        """ Para o motor e o mantém travado no ângulo atual. """
        return self.getMotor().run(velocidade)
    

    def moverDuranteUmTempo(self, velocidade: float=0, tempo: int=0, aguardarAcaoFinalizar: bool =True, acaoAoFinalizar: __AcaoFinalRobo = PararInstantaneamenteEMantenhaNoAngulo()):
        """ Mover o motor durante um determinado tempo. """
        """ velocidade: Em graus/segundos """
        """ tempo: Em milisegundos """
        """ aguardarAcaoFinalizar: por padrao é true """
        """ acaoAoFinalizar: por padrao recebe AcaoFinalRobo.pararInstantaneamenteEMantenhaNoAngulo """

        return self.getMotor().run_time(velocidade, tempo, wait=aguardarAcaoFinalizar, then=acaoAoFinalizar.executar())

    def moverUmAngulo(self, velocidade: float, angulo: int, aguardarAcaoFinalizar: bool =True, acaoAoFinalizar: __AcaoFinalRobo = PararInstantaneamenteEMantenhaNoAngulo()):
        """ Mover o motor por um determinado angulo. """
        """ velocidade: Em graus/segundos """
        """ angulo: Em graus """
        """ aguardarAcaoFinalizar: por padrao é true """
        """ acaoAoFinalizar: por padrao recebe AcaoFinalRobo.pararInstantaneamenteEMantenhaNoAngulo """
        return self.getMotor().run_angle(velocidade, angulo, wait=aguardarAcaoFinalizar, then=acaoAoFinalizar.executar())
    
    
    def moverParaUmAnguloSuavemente(self, velocidade: float, anguloDestino: int, aguardarAcaoFinalizar: bool =True, acaoAoFinalizar: __AcaoFinalRobo = PararInstantaneamenteEMantenhaNoAngulo()):
        """ Mover o motor para um determinado angulo baseado na referencia 0 do motor. """
        """ velocidade: Em graus/segundos """
        """ anguloDestino: Baseado na referencia 0 do motor """
        """ aguardarAcaoFinalizar: por padrao é true """
        """ acaoAoFinalizar: por padrao recebe AcaoFinalRobo.pararInstantaneamenteEMantenhaNoAngulo """
        return self.getMotor().run_target(velocidade, anguloDestino, wait=aguardarAcaoFinalizar, then=acaoAoFinalizar.executar())

    def moverAteTravar(self, velocidade: float = 0, forcaLimite: int =100, acaoAoFinalizar: __AcaoFinalRobo = PararInstantaneamenteEMantenhaNoAngulo()):
        """ Mover o motor até que ele trave """
        """ velocidade: Em graus/segundos """
        """ forcaLimite: forca limite para considerar travado, sendo em porcentagem do torque total do motor 0 - 100% """
        """ acaoAoFinalizar: por padrao recebe AcaoFinalRobo.pararInstantaneamenteEMantenhaNoAngulo """
        return self.getMotor().run_until_stalled(velocidade, duty_limit=forcaLimite, then=acaoAoFinalizar.executar())

    def moverPorPotencia(self, potencia: float):
        """ Mover o motor baseado em sua potencia """
        """ potencia: - 100% até 100% da potencia do motor"""
        return self.getMotor().dc(potencia)
    

    def moverParaUmAnguloRapidamente(self, anguloDestino: int):
        """ Mover o motor baseado em sua potencia """
        """ potencia: - 100% até 100% da potencia do motor"""
        return self.getMotor().track_target(anguloDestino)


      


class RoboImports:
    hub = None 
    def __init__(self, hub_type):
        self.hub_type = hub_type
        self.hub = self.load_hub()

    def load_hub(self):
        print(self.hub_type)
        if self.hub_type == HubRobo.EV3BRICK:
            global Motor, UltrasonicSensor,LUMPDevice,DCMotor, ColorSensor, GyroSensor, Port, Stop, Direction, DriveBase, EV3Brick
            from pybricks.ev3devices import Motor, UltrasonicSensor, ColorSensor, GyroSensor
            from pybricks.parameters import Port, Stop, Direction
            from pybricks.robotics import DriveBase
            from pybricks.iodevices import LUMPDevice, DCMotor
            from pybricks.hubs import EV3Brick
            return EV3Brick()

        elif self.hub_type == HubRobo.PRIMEHUB:
            global Motor, ColorSensor, ColorDistanceSensor, UltrasonicSensor, ForceSensor, Port, Stop, Direction, DriveBase, PrimeHub
            from pybricks.pupdevices import Motor, ColorSensor, ColorDistanceSensor, UltrasonicSensor, ForceSensor
            from pybricks.parameters import Port, Stop, Direction
            from pybricks.robotics import DriveBase
            from pybricks.hubs import PrimeHub
            return PrimeHub()

        else:
            raise ValueError("Tipo de hub não suportado.")

      
    def get_motor(self, port: str):
        return Motor(self.__definirPorta(Port=port))

    def getGiroscopico(self, port: str):
        return GyroSensor(self.__definirPorta(port))


    def getPorta(self):
        """ Retorna a classe Port do lego. """
        return Port
    
    def getStop(self):
        """ Retorna a classe de Stop do lego. """
        return Stop
    
    
    def getColorSensor(self, Port: str):
        return ColorSensor(self.__definirPorta(Port))

    
    
    def getLUMPDevice(self, Port: str):
            return LUMPDevice(self.__definirPorta(Port=Port))



    def getUltrasonicSensor(self, Port: str):
            return UltrasonicSensor(self.__definirPorta(Port=Port))


    def getDCMotor(self, Port: str):
        """ Retorna o objeto DC do Motor do lego """
        return DCMotor(self.__definirPorta(Port=Port))
    

    def getDirection(self):
        """ Retorna a classe Direction do lego """
        return Direction


    def getDriveBase(self, motorEsquerdo: RoboMotor, motorDireito: RoboMotor, diametroRoda: float, distanciaEntreAsRodas: int ):
        """ Retorna o objeto DriveBase do lego """
        return DriveBase(motorEsquerdo.getMotor(), motorDireito.getMotor(), wheel_diameter=diametroRoda, axle_track=distanciaEntreAsRodas)


    def getEv3Brick(self):
        """ Retorna o objeto EV3Brick do lego """
        return EV3Brick


    def getPorta(self):
        """ Retorna a classe com a porta desejada do lego """
        return Port
    
    
    def __definirPorta(self, Port: str):
        """ Faz tratativa para a porta do lego """
        porta = None
        if(Port.upper() == "A"):
            porta = self.getPorta().A
        elif(Port.upper() == "B"):
            porta = self.getPorta().B
        elif(Port.upper() == "C"):
            porta = self.getPorta().C
        elif(Port.upper() == "D"):
            porta = self.getPorta().D
        elif(Port.upper() == "1"):
            porta = self.getPorta().S1
        elif(Port.upper() == "2"):
            porta = self.getPorta().S2
        elif(Port.upper() == "3"):
            porta = self.getPorta().S3
        elif(Port.upper() == "4"):
            porta = self.getPorta().S4
        if(porta == None):
            raise TypeError("Porta não encontrada")
        return porta
    

class RoboBrick:
    __driveBase = None
    def __init__(self, 
            motorEsquerdo: RoboMotor,
            motorDireito: RoboMotor,
            diametroRoda: float,
            distanciaEntreAsRodas: int,
    ) -> None:
        print("#### RoboBrick ####")
        self.__driveBase = HubBase.__instance.getImports().getDriveBase(
            motorDireito=motorDireito, 
            motorEsquerdo=motorEsquerdo, 
            diametroRoda=diametroRoda, 
            distanciaEntreAsRodas=distanciaEntreAsRodas,
        )
        
    def virar90grausEsquerda(self):
        """ Virar 90 graus para esquerda  """
        return self.virarAngulo(90)
    
    def virar90grausDireita(self):
        """ Virar 90 graus para direita  """
        return self.virarAngulo(-90)
    
    def virar180grausDireita(self):
        """ Virar 180 graus para direita  """
        return self.virarAngulo(-180)
    
    def virar180grausEsquerda(self):
        """ Virar 180 graus para esquerda  """
        return self.virarAngulo(180)

    
    def virarAngulo(self, angulo: float =0):
        """ Virar angulo definido  """
        return self.__driveBase.turn(then=PararInstantaneamenteEMantenhaNoAngulo().executar(), angle=angulo, wait=True)
    
