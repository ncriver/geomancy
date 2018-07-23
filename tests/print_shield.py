from context import structures, analysis
Shield = structures.Shield

if __name__ == "__main__":
    a = Shield.quick_cast()
    for i in a.index:
        print(i.get_name())
    print(a.text_art())
    my_fortune = analysis.SimpleAnalysis(a)
    print(my_fortune.get_result())