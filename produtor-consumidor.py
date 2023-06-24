# -*- coding: ISO-8859-1 -*-
import _thread
import time, random
import threading

#classe buffer limitado
class BufferLimitado:
    #tamanho do buffer
    #quantidade de recursos do buffer
    TAM_BUFFER = 1
    #mutex do buffer
    mutex = threading.Semaphore(1)
    empty = threading.Semaphore(TAM_BUFFER)
    full = threading.Semaphore(0)
    #regioes criticas dos consumidores
    # pegamos 3 elementos para ser consumidos pelo consumidor
    buffer = [-1, -1, -1]
    #metodo retornavel, que verifica a situação do buffer
    def verificarSituacaoBuffer(self):
        count = 0
        quantidade = 0
        while (count < 3):
            if (self.buffer[count] == -1):
                quantidade = quantidade + 1

            count = count + 1
        return quantidade

    #Metodo que faz a remoção do elementos da posição randomica
    #retorna uma mensagem
    def removerBuffer(self):
        mensagem = " "
        while(self.verificarSituacaoBuffer()!=3):
            #metodo randomico
            posi=random.randint(0,2)

            if(self.buffer[posi]!=-1):
                x=self.buffer[posi]
                self.buffer[posi]=-1

                mensagem = mensagem + " Consumidor consumiu " + str(x) + " na posicao " + str(posi) + "\n"
        return mensagem


    #metodo que insere no buffer do array
    def inserirBuffer(self,item):
        mensagem = " "
        count = 0
        while(count<3):
            if(self.buffer[count]==-1):
                self.buffer[count] = item
                mensagem = mensagem + " Produtor produziu " +  str(item) + " na posicao " + str(count) + "\n"
            count = count+1
        return mensagem

    def insert(self, item):
        self.empty.acquire()
        self.mutex.acquire()
        print("   ")
        print(self.inserirBuffer(item))
        print("   ")

        self.mutex.release()
        self.full.release()

    def remove(self):
        self.full.acquire()
        self.mutex.acquire()
        item = self.removerBuffer()
        self.mutex.release()
        self.empty.release()
        return item


b = BufferLimitado()


def produtor():
    for i in range(0, 10):
        # time.sleep(random.randint(1, 10) / 100.0)
        print("   ")
        b.insert(i)
        print("   ")


def consumidor():
    for i in range(0, 10):
        # time.sleep(random.randint(1, 10) / 100.0)
        item = b.remove()

        print(item)


_thread.start_new_thread(produtor, ())
_thread.start_new_thread(consumidor, ())

while 1: pass
