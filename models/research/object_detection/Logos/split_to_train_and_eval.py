import random

with open("data\\logo_labels.csv") as fr:
    with open("data\\train.csv", "w") as f1, open("data\\eval.csv", "w") as f2:
        for line in fr.readlines():
            rd = random.randint(1, 100)
            f = f1 if rd < 76 else f2
            f.write(line)