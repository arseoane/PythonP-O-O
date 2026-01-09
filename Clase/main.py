from calculadorabinaria import *

calc = CalculadoraBinaria(10, 5)
print(calc.operacion('+'))
print(calc.operacion('/'))

errorcalc = CalculadoraBinaria(10, 0)

print(errorcalc.operacion('-'))
print(errorcalc.operacion('*'))
print(errorcalc.operacion('/'))
print(errorcalc.operacion('@'))

print(calc.operacion('+'))
print(calc.get_a())

calc.set_b(999)
print(calc.operacion('/'))

try:
    result = 10 / 0
except ZeroDivisionError:
    print("Non se pode dividir por 0.")
except Exception:
    print("Erro xeral")