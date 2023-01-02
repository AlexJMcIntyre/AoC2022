file = open("13.txt")
list_import = file.readlines()

ds = []
for lr in list_import:
    ds.append(lr.strip())

lt = 0
rt = 0  # totals

def parse_list(f_string):
    f_list = []  # the whole packet to return
    ce = ""  # current element
    i = 0
    while i < len(f_string):
        c = f_string[i]
        if i == 0:
            pass  # ignore known initial [
        elif c == "[":
            # bracket problems! Need to find matching closing bracket for nested lists
            ss = f_string[i:]
            vc = 1
            j = 1
            while vc > 0:
                if ss[j] == "[":
                    vc += 1
                if ss[j] == "]":
                    vc -= 1
                j += 1
            f_list.append(parse_list(f_string[i:j + i]))
            i += j-1
        elif c == ",":
            if ce != '':
                f_list.append(int(ce))
            ce = ""
        elif c == "]":
            if ce != '':
                f_list.append(int(ce))
            return f_list
        else:
            ce += c
        i += 1


def compare_lists(lf, rf):
    print("compare ", lf, " vs ", rf)
    co = 0
    if type(lf) is int and type(rf) is int:  # if both are integers
        if lf == rf:
            # print("Same, continue")
            return 0  # unknown
        elif lf < rf:
            print("left is smaller, so inputs are *in the right order*")
            return 1  # correct
        else:
            print("right is smaller, so inputs are *not* in the right order")
            return -1  # incorrect
    elif type(lf) is list and type(rf) is list:  # elif both are lists
        i = 0
        while co == 0:
            if len(lf) > i and len(rf) > i:  # compare the ith from each
                co = compare_lists(lf[i], rf[i])
            elif len(lf) == len(rf) == i:
                # both lists ran out, continue
                return 0  # unknown
            elif len(lf) <= i:  # left smaller
                print("Left side ran out of items, so inputs are in *the right order*")
                return 1  # correct
            elif len(rf) <= i:  # right smaller
                print("Right side ran out of items, so inputs are *not* in the right order")
                return -1  # incorrect
            i += 1
        return co  # if you're here, the nested function returned a value. return it.
    else:  # else one is integer
        print("mix, convert")
        if type(lf) is int:
            lf = [lf]
        else:
            rf = [rf]
        return compare_lists(lf, rf)

# def compare_lists(lf, rf):
#     global solved, correct_order
#     print("compare ", lf, " vs ", rf)
#     if type(lf) is int and type(rf) is int:  # if both are integers
#         if lf == rf:
#             print("Same, continue")
#             pass
#         elif lf<rf:
#             print("left is smaller, so inputs are *in the right order*")
#             solved = 1
#             correct_order = 1
#         else:
#             print("right is smaller, so inputs are *not* in the right order")
#             solved = 1
#             correct_order = 0
#     elif type(lf) is list and type(rf) is list:  # elif both are lists
#         i = 0
#         while solved == 0:
#             if len(lf) > i and len(rf) > i:  # compare the ith from each
#                 compare_lists(lf[i], rf[i])
#             elif len(lf) < i and len(rf) < i:  # both same, continue
#                 print("both same")
#                 pass
#             elif len(lf) <= i:  # left smaller
#                 print("Left side ran out of items, so inputs are in *the right order*")
#                 solved = 1
#                 correct_order = 1
#             elif len(rf) <= i:  # right smaller
#                 print("Right side ran out of items, so inputs are *not* in the right order")
#                 solved = 1
#                 correct_order = 0
#             else:
#                 print("no comparison, move on")
#                 break
#             i += 1
#     else:  # else one is integer
#         print("mix, convert")
#         if type(lf) is int:
#             lf = [lf]
#         else:
#             rf = [rf]
#         compare_lists(lf, rf)

sol = 0
for i in range(0, len(ds), 3):
    print("== Pair", str(int((i+3)/3)), " ==")
    ls = parse_list(ds[i])
    rs = parse_list(ds[i+1])
    if compare_lists(ls, rs) == 1:
        sol += (int((i+3)/3))
print(sol)
