from exceptions import NotANumberException

def convert_number(num):
    try:
        return int(num)
    except ValueError:
        try:
            return float(num)
        except ValueError:
            raise NotANumberException(num)