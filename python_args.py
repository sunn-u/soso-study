
def args_test(*args):
    print(f'*agrs type: {type(args)}')
    for arg in args:
        print(arg)
    return 0

args_test('a','b','c')

def kwargs_test(**kwargs):
    print(f'**kwargs type: {type(kwargs)}')
    for key, value in kwargs.items():
        print(f'key:{key}({type(key)}), value:{value}({type(value)})')
    return 0

kwargs_test(sunn=940817, soo=940820)
