string = ('17,357;17,357;6,0;0')

old_strs = string.split(';')


for i in range(len(old_strs)):
    if i == 0:
        new_str = old_strs[i]
    elif i == len(old_strs)-1:
        new_str += ';' + old_strs[i-1]
    else:
        new_str += ';'+ old_strs[i]

