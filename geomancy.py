import random
import collections

class Geofigure(object):
    """The class represents the building block of a geomancy fortune casting session.
    Each Geofigure object represents a geomancy figure formed by throwing a two-faced die four times."""        
    def __init__(self, first, second, third, fourth):
        dots = [first, second, third, fourth]
        self.dots = []
        self.elem_order = ['fire', 'air', 'water', 'earth']
        self.elementals = collections.OrderedDict()

        for dot, elem in zip(dots, self.elem_order):
            dot_num = self.even_odd_num(dot)
            self.dots.append(dot_num)
            self.elementals[elem] = dot_num
        
    def even_odd_num(self, number):
        return 2-(number%2)
    def add(self, another):
        new_dots = []
        for i in range(len(self.dots)):
            new_dots.append(self.dots[i] + another.dots[i])     
        return Geofigure(*new_dots)
    def __eq__(self, another):
        if isinstance(another, Geofigure):
            return self.dots == another.dots
        else:
            return False
    def num_value(self):
        value = 0
        for i in range(len(self.dots)):
            value += self.dots[i]*(2**i)
        return value
    def __str__(self):
        pretty_str = ''
        for d in self.dots:
             if d % 2 == 1:
                 pretty_str += ' * \n'
             else:
                 pretty_str += '* *\n'
        pretty_str = pretty_str[0:-1]
        return pretty_str
    def __repr__(self):
        return "Geofigure:" + self.dots.__repr__()
    @classmethod
    def quick_throw(cls):
        throw_results = []
        for i in range(4):
            throw_results.append(random.randint(1,2))
        return cls(*throw_results)

        

class Geoshield(object):
    def __init__(self, firstm, secondm, thirdm, fourthm):
        self.mothers = [firstm, secondm, thirdm, fourthm]
        self.daughters = []
        for i in range(len(self.mothers[0].dots)):
            new_dots = []
            for j in range(len(self.mothers)):
                new_dots.append(self.mothers[j].dots[i])
            self.daughters.append(Geofigure(*new_dots))
        self.nieces = []
        self.nieces.append(self.mothers[0].add(self.mothers[1]))
        self.nieces.append(self.mothers[2].add(self.mothers[3]))
        self.nieces.append(self.daughters[0].add(self.daughters[1]))
        self.nieces.append(self.daughters[2].add(self.daughters[3]))
        self.right_witness = self.nieces[0].add(self.nieces[1])
        self.left_witness = self.nieces[2].add(self.nieces[3])
        self.judge = self.right_witness.add(self.left_witness)

    @classmethod
    def quick_divine(cls):
        mothers = []
        for i in range(0, 4):
            mothers.append(Geofigure.quick_throw())
        return cls(*mothers)
    
    def shield_diagram(self):
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
       


def run_test():
    new_vals = [1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1]
    moms = []
    for i in range(4):
        moms.append(Geofigure(*new_vals[i*4:(i*4)+4]))
    return Geoshield(*moms)

    

            
