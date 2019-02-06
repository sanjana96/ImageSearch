import ImageSearch


def test_image_search():
    path = '../test/resource'

    result = [{'text': 'Madagascar', 'result': ['text_bottom.jpg']},
              {'text': 'lazy', 'result': ['simple_text.png']},
              {'text': 'when you think you have been', 'result': ['meme_text_top_bottim.jpg']}]

    for element in result:
        assert list(ImageSearch.find(path, element['text'])) == element['result']

# TODO: Test exceptions
