# Modules
from random import randint

# Exception
class EwJavascript(Exception):
    def __init__(self) -> None:
        super().__init__('Ew Javascript')

# Loop
while 1:
    # Input
    if 'javascript' not in input().lower():
        print(f'Fuck Javascript{"!" * randint(1, 10)}')
    else:
        raise EwJavascript # Ew Javascript
