import argparse


def amongsay(text):
    def cut_string(string: str):
        among_width = 32
        if len(string) < among_width:
            centering_len = (among_width - len(string)) / 2
            if int(centering_len) <= centering_len - 0.5:
                centering_len = (int(centering_len) + 1)
            else:
                centering_len = int(centering_len)
            speech_bubble = f"|{' ' * int(centering_len)}{string}{' ' * int(centering_len)}|\n"
            longest_len = len(string)
        else:
            split_string = []
            while len(string) > among_width:
                if " " in string:
                    cut_index = string[:among_width].rfind(" ") + 1
                elif "\n" in string:
                    cut_index = string[:among_width].rfind("\n")
                else:
                    cut_index = among_width
                split_string.append(string[:cut_index])
                string = string[cut_index:]
            split_string.append(string)

            longest_len = 0
            for i in range(len(split_string)):
                if len(split_string[i]) > len(split_string[i-1]):
                    longest_len = len(split_string[i])

            speech_bubble = ""
            prev_len = 37
            for line in split_string:
                centering_len = longest_len/2 - len(line)/2
                if type(centering_len) == float:
                    centering_len = int(centering_len) + 1
                new_line = f"|{' ' * int(centering_len)}{line}{' ' * int(centering_len)}|\n"
                if len(new_line) < prev_len:
                    new_line = f"|{' ' * int(centering_len)}{line}{' ' * (int(centering_len) + 1)}|\n"
                speech_bubble += new_line
                prev_len = len(new_line)

            longest_len += 2
        if longest_len > among_width:
            speech_bubble += f"\{'_' * (longest_len)}/"
        else:
            speech_bubble += f"\{'_' * (among_width)}/"

        return speech_bubble

    crewmate = ["          __.-------..._",
               "        /                \ ",
               "       /      ____________\_",
               "  ____/     /               \ ",
               "/    |     /                 \ ",
               "|    |     |                 | ",
               "|    |      \               / ",
               "|    |        \____________/ ",
               "|    |                    | ",
               "\____|                    | ",
               "     |          |         | ",
               "     |          |         | ",
               "     |          |         | ",
               "     \_________/ \________/ "]

    bubble = cut_string(text)
    print(bubble)
    for line in crewmate:
        print(line)


def main():
    if __name__ == "__main__":
        parser = argparse.ArgumentParser(
            prog="amongsay",
            description="Prints a crewmate from Among Us echoing given text")
        parser.add_argument('-s', '--string', type=str, help="Provide some text that the crewmate will say")
        args, unknown_args = parser.parse_known_args()
        text = ""
        if args.string:
            text = args.string
        if unknown_args:
            if args.string:
                text += " "
            text += " ".join(unknown_args)
        amongsay(text)

main()
