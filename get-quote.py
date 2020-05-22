import random


def primary():
    # print("Keep it logically awesome.")

    # the var F will open the quotes.txt file, then thew QUOTES will read all lines of the file, and the CLOSE will close the file
    f = open("quotes.txt")
    quotes = f.readlines()
    f.close()

    last = 13
    rnd = random.randint(0, last)
    # to print a quote from the array
    print(quotes[rnd])


if __name__ == "__main__":
    primary()
