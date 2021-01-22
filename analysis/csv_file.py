import os
import logging as lg
import pandas as pd


lg.basicConfig(level=lg.DEBUG)


def launch_analysis(data_file):
    directory = os.path.dirname(os.path.dirname(__file__))
    file = os.path.join(directory, "data", data_file)

    try:
        lg.debug('{}'.format(pd.read_csv(file, sep=";")))
    except FileNotFoundError as e:
        lg.critical("Une erreur critique est survenue : {}".format(e))


def main():
    launch_analysis("current_mps.csv")


if __name__ == "__main__":
    main()
