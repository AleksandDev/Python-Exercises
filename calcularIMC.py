def calcularIMC():
  peso = float(input("Digite seu peso: "))
  altura = float(input("Digite sua altura: "))
  IMC = peso / (altura * altura)
  return IMC
  print(calcularIMC())

def determinar_categoria():
  peso = float(input("Digite seu peso: "))
  altura = float(input("Digite sua altura: "))
  IMC = peso / (altura * altura)
  if IMC < 18:
      print("Abaixo do peso")
  elif IMC >= 18 and IMC < 25:
      print("Peso normal")
  elif IMC >= 25 and IMC < 30:
      print("Sobrepeso")
  elif IMC >= 30:
      print("Obesidade")
