import math

class Triangulo():
  v1 = list()
  v2 = list()
  med = list()
  baris = list()
  def __init__(self, x1, x2, x3, y1, y2, y3):
    self.x1 = x1
    self.x2= x2
    self.x3 = x3
    self.y1 = y1
    self.y2 = y2
    self.y3 = y3

    self.v1.append(self.x1)
    self.v1.append(self.x2)
    self.v1.append(self.x3)
    self.v2.append(self.y1)
    self.v2.append(self.y2)
    self.v2.append(self.y3)

  def arestas(self):
    self.dab = math.sqrt( ( (t.v1[1] - t.v1[0]) **2) + ( (t.v2[1] - t.v2[0])**2) ) 
    self.dac = math.sqrt( ( (t.v1[2] - t.v1[0]) **2) + ( (t.v2[2] - t.v2[0])**2) )
    self.dbc = math.sqrt( ( (t.v1[2] - t.v1[1]) **2) + ( (t.v2[2] - t.v2[1])**2) )
    print(f'arestas: {self.dab}, {self.dac}, {self.dbc}')

  def perimetro(self):
    self.p = self.dab + self.dac + self.dbc
    print(f'o perímetro é {self.p}')

  def area(self):
    self.semip = self.p/2
    self.a = math.sqrt(self.semip * (self.semip - self.dab) * (self.semip - self.dac) * (self.semip - self.dbc))
    print(f'a área é {self.a}')

  def perguntas(self):
    if (self.dab == self.dac) and (self.dac == self.dbc):
      print('é equilátero')

    elif (self.dab == self.dac and self.dab > self.dbc)  or (self.dac == self.dbc and self.dac > self.dab) or (self.dbc == self.dab and self.dbc > self.dac):
      print('é isóceles')
    else:
      print('o triângulo não é equilátero e nem isóceles')

    if (self.dab > self.dac and self.dab > self.dbc):
      soma = self.dac + self.dbc 
      if soma == self.dab:
        v = True
        print('é degenerado')
      else:
        print('ele não é degenerado')

    elif (self.dac > self.dab and self.dac > self.dbc):
      soma = self.dab + self.dbc 
      if soma == self.dac:
        v = True
        print('é degenerado')
      else:
        print('ele não é degenerado')

    elif (self.dbc > self.dab and self.dbc > self.dac):
      soma = self.dab + self.dac 
      if soma == self.dbc:
        v = True
        print('é degenerado')
      else:
        print('ele não é degenerado')

    else:
      print('ele não é degenerado')

    if(self.dab > self.dac and self.dab > self.dbc):
      try:
        v = False
        if v == False:
          pitagoras = (self.dab ** 2) == (self.dac ** 2) + (self.dbc ** 2)
          print('é retângulo')
        else:
          print('ele não é retângulo')
      except:
        print('ele não retângulo')
    
    elif (self.dac > self.dab and self.dac > self.dbc):
      try:
        v = False
        if v == False:
          pitagoras = (self.dac ** 2) == (self.dab ** 2) + (self.dbc ** 2)
          print('é retângulo')
        else:
          print('ele não é retângulo')
      except:
        print('ele não retângulo')
    
    elif (self.dbc > self.dac and self.dbc > self.dab):
      try:
        v = False
        if v == False:
          pitagoras = (self.dbc ** 2) == (self.dac ** 2) + (self.dab ** 2)
          print('é retângulo')
        else:
          print('ele não é retângulo')
      except:
        print('ele não retângulo')

    else:
      print('o triângulo não é retângulo')


  def mediana(self):
    self.mx = (t.v1[0] + t.v1[1])/2
    self.my = (t.v2[0] + t.v2[1])/2

    self.med.append(self.mx)
    self.med.append(self.my)

  def baricentro(self):
    self.barix = (t.v1[0] + t.v1[1] + t.v1[2])/3
    self.bariy = (t.v2[0] + t.v2[1] + t.v2[2])/3
    
    self.baris.append(self.barix)
    self.baris.append(self.bariy)

x1, y1 = input("Digite os números do vertice 1: ").split(",")
x2, y2 = input("Digite os números do vertice 2: ").split(",")
x3, y3 = input("Digite os números do vertice 3: ").split(",")

t = Triangulo(float(x1), float(x2), float(x3), float(y1), float(y2), float(y3))

t.mediana()

t.baricentro()

t.arestas()
print('\n')
t.perguntas()
print('\n')
t.perimetro()
print('\n')
t.area()
print('\n')