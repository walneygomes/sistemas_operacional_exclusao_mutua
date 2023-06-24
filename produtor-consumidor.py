import threading
class buffer:
    look=0
    buffer=0
    def setInsertBuffer(self, valor):
        self.buffer=valor
        print(f"inserir o valor "+str(valor))

    def setDeletarBuffer(self):
        print("consumindo o valor "+str(self.buffer))
        self.buffer=0
    def verificarBuffer(self):
        return self.look

class consumidor(threading.Thread):
    recurso_partilhado=buffer()
    def __init__(self,buffer):
        threading.Thread.__init__(self)
        self.recurso_partilhado=buffer

    def getBuffer(self):
        global recurso_partilhado
        recurso_partilhado.setDeletarBuffer()

