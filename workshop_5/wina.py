def game():
    pass

def trim(line: str) -> str:
    return ''.join([char.upper() for char in line if char != ' '])

def trim2(line: str) -> str:
    return line.replace(' ', '')

def trim3(line: str) -> str:
    a = []

    for substr in line.split():
        a.append(substr.strip())
    
    return ''.join(a)

if __name__ == '__main__':
    # import main
    # print(__name__)
    # print(main.__name__)

    print(trim3('h e l           lo'))