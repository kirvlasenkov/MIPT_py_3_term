import zipfile
import re
import os
import pickle


class TextLoader:
    """
    All unzipped archives
    located in ./extracted_files
    """

    def __init__(self, path: str):
        if os.path.exists(path):
            os.path.normcase(path)
            self.__folder_name = os.path.split(path)[1].rsplit(".", 1)[0]

            zip_file = zipfile.ZipFile(path)
            zip_file.extractall("./extracted_files")
            zip_file.close()

            self.__files_path = os.path.join("./extracted_files", self.__folder_name)
            self.__files = [file for file in os.listdir(self.__files_path)
                            if os.path.isfile(os.path.join(self.__files_path, file))]
            self.__iterable_files = iter(self.__files)

        else:
            raise IOError("non-existent path")

    def __len__(self) -> int:
        return len(self.__files)

    @staticmethod
    def normalize(txt: str) -> str:
        return re.sub(r"[.,!?;:-]", " ", txt).lower()

    def __iter__(self):
        return self

    def __next__(self):
        file = next(self.__iterable_files)
        current_path = os.path.join(self.__files_path, file)

        with open(current_path, "r") as f:
            text = TextLoader.normalize(f.read())

        with open(current_path, "w") as f:
            f.write(text)

        return open(current_path, "r")

    def __getstate__(self):
        state = self.__dict__.copy()
        return state

    def __setstate__(self, state):
        self.__dict__ = state
        self.__files = [file for file in os.listdir(self.__files_path)
                        if os.path.isfile(os.path.join(self.__files_path, file))]


'''
if __name__ == "__main__":
    text = TextLoader("/Users/vlasenckov/MIPT/git_project/MIPT_py_3_term/w13/sample.zip")

    dumped_text = pickle.dumps(text)
    loaded_text = pickle.loads(dumped_text)

    for file in loaded_text:
        print(file.read())
'''
