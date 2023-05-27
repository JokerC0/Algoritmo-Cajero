p = 1
vt = 0

while p == 1:
	print("Ingrese el Codigo del Producto")
	cp = int(input());
	print("Ingrese el Nombre del Producto")
	np = input();
	print("Ingrese el Valor del Producto")
	vp = int(input());
	print("Ingrese la Cantidad del Producto")
	cap = int(input());

	vtp = vp * cap
	vt = vt + vtp

	print("Cantidad",cap,"Detalle",cp,"-",np," Valor $",vtp)

	print("Ingresar Mas Productos SI/NO")
	mp = input();

	if mp != "si":
		p = 0

iva = vt * 0.19
total = vt + iva

print("Subtotal $",vt,"  IVA $",iva,"  Total Venta $",total)




