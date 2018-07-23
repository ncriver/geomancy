from context import structures
Shield = structures.Shield

if __name__ == "__main__":
    a = Shield.quick_cast()
    for i in a.index:
        print(i.get_name())
    print(a.text_art())