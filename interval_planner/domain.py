def normalize(intervals, merge_touching=False):
    ordered=sorted(intervals)
    if len(ordered)>100 or any(type(a) is not int or type(b) is not int or a<0 or b>10000 or a>=b for a,b in ordered):
        raise ValueError('invalid_intervals')
    merged=[]; overlap=False
    for start,end in ordered:
        if merged and (start<merged[-1][1] or (merge_touching and start==merged[-1][1])):
            overlap=overlap or start<merged[-1][1]
            merged[-1][1]=max(merged[-1][1],end)
        else: merged.append([start,end])
    return {'intervals':merged,'overlap':overlap}
