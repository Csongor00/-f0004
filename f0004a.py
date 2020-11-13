név = input('Hogy híjják kendet? ')
kor = input('És hány éves kend? ') 

kor = int(kor) 
ev = input ('Melyik evben vagyunk?')
ev = int(ev)

születési_év = ev - kor
print(név, ', kend ', születési_év, '-ban született.', sep='')