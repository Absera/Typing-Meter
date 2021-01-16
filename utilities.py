import random


def randomize(from_, to):
    # from is list of words
    # to is file to be written on
    # sample: from = ["hello", "what"]
    #         to = open("random_words", "w")
    for _ in range(len(from_)):
        to.write(random.choice(from_))


def strip_list(list):
    string = ""
    for i in list:
        string += i.strip() + " "
    return string


def split_float(floating):
    return int(str(floating).split(".")[0])
