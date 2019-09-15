# MyDiPy Version 1.2.1
from colorama import init, Back, Fore, Style

init()


def change(f):
    # Open file:
    global r
    def_st = []
    def_g = []
    def_di = {}
    def_th = ''
    def_an = ''
    # Codes:
    sp_key = 0
    for u in r:
        if u == '#@*?#':
            sp_key = 1
            continue
        if sp_key == 1:
            def_st.append(u)
            sp_key = 0
    # Theme and Storage's:
    def_block = 0
    def_globally = 0
    sp_key = 1
    for u in r:
        if u == '#@*?#' and def_globally == 1:
            def_g.append(def_di)
            def_di = {}
            sp_key = 1
            def_globally = 0
        if u == '#@*?#':
            def_block = 1
            continue
        if def_block == 1:
            def_block = 0
            def_globally = 1
            continue
        if u == '#&:%#' and sp_key == 0:
            sp_key = 1
            continue
        if u == '#&:%#' and sp_key == 1:
            sp_key = 0
            if def_th != '':
                def_di[def_th] = def_an
            def_th = ''
            def_an = ''
            continue
        if u != '#@*?#' and sp_key == 0:
            def_th += u + ' '
        if u != '#@*?#' and sp_key == 1:
            def_an += u + ' '
    # Zip:
    def_gd = dict(zip(def_st, def_g))
    # Function:
    for u in def_gd.keys():
        if f == str(u):
            storage = def_gd[u]
            return storage


# Open file:
with open('Content.txt', encoding='utf-8') as bili:
    r = bili.read().strip().split(' ')
st = []
g = []
di = {}
th = ''
an = ''
gn = []
# Global theme:
key1 = 0
for i in r:
    if i == '#^~$#':
        key1 = 1
        continue
    if key1 == 1:
        gn.append(i)
        key1 = 0
# Codes:
key = 0
block1 = 0
for i in r:
    if i == '#^~$#':
        block1 = 1
        continue
    if block1 == 1:
        block1 = 0
        continue
    if i == '#@*?#':
        key = 1
        continue
    if key == 1:
        st.append(i)
        key = 0
# Theme and Storage's:
block = 0
block2 = 0
glob_block = 0
key = 1
for i in r:
    if i == '#^~$#':
        block2 = 1
        continue
    if block2 == 1:
        block2 = 0
        continue
    if i == '#@*?#' and glob_block == 1:
        g.append(di)
        di = {}
        key = 1
        glob_block = 0
    if i == '#@*?#':
        block = 1
        continue
    if block == 1:
        block = 0
        glob_block = 1
        continue
    if i == '#&:%#' and key == 0:
        key = 1
        continue
    if i == '#&:%#' and key == 1:
        key = 0
        if th != '':
            di[th] = an
        th = ''
        an = ''
        continue
    if i != '#@*?#' and key == 0:
        th += i + ' '
    if i != '#@*?#' and key == 1:
        an += i + ' '
# Zip:
gd = dict(zip(st, g))
ggn = dict(zip(st, gn))
F = str(st[0])  # Default theme
memory = F
d = change(F)
key = 0
k = 0
# Result:
while True:
    if key == 1:
        print(Back.RED + '>Exit? y / n' + Back.RESET)
        ex = input()
        if ex.lower() == 'y':
            break
    while True:
        print(Back.GREEN + 'Themes:' + Back.RESET)
        for i in d:  # print themes
            print(Back.RESET + Fore.GREEN + i.strip() + Fore.RESET, Fore.RED + '#####' + Fore.RESET, end=' ')
        print()
        for i in ggn.keys():  # print codes
            if memory != str(i):
                print(Fore.BLUE + '>To open the', ggn[i], ', enter the code:', Fore.YELLOW + i + Fore.RESET)
        F = input()  # >press F for respect
        k = 0
        for i in st:
            if F == str(i):
                memory = F
                d = change(F)
                k = 1
        if k == 1:
            continue
        s = []
        result = []
        resultT = []
        for i in d.values():  # text search from the source 'd'
            s.append(i)  # form 'd' to 's'
        for i in s:  # text search from the source 's'
            if i.lower().strip().find(F.lower()) != -1:
                result.append(i)
        for i in d.keys():  # theme search from the source 'd'
            if i.lower().strip() == F.lower().strip():
                resultT.append(d[i])
        if not result and not resultT:  # not found
            print(Style.BRIGHT + '[not found]' + Style.RESET_ALL)
        else:
            for i in set(result):  # text search
                if i not in resultT:
                    print(Back.YELLOW + '-------------------------------------THEME'
                                        '-------------------------------------' + Back.RESET + i)
            for i in set(resultT):  # theme search
                print(Back.LIGHTGREEN_EX + '-------------------------------------THEME'
                                           '-------------------------------------' + Back.RESET + i)
        key = 1
        break
# © This is free software; There are NO warranties; The program is NOT intended for SALES.
