from .context import structures
Shield = structures.Shield

def test_text_art():
    text_art = Shield.quick_cast().text_art()
    print(text_art)
    assert text_art is not None
    assert len(text_art) > 1
    assert "*" in text_art