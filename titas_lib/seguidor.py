
from titas_lib.robo_motor import RoboMotor

class SeguidorLinha:
    """" INICIA A CLASSE SEGUIDOR DE LINHA ex: SeguidorLinha() 
    (kp) é a constante proporcional.
    (Kd) é a constante derivativa
    """

    __kp = 10
    __kd = 10
    __erro = 0
    __erroAnterior = 0        
    __potencia_maxima = 90

    def __calcularErro(self, leitura_sensor_esquerdo, leitura_sensor_direito):
        return (leitura_sensor_esquerdo - leitura_sensor_direito)

    def __calcularPotencia(self, kp, kd, erro, erroAnterior):
        return ((erro * kp) + kd * (erro - erroAnterior))

    def ___excedenteMotores(self, potenciaCalculada):
        if(abs(potenciaCalculada) < self.__potencia_maxima):
            return 0
        if(potenciaCalculada < 0):
            return (self.__potencia_maxima - potenciaCalculada)
        return (potenciaCalculada - self.__potencia_maxima)

    def seguirLinhaPreta(self, cor_vermelha_esquerda: int, cor_vermelha_direta: int,  motor_direito: RoboMotor, motor_esquerdo: RoboMotor,  kp: float = 1, kd: float = 1, potencia_motores: int = 70):
        self.__kp = kp
        self.__kd = kd
        self.__potencia_maxima = potencia_motores
        if(motor_direito == None or motor_esquerdo == None):
            print("#### Verifique se os motores foram passados corretamente #####")
        else:
          if(cor_vermelha_esquerda == None or cor_vermelha_direta == None):
              print("#### Verifique se os rgb(s) de cor foram passados corretamente #####")
          else:
              leitura_sensor_esquerdo = cor_vermelha_esquerda
              leitura_sensor_direito = cor_vermelha_direta
              self.__aux = self.__erro
              self.__erro = self.__calcularErro(
                  leitura_sensor_esquerdo, leitura_sensor_direito)
              self.__erroAnterior = self.__aux

            #   erro = abs(self.__erro)
            #   if(erro > 2):
            #       self.__potencia_maxima = potencia_motores - erro

              # calcula a potencia
              potencia = self.__calcularPotencia(
                  self.__kp, self.__kd, self.__erro, self.__erroAnterior)
              
              potencia_esquerdo = potencia_motores + potencia
              potencia_direito = potencia_motores - potencia

            #   print("potencia ", potencia)


              diferenca_d = self.___excedenteMotores(potencia_direito)
              diferenca_e = self.___excedenteMotores(potencia_esquerdo)


            #   print("excedente esquerda ", diferenca_e)
            #   print("excedente direita ", diferenca_d)


              potencia_direito = potencia_direito - diferenca_e
              potencia_esquerdo = potencia_esquerdo  - diferenca_d


              potencia_esquerdo = max(-self.__potencia_maxima, min(potencia_esquerdo, self.__potencia_maxima))
              potencia_direito = max(-self.__potencia_maxima, min(potencia_direito, self.__potencia_maxima))
            #   print("potencia esquerda ", potencia_esquerdo)
            #   print("potencia direita ", potencia_direito)

              # mover motores
              motor_direito.moverPorPotencia(potencia_direito)
              motor_esquerdo.moverPorPotencia(potencia_esquerdo)