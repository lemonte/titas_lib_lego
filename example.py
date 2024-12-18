#!/usr/bin/env pybricks-micropython

from titas_lib import *

hub = HubType(RoboHub.EV3BRICK)

motor = RoboMotor(port="d")
motor_dir = RoboMotor(port="a")

cor_esq = RoboCor(port="3")
cor_dir = RoboCor(port="4")



# while True:
#   PIDController().seguirLinha(
#     kd=1,
#     kp=2,
#     cor_vermelha_direita=cor_dir.pegarReflexao(),
#     cor_vermelha_esquerda=cor_esq.pegarReflexao(),
#     motor_direito=motor_dir,
#     motor_esquerdo=motor,
#     potencia_motores=100
#   )