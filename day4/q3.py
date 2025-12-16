def fun_overlapping():
    l1=[11,22,33,44,55]
    l2=[1,2,3,4,5]
    print(f"l1={l1}")
    print(f"l2={l2}")
    s1=set(l1)
    s2=set(l2)
    print(f"s1={s1}")
    print(f"s2={s2}")
    intersection=s1.intersection(s2)
    if(intersection !=0):
        print(True)
    else:
        print(False)
fun_overlapping()