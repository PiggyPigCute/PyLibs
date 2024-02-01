

_DIGITS = "0123456789abcdefghijklmnopqrstuvwxyzαβγδεζηιθκλµ𝘷ξ𝘰πρστυφχψω"


def base(n:int, b:int) -> str:
    if n == 0:
        return ""
    return base(n//b, b) + _DIGITS[n%b]


def reset_base(n:str, b:int) -> int:
    if n == "":
        return 0
    return _DIGITS.index(n[-1]) + b*reset_base(n[:-1], b)
