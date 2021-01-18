import os
import logging as lg

lg.basicConfig(level=lg.DEBUG)


def launch_analysis(data_file):
    directory = os.path.dirname(os.path.dirname(__file__))
    file = os.path.join(directory, "data", data_file)

    breakpoint()

    try:
        with open(file, 'r') as file:
            preview = file.readline()
            lg.debug('{}'.format(preview))
    except FileNotFoundError as e:
        lg.critical("Une erreur critique est survenue : {}".format(e))


def main():
    launch_analysis("current_mps.csv")


if __name__ == "__main__":
    main()
