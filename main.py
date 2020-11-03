import cv2

class Node:
    def __init__(self, data):
        self.data = data
        self.prox = None

class LinkedList:

    def __init__(self):
        self.head = None
        self.tail = None


    def atEnd(self, newData):
        newNode = Node(newData)

        if (self.head):
            self.tail.prox = newNode
            self.tail = newNode
            self.tail.prox = self.head
        else:
            newNode.prox = newNode
            self.tail = newNode
            self.head = newNode



    def mostraImagem(self):
        aux = self.head
        while True:
            img = cv2.imread(aux.data, cv2.IMREAD_UNCHANGED)
            cv2.imshow("foto", img)
            cv2.waitKey(40)
            aux = aux.prox

gif = LinkedList()

gif.atEnd("imagens/1.jpg")
gif.atEnd("imagens/2.jpg")
gif.atEnd("imagens/3.jpg")
gif.atEnd("imagens/4.jpg")

gif.mostraImagem()