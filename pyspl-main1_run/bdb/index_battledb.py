

fe1 = open('ALP_INDEX.txt', "r")
count = 0
st =''
for x in fe1:
    if count == 0:
        st = x
    count = count + 1
lis =st.split(' ')
for y in lis:
    for z in lis:
        fn = 'sl_'+y.lower()+z.lower()+'.txt'
        f = open(fn, "w")
        f.close()
