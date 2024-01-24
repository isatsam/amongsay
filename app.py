def amongsays(text):
    def spread_text(one_line):
        if len(one_line) > 35:
            next_line = one_line
            by_lines = []
            while len(next_line) > 35:
                if " " in next_line:
                    cut = next_line[35:].rfind(" ")-1
                else:
                    cut = 35
                by_lines.append(next_line[:cut])
                next_line = next_line[cut:]
            by_lines.append(next_line)
        else:
            by_lines = [one_line]

        centering = ' ' * (int(len(by_lines[0])/2))
        len_of_words = len(centering)*2 + len(by_lines[0])

        speech_bubble = ""
        for line in by_lines:
            speech_bubble += f"|{centering}{line}{centering}|\n"

        speech_bubble += f"\{'_' * len_of_words}/"
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

    bubble = spread_text(text)
    print(bubble)
    for line in crewmate:
        print(line)


def main():
    if __name__ == '__main__':
        user_input = input()
        amongsays(user_input)


main()
