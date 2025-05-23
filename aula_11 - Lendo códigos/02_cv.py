
d = float(input("Informe a distancia desejada: "))
v = float(input("Informe a velocidade media: "))
t = d / v

t_str = str(int(t))+'h'

t_frac = t - int(t)

if 0.0 <= t_frac <= 0.25:
	t_str += '15m'
elif 0.25 < t_frac <= 0.50:
	t_str += '30m'
elif 0.50 < t_frac <= 0.75:
	t_str += '45m'
elif 0.75 < t_frac <= 1.0:
	t_str = str(int(t)+1)+'h'

c = 12.5

if v <= 60:
	c = 14.2
elif 60 <= v < 80:
	c = 13.8
elif 80 <= v < 93:
	c = 12.5
elif 93 <= v < 110:
	c = 11.3
elif v >= 110:
	c = 10.1		

l = d / c
print(f"Para percorrer {d:.2f}km com velocidade {v:.2f}km/h você leverá aproximadamente {t_str} e consumirá {l:.2f}L de combustível...")
