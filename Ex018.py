from math import cos, tan, sin, radians
a = float(input('Coloque o ângulo:'))
r = radians(a)
c = cos(r)
s = sin(r)
t = tan(r)
print('O seu cosseno é {:.2f} \nO seu seno é {:.2f}\nE sua tangente é {:.2f}'.format(c, s, t))
