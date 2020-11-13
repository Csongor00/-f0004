nev = input('Hogy hijjak kendet? ')
kor = input('Es hany eves kend? ') 

kor = int(kor) 
ev = input('Melyik evben jarunk? ')
ev = int(ev)

szuletesi_ev = ev - kor

print(nev, ', kend ', szuletesi_ev, '-ban szuletett.', sep='')

erettsegi_ev = szuletesi_ev + 18

print(nev, ', kend ', erettsegi_ev, '-ban erettsegizik.', sep='')