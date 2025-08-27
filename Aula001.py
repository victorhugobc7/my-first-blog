verify1 = 6 >= 12 / 2
verify2 = 6 < 20 and 30 > 10

# Condicionais
if verify1 and verify2:
    {print("truth.")}
else:
    print("lies.")

# Funções
valorVolume = 50


def verificarVolume(volumeAVerificar):
    if volumeAVerificar <= 20:
        print("O som está baixo")
    elif volumeAVerificar > 20 and volumeAVerificar <= 40:
        print("Um volumeAVerificar decente.")
    elif volumeAVerificar > 40 and volumeAVerificar <= 60:
        print("VolumeAVerificar perfeito.")
    elif volumeAVerificar > 60 and volumeAVerificar <= 80:
        print("Começando a ficar alto.")
    elif volumeAVerificar > 80 and volumeAVerificar <= 100:
        print("Alto")
    else:
        print("Volume inválido")


verificarVolume(0)

# Laços

girls = ["Rachel", "Monica", "Phoebe", "Ola"]
for element in girls:
    print(element)
    print("--------")

for i in range(1, 10):
    print(i)
