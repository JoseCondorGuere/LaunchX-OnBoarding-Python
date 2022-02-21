def main():
    try:
        configuration = open("C:\\Users\Indra\Downloads\CursoIntroPython-main\CursoIntroPython-main\Módulo 10 - Manejo de errores\config.txt")
    except FileNotFoundError:
        print("Couldn't find the config.txt file!")

if __name__ == '__main__':
    main()