import traceback
from os import path
from random import sample, randint
import sys
from winsound import PlaySound, SND_NODEFAULT, SND_FILENAME, SND_NOSTOP

arti = ["mano destra", "mano sinistra", "piede destro", "piede sinistro"]
colori = ["verde", "giallo", "blu", "rosso"]
base = path.join(path.abspath(path.dirname(__file__)), "wavs")

def play(name):
    PlaySound(path.join(base, f"{name}.wav"), SND_FILENAME | SND_NODEFAULT | SND_NOSTOP)


def main():
    print(base)
    print("Premi enter per sentire la mia bella voce.")
    for _ in sys.stdin:
        arto, colore, numero = (sample(arti, 1)[0], sample(colori, 1)[0], randint(1, 6))
        print(f"{arto},\t{colore},\t{numero}", end='', flush=True)
        play(arto)
        play(colore)
        play(numero)


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        pass
    except Exception:
        print()
        print("senti, l'ho fatto di fretta")
        traceback.print_exc()
        input()
