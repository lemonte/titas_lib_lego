#!/usr/bin/env pybricks-micropython

from pybricks.pupdevices import Motor, ColorSensor
from pybricks.parameters import Port

# Inicializa os motores e sensores de cor
motor_esquerdo = Motor(Port.A)
motor_direito = Motor(Port.B)
sensor_cor_esquerdo = ColorSensor(Port.C)
sensor_cor_direito = ColorSensor(Port.D)


erroAnterior = 0    

def calcularErro(leitura_sensor_esquerdo, leitura_sensor_direito):
    return leitura_sensor_esquerdo - leitura_sensor_direito

def calcularPotencia( kp, kd, erro, erroAnterior):
    return (erro * kp) + kd * (erro - erroAnterior)

def excedenteMotores(potenciaCalculada, potencia_maxima):
    if abs(potenciaCalculada) < potencia_maxima:
        return 0
    if potenciaCalculada < 0:
        return potencia_maxima - abs(potenciaCalculada)
    return potenciaCalculada - potencia_maxima


def calculoPID(
    valor_referencia_1: int, 
    valor_referencia_2: int, 
    kp: float = 1, 
    kd: float = 1, 
    valor_maximo_permitido: int = 70
):

    if valor_referencia_1 is None or valor_referencia_2 is None:
        raise TypeError("#### Verifique se os valores RGB foram passados corretamente #####")

    # Calcula o erro
    erro = calcularErro(valor_referencia_1, valor_referencia_2)
    potencia = calcularPotencia(kp, kd, erro, __erroAnterior)
    __erroAnterior = erro

    # Calcula potência para cada motor
    potencia_esquerdo = valor_maximo_permitido + potencia
    potencia_direito = valor_maximo_permitido - potencia

    diferenca_d = excedenteMotores(potencia_direito, valor_maximo_permitido)
    diferenca_e = excedenteMotores(potencia_esquerdo, valor_maximo_permitido)

    potencia_direito -= diferenca_e
    potencia_esquerdo -= diferenca_d

    potencia_esquerdo = max(-valor_maximo_permitido, min(potencia_esquerdo, valor_maximo_permitido))
    potencia_direito = max(-valor_maximo_permitido, min(potencia_direito, valor_maximo_permitido))

    # Mover motores
    return [potencia_esquerdo, potencia_direito]



def seguirLinha(
    cor_vermelha_esquerda: int, 
    cor_vermelha_direita: int, 
    motor_direito: Motor, 
    motor_esquerdo: Motor, 
    kp: float = 1, 
    kd: float = 1, 
    potencia_motores: int = 70
):

    if motor_direito is None or motor_esquerdo is None:
        print("#### Verifique se os motores foram passados corretamente #####")
        raise TypeError("#### Verifique se os motores foram passados corretamente #####")

    potencia_esquerdo, potencia_direito = calculoPID(
        cor_vermelha_esquerda,
        cor_vermelha_direita,
        kp,
        kd,
        potencia_motores,
    )
    motor_direito.dc(potencia_direito)
    motor_esquerdo.dc(potencia_esquerdo)



while True:
  seguirLinha(
      sensor_cor_esquerdo.reflection(),
      sensor_cor_direito.reflection(),
      motor_direito,
      motor_esquerdo,
      kp=1,
      kd=1,
      potencia_motores=70
  )