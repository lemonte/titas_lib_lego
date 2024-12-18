from titas_lib.hub_base import HubType, RoboHub

class RoboBrick:
   """ Traz funções do brick """
   __hubBase = None
    
   def __init__(self) -> None:
      self.__hubBase = HubType.brick

  
   def beep(self,
   frequencia: int = 500,
   duracao: int = 100):
      """ Emite som """
      self.definirVolume(100)
      self.__hubBase.speaker.beep(frequency=frequencia, duration=duracao)


   def definirVolume(self, volume: int = 100):
      """ Define volume do alto falante """
      if(HubType.hub_type == RoboHub.EV3BRICK):
         self.__hubBase.speaker.set_volume(volume)
      if(HubType.hub_type == RoboHub.SPIKEHUB):
         self.__hubBase.speaker.volume(volume)

   def beepErro(self):
      """ Sinaliza erro """
      self.definirVolume(100)
      self.beep(frequencia=100, duracao=500)

   def falar(self, texto: str):
      """ Fala o texto """
      self.definirVolume(100)
      if(HubType.hub_type == RoboHub.EV3BRICK):
         self.__hubBase.speaker.set_speech_options(language='pt-br', voice='m3', speed=120)
         self.__hubBase.speaker.say(text=texto)