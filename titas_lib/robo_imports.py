# robo_imports.py
from titas_lib.hub_base import RoboHub
from pybricks.parameters import *

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
        print("Carregando EV3BRICK")
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

    @staticmethod
    def definirPorta(port: str):
        porta_map = {
            "A": Port.A, "B": Port.B, "C": Port.C, "D": Port.D,
            "1": Port.S1, "2": Port.S2, "3": Port.S3, "4": Port.S4,
        }
        try:
            return porta_map[port.upper()]
        except KeyError:
            raise TypeError("Porta não encontrada")

