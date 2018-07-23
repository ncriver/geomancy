def center_lines(lines, width):
    line_list = [s.center(width) for s in lines.split('\n')]
    return '\n'.join(line_list)
    
def merge_strings(first, second, between_char = ''):
    """Merges the lines of two string inputs into single lines in left-right order."""
    first_lines = first.split('\n')
    second_lines = second.split('\n')
    zipped_lines = zip(first_lines, second_lines)
    merged_lines = []
    for i in zipped_lines:
        merged_lines.append(between_char.join(i))

    # If it turns out the two input strings have different number of lines,
    # we will add the extra lines to the result.
    min_len = min(len(first_lines), len(second_lines))        
    if len(first_lines) > len(second_lines):
        merged_lines.extend(first_lines[min_len:])
    else:
        merged_lines.extend(second_lines[min_len:])
    return '\n'.join(merged_lines)
       