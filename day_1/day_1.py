from io import TextIOWrapper


digits_as_text = {
    'zero': '0', 'one': '1', 'two': '2', 'three': '3', 'four': '4', 
    'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9',
}
        
        
class DigitNotFoundException(Exception):
    pass        
        
        
def get_digit(line: str, index: int) -> str:
    if (char := line[index]).isdigit():
        return char
    for k, v in digits_as_text.items():
        if line.find(k, index) == index:
            return v
    raise DigitNotFoundException


def first_and_last_digits(line: str) -> tuple[str, str]:
    digits = [*digits_as_text.keys(), *digits_as_text.values()]
    first_index = min(filter(lambda idx: idx > -1, 
            [line.find(digit) for digit in digits]))
    last_index = max([line.rfind(digit) for digit in digits])
    first = get_digit(line, first_index)
    last = get_digit(line, last_index)
    return first, last
    

def process_line(line: str) -> int:
    first, last = first_and_last_digits(line)
    return int(f'{first}{last}')


def process_document(document: TextIOWrapper) -> int:
    return sum([process_line(line) for line in document])


if __name__ == '__main__':
    # test_lines = {
    #     'ninefourone1': 91,
    #     '53sevenvvqm': 57,
    #     'kscpjfdxp895foureightckjjl1': 81,
    #     '72fivebt9ndgq': 79,
    #     '28gtbkszmrtmnineoneightmx': 28,
    #     'four66jqrbtqcsxjtqjvfjhl1': 41,
    # }
    
    # for line, expected in test_lines.items():
    #     print(f'"{line}", expected: {expected} -> {process_line(line)} {expected == process_line(line)}')
        
    with open('input.txt', mode='r') as calibration_file:
        processing_result = process_document(calibration_file)
        print(processing_result)
            