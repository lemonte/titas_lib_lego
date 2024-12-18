# hub_base.py
from titas_lib.hub_robo import RoboHub
from titas_lib.robo_imports import RoboImports

class HubType(RoboImports):
    __instance = None  

    def __new__(cls, hub=RoboHub.EV3BRICK):  
        if cls.__instance is None:
            print("#### Inicializando HubType ####")
            cls.__instance = super(HubType, cls).__new__(cls)
        return cls.__instance

    def __init__(self, hub=RoboHub.EV3BRICK):
        if not hasattr(self, "_initialized"): 
            super().__init__(hub_type=hub)  
            self._initialized = True 