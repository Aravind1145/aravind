from collections import OrderedDict
ji=str(input())
def remove_duplicate(ji):
    return "".join(OrderedDict.fromkeys(ji))
print(remove_duplicate(ji))
