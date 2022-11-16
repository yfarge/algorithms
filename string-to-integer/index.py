def myAtoi(s: str):
    start, end = 0, 0
    prefix = "+0"
    n = len(s)

    # remove leading white spaces
    while start < n and s[start] == " ":
        start += 1

    # check if remaining length > 0
    if n - start == 0:
        return 0

    # setting prefix
    if s[start] == "+" or s[start] == "-":
        prefix = str(s[start]) + '0'
        start = 1

    # ignore non-integer characters
    for i in range(start, n):
        if not s[i].isdigit():
            break
        end += 1
    num = int(prefix + "".join(s[start:start + end]))
    return max(pow(-2, 31), min(num, pow(2, 31) - 1))
