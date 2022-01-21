
def string_update(s):
    if len(s) > 2:
        if s[-3:] == 'ing':
            res = s.replace('ing','ly')
            return res
        if s[-2:] == 'ly':
            res = s.replace('ly', 'ing')
            return res
    else:
        return s

print(string_update("ending"))
print(string_update("evenly"))
print(string_update("ok"))