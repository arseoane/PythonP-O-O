from calculadorabinaria import *

calc = CalculadoraBinaria(10, 5)
print(calc.operacion('+'))
print(calc.operacion('/'))

errorcalc = CalculadoraBinaria(10, 0)

print(errorcalc.operacion('-'))
print(errorcalc.operacion('*'))
print(errorcalc.operacion('/'))
print(errorcalc.operacion('@'))