import json
import requests
from requests.auth import HTTPProxyAuth
import os
import time
import sys

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
final_list = []
is_win = 0
count_global = 0
uaglobal = []
total_global = 0
def print_status(pr,au,p,q,namex,start_time):
    clear = lambda: os.system('cls')
    clear()
    per = p / q * 100
    print(f'Splinterland Crawl Tool')
    end_time = time.time() - start_time
    print(f'Running Time.............{end_time}')
    print(f'Running..................{per}%')
    print(f'Running account..........{namex}')
    print(f'Total Battle.............{q}')
    print(f'Total processed battle...{p}')
    xxxc = len(uaglobal)
    if xxxc > 0:
        print(f'Total Skipped battle.....{uaglobal[0]}')
    else: 
        print(f'Total Skipped battle.....0')
    print(pr)
    print(au)
    
    
def find_index_in_list(listi):
    for i in range(len(final_list)):
        if listi[0] == final_list[i][0]:
            if  listi[1] == final_list[i][1] and listi[2] == final_list[i][2] and listi[3] == final_list[i][3] and listi[4] == final_list[i][4] and listi[5] == final_list[i][5] and listi[6] == final_list[i][6] and listi[7] == final_list[i][7] and listi[8] == final_list[i][8]:
                return i
    return -1
    
def find_index_in_list2(listi,inlxxx):
    try:
        for i in range(len(inlxxx)):
            if str(listi[0]) == str(inlxxx[i][0]):
                if  str(listi[1]) == str(inlxxx[i][1]):
                    if str(listi[2]) == str(inlxxx[i][2]):
                        if str(listi[3]) == str(inlxxx[i][3]):
                            if str(listi[4]) == str(inlxxx[i][4]):
                                if str(listi[5]) == str(inlxxx[i][5]):
                                    if str(listi[6]) == str(inlxxx[i][6]):
                                        if str(listi[7]) == str(inlxxx[i][7]):
                                            if str(listi[8]) == str(inlxxx[i][8]):
                                                return i
                                        elif str(listi[7]) == '' and inlxxx[i][7] == 0:
                                            return i
                                    elif str(listi[6]) == '' and inlxxx[i][6] == 0:
                                            return i
                                elif str(listi[5]) == '' and inlxxx[i][5] == 0:
                                        return i
                            elif str(listi[4]) == '' and inlxxx[i][4] == 0:
                                    return i
                        elif str(listi[3]) == '' and inlxxx[i][3] == 0:
                            return i
                    elif str(listi[2]) == '' and inlxxx[i][2] == 0:
                        return i
                elif str(listi[1]) == '' and inlxxx[i][1] == 0:
                    return i
    except:
        return -1
    return -1
def get_summoner_name(jsondata,id):
    for data in jsondata:
        if str(data['id'])==id:
            return data['name']

def get_match_data_by_id(proxies,auth,jsond1,id,data,is_win):
    url = 'https://game-api.splinterlands.com/battle/result?id=' + id
    print(f'{bcolors.OKBLUE}{url}{bcolors.ENDC}')
    #jsondata = get_api_req(proxies,auth,url)]
    
    jsondata = json.loads(json.dumps(data))
#    print('end call')
    #try:
    atr = ''
    try: 
        atr = json.loads(jsondata['details'])['type']
    except:
        atr = '' 
    if atr != '':
        pass
    else:
        mana_cap = str(jsondata['mana_cap'])
        #summoner = get_summoner_name(jsond1,json.loads(jsondata['team'])['summoner'].split('-')[1])
        s = ''
        s = json.loads(json.dumps(json.loads(json.dumps(json.loads(jsondata['details'])['team1']))['summoner']))['uid']
#        print(s)
        summoner_id = s.split('-')[1]
        monsters = json.loads(json.dumps(json.loads(jsondata['details'])['team1']))['monsters']
        le = len(monsters)
        t1 = ''
        t2 = ''
        t3 = ''
        t4 = ''
        t5 = ''
        t6 = ''
        id1 = ''
        id2 = ''
        id3 = ''
        id4 = ''
        id5 = ''
        id6 = ''
        winnername = json.loads(json.dumps(json.loads(jsondata['details'])['team1']))['player']
        if le >= 1:
            #t1 = get_summoner_name(jsond1,json.loads(jsondata['team'])['monsters'][0].split('-')[1])
            #id1 = json.loads(jsondata['team'])['monsters'][0].split('-')[1]
            id1 = json.loads(json.dumps(json.loads(json.dumps(json.loads(jsondata['details'])['team1']))['monsters'][0]))['uid'].split('-')[1]
        if le >= 2:
            id2 = json.loads(json.dumps(json.loads(json.dumps(json.loads(jsondata['details'])['team1']))['monsters'][1]))['uid'].split('-')[1]
        if le >= 3:
            id3 = json.loads(json.dumps(json.loads(json.dumps(json.loads(jsondata['details'])['team1']))['monsters'][2]))['uid'].split('-')[1]
        if le >= 4:
            id4 = json.loads(json.dumps(json.loads(json.dumps(json.loads(jsondata['details'])['team1']))['monsters'][3]))['uid'].split('-')[1]
        if le >= 5:
            id5 = json.loads(json.dumps(json.loads(json.dumps(json.loads(jsondata['details'])['team1']))['monsters'][4]))['uid'].split('-')[1]
        if le >= 6:
            id6 = json.loads(json.dumps(json.loads(json.dumps(json.loads(jsondata['details'])['team1']))['monsters'][5]))['uid'].split('-')[1]
        ruleset = jsondata['ruleset']
        #ruleset = urllib.parse.quote(ruleset)
        #f = open("thanhdeptraivailon.csv", "a")
        #f.write(f'{mana_cap},{summoner},{t1},{t2},{t3},{t4},{t5},{t6}\n')
        #f.close()   
        i = -1
        i = find_index_in_list([mana_cap,summoner_id,id1,id2,id3,id4,id5,id6,ruleset,0,0,0])
        if winnername == jsondata['winner']:
            is_win = 1
        else:    
            is_win = 0
        if i < 0:
            if is_win == 1:
                final_list.append([mana_cap,summoner_id,id1,id2,id3,id4,id5,id6,ruleset,1,0,1])
            else:
                final_list.append([mana_cap,summoner_id,id1,id2,id3,id4,id5,id6,ruleset,0,1,1])
        else:
            if is_win == 1:
                final_list[i][9] = final_list[i][9] + 1
                final_list[i][11] = final_list[i][11] + 1
            else:
                final_list[i][10] = final_list[i][9] + 1
                final_list[i][11] = final_list[i][11] + 1                
#        print(f'{mana_cap},{summoner_id},{id1},{id2},{id3},{id4},{id5},{id6},{ruleset}\n')
        
        if summoner_id == '145' and id1== '412' and id2=='426' and id3 =='414':
            ftg = open('log_t.txt','w')
            ftg.write([mana_cap,summoner_id,id1,id2,id3,id4,id5,id6,ruleset,0,1,1])
            ftg.write('\n')
            ftg.write(id)
            ftg.write('\n-----------------')
            ftg.write(data)
            ftg.write('\n--End Record--')
            ftg.close()
            
        id1 = ''
        id2 = ''
        id3 = ''
        id4 = ''
        id5 = ''
        id6 = ''
        s = ''
        s = json.loads(json.dumps(json.loads(json.dumps(json.loads(jsondata['details'])['team2']))['summoner']))['uid']
#        print(s)
        summoner_id = s.split('-')[1]
        monsters2 = json.loads(json.dumps(json.loads(jsondata['details'])['team2']))['monsters']

        le = len(monsters2)
 
        if le >= 1:
            #t1 = get_summoner_name(jsond1,json.loads(jsondata['team'])['monsters'][0].split('-')[1])
            #id1 = json.loads(jsondata['team'])['monsters'][0].split('-')[1]
            id1 = json.loads(json.dumps(json.loads(json.dumps(json.loads(jsondata['details'])['team2']))['monsters'][0]))['uid'].split('-')[1]
        if le >= 2:
            id2 = json.loads(json.dumps(json.loads(json.dumps(json.loads(jsondata['details'])['team2']))['monsters'][1]))['uid'].split('-')[1]
        if le >= 3:
            id3 = json.loads(json.dumps(json.loads(json.dumps(json.loads(jsondata['details'])['team2']))['monsters'][2]))['uid'].split('-')[1]
        if le >= 4:
            id4 = json.loads(json.dumps(json.loads(json.dumps(json.loads(jsondata['details'])['team2']))['monsters'][3]))['uid'].split('-')[1]
        if le >= 5:
            id5 = json.loads(json.dumps(json.loads(json.dumps(json.loads(jsondata['details'])['team2']))['monsters'][4]))['uid'].split('-')[1]
        if le >= 6:
            id6 = json.loads(json.dumps(json.loads(json.dumps(json.loads(jsondata['details'])['team2']))['monsters'][5]))['uid'].split('-')[1]
        ruleset = jsondata['ruleset']
        #ruleset = urllib.parse.quote(ruleset)
        #f = open("thanhdeptraivailon.csv", "a")
        #f.write(f'{mana_cap},{summoner},{t1},{t2},{t3},{t4},{t5},{t6}\n')
        #f.close()   
        i = -1
        i = find_index_in_list([mana_cap,summoner_id,id1,id2,id3,id4,id5,id6,ruleset,0,0,0])
        if i < 0:
            if is_win == 0:
                final_list.append([mana_cap,summoner_id,id1,id2,id3,id4,id5,id6,ruleset,1,0,1])
            else:
                final_list.append([mana_cap,summoner_id,id1,id2,id3,id4,id5,id6,ruleset,0,1,1])
        else:
            if is_win == 0:
                final_list[i][9] = final_list[i][9] + 1
                final_list[i][11] = final_list[i][11] + 1
            else:
                final_list[i][10] = final_list[i][9] + 1
                final_list[i][11] = final_list[i][11] + 1                
#        print(f'{mana_cap},{summoner_id},{id1},{id2},{id3},{id4},{id5},{id6},{ruleset}\n')
    #except:
    #    print("Exception")
        

def get_api_req(proxies,auth,url):
    try:
        r = requests.get(url,proxies=proxies,auth=auth)
        return r.json()
    except:
        return None

def get_winner_maid(proxies,auth,jsond1,url,name,total_global,count_global,start_time):
    try:
        print(f'Starting collect {name}')
        url = url + name
        jsondata = get_api_req(proxies,auth,url)
        print(f'Completing request')
        count = 0
        for data in jsondata['battles']:
            count_global = count_global + 1
            count = count + 1
            print_status(proxies,auth,count_global,total_global,name,start_time)
#            print(str(count))
#            print(data['battle_queue_id_1'])
            un = data['battle_queue_id_1'][:5]
            un = 'bdb/'+un + '.txt'
            try:
                fxxx=open(un,'r')
            except:
                flag = 0
            flag = 0
            try:
                for dxxxx in fxxx:
                    dxxxx = dxxxx.replace('\n','')
                    if dxxxx == data['battle_queue_id_1']:
                        flag = 1
                        break
            except:
                flag = 0
            if flag == 1:
                slle = len(uaglobal)
                if slle == 0:
                    uaglobal.append(1)
                else:
                    uaglobal[0] = uaglobal[0] + 1
                print_status(proxies,auth,count_global,total_global,name,start_time)
            fxxx.close()
            if flag == 0:
                get_match_data_by_id(proxies,auth,jsond1,data['battle_queue_id_1'],data,1)
                try:
                    fxxx1 = open(un,'a')
                    sfxxx1 = data['battle_queue_id_1']
                    fxxx1.write(f'{sfxxx1}\n')
                    fxxx1.close()
                except:
                    fxxx1 = open(un,'w')
                    sfxxx1 = data['battle_queue_id_1']
                    fxxx1.write(f'{sfxxx1}\n')
                    fxxx1.close()
    except:
        print('Error occurred x')
    return count_global

def get_detail():
    url = 'https://game-api.splinterlands.com/cards/get_details'
    jsondata = get_api_req(url)
    return jsondata
    
def process_output(ofname):
    f = open(ofname, "w")
    f.write('[')
    fx = 1
    for x in final_list:
        if fx == 1:
            f.write('{')
            fx = fx + 1
        else:
            f.write(',{')
        f.write('"summoner_id":')
        ar = 0
        try:
            ar = int(str(x[1]))
        except:
            ar = 0
        f.write(f'{ar}')
        f.write(',')
        f.write('"monster_1_id":')
        ar = 0
        try:
            ar = int(str(x[2]))
        except:
            ar = 0
        f.write(f'{ar}')
        f.write(',')
        f.write('"monster_2_id":')
        ar = 0
        try:
            ar = int(str(x[3]))
        except:
            ar = 0
        f.write(f'{ar}')
        f.write(',')
        ar = 0
        try:
            ar = int(str(x[4]))
        except:
            ar = 0
        f.write('"monster_3_id":')
        f.write(f'{ar}')
        f.write(',')
        f.write('"monster_4_id":')
        ar = 0
        try:
            ar = int(str(x[5]))
        except:
            ar = 0
        f.write(f'{ar}')
        f.write(',')
        f.write('"monster_5_id":')
        ar = 0
        try:
            ar = int(str(x[6]))
        except:
            ar = 0
        f.write(f'{ar}')
        f.write(',')
        f.write('"monster_6_id":')
        ar = 0
        try:
            ar = int(str(x[7]))
        except:
            ar = 0
        f.write(f'{ar}')
        f.write(',')
        f.write('"ruleset":"')
        f.write(f'{x[8]}')
        f.write('",')
        f.write('"mana_cap":')
        f.write(f'{x[0]}')
        f.write(',')
        f.write('"tot":')
        f.write(f'{x[11]}')
        f.write(',')
        f.write('"ratio":')
        a = x[9] / x[11]
        f.write(f'{a}')
        f.write('}')
    f.write(']')
    f.close()
        
def sort_func(e):
    return e[8]
def sort_func2(e):
    return e[0]
def sort_func3(e):
    return e[9]*e[10]/100
def process_input_file():
    f=open("nick.txt", "r")
    count = 0
    for x in f:
        count = count + 1
    f.close()

    f2=open("nick.txt", "r")
    i = 0
    j = 1
    fname = "nick"+str(j) + ".txt"
    for y in f2:
        i = i + 1
        if i == 1:
            f3 = open(fname, "w")
        if i%100 != 0:
            f3.write(y)
        elif i%100 == 0:
            f3.write(y)
            f3.close()
            j = j+1
            fname = "nick"+str(j) + ".txt"
            f3 = open(fname, "w")
        elif i == count:
            f3.write(y)
            f3.close()
            
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


clear = lambda: os.system('cls')
clear()
url = 'https://game-api.splinterlands.com/battle/history?player='
i = 100
#jd1 = get_detail()
f = open("thanhdeptraivailon.csv", "w")
f.close()
f3 = open("thanhdeptraivailon.csv", "w")
f3.write("")
f3.close()
iop = len(sys.argv)
ufname = "nick.txt"
ofname = "thanhdeptraivailon.csv"
link =''
usr =''
pa = ''
if iop >2:
    ufname = sys.argv[1]
    ofname = sys.argv[2]
    link = sys.argv[3]
    usr = sys.argv[4]
    pa = sys.argv[5]

proxies = {"http":'103.90.229.230:9030'}
auth = HTTPProxyAuth('phamductrungit510', '6f50fd91f')

print(f'{ufname} {ofname}')
ofname = 'output/'+ofname
f1 = open(ufname, "r")
jd1 = []

print('Starting.../n')
start_time = time.time()
for tq in f1:
    total_global = total_global + 1
total_global = total_global * 50
print(f'Total: {f1}')
f1.close()
fe1 = open(ufname, "r")
for xy in fe1:
    xy = xy.replace('\n','')
    #if count_global % 100 == 0:
        #time.sleep(1)
    count_global = get_winner_maid(proxies,auth,jd1,url,xy,total_global,count_global,start_time)
    
fe1.close()
process_output(ofname)
final_list.sort(key=sort_func)
tmp_str = ''
myli = []
myli2 = []
lenfna = len( final_list )
i = 0
ola = ''
tmp_item8 = ''
for iconcac in final_list:
    print(iconcac)
for itemnnnn in range(len(final_list)):
    item = final_list[itemnnnn]
    i = i + 1
    ola = item[8].split('|')[0]
    if tmp_str == '':
        tmp_str = item[8]
        myli.append(item)
    else:
        if tmp_str == item[8]  and i != lenfna:
            myli.append(item)
            #do something
        else:
            if i == lenfna:
                myli.append(item)
            myli.sort(key=sort_func2)
            manax = ''
            myli2=[]
            lenconcac = len(myli)
            aconcac = 0
            for itemxxxxx in range(len(myli)):
                itemx = myli[itemxxxxx]
                aconcac = aconcac + 1
                if manax == '':
                    manax = itemx[0]
                    myli2.append(itemx)
                else:
                    if manax == itemx[0] and aconcac != lenconcac:
                        myli2.append(itemx)
                    else:
                        if aconcac == lenconcac:
                            myli2.append(itemx)
                        filename = 'result/'+tmp_str + manax + 'mana' + '.JSON'
                        filename = filename.replace(' ','')
                        filename = filename.replace('|','%7C')
                        try:
                            out_list=[]
                            try:
                                out_list = open_and_gen_list(filename)
                            except:
                                out_list = []
                            if out_list is None:
                                out_list = []
                            for xxuu in myli2:
                                flc = find_index_in_list2([xxuu[1],xxuu[2],xxuu[3],xxuu[4],xxuu[5],xxuu[6],xxuu[7],xxuu[8],xxuu[0]],out_list)
                                if flc < 0:
                                    rxxxx = xxuu[9] / xxuu[11] * 100
                                    out_list.append([xxuu[1],xxuu[2],xxuu[3],xxuu[4],xxuu[5],xxuu[6],xxuu[7],xxuu[8],xxuu[0],xxuu[11],rxxxx])
                                else:
                                    axxxx = out_list[flc][9]
                                    out_list[flc][9] = out_list[flc][9] + xxuu[11]
                                    out_list[flc][10] = (xxuu[9] + axxxx*out_list[flc][10]/100)/out_list[flc][9] * 100
                                    
                            f = open(filename, "w")
                            f.write('[')
                            fx = 1
                            out_list.sort(reverse=True,key=sort_func3)
                            print(out_list)
                            for x in out_list:
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
                                ar = 0
                                try:
                                    ar = int(str(x[3]))
                                except:
                                    ar = 0
                                f.write(',')
                                f.write('"monster_3_id":')
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
                                f.write('"ruleset":"')
                                f.write(f'{x[7]}')
                                f.write('",')
                                f.write('"mana_cap":')
                                f.write(f'{x[8]}')
                                f.write(',')
                                f.write('"tot":')
                                f.write(f'{x[9]}')
                                f.write(',')
                                f.write('"ratio":')
                                f.write(f'{x[10]}')
                                f.write('}')
                            f.write(']')
                            f.close()
                        except:
                            print(f'Error create file: {filename}')
                        myli2=[]
                        myli2.append(itemx)
                        manax = itemx[0]
                        
            myli = []
            myli.append(item)
            tmp_str = item[8]
time.sleep(120)
#print(final_list)
