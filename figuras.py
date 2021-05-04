print(__name__)

def triangulo(b, h):
    return b * h / 2

def cuadrado(l):
    return l*l

if __name__ == '__main__':
    b = input('base')
    h = input('altura')

    print(triangulo(int(b), int(h)))

