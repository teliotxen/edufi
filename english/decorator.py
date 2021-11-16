def login_decorator():
    def deco_func():
        print('tstory')
        return '1'
    return deco_func