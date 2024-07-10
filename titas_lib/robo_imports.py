# robo_imports.py
from titas_lib.hub_base import RoboHub

Motor = None
UltrasonicSensor = None
ColorSensor = None
GyroSensor = None
LUMPDevice = None
DCMotor = None
Port = None
Stop = None
Direction = None
DriveBase = None
EV3Brick = None
Color = None
Button = None
Icon = None
Side = None
PrimeHub = None

def load_hub(hub_type):
    global Motor, UltrasonicSensor, ColorSensor, GyroSensor, LUMPDevice, DCMotor, Port, Stop, Direction, DriveBase, EV3Brick, Color, Button, Icon, Side, PrimeHub
    if hub_type == RoboHub.EV3BRICK:
        from pybricks.ev3devices import Motor, UltrasonicSensor, ColorSensor, GyroSensor
        from pybricks.parameters import Port, Stop, Direction, Color, Button
        from pybricks.robotics import DriveBase
        from pybricks.iodevices import LUMPDevice, DCMotor
        from pybricks.hubs import EV3Brick
    elif hub_type == RoboHub.SPIKEHUB:
        from pybricks.pupdevices import Motor, ColorSensor, ColorDistanceSensor, UltrasonicSensor, ForceSensor
        from pybricks.parameters import Port, Stop, Direction, Color, Button, Icon, Side
        from pybricks.robotics import DriveBase
        from pybricks.hubs import PrimeHub
    else:
        raise ValueError("Tipo de hub não suportado.")

class RoboImports:
    hub = None
    hub_type = None

    def __init__(self, hub_type):
        self.hub_type = hub_type
        load_hub(hub_type)
        self.hub = self.get_hub()

    def get_hub(self):
        if self.hub_type == RoboHub.EV3BRICK:
            return EV3Brick()
        elif self.hub_type == RoboHub.SPIKEHUB:
            return PrimeHub()
        else:
            raise ValueError("Tipo de hub não suportado.")

    def get_motor(self, port: str, reverse:bool =False):
        direction = Direction.CLOCKWISE
        if(reverse):
            direction = Direction.COUNTERCLOCKWISE
        return Motor(self.__definirPorta(port), positive_direction=direction)

    def getGiroscopico(self, port: str):
        try:
            return GyroSensor(self.__definirPorta(port))
        except Exception as e:
            raise ValueError("Não foi possível iniciar o Giroscópio. porta: " + port)

    def getStop(self):
        """ Retorna a classe de Stop do lego. """
        return Stop

    def getColor(self):
        """ Retorna a classe de Color do lego. """
        return Color

    def getColorSensor(self, Port: str):
        try:
            return ColorSensor(self.__definirPorta(Port))
        except Exception as e:
            raise ValueError("Não foi possível iniciar o sensor de Cor. porta: " + Port)

    def getLUMPDevice(self, Port: str):
        try:
            return LUMPDevice(self.__definirPorta(Port=Port))
        except Exception as e:
            raise ValueError("Não foi possível iniciar o LUMPDevice. porta: " + Port)

    def getUltrasonicSensor(self, Port: str):
        try:
            return UltrasonicSensor(self.__definirPorta(Port=Port))
        except Exception as e:
            raise ValueError("Não foi possível iniciar o UltrasonicSensor. porta: " + Port)

    def getDCMotor(self, Port: str):
        """ Retorna o objeto DC do Motor do lego """
        try:
            return DCMotor(self.__definirPorta(Port=Port))
        except Exception as e:
            raise ValueError("Não foi possível iniciar o DCMotor. porta: " + Port)

    def getDirection(self):
        """ Retorna a classe Direction do lego """
        return Direction

    def getDriveBase(self, motorEsquerdo, motorDireito, diametroRoda: float, distanciaEntreAsRodas: int):
        """ Retorna o objeto DriveBase do lego """
        try:
            return DriveBase(motorEsquerdo.getMotor(), motorDireito.getMotor(), wheel_diameter=diametroRoda, axle_track=distanciaEntreAsRodas)
        except Exception as e:
            raise ValueError("Não foi possível iniciar o DriveBase.")

    def getPorta(self):
        """ Retorna a classe com a porta desejada do lego """
        return Port

    def __definirPorta(self, Port: str):
        """ Faz tratativa para a porta do lego """
        porta = None
        if Port.upper() == "A":
            porta = self.getPorta().A
        elif Port.upper() == "B":
            porta = self.getPorta().B
        elif Port.upper() == "C":
            porta = self.getPorta().C
        elif Port.upper() == "D":
            porta = self.getPorta().D
        elif Port.upper() == "1":
            porta = self.getPorta().S1
        elif Port.upper() == "2":
            porta = self.getPorta().S2
        elif Port.upper() == "3":
            porta = self.getPorta().S3
        elif Port.upper() == "4":
            porta = self.getPorta().S4
        if porta is None:
            raise TypeError("Porta não encontrada")
        return porta
