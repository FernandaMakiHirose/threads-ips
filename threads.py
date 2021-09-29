from threading import Thread
from time import sleep

def carro(velocidade, piloto):
    trajeto = 0
    while trajeto <= 100:
        print(f'O piloto {piloto} já percorreu {velocidade}Km')
        trajeto += velocidade
        sleep(0.5)


carro_1 = Thread(target=carro, args=[1, 'Maki']) 
carro_2 = Thread(target=carro, args=[2, 'Fernanda']) 

carro_1.start()
carro_2.start()

