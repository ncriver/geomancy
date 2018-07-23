import random
from collections import OrderedDict
from .stringfuncs import center_lines, merge_strings

class Figure(object):
    """The class represents the building block of a geomancy fortune casting session.
    Each Geofigure object represents a geomancy figure formed by throwing a two-faced die four times."""        
    def __init__(self, first, second, third, fourth):
        self.elem_order = ['fire', 'air', 'water', 'earth']
        self.elementals = OrderedDict()
        nums = (first, second, third, fourth)
        self.update(*nums)

    def get_one_or_two(self, number):
        """Returns 1 for odd number input and 2 for even number input."""
        return 2-(int(number)%2)

    def update(self, first, second, third, fourth):
        """Updates the numbers in Geofigure object"""
        nums = (first,second,third,fourth)
        self.nums = tuple(self.get_one_or_two(x) for x in nums)
        for num, elem in zip(self.nums, self.elem_order):
            one_or_two = self.get_one_or_two(num)
            self.elementals[elem] = one_or_two
        self.set_name()

    def set_name(self):
        """Sets the correct latin name for the figure."""
        num_string = ""
        for num in self.nums:
            num_string += str(num)
        latin_names = OrderedDict([('1121', 'Puer'),
                                    ('1212', 'Amissio'),
                                    ('2212', 'Albus'),
                                    ('2222', 'Populus'),
                                    ('2211', 'Fortuna Major'),
                                    ('2112', 'Conjunctio'),
                                    ('1211', 'Puella'),
                                    ('2122', 'Rubeus'),
                                    ('2121', 'Acquisitio'),
                                    ('1221', 'Carcer'),
                                    ('2221', 'Tristitia'),
                                    ('1222', 'Laetitia'),
                                    ('1112', 'Cauda Draconis'),
                                    ('2111', 'Caput Draconis'),
                                    ('1122', 'Fortuna Minor'),
                                    ('1111', 'Via')])
        self.name = "Unset"
        if num_string in latin_names:
            self.name = latin_names[num_string]
        return self.name

    def get_name(self):
        """Returns the latin name of the figure."""
        return self.name
   
    def __add__(self, another):
        "Adds two figures and returns a new Fgure object."
        new_dots = []
        for i in range(len(self.nums)):
            new_dots.append(self.nums[i] + another.nums[i])
        return type(self)(*new_dots)

    def __eq__(self, another):
        """Two figures are equal if they have the same numerical values."""
        if isinstance(another, Figure):
            return self.nums == another.nums
        else:
            return False

    def __repr__(self):
        return "Figure" + tuple(self.nums).__repr__()

    def __str__(self):
        width = len(self.get_name())
        if width < 5:
            width = 5
        
        pretty_str = ''
        for d in self.nums:
             if d % 2 == 1:
                 pretty_str += '*'.center(width) + '\n'
             else:
                 pretty_str += '* *'.center(width) + '\n'
        
        def get_short_name(name, width):
            short_name = name
            if short_name == 'Fortuna Major' and width < len("Fortuna Ma"):
                short_name = 'Major'[0:width]
            elif short_name == 'Fortuna Minor' and width < len("Fortuna Mi"):
                short_name = 'Minor'[0:width]
            elif short_name == 'Puer' and width < len('Puer'):
                short_name = 'Pur'[0:width]
            elif short_name == 'Puella' and width < len('Puer'):
                short_name = 'Pel'[0:width]
            else:
                short_name = short_name[0:width]
            return short_name
        
        short_name = get_short_name(self.get_name(), width)
        if len(short_name) < width:
            short_name = short_name.center(width)

        pretty_str += short_name
        # pretty_str = pretty_str[0:-1]
        return pretty_str

    def __hash__(self):
        return hash(tuple(self.nums + [self.name]))

    @classmethod
    def quick_throw(cls):
        """A class method that returns a Figure object with a random set of numbers."""
        throw_results = []
        for i in range(4):
            throw_results.append(random.randint(1,2))
        return cls(*throw_results)
        
class Shield(object):
    """The class represents the geomantic shield chart formed out of four starting geomantic figure object.
    
    Through addition and transposing, the caster forms eleven additional geomantic figures for a total of fiften figures.
    The __init__() arguments are four Figure objects.
    """
    def __init__(self, firstm, secondm, thirdm, fourthm):
        self.mothers = [firstm, secondm, thirdm, fourthm]
        self.daughters = []
        for i in range(len(self.mothers[0].nums)):
            new_dots = []
            for j in range(len(self.mothers)):
                new_dots.append(self.mothers[j].nums[i])
            self.daughters.append(Figure(*new_dots))
        self.nieces = []
        self.nieces.append(self.mothers[0] + self.mothers[1])
        self.nieces.append(self.mothers[2] + self.mothers[3])
        self.nieces.append(self.daughters[0] + self.daughters[1])
        self.nieces.append(self.daughters[2] + self.daughters[3])
        self.right_witness = self.nieces[0] + self.nieces[1]
        self.left_witness = self.nieces[2] + self.nieces[3]
        self.judge = self.right_witness + self.left_witness
        self.index = []
        self.index.extend(self.mothers)
        self.index.extend(self.daughters)
        self.index.extend(self.nieces)
        self.index.extend([self.right_witness,self.left_witness,self.judge])


    @classmethod
    def quick_cast(cls):
        """A class method that returns a Shield object formed from four random Figure objects."""
        mothers = []
        for i in range(0, 4):
            mothers.append(Figure.quick_throw())
        return cls(*mothers)
    
    def text_art(self):
        mother_str = str(self.mothers[0])
        figure_height = len(mother_str.split('\n'))
        figure_separator = '|'
        # We need to get the optimal width for the figures at each row.
        ## We first get width of the Figure with the longest name.
        rows = []
        rows.append(self.mothers.copy() + self.daughters)
        rows.append(self.nieces)
        rows.append([self.right_witness,self.left_witness])
        rows.append([self.judge])
        max_widths = []
        for figures in rows:
            widths = [len(x.get_name()) for x in figures]
            max_widths.append(max(widths))

        # We now see if an optimal set of widths exists.
        def quo_mod(dividend, divisor):
            return (dividend // divisor, dividend % divisor,)
        for poss_width in range(40,100):
            quos, mods = zip(*map(quo_mod, [poss_width-7, poss_width-3, poss_width-1, poss_width], [8,4,2,1]))
            conditions = []
            conditions.append(sum(mods) == 0)
            for q, mw in zip(quos,max_widths):
                conditions.append(q >= mw)
            if all(conditions):
                art_width = poss_width
                for i, q in enumerate(quos):
                    max_widths[i] = q
                    break

        # If an optimal set of widths do not exist, we fall back to 
        ## the width of the figure with the longest name in all the charts.
        if not all(conditions):
            all_max = max(max_widths)
            # We have to set the width of the figure for each row differently.
            lfs = len(figure_separator)
            max_widths = [all_max, all_max * 2 + lfs, all_max * 4 + lfs * 3, all_max * 8 + lfs * 7]
            art_width = all_max * 8 + lfs * 7
        mother_width = max_widths[0]
        # Centering and padding mother_str
        mother_str = center_lines(mother_str, mother_width)
        for m in self.mothers[1:]:
            mother_str = merge_strings(center_lines(str(m), mother_width), mother_str, figure_separator)
        daughter_str = center_lines(str(self.daughters[0]), mother_width)
        for d in self.daughters[1:]:
            daughter_str = merge_strings(center_lines(str(d), mother_width), daughter_str, figure_separator)
        output_str = merge_strings(daughter_str, mother_str, figure_separator)
        
        row_separator = '-' * art_width
        output_str += '\n' + row_separator + '\n'
        
        niece_width = max_widths[1]
        niece_str = center_lines(str(self.nieces[0]),niece_width)
        for n in self.nieces[1:]:
            niece_str = merge_strings(center_lines(str(n), niece_width), niece_str, figure_separator)
        output_str += niece_str + '\n' + row_separator + '\n'
        
        witness_width = max_widths[2]
        witness_str = merge_strings(center_lines(str(self.left_witness), witness_width),
                                         center_lines(str(self.right_witness), witness_width), figure_separator )
        output_str += witness_str + '\n'
        output_str += row_separator + '\n'
        
        judge_str = center_lines(str(self.judge), max_widths[3])
        output_str += judge_str
        return output_str
