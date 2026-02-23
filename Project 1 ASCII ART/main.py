import sys


def load_banner(filename):
    try:
        with open(filename, 'r') as f:
            lines = f.read().splitlines()
        banner_dict = {}
        current_ascii = 32
        for i in range(0, len(lines), 9):
            char_lines = lines[i + 1: i + 9]
            if char_lines:
                banner_dict[current_ascii] = char_lines
                current_ascii += 1
        return banner_dict
    except FileNotFoundError:
        return None


def main():
    if len(sys.argv) < 2:
        return

    input_text = sys.argv[1].replace('\\n', '\n')
    parts = input_text.split('\n')

    banner = load_banner("standard.txt")
    if not banner:
        print("Error: banner file not found")
        return

    for part in parts:
        if part == "":
            print()
            continue

        for i in range(8):
            output_line = ""
            for char in part:
                ascii_code = ord(char)
                if ascii_code in banner:
                    output_line += banner[ascii_code][i]
            print(output_line)


if __name__ == "__main__":
    main()