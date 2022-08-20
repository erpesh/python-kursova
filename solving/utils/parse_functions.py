def parse_functions(funcs):
    for i in range(len(funcs)):
        func_splited = funcs[i].split('=')
        funcs[i] = func_splited[0] + "-" + f"({func_splited[1]})"
    return funcs
