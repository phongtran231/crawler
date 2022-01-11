import sys
import json
def sort_func(e):
    return e[7]
def sort_func2(e):
    return e[8]
def sort_func3(e):
    return e[10]*e[9]
def find_index_in_list(ii,lis):
    for x in range(len(lis)):
        if ii['summoner_id'] == lis[x][0] and ii['monster_1_id'] == lis[x][1] and ii['monster_2_id'] == lis[x][2] and ii['monster_3_id'] == lis[x][3] and ii['monster_4_id'] == lis[x][4] and ii['monster_5_id'] == lis[x][5] and ii['monster_6_id'] == lis[x][6] and ii['ruleset'] == lis[x][7] and ii['mana_cap'] == lis[x][8]:
            return x
    return -1
def open_and_gen_list(fnaxxxx):
    try:
        fxyz = open(fnaxxxx,'r')
        out_list = []
        j = []
        j = json.load(fxyz)
        fxyz.close()
        for yy in j:
            out_list.append([yy['summoner_id'],yy['monster_1_id'],yy['monster_2_id'],yy['monster_3_id'],yy['monster_4_id'],yy['monster_5_id'],yy['monster_6_id'],yy['ruleset'],yy['mana_cap'],yy['tot'],yy['ratio']])
        return out_list
    except:
        return None
num_out = int( sys.argv[1] )
final_list = []

for i in range(num_out):
    i=i+1
    fname = 'output/output'+str(i)+'.txt'
    print(fname)
    f = open(fname,'r')
    j=[]
    j = json.load(f)
    f.close()
    for yy in j:
        aa = find_index_in_list(yy,final_list)
        if aa==-1:
            final_list.append([yy['summoner_id'],yy['monster_1_id'],yy['monster_2_id'],yy['monster_3_id'],yy['monster_4_id'],yy['monster_5_id'],yy['monster_6_id'],yy['ruleset'],yy['mana_cap'],yy['tot'],yy['ratio']])
        else:
            kk = final_list[aa][9]
            final_list[aa][9] = final_list[aa][9] + yy['tot']
            final_list[aa][10] = ( yy['ratio'] * yy['tot'] + final_list[aa][10]*kk ) / final_list[aa][9]


final_list.sort(key=sort_func)
tmp_str = ''
myli = []
myli2 = []
lenfna = len( final_list )
print( final_list )
for item in final_list:
    print(item)
    i = i + 1
    if tmp_str == '':
        tmp_str = item[7]
        myli.append(item)
    else:
        if tmp_str == item[7]  and i != lenfna:
            myli.append(item)
            #do something
        else:
            if i == lenfna:
                myli.append(item)
            myli.sort(key=sort_func2)
            manax = ''
            for itemx in myli:
                if manax == '':
                    manax = itemx[8]
                else:
                    if manax == itemx[8] and i != lenfna:
                        myli2.append(itemx)
                    else:
                        print(itemx[7])
                        filename = 'result_final/'+str(itemx[7]) + str(manax) + 'mana' + '.txt'
                        print(filename)
                        filename = filename.replace(' ','')
                        filename = filename.replace('|','%7C')
                        try:
                            out_list = open_and_gen_list(filename)
                            f = open(filename, "w")
                            f.write('[')
                            fx = 1
                            myli2.sort(reverse=True,key=sort_func3)
                            for x in myli2:
                                if fx == 1:
                                    f.write('{')
                                    fx = fx + 1
                                else:
                                    f.write(',{')
                                f.write('"summoner_id":')
                                ar = 0
                                try:
                                    ar = int(str(x[0]))
                                except:
                                    ar = 0
                                f.write(f'{ar}')
                                f.write(',')
                                f.write('"monster_1_id":')
                                ar = 0
                                try:
                                    ar = int(str(x[1]))
                                except:
                                    ar = 0
                                f.write(f'{ar}')
                                f.write(',')
                                f.write('"monster_2_id":')
                                ar = 0
                                try:
                                    ar = int(str(x[2]))
                                except:
                                    ar = 0
                                f.write(f'{ar}')
                                f.write(',')
                                f.write('"monster_3_id":')
                                ar = 0
                                try:
                                    ar = int(str(x[3]))
                                except:
                                    ar = 0
                                f.write(f'{ar}')
                                f.write(',')
                                f.write('"monster_4_id":')
                                ar = 0
                                try:
                                    ar = int(str(x[4]))
                                except:
                                    ar = 0
                                f.write(f'{ar}')
                                f.write(',')
                                f.write('"monster_5_id":')
                                ar = 0
                                try:
                                    ar = int(str(x[5]))
                                except:
                                    ar = 0
                                f.write(f'{ar}')
                                f.write(',')
                                f.write('"monster_6_id":')
                                ar = 0
                                try:
                                    ar = int(str(x[6]))
                                except:
                                    ar = 0
                                f.write(f'{ar}')
                                f.write(',')
                                f.write('"ruleset":')
                                f.write(f'{x[7]}')
                                f.write(',')
                                f.write('"mana_cap":')
                                ar = 0
                                try:
                                    ar = int(str(x[8]))
                                except:
                                    ar = 0
                                f.write(f'{ar}')
                                f.write(',')
                                f.write('"tot":')
                                ar = 0
                                try:
                                    ar = int(str(x[9]))
                                except:
                                    ar = 0
                                f.write(f'{ar}')
                                f.write(',"ratio":')
                                ar = 0
                                try:
                                    ar = int(str(x[10]))
                                except:
                                    ar = 0
                                f.write(f'{ar}')
                                f.write('}')
                            f.write(']')
                            f.close()
                        except:
                            print(f'Error create file: {filename}')
                        myli2=[]
                        myli2.append(itemx)
                        manax = itemx[8]
                        
            
            myli = []
            myli.append(item)
            tmp_str = item[7]
