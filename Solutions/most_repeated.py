a = 'This is a common interview question'
neww = {}
for x in a:
    val = a.count(x)
    neww[x] = val
new_dict = sorted(neww.items(), key=lambda kv: kv[1], reverse=True)

print(new_dict[0])
