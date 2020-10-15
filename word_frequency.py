from string import punctuation


STOP_WORDS = [
    'a', 'an', 'and', 'are', 'as', 'at', 'be', 'by', 'for', 'from', 'has',
    'he', 'i', 'in', 'is', 'it', 'its', 'of', 'on', 'that', 'the', 'to',
    'were', 'will', 'with'
]


def ispunct(s):
    if s == "":
        return False

    for c in s:
        if c in punctuation:
            return False

    return True


class FileReader:
    def __init__(self, filename):
        self.filename = filename


    def read_contents(self):
        with open(self.filename) as wordsfile:
            return wordsfile.read()


class WordList:
    def __init__(self, text):
        self.text = text
        self.word_count = {}


    def extract_words(self):
        self.words_list = self.text.lower()

        for p in punctuation:
            self.words_list = self.words_list.replace(p, '')

        self.words_list = self.words_list.split()


    def remove_stop_words(self):
        for s_w in STOP_WORDS:
            while s_w in self.words_list:
                self.words_list.remove(s_w)


    def get_freqs(self):
        for w in self.words_list:
            if w in self.word_count:
                self.word_count[w] += 1

            else:
                self.word_count[w] = 1

        return self.word_count


class FreqPrinter:
    def __init__(self, freqs):
        self.freqs = freqs


    def print_freqs(self):
        width = max(len(w) for w in self.freqs)
        word_string = ""

        for w in sorted(self.freqs, key=self.freqs.get, reverse=True):
            n = self.freqs[w]
            word_string += f"{w:>{width}} | {n} {'*' * n}\n"

        print(word_string)


if __name__ == "__main__":
    import argparse
    import sys
    from pathlib import Path

    parser = argparse.ArgumentParser(
        description='Get the word frequency in a text file.')
    parser.add_argument('file', help='file to read')
    args = parser.parse_args()

    file = Path(args.file)
    if file.is_file():
        reader = FileReader(file)
        word_list = WordList(reader.read_contents())
        word_list.extract_words()
        word_list.remove_stop_words()
        printer = FreqPrinter(word_list.get_freqs())
        printer.print_freqs()
    else:
        print(f"{file} does not exist!")
        sys.exit(1)
