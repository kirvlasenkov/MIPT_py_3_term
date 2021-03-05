import markovify


def produce_phrases(file):
    """
    Function, which implements all the
    magic with Markov's chains. As you
    can see, looks pretty easy:)
    @param file: input file, consisted of text
    to be converted into sensible phrases
    @return: "sensible phrases of MIPT teachers"
    """
    with open(file, "r", encoding='utf-8') as file:
        text = file.read()

    produced_phrases = []

    text_model = markovify.Text(text)
    # text_model_2 = markovify.Text(text)
    # text_model = markovify.combine([text_model_1, text_model_2], [1, 1])
    # json_module = text_model.to_json()
    # text_model = markovify.Text.from_json(json_module)

    for _ in range(10000):
        produced_phrases.append(text_model.make_sentence())

    return produced_phrases


if __name__ == "__main__":
    produce_phrases("prepared_phrases.txt")
