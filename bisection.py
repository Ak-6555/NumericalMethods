def f(x):
    return (x * x + 2 * x - 1);


def bisection(left, right, tolerant_value):
    while True:
        mid = (left + right) / 2;
        if (f(mid) * f(right) < 0):
            left = mid;
        else:
            right = mid;
        if (abs(f(mid)) < tolerant_value):
            break;

    print("\n Root : %0.10f" % mid);


value1 = int(input());
value2 = int(input());

if (f(value1) * f(value2) > 0):
    print("\n wrong guess");
else:
    tolerant = float(input());
    value1, value2 = value2, value1;

bisection(value1, value2, tolerant);



