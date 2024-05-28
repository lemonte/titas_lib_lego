# robo_imports.py
from titas_lib.hub_base import RoboHub



class RoboImports:
    hub = None 
    hub_type= None

    def __init__(self, hub_type):
        self.hub_type = hub_type
        self.hub = self.load_hub()

    def load_hub(self):
        if self.hub_type == RoboHub.EV3BRICK:
            global Motor, UltrasonicSensor,LUMPDevice,DCMotor, ColorSensor, GyroSensor, Port, Stop, Direction, DriveBase, EV3Brick
            from pybricks.ev3devices import Motor, UltrasonicSensor, ColorSensor, GyroSensor
            from pybricks.parameters import Port, Stop, Direction
            from pybricks.robotics import DriveBase
            from pybricks.iodevices import LUMPDevice, DCMotor
            from pybricks.hubs import EV3Brick
            return EV3Brick()

        elif self.hub_type == RoboHub.SPIKEHUB:
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


    def getDriveBase(self, motorEsquerdo, motorDireito, diametroRoda: float, distanciaEntreAsRodas: int ):
        """ Retorna o objeto DriveBase do lego """
        return DriveBase(motorEsquerdo.getMotor(), motorDireito.getMotor(), wheel_diameter=diametroRoda, axle_track=distanciaEntreAsRodas)


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
    

