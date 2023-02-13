# constants
EXTRA_PADDING: int = 2
SPACE_PADDING: int = 4


def problem_arranger(problem: str, calculate: bool = False) -> tuple[str, str, str]:
    num, op, den = problem.split(" ")
    res = ""
    if calculate:
        if op == "+":
            res = str(int(num) + int(den))
        elif op == "-":
            res = str(int(num) - int(den))
    length = max(len(num), len(den)) + EXTRA_PADDING
    num, den, res = num.rjust(length), den.rjust(length), res.rjust(length)
    den = op + den[1:]
    return num, den, res


def validate_problem(num: str, den: str) -> tuple[bool, str]:
    try:
        num = int(num)
        op = den[0]
        den = int(den[1:])
        # correct operator
        if op not in ["+", "-"]:
            return False, "Error: Operator must be '+' or '-'."
        # too many digits
        if len(str(num)) > 4 or len(str(den)) > 4:
            return False, "Error: Numbers cannot be more than four digits."
    # only digits
    except ValueError:
        return False, "Error: Numbers must only contain digits."

    return True, "No problems"


def arithmetic_arranger(problems: list[str], calculate: bool = False) -> str:
    num_line, den_line, res_line, divider = ("", "", "", "")
    if len(problems) > 5:
        return "Error: Too many problems."
    for problem in problems:
        num, den, res = problem_arranger(problem, calculate)
        valid, message = validate_problem(num, den)
        if not valid:
            return message
        num_line += num + (" " * SPACE_PADDING)
        den_line += den + (" " * SPACE_PADDING)
        res_line += res + (" " * SPACE_PADDING)
        divider += ("-" * len(num)) + (" " * SPACE_PADDING)
    num_line = num_line.rstrip() + "\n"
    den_line = den_line.rstrip() + "\n"
    res_line = res_line.rstrip() + "\n"
    divider = divider.rstrip() + "\n"

    final = num_line + den_line + divider
    if calculate:
        final += res_line
    return final.rstrip()
