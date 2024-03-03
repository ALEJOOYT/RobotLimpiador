import random

class Robot:
    def __init__(self, numeroCuadrantes):
        self.numeroCuadrantes = numeroCuadrantes
        self.cuadranteActual = random.randint(1, numeroCuadrantes)
        self.cuadrantesLimpios = set()

    def moverAlSiguienteCuadrante(self):
        siguienteCuadrante = random.randint(1, self.numeroCuadrantes)
        print(f"Moviendo desde el cuadrante {self.cuadranteActual} al cuadrante {siguienteCuadrante}")
        self.cuadranteActual = siguienteCuadrante

    def limpiarCuadranteActual(self):
        print(f"Limpiando el cuadrante {self.cuadranteActual}")
        self.cuadrantesLimpios.add(self.cuadranteActual)

    def estaCuadranteLimpio(self):
        return self.cuadranteActual in self.cuadrantesLimpios

def dibujarRobotEnCuadrante(cuadranteActual, numeroCuadrantes, cuadrantesLimpios):
    for i in range(1, numeroCuadrantes + 1):
        if i == cuadranteActual:
            print("🤖", end=" ")
        elif i in cuadrantesLimpios:
            print("✨", end=" ")
        else:
            print("💩", end=" ")
    print()

def main():
    numeroCuadrantes = int(input("Ingrese el número de cuadrantes: "))
    robot = Robot(numeroCuadrantes)

    while len(robot.cuadrantesLimpios) < numeroCuadrantes:
        dibujarRobotEnCuadrante(robot.cuadranteActual, numeroCuadrantes, robot.cuadrantesLimpios)
        if robot.estaCuadranteLimpio():
            robot.moverAlSiguienteCuadrante()
        else:
            robot.limpiarCuadranteActual()

    print("Todos los cuadrantes están limpios.")
    dibujarRobotEnCuadrante(robot.cuadranteActual, numeroCuadrantes, robot.cuadrantesLimpios)

if __name__ == "__main__":
    main()
