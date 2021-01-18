import os


def launch_analysis(data_file):
    directory = os.path.dirname(os.path.dirname(__file__))
    file = os.path.join(directory, "data", data_file)

    with open(file, 'r') as file:
        preview = file.readline()
        print(preview)


def main():
    launch_analysis("current_mps.csv")


if __name__ == "__main__":
    main()
