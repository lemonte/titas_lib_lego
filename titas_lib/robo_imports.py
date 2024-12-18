# robo_imports.py
from titas_lib.hub_base import RoboHub
from titas_lib.robo_motor import RoboMotor
from pybricks.parameters import *
from pybricks.robotics import DriveBase

Motor = None
UltrasonicSensor = None
ColorSensor = None
GyroSensor = None
LUMPDevice = None
DCMotor = None
EV3Brick = None
PrimeHub = None

def load_hub(hub_type):
    global Motor, UltrasonicSensor, ColorSensor, GyroSensor, LUMPDevice, DCMotor, EV3Brick, PrimeHub
    if hub_type == RoboHub.EV3BRICK:
        from pybricks.ev3devices import Motor, UltrasonicSensor, ColorSensor, GyroSensor
        from pybricks.iodevices import LUMPDevice, DCMotor
        from pybricks.hubs import EV3Brick
    elif hub_type == RoboHub.SPIKEHUB:
        from pybricks.pupdevices import Motor, ColorSensor, ColorDistanceSensor, UltrasonicSensor, ForceSensor
        from pybricks.hubs import PrimeHub
    else:
        raise ValueError("Tipo de hub não suportado.")

class RoboImports:
    brick = None
    hub_type = None

    def __init__(self, hub_type):
        self.hub_type = hub_type
        load_hub(hub_type)
        self.brick = self.__get_hub()

    def __get_hub(self):
        if self.hub_type == RoboHub.EV3BRICK:
            return EV3Brick()
        elif self.hub_type == RoboHub.SPIKEHUB:
            return PrimeHub()
        else:
            raise ValueError("Tipo de hub não suportado.")


    def definirPorta(self, port: str):
        """ Faz tratativa para a porta do lego """
        porta = None
        if port.upper() == "A":
            porta = Port.A
        elif port.upper() == "B":
            porta = Port.B
        elif port.upper() == "C":
            porta = Port.C
        elif port.upper() == "D":
            porta = Port.D
        elif port.upper() == "1":
            porta = Port.S1
        elif port.upper() == "2":
            porta = Port.S2
        elif port.upper() == "3":
            porta = Port.S3
        elif port.upper() == "4":
            porta = Port.S4
        if porta is None:
            raise TypeError("Porta não encontrada")
        return porta
