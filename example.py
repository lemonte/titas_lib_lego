#!/usr/bin/env pybricks-micropython

# script.py
from titas_lib import HubType, RoboHub,SeguidorLinha, RoboBrick, RoboMotor, RoboCor, RoboUltrassonico, RoboBase

HubType(RoboHub.EV3BRICK)


motor = RoboMotor(Port="d")
motor_dir = RoboMotor(Port="a")

cor_esq = RoboCor(Port="3")
cor_dir = RoboCor(Port="4")

codigoSeguidor = SeguidorLinha()

base = RoboBase(
  motorDireito=motor_dir,
  motorEsquerdo=motor,
  diametroRoda = 10,
  distanciaEntreAsRodas=20
)


# Funcao para mover para frente ate que outro comando mande parar
base.moverSemParar(velocidade=100, angulo_curvatura=0)

codigoSeguidor.seguirLinhaPreta(
  kd=1,
  kp=2,
  cor_vermelha_direta=cor_dir.pegarCor(),
  cor_vermelha_esquerda=cor_esq.pegarCor(),
  motor_direito=motor_dir,
  motor_esquerdo=motor,
  potencia_motores=100
)