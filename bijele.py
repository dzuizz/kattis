k, q, r, b, kn, p = map(int, input().split())
def change(v, bi):
    tar = 0
    if v > bi:
        tar -= (v-bi)
    elif v < bi:
        tar += (bi-v)
    return tar
a = change(k, 1)
bb = change(q, 1)
c = change(r, 2)
d = change(b, 2)
e = change(kn, 2)
f = change(p, 8)
print(f"{a} {bb} {c} {d} {e} {f}")
