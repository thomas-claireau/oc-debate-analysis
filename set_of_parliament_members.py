import os
import analysis.csv_file as c_an
import pandas as pd
import pdb
import numpy as np
import matplotlib.pyplot as plt


class SetOfParliamentMembers:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return "Nombre total de membres : {}".format(len(self.dataframe))

    def data_from_csv(self, csv_file):
        directory = os.path.dirname(__file__)
        self.dataframe = pd.read_csv(
            os.path.join(directory, "data", csv_file), ";")

    def data_from_dataframe(self, dataframe):
        self.dataframe = dataframe

    def display_chart(self):
        data = self.dataframe
        female_mps = data[data.sexe == "F"]
        male_mps = data[data.sexe == "H"]

        count = [len(female_mps), len(male_mps)]
        count = np.array(count)
        np_mps = count.sum()
        proportion = count / np_mps

        labels = ["Female ({})".format(count[0]), "Male ({})".format(count[1])]

        fix, ax = plt.subplots()
        ax.axis("equal")
        ax.pie(
            proportion,
            labels=labels,
            autopct="%1.1f pourcents"
        )

        plt.show()

    def split_by_political_party(self):
        result = {}
        data = self.dataframe

        all_parties = data["parti_ratt_financier"].dropna().unique()

        for party in all_parties:
            data_subset = data[data.parti_ratt_financier == party]
            subset = SetOfParliamentMembers('Mps of {}'.format(party))
            subset.data_from_dataframe(data_subset)
            result[party] = subset

        return result


def launch_analysis(data_file, by_party=False):
    sopm = SetOfParliamentMembers('All mps')
    sopm.data_from_csv(data_file)

    breakpoint()

    # sopm.display_chart()

    # if by_party:
    #     for party, s in sopm.split_by_political_party().items():
    #         s.display_chart()


def main():
    launch_analysis("current_mps.csv")


if __name__ == "__main__":
    main()
