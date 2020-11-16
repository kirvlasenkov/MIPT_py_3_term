import zipfile
import re
import os


class TextLoader:
    """
    All unzipped archives
    located in ./extracted_files
    """

    def __init__(self, path: str):
        if os.path.exists(path):
            os.path.normcase(path)
            self.folder_name = os.path.split(path)[1].rsplit(".", 1)[0]

            zip_file = zipfile.ZipFile(path)
            zip_file.extractall("./extracted_files")
            zip_file.close()

            self.files_path = os.path.join("./extracted_files", self.folder_name)
            self.files = [file for file in os.listdir(self.files_path)
                          if os.path.isfile(os.path.join(self.files_path, file))]
            self.iterable_files = iter(self.files)

        else:
            raise IOError("non-existent path")

    def __len__(self) -> int:
        return len(self.files)

    @staticmethod
    def normalize(txt: str) -> str:
        return re.sub(r"[.,!?;:-]", " ", txt).lower()

    def __iter__(self):
        return self

    def __next__(self):
        file = next(self.iterable_files)
        current_path = os.path.join(self.files_path, file)

        with open(current_path, "r") as f:
            text = TextLoader.normalize(f.read())

        with open(current_path, "w") as f:
            f.write(text)

        return open(current_path, "r")


# if __name__ == "__main__":
# text = TextLoader("/Users/vlasenckov/MIPT/git_project/MIPT_py_3_term/w9/sample.zip")
# for file in text:
#    print(file.read())
