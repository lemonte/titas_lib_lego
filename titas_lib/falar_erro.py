from titas_lib.robo_brick import RoboBrick

def falar_erro(funcao):
    def funcao_envolvida(*args, **kwargs):
        try:
            return funcao(*args, **kwargs)
        except Exception as e:
            robo_brick = RoboBrick()
            mensagem_de_erro = str(e)
            print(mensagem_de_erro)
            robo_brick.beepErro()
            robo_brick.falar(mensagem_de_erro)
            raise 

    return funcao_envolvida