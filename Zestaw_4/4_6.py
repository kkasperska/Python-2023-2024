def sum_seq(sequence):
    out = 0
    for i in sequence:
        if isinstance(i, (list, tuple)):
            out += sum_seq(i)
        else:
            out += i

    return out


seq = [1,(2,3),[],[4,(5,6,7)],8,[9]]
print(sum_seq(seq))