def remove_uppercase(string):
    return string.lower()

def remove_space(string):
    return string.replace(' ', '_')

def remove_fuss(string):
    string = string.replace("'", '_')
    return string.replace("-", '')
    


def remove_dots(string):
    if '.' in string :
        split = string.split('.')
        cleaned = ""
        for i in range(len(split)-1):
            cleaned += split[i]
        return cleaned +"."+split[-1]
    return string


def run_modules_on_list(string_list, ruppercase = True, rspace = True, rfuss = True, rdots = True):
    output_list = []
    for i in range(len(string_list)) :
        output_list.append(string_list[i])
        if ruppercase :
            string_list[i] = remove_uppercase(string_list[i])
        if rfuss :
            string_list[i] = remove_fuss(string_list[i])
        if rdots :
            string_list[i] = remove_dots(string_list[i])
        if rspace :
            string_list[i] = remove_space(string_list[i])
    return output_list
