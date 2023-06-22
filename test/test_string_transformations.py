from stringstandardization.string_transformations import remove_special_characters

def test_full_name():
    name = "João Guimarães"
    std_name = remove_special_characters(name)
    assert len(std_name.split(' ')) > 1
