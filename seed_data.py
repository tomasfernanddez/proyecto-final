from ejemplo.models import Familiar
Familiar(nombre="Rosario", direccion="Rio Parana 745", fecha="2001-12-01",numero_pasaporte=123123).save()
Familiar(nombre="Alberto", direccion="Rio Parana 745", fecha="1993-03-15",numero_pasaporte=890890).save()
Familiar(nombre="Samuel", direccion="Rio Parana 745", fecha="1998-01-29",numero_pasaporte=345345).save()
Familiar(nombre="Florencia", direccion="Rio Parana 745", fecha="1996-07-19", numero_pasaporte=567567).save()
print("Se cargó con éxito los usuarios de pruebas")


from ejemplo.models import Auto
Auto(marca="Fiat", modelo="Palio", color="Negro",patente="OBF 809").save()
Auto(marca="Peugeot", modelo="207", color="Gris",patente="JGF 452").save()
Auto(marca="Renault", modelo="Clio", color="Azul",patente="PGR 134").save()
Auto(marca="Volkswagen", modelo="Golf", color="Blanco", patente="HTF 535").save()
print("Se cargó con éxito los autos de pruebas")


from ejemplo.models import Mascota
Mascota(nombre="Luca", animal="Gato", raza="Bulldog", fecha="2010-07-14").save()
Mascota(nombre="Romeo", animal="Perro", raza="Golden", fecha="2015-03-25").save()
Mascota(nombre="Moria", animal="Perro", raza="Border Collie", fecha="2018-09-30").save()
Mascota(nombre="Branca", animal="Perro", raza="Labrador", fecha="2013-01-07").save()
print("Se cargó con éxito las mascotas de pruebas")