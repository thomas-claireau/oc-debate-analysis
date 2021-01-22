import os
import logging as lg

lg.basicConfig(level=lg.DEBUG)


def launch_analysis(data_file):
    directory = os.path.dirname(os.path.dirname(__file__))
    file = os.path.join(directory, "data", data_file)

    try:
        with open(file, 'r') as file:
            preview = file.readline()
            lg.debug(preview)
    except FileNotFoundError as e:
        lg.critical('Une erreur critique est survenue : {}'.format(e))


def main():
    launch_analysis("SyceronBrut.xml")


if __name__ == "__main__":
    main()
