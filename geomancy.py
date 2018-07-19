import random
import collections

class Figure(object):
    """The class represents the building block of a geomancy fortune casting session.
    Each Geofigure object represents a geomancy figure formed by throwing a two-faced die four times."""        
    def __init__(self, first, second, third, fourth):
        self.elem_order = ['fire', 'air', 'water', 'earth']
        self.elementals = collections.OrderedDict()
        self.nums = [first, second, third, fourth]
        self.nums = [self.get_one_or_two(x) for x in self.nums]
        for num, elem in zip(self.nums, self.elem_order):
            one_or_two = self.get_one_or_two(num)
            self.elementals[elem] = one_or_two
        self.set_name()

    def get_one_or_two(self, number):
        """Returns 1 for odd number input and 2 for even number input."""
        return 2-(int(number)%2)

    def set_name(self):
        num_string = ""
        for num in self.nums:
            num_string += str(num)
        latin_names = collections.OrderedDict([('1121', 'puer'), ('1211', 'puella')])
        self.name = "Unset"
        if num_string in latin_names:
            self.name = latin_names[num_string]
        return self.name

    def update(self, first, second, third, fourth):
        """Updates the numbers in Geofigure object"""
        self.nums = [first, second, third, fourth]
        self.nums = [self.get_one_or_two(x) for x in self.nums]
        for num, elem in zip(self.nums, self.elem_order):
            one_or_two = self.get_one_or_two(num)
            self.elementals[elem] = one_or_two

    def __add__(self, another):
        "Adds two figures and returns a new Geofigure object."
        new_dots = []
        for i in range(len(self.nums)):
            new_dots.append(self.nums[i] + another.nums[i])
        return type(self)(*new_dots)

    def __eq__(self, another):
        if isinstance(another, Figure):
            return self.nums == another.nums
        else:
            return False
    
    def num_value(self):
        value = 0
        for i in range(len(self.nums)):
            value += self.nums[i]*(2**i)
        return value

    def get_name(self):
        pass

    def __str__(self):
        pretty_str = ''
        for d in self.nums:
             if d % 2 == 1:
                 pretty_str += ' * \n'
             else:
                 pretty_str += '* *\n'
        pretty_str = pretty_str[0:-1]
        return pretty_str
    def __repr__(self):
        return "Geofigure:" + self.nums.__repr__()

    @classmethod
    def quick_throw(cls):
        throw_results = []
        for i in range(4):
            throw_results.append(random.randint(1,2))
        return cls(*throw_results)
        
class Shield(object):
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

    @classmethod
    def quick_cast(cls):
        mothers = []
        for i in range(0, 4):
            mothers.append(Figure.quick_throw())
        return cls(*mothers)
    
    def text_art(self):
        mother_str = str(self.mothers[0])
        for m in self.mothers[1:]:
            mother_str = self.merge_strings(mother_str, str(m), False, ' | ')
        daughter_str = str(self.daughters[0])
        for d in self.daughters[1:]:
            daughter_str = self.merge_strings(daughter_str, str(d), False, ' | ')
        output_str = self.merge_strings(mother_str, daughter_str, False, ' | ')
        row_separator = '-'*45
        output_str += '\n' + row_separator + '\n'
        niece_str = self.merge_strings(str(self.nieces[0]), '   \n'*4)
        for n in self.nieces[1:]:
            niece_str = self.merge_strings(niece_str, str(n), False, '    |    ')
        niece_str = self.merge_strings('   \n'*4, niece_str)
        output_str += niece_str + row_separator + '\n'
        witness_str = self.merge_strings(str(self.left_witness), str(self.right_witness), True, ' '*9+'|'+' '*9)
        witness_str = self.merge_strings((' '*10+'\n')*4, witness_str)
        output_str += witness_str   
        output_str += row_separator + '\n'
        judge_str = self.merge_strings((' '*21+'\n')*4, str(self.judge))
        output_str += judge_str
        return output_str
       
    def merge_strings(self, first, second, ltor_order = True, between_char = ''):
        first_list = first.split('\n')
        second_list = second.split('\n')

        if ltor_order:
            zipped_list = zip(first_list, second_list)
        else:
            zipped_list = zip(second_list, first_list)
        merged_list = []
        for i in zipped_list:
            merged_list.append(between_char.join(i))

        min_len = min(len(first_list), len(second_list))        
        if len(first_list) > len(second_list):
            merged_list.extend(first_list[min_len:])
        else:
            merged_list.extend(second_list[min_len:])
        return '\n'.join(merged_list)
       
if __name__ == "__main__":
    print(Shield.quick_cast().text_art())
    a = Figure(1,1,2,1)
    a.set_name()
    print(a.name)
