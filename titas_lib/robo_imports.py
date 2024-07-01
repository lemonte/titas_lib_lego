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
PrimeHub = None
Color = None
Button = None
Icon = None
Side = None
ColorDistanceSensor = None
ForceSensor = None
ColorDistanceSensor = None

def load_hub(hub_type):
    global Motor, UltrasonicSensor, ColorSensor, GyroSensor, LUMPDevice, DCMotor, Port, Stop, Direction, DriveBase, EV3Brick, Color, Button, Icon, Side
    if hub_type == RoboHub.EV3BRICK:
        from pybricks.ev3devices import Motor as ev3Motor, UltrasonicSensor as ev3UltrasonicSensor, ColorSensor as ev3ColorSensor, GyroSensor as ev3GyroSensor
        from pybricks.parameters import Port as ev3Port, Stop as ev3Stop, Direction as ev3Direction, Color as ev3Color, Button as ev3Button, Icon as ev3Icon, Side as ev3Side
        from pybricks.robotics import DriveBase as ev3DriveBase
        from pybricks.iodevices import LUMPDevice as ev3LUMPDevice, DCMotor as ev3DCMotor
        from pybricks.hubs import EV3Brick as ev3EV3Brick
        
        Motor = ev3Motor
        UltrasonicSensor = ev3UltrasonicSensor
        ColorSensor = ev3ColorSensor
        GyroSensor = ev3GyroSensor
        LUMPDevice = ev3LUMPDevice
        DCMotor = ev3DCMotor
        Port = ev3Port
        Stop = ev3Stop
        Direction = ev3Direction
        DriveBase = ev3DriveBase
        EV3Brick = ev3EV3Brick
        Color = ev3Color
        Button = ev3Button
        Icon = ev3Icon
        Side = ev3Side
        
    elif hub_type == RoboHub.SPIKEHUB:
        from pybricks.pupdevices import Motor as spikeMotor, ColorSensor as spikeColorSensor, ColorDistanceSensor as spikeColorDistanceSensor, UltrasonicSensor as spikeUltrasonicSensor, ForceSensor as spikeForceSensor
        from pybricks.parameters import Port as spikePort, Stop as spikeStop, Direction as spikeDirection, Color as spikeColor, Button as spikeButton, Icon as spikeIcon, Side as spikeSide
        from pybricks.robotics import DriveBase as spikeDriveBase
        from pybricks.hubs import PrimeHub as spikePrimeHub
        
        Motor = spikeMotor
        ColorSensor = spikeColorSensor
        ColorDistanceSensor = spikeColorDistanceSensor
        UltrasonicSensor = spikeUltrasonicSensor
        ForceSensor = spikeForceSensor
        Port = spikePort
        Stop = spikeStop
        Direction = spikeDirection
        DriveBase = spikeDriveBase
        PrimeHub = spikePrimeHub
        Color = spikeColor
        Button = spikeButton
        Icon = spikeIcon
        Side = spikeSide
        
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

    def get_motor(self, port: str):
        return Motor(self.__definirPorta(port))

    def getGiroscopico(self, port: str):
        return GyroSensor(self.__definirPorta(port))

    def getStop(self):
        """ Retorna a classe de Stop do lego. """
        return Stop

    def getColorSensor(self, Port: str):
        return ColorSensor(self.__definirPorta(Port))

    def getLUMPDevice(self, Port: str):
        return LUMPDevice(self.__definirPorta(Port))

    def getUltrasonicSensor(self, Port: str):
        return UltrasonicSensor(self.__definirPorta(Port))

    def getDCMotor(self, Port: str):
        """ Retorna o objeto DC do Motor do lego """
        return DCMotor(self.__definirPorta(Port))

    def getDirection(self):
        """ Retorna a classe Direction do lego """
        return Direction

    def getDriveBase(self, motorEsquerdo, motorDireito, diametroRoda: float, distanciaEntreAsRodas: int):
        """ Retorna o objeto DriveBase do lego """
        return DriveBase(motorEsquerdo.getMotor(), motorDireito.getMotor(), wheel_diameter=diametroRoda, axle_track=distanciaEntreAsRodas)

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
