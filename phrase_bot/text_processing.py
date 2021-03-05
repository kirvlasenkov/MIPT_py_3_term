import re
import time
import os


def prepare_phrases(ifile, ofile):
    """
    Transform each phrase to the
    pleasing-to-the-eye form
    (also required by markovify)
    """
    phrase_db = []
    surnames = []
    try:
        phrase = []
        if os.path.exists:
            with open(ifile, 'r', encoding='utf-8') as ifile:
                for _ in range(1000):
                    line = ifile.readline()
                    if not re.search("^#", line):
                        # line = re.sub(r"C?:", " ", line)
                        phrase.append(line.replace("П: ", " ").replace("С", " "))

                    else:
                        if len(re.findall(r'^#\w*\Bmipt', line)) > 0:
                            surname = re.findall(r'^#\w*\Bmipt', line)[0].split("#")[1].split("_")[0]
                            surnames.append(surname)
                        line = re.sub(r'^#\w*\Bmipt', " ", line).replace("С:", " ").replace("П: ", " ")
                        line = re.sub(r"\w.?\w.?#\w*\Bmipt", " ", line)
                        phrase.append(line)
                        phrase_db.append(phrase)
                        phrase = []
        else:
            raise IOError("Wrong path to the file with raw phrases")

    except IOError:
        print("wrong path to the input file!!!")
        return

    with open(ofile, "w") as file:
        for phrase in phrase_db:
            file.writelines(phrase)

    return ofile, surnames


if __name__ == "__main__":
    start = time.time()
    # print(re.search(r"^\w.\w. #\w*\Bmipt", string="A.G. #vlvmv_mipt"))
    # print(re.sub(r"[A]", " ", "cdlmv"))
    prepare_phrases("phrases.txt", "prepared_phrases.txt")
    print(time.time() - start)
