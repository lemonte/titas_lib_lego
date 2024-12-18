from titas_lib.robo_motor import RoboMotor

    # Variáveis de estado do seguidor de linha

class PIDController:

    __erroAnterior = 0    

    def __calcularErro(self, leitura_sensor_esquerdo, leitura_sensor_direito):
        return leitura_sensor_esquerdo - leitura_sensor_direito

    def __calcularPotencia(self, kp, kd, erro, erroAnterior):
        return (erro * kp) + kd * (erro - erroAnterior)

    def __excedenteMotores(self, potenciaCalculada, potencia_maxima):
        if abs(potenciaCalculada) < potencia_maxima:
            return 0
        if potenciaCalculada < 0:
            return potencia_maxima - abs(potenciaCalculada)
        return potenciaCalculada - potencia_maxima


    def calculoPID(
        self,
        valor_referencia_1: int, 
        valor_referencia_2: int, 
        kp: float = 1, 
        kd: float = 1, 
        valor_maximo_permitido: int = 70
    ):

        if valor_referencia_1 is None or valor_referencia_2 is None:
            raise TypeError("#### Verifique se os valores RGB foram passados corretamente #####")

        # Calcula o erro
        erro = self.__calcularErro(valor_referencia_1, valor_referencia_2)
        potencia = self.__calcularPotencia(kp, kd, erro, self.__erroAnterior)
        self.__erroAnterior = erro

        # Calcula potência para cada motor
        potencia_esquerdo = valor_maximo_permitido + potencia
        potencia_direito = valor_maximo_permitido - potencia

        diferenca_d = self.__excedenteMotores(potencia_direito, valor_maximo_permitido)
        diferenca_e = self.__excedenteMotores(potencia_esquerdo, valor_maximo_permitido)

        potencia_direito -= diferenca_e
        potencia_esquerdo -= diferenca_d

        potencia_esquerdo = max(-valor_maximo_permitido, min(potencia_esquerdo, valor_maximo_permitido))
        potencia_direito = max(-valor_maximo_permitido, min(potencia_direito, valor_maximo_permitido))

        # Mover motores
        return [potencia_esquerdo, potencia_direito]



    def seguirLinha(
        self,
        cor_vermelha_esquerda: int, 
        cor_vermelha_direita: int, 
        motor_direito: RoboMotor, 
        motor_esquerdo: RoboMotor, 
        kp: float = 1, 
        kd: float = 1, 
        potencia_motores: int = 70
    ):

        if motor_direito is None or motor_esquerdo is None:
            print("#### Verifique se os motores foram passados corretamente #####")
            raise TypeError("#### Verifique se os motores foram passados corretamente #####")

        potencia_esquerdo, potencia_direito = self.calculoPID(
            cor_vermelha_esquerda,
            cor_vermelha_direita,
            kp,
            kd,
            potencia_motores,
        )
        motor_direito.moverPorPotencia(potencia_direito)
        motor_esquerdo.moverPorPotencia(potencia_esquerdo)
