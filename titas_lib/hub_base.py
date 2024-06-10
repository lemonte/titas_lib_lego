# hub_base.py
from titas_lib.hub_robo import RoboHub
from titas_lib.robo_imports import RoboImports

class HubType:
    __instance = None
    __imports = None


    def __init__(self, hub=RoboHub.EV3BRICK):
        if HubType.__instance is None:
            print("#### RoboImports ####")
            self.__imports = RoboImports(hub_type=hub)
            HubType.__instance = self


    def getImports(self):
        if self.__imports is None:
          self.__imports = RoboImports(hub_type=RoboHub.EV3BRICK)
        return self.__imports
