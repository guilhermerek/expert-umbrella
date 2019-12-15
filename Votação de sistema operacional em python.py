#Desafio 3, grupo The Dogs
melhorOS = ['Windows Server', 'Unix', 'Linux', 'Netware', 'Mac OS', 'Outro']
a = 1
w = []
u = []
l = []
n = []
m = []
o = []
g = []
while(a != 0):
    a = int(input('Digite o número do sistema você acha melhor para servidores: Windows Server(1), Unix(2), Linux(3), Netware(4), Mac OS(5), ou outros(6):\n'))
    if(a == 1):
        w.append(a)
        g.append(a)
    if(a == 2):
        u.append(a)
        g.append(a)
    if(a == 3):
        l.append(a)
        g.append(a)
    if(a == 4):
        n.append(a)
        g.append(a)
    if(a == 5):
        m.append(a)
        g.append(a)
    if(a == 6):
        o.append(a)
        g.append(a)
y = len(g)
t = len(w)
porcentagem1 = (t*100)/y
i = len(u)
porcentagem2 = (i*100)/y
lin = len(l)
porcentagem3 = (lin*100)/y
net = len(n)
porcentagem4 = (net*100)/y
macos = len(m)
porcentagem5 = (macos*100)/y
ou = len(o)
porcentagem6 = (ou*100)/y
if(a == 0):
    print('='*50)
    print('Sistema Operacional         Votos      %')
    print('Windows Server                {}       {:.0f}%' .format(t, porcentagem1))
    print('Unix                          {}       {:.0f}%' .format(i, porcentagem2))
    print('Linux                         {}       {:.0f}%' .format(lin, porcentagem3))
    print('NetWare                       {}       {:.0f}%' .format(net, porcentagem4))
    print('Mac OS                        {}       {:.0f}%' .format(macos, porcentagem5))
    print('Outros                        {}       {:.0f}%' .format(ou, porcentagem6))
    print('='*50)
    print('Total                         {}' .format(y))
if(t > i) and (t > lin) and (t > net) and (t > macos) and (t > ou):
    print('O sistema mais votado foi o Windows Server, com {} votos, correspondendo a {:.0f}% dos votos.' .format(t, porcentagem1))
if(i > t) and (i > lin) and (i > net) and (i > macos) and (i > ou):
    print('O sistema mais votado foi o Unix, com {} votos, correspondendo a {:.0f}% dos votos.' .format(i, porcentagem2))
if(lin > t) and (lin > i) and (lin > net) and (lin > macos) and (lin > ou):
    print('O sistema mais votado foi o Linux, com {} votos, correspondendo a {:.0f}% dos votos.' .format(lin, porcentagem3))
if(net > t) and (net > i) and (net > lin) and (net > macos) and (net > ou):
    print('O sistema mais votado foi o NetWare, com {} votos, correspondendo a {:.0f}% dos votos.' .format(net, porcentagem4))
if(macos > t) and (macos > i) and (macos > lin) and (macos > net) and (macos > ou):
    print('O sistema mais votado foi o Mac OS, com {} votos, correspondendo a {:.0f}% dos votos.' .format(macos, porcentagem5))
if(ou > t) and (ou > i) and (ou > lin) and (ou > net) and (ou > macos):
    print('O sistema mais votado foi Outros, com {} votos, correspondendo a {:0.f}% dos votos.' .format(ou, porcentagem6))

#Desafio 3, grupo The Dogs
