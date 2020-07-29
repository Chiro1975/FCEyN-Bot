from pony.orm import *
from base import *


def completarBaseFisica():
	with db_session:
		ListableFisica(name = 'Cálculo Numérico', url = 'https://t.me/calculonumericodmuba', validated = True)
		ListableFisica(name = 'Estructura I', url = 'https://t.me/joinchat/DLkiixik89S1AEHqcte-0Q', validated = True)
		ListableFisica(name = 'Estructura II', url = 'https://t.me/joinchat/DLkiixhS7BjCchvX-n6Pvw', validated = True)
		ListableFisica(name = 'Estructura III', url = 'https://t.me/estructura_3_fcen', validated = True)
		ListableFisica(name = 'Estructura IV', url = 'https://t.me/joinchat/DLkiixstK37Sq0gPhkrUkA', validated = True)
		ListableFisica(name = 'Física I', url = 'https://t.me/joinchat/DLkiixtQ6Yby3S-7UD7b5g', validated = True)
		ListableFisica(name = 'Física II', url = 'https://t.me/joinchat/DLkiix1oOS_ZOnH_ZpsALg', validated = True)
		ListableFisica(name = 'Física III', url = 'https://t.me/joinchat/DLkiixwqxDuOk248htozWA', validated = True)
		ListableFisica(name = 'Física IV', url = 'https://t.me/joinchat/DLkiixs2n2cAkiIeU8GfrA', validated = True)
		ListableFisica(name = 'Física Teorica I', url = 'https://t.me/joinchat/DLkiixlnkgji_Nf4AgjA9w', validated = True)
		ListableFisica(name = 'Física Teorica II', url = 'https://t.me/joinchat/DLkiixoKsP4yZCMkjv3ocg', validated = True)
		ListableFisica(name = 'Física Teorica III', url = 'https://t.me/joinchat/DLkiixYJHg1er5aEJwmpkA', validated = True)
		ListableFisica(name = 'Mecánica Clásica', url = 'https://t.me/joinchat/M4tMXxdABT3hJ7jueIDbhQ', validated = True)
		ListableFisica(name = 'Matemática I', url = 'https://t.me/joinchat/CDIKsEEaeLEy37CL0CuyrA', validated = True)
		ListableFisica(name = 'Matemática II', url = 'https://t.me/joinchat/DLkiixo4ZdBrw0VFHkjDfQ', validated = True)
		ListableFisica(name = 'Matemática III', url = 'https://t.me/joinchat/D_PY9Q0AkO9ej2BZdRn6tw', validated = True)
		ListableFisica(name = 'Matemática IV', url = 'https://t.me/joinchat/DLkiixoDdGXh3drs0cfA_A', validated = True)

def completarBaseMatematica():
	with db_session:
		ListableMatematica(name = 'Álgebra I', url = 'https://t.me/algebra1dmuba', validated = True)	
		ListableMatematica(name = 'Álgebra II', url = 'https://t.me/algebra2dmuba', validated = True)
		ListableMatematica(name = 'Álgebra III', url = 'https://t.me/algebra3dmuba', validated = True)	
		ListableMatematica(name = 'Análisis I', url = 'https://t.me/joinchat/CDIKsEEaeLEy37CL0CuyrA', validated = True)
		ListableMatematica(name = 'Análisis II', url = 'https://t.me/joinchat/D_PY9Q0AkO9ej2BZdRn6tw', validated = True)
		ListableMatematica(name = 'Análisis Complejo', url = 'https://t.me/joinchat/GXS9AFCPbh7lkMNAJkpk7g', validated = True)
		ListableMatematica(name = 'Análisis Funcional', url = 'https://t.me/joinchat/GXS9AFcKDu6_Bz0YIN65Vg', validated = True)
		ListableMatematica(name = 'Análisis Real', url = 'https://t.me/joinchat/GXS9AFh0uX2mUf8VKYAJUQ', validated = True)
		ListableMatematica(name = 'Cálculo Avanzado', url = 'https://t.me/calculoAvanzadoDMUBA', validated = True)
		ListableMatematica(name = 'Cálculo Numérico', url = 'https://t.me/calculonumericodmuba', validated = True)
		ListableMatematica(name = 'Ecuac. Diferenciales A', url = 'https://t.me/joinchat/GXS9AEThY70jvGB9Oky2SA', validated = True)
		ListableMatematica(name = 'Estadística', url = 'https://t.me/joinchat/FElywR2BZ84GO6nm5VqiCg', validated = True)
		ListableMatematica(name = 'Geo. Diferencial', url = 'https://t.me/joinchat/GXS9AFY0j5_wXkzHXzfe6w', validated = True)
		ListableMatematica(name = 'Geo. Proyectiva', url = 'https://t.me/joinchat/GXS9AFKnPu4yojO0Nh4GKA', validated = True)
		ListableMatematica(name = 'Intro Computación', url = 'https://t.me/joinchat/TQ492hhckDzc_1cyBdGBWw', validated = True)
		ListableMatematica(name = 'Inv. Operativa', url = 'https://t.me/joinchat/COqYnxREy2zSnRPPCQ2ctQ', validated = True)
		ListableMatematica(name = 'Lineal', url = 'https://t.me/joinchat/DZ8z20GkCEtgfUUnAmLqHw', validated = True)
		ListableMatematica(name = 'Proba', url = 'https://t.me/probadmuba', validated = True)
		ListableMatematica(name = 'Taller CA', url = 'https://t.me/TCAvanzado', validated = True)
		ListableMatematica(name = 'Topología', url = 'https://t.me/joinchat/GXS9AFdT3IzHkio9kwf1aQ', validated = True)

def completarOptativas():
	with db_session:
		ListableMatematicaOptativa(name = 'Conmutativa', url = 'https://t.me/joinchat/G3ibBxxLvFSx69_R2D0X2Q', validated = True)
		ListableMatematicaOptativa(name = 'Algo I', url = 'https://t.me/joinchat/DS9ZukBsXL9pRalZw2aDJA', validated = True)
		ListableMatematicaOptativa(name = 'Algo II', url = 'https://t.me/joinchat/CDIKsEB0p9PpZUXArQ2xvQ', validated = True)
		ListableMatematicaOptativa(name = 'Algo III', url = 'https://t.me/joinchat/CDIKsD_KzUT77NodKvmeiw', validated = True)
		ListableMatematicaOptativa(name = 'Geometría', url = 'https://t.me/joinchat/M4tMXxEvd5OdXjRGFrfxjg', validated = True)
		ListableMatematicaOptativa(name = 'Mecánica Clásica', url = 'https://t.me/joinchat/M4tMXxdABT3hJ7jueIDbhQ', validated = True)
		ListableMatematicaOptativa(name = 'Métodos', url = 'https://t.me/joinchat/DUhF70JyiUKf33_5wHz3mQ', validated = True)
		ListableMatematicaOptativa(name = 'Lógica', url = 'https://t.me/joinchat/Cjh7_EHiOJWqyIbsEgyc8A', validated = True)