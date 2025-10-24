# script.rpy - CLUE MEDIEVAL (version pistas)

define narrator = Character(None, kind=nvl)

# PERSONAJES
define e = Character("Espadachin")
define c = Character("Curandero")
define k = Character("Cocinero")
define b = Character("Bibliotecaria")
define j = Character("Bufon")

# VARIABLES
default culpable = ""
default arma = ""
default lugar = ""
default historia = 0
default historia_activa = None
default eleccion_personaje = ""
default eleccion_arma = ""
default eleccion_lugar = ""
default pistas_por_visitar = []
default lugar_actual = ""

init python:
    import random
    import renpy

    personajes = ["Espadachin", "Curandero", "Cocinero", "Bibliotecaria", "Bufon"]
    armas = ["Espada", "Veneno", "Cuchillo de Carnicero", "Conjuro de Muerte", "Daga del Dragon"]
    lugares = ["Cuarto del Rey", "Cocina Real", "Biblioteca", "Pasillo del Castillo", "Laboratorio"]

    personajes_obj = {
        "Espadachin": e,
        "Curandero": c,
        "Cocinero": k,
        "Bibliotecaria": b,
        "Bufon": j,
    }

    olor_por_arma = {
        "Espada": "El olor a sangre llena el lugar.",
        "Veneno": "El olor a magia llena el lugar.",
        "Cuchillo de Carnicero": "El olor a sangre llena el lugar.",
        "Conjuro de Muerte": "El olor a magia llena el lugar.",
        "Daga del Dragon": "El olor a sangre y magia llena el lugar.",
    }

    rastro_por_arma = {
        "Espada": "Hay MUCHA sangre esparcida por el suelo.",
        "Veneno": "Hay una intensa presencia de MAGIA en el aire.",
        "Cuchillo de Carnicero": "Solo un poco de sangre seca en el suelo.",
        "Conjuro de Muerte": "Apenas un debil rastro magico flota en el ambiente.",
        "Daga del Dragon": "Hay rastros leves de sangre y magia a la vez.",
    }

    historias = [
        {
            "id": 1,
            "titulo": "Sombras en el Pasillo",
            "culpable": "Bufon",
            "arma": "Daga del Dragon",
            "lugar": "Pasillo del Castillo",
            "introduccion": "Los ecos de risas falsas aun resuenan en el pasillo donde callo el rey.",
            "resolucion": [
                "El Bufon trato de ocultar sus huellas tras bromas y disfraces, pero la mezcla de sangre y magia lo traiciono.",
                "Cuando los guardias lo enfrentaron, confeso haber usado la Daga del Dragon en el Pasillo del Castillo.",
                "Juraba proteger al rey con espectaculos, pero la codicia lo llevo a apunalarlo a traicion.",
            ],
            "pistas": {
                "Cuarto del Rey": {
                    "personaje": "Espadachin",
                    "descripcion": [
                        "Las cortinas pesadas del cuarto del rey apenas se mueven.",
                        "El Espadachin permanece alerta junto a la puerta.",
                    ],
                    "asesino_visto": True,
                    "dialogo_extra": [
                        "No entiendo esos trucos de magia, pero el bufon salio de su sala con una mirada extrana.",
                        "Si quieres saberlo, ese filo olia a humo y escamas.",
                    ],
                },
                "Cocina Real": {
                    "personaje": "Cocinero",
                    "descripcion": [
                        "Los calderos hierven y el aroma de hierbas llena el ambiente.",
                    ],
                    "dialogo_extra": [
                        "No me muevo de la cocina. El bufon vino a pedir vino y se fue escondiendo algo en la manga.",
                    ],
                },
                "Biblioteca": {
                    "personaje": "Bibliotecaria",
                    "descripcion": [
                        "Los estantes vibran con susurros magicos y paginas que se pasan solas.",
                    ],
                    "arma_en_sala": True,
                    "dialogo_extra": [
                        "La hoja que vi llevaba runas de dragon. Solo alguien que combina armas y magia usaria eso.",
                    ],
                },
                "Pasillo del Castillo": {
                    "descripcion": [
                        "Antorchas parpadean y en el suelo quedan destellos rojizos y violetas.",
                        "Un silencio tenso recorre el corredor real.",
                    ],
                    "es_escena": True,
                },
                "Laboratorio": {
                    "personaje": "Curandero",
                    "descripcion": [
                        "Frascos brillan con brebajes que burbujean suavemente.",
                    ],
                    "dialogo_extra": [
                        "Detecte un rastro tenue de magia mezclada con sangre. Solo el bufon sabe ocultar algo asi.",
                    ],
                },
            },
        },
        {
            "id": 2,
            "titulo": "Susurros entre los Tomos",
            "culpable": "Bibliotecaria",
            "arma": "Conjuro de Muerte",
            "lugar": "Biblioteca",
            "introduccion": "Los tomos prohibidos de la biblioteca destellan con una luz prohibida tras la muerte del rey.",
            "resolucion": [
                "La Bibliotecaria habia memorizado un Conjuro de Muerte oculto en los libros sellados.",
                "Desde la Biblioteca lanzo la sentencia contra el rey, envolviendo la sala en magia oscura.",
                "Juro que era para proteger el conocimiento del reino, pero la justicia la alcanzo entre los estantes.",
            ],
            "pistas": {
                "Cuarto del Rey": {
                    "personaje": "Espadachin",
                    "descripcion": [
                        "Las armaduras alineadas reflejan destellos verdosos de energia.",
                    ],
                    "dialogo_extra": [
                        "No vi sangre, solo chispas de magia que salian del corredor rumbo a la biblioteca.",
                    ],
                },
                "Cocina Real": {
                    "personaje": "Cocinero",
                    "descripcion": [
                        "Cuchillos impecables reposan en su lugar habitual.",
                    ],
                    "dialogo_extra": [
                        "La bibliotecaria me pidio hierbas para un ritual y no solto sus libros en toda la noche.",
                    ],
                },
                "Biblioteca": {
                    "personaje": "Bibliotecaria",
                    "descripcion": [
                        "Las velas azules chisporrotean con fuerza peligrosa.",
                    ],
                    "es_escena": True,
                    "arma_en_sala": True,
                    "dialogo_extra": [
                        "El conjuro resonaba en mi cabeza... digo, en la de alguien mas. Fue una noche muy larga.",
                    ],
                },
                "Pasillo del Castillo": {
                    "personaje": "Bufon",
                    "descripcion": [
                        "Confeti marchito cubre algunas losas del piso.",
                    ],
                    "asesino_visto": True,
                    "dialogo_extra": [
                        "La bibliotecaria casi nunca deja sus libros, pero la vi deslizarse por aqui murmurando palabras oscuras.",
                    ],
                },
                "Laboratorio": {
                    "personaje": "Curandero",
                    "descripcion": [
                        "Circulos arcanos brillan sobre las mesas de piedra.",
                    ],
                    "dialogo_extra": [
                        "Esa noche senti un torrente de magia que no era mio. Venia directo desde la biblioteca.",
                    ],
                },
            },
        },
        {
            "id": 3,
            "titulo": "Honor Fracturado",
            "culpable": "Espadachin",
            "arma": "Espada",
            "lugar": "Cuarto del Rey",
            "introduccion": "El Espadachin juro proteger al monarca, pero ahora su espada yace manchada junto al trono.",
            "resolucion": [
                "El Espadachin afirmo actuar por el bien del reino, pero la sangre del rey cubria su Espada.",
                "En el Cuarto del Rey libero toda su furia tras descubrir secretos que no pudo soportar.",
                "Su honor se quebranto, y el consejo lo condeno al destierro eterno.",
            ],
            "pistas": {
                "Cuarto del Rey": {
                    "personaje": "Espadachin",
                    "descripcion": [
                        "El trono aun esta cubierto por un manto de seda rasgado.",
                    ],
                    "es_escena": True,
                    "arma_en_sala": True,
                    "dialogo_extra": [
                        "Juro que vi una sombra blandir mi espada... No fui yo, lo prometo.",
                    ],
                },
                "Cocina Real": {
                    "personaje": "Cocinero",
                    "descripcion": [
                        "Hay manchas de armadura pulida en la mesa principal.",
                    ],
                    "dialogo_extra": [
                        "El espadachin vino por un filete crudo para entrenar golpes. Parecia fuera de si.",
                    ],
                },
                "Biblioteca": {
                    "personaje": "Bibliotecaria",
                    "descripcion": [
                        "Un libro de tacticas militares esta abierto sobre el atril.",
                    ],
                    "dialogo_extra": [
                        "El resonar de una espada me desperto. Ninguna magia, solo acero decidido.",
                    ],
                },
                "Pasillo del Castillo": {
                    "personaje": "Bufon",
                    "descripcion": [
                        "Un rastro de sangre se pierde entre columnas adornadas.",
                    ],
                    "arma_en_sala": True,
                    "dialogo_extra": [
                        "Me parece que vi a alguien usar Espada pero no estoy seguro de eso.",
                        "Y entre nos, el espadachin corria con el casco en la mano lejos de sus guardias.",
                    ],
                },
                "Laboratorio": {
                    "personaje": "Curandero",
                    "descripcion": [
                        "Bandas de tela y pociones sanadoras reposan listas.",
                    ],
                    "asesino_visto": True,
                    "dialogo_extra": [
                        "No manejo armas, pero vi al espadachin salir del cuarto del rey cubierto de sangre.",
                    ],
                },
            },
        },
        {
            "id": 4,
            "titulo": "Antidoto Fallido",
            "culpable": "Curandero",
            "arma": "Veneno",
            "lugar": "Laboratorio",
            "introduccion": "El laboratorio del curandero se impregna de aromas toxicos tras la caida del rey.",
            "resolucion": [
                "El Curandero mezclo un Veneno devastador diciendo que seria un remedio para el dolor del rey.",
                "Lo administro en el Laboratorio y dejo que la magia hiciera el resto.",
                "Su juramento de sanar se corrompio, y ahora enfrenta las consecuencias.",
            ],
            "pistas": {
                "Cuarto del Rey": {
                    "personaje": "Espadachin",
                    "descripcion": [
                        "El aire aqui se siente limpio, sin rastro de sangre.",
                    ],
                    "dialogo_extra": [
                        "No vi armas aqui. Solo frascos que el curandero llevaba y traia como si ocultara algo.",
                    ],
                },
                "Cocina Real": {
                    "personaje": "Cocinero",
                    "descripcion": [
                        "Hiervas secas y especias estan perfectamente alineadas.",
                    ],
                    "dialogo_extra": [
                        "El curandero me pidio hierbas raras y dijo que eran para una cura urgente.",
                    ],
                },
                "Biblioteca": {
                    "personaje": "Bibliotecaria",
                    "descripcion": [
                        "Un manuscrito sobre antitoxinas queda abierto en la mesa lateral.",
                    ],
                    "dialogo_extra": [
                        "Reviso tratados de venenos toda la noche. Ningun hechizo, solo formulas peligrosas.",
                    ],
                },
                "Pasillo del Castillo": {
                    "personaje": "Bufon",
                    "descripcion": [
                        "El eco de pasos apresurados resuena en las paredes.",
                    ],
                    "asesino_visto": True,
                    "dialogo_extra": [
                        "Me parece que vi a Curandero fuera de su lugar de trabajo, solo no digas nada de eso.",
                        "Olvidaba cerrar las puertas del laboratorio cuando corria hacia la camara del rey.",
                    ],
                },
                "Laboratorio": {
                    "personaje": "Curandero",
                    "descripcion": [
                        "Calderos de cristal destellan con vapores violetas.",
                    ],
                    "es_escena": True,
                    "arma_en_sala": True,
                    "dialogo_extra": [
                        "Preparaba un remedio... pero alguien debio mezclar demasiada magia en el veneno.",
                    ],
                },
            },
        },
        {
            "id": 5,
            "titulo": "Sabor a Traicion",
            "culpable": "Cocinero",
            "arma": "Cuchillo de Carnicero",
            "lugar": "Cocina Real",
            "introduccion": "La Cocina Real huele a especias, pero una nota metalica delata un crimen impensable.",
            "resolucion": [
                "El Cocinero oculto el Cuchillo de Carnicero entre sus utensilios favoritos.",
                "En la Cocina Real espero al rey para servirle y acabo con su vida con un corte certero.",
                "Juro que era para proteger una conspiracion culinaria, pero nadie le creyo.",
            ],
            "pistas": {
                "Cuarto del Rey": {
                    "personaje": "Espadachin",
                    "descripcion": [
                        "El suelo esta impecable, sin rastro de magia.",
                    ],
                    "asesino_visto": True,
                    "dialogo_extra": [
                        "Me parece que vi a Cocinero fuera de su lugar de trabajo, solo no digas nada de eso.",
                        "Venia con un cuchillo envuelto en tela rumbo a la cocina.",
                    ],
                },
                "Cocina Real": {
                    "personaje": "Cocinero",
                    "descripcion": [
                        "La mesa principal tiene una muesca nueva impregnada de sangre.",
                    ],
                    "es_escena": True,
                    "arma_en_sala": True,
                    "dialogo_extra": [
                        "Era solo para cortar carne... No se como termino asi.",
                    ],
                },
                "Biblioteca": {
                    "personaje": "Bibliotecaria",
                    "descripcion": [
                        "Recetas antiguas y libros de etiqueta culinaria estan desordenados.",
                    ],
                    "dialogo_extra": [
                        "El cocinero nunca busca hechizos, solo recetas. Pero hoy dejo grasa sobre mis manuscritos.",
                    ],
                },
                "Pasillo del Castillo": {
                    "personaje": "Bufon",
                    "descripcion": [
                        "Se escuchan risas nerviosas a lo lejos.",
                    ],
                    "dialogo_extra": [
                        "El olor a sangre es debil, pero sigue el camino hasta la cocina.",
                    ],
                },
                "Laboratorio": {
                    "personaje": "Curandero",
                    "descripcion": [
                        "Una mesa auxiliar tiene manchas frescas limpiadas a la prisa.",
                    ],
                    "arma_en_sala": True,
                    "dialogo_extra": [
                        "Me parece que vi a alguien usar Cuchillo de Carnicero pero no estoy seguro de eso.",
                        "Solo se que no fui yo; no se manejar armas.",
                    ],
                },
            },
        },
    ]

    def seleccionar_historia():
        global historia_activa, culpable, arma, lugar, historia, pistas_por_visitar
        historia_activa = random.choice(historias)
        culpable = historia_activa["culpable"]
        arma = historia_activa["arma"]
        lugar = historia_activa["lugar"]
        historia = historia_activa["id"]
        pistas_por_visitar = list(lugares)

    def narrar_lineas(lineas):
        for linea in lineas:
            renpy.say(narrator, linea)

    def hablar_lineas(hablante, lineas):
        for linea in lineas:
            hablante(linea)

# INICIO
label start:
    scene black
    with fade

    narrator "Bienvenido al CLUE MEDIEVAL."
    narrator "Un terrible crimen ha ocurrido dentro del castillo real..."
    narrator "Tu deber es descubrir al culpable antes del amanecer."

    $ seleccionar_historia()

    narrator "Los guardias encontraron rastros extranos en la escena del crimen."
    narrator rastro_por_arma[arma]
    narrator "El crimen ocurrio en el [lugar]."
    narrator historia_activa["introduccion"]

    narrator "Cinco sospechosos fueron llamados ante el consejo real:"
    narrator "Espadachin, Curandero, Cocinero, Bibliotecaria y Bufon"
    pause 1

    narrator "Observa las pistas y trata de deducir quien, con que arma y donde cometio el crimen."
    jump explorar_castillo

label explorar_castillo:
    if len(pistas_por_visitar) == 0:
        narrator "Has reunido todas las pistas disponibles en el castillo."
        jump elige_personaje

    "Donde quieres investigar ahora?"
    menu:
        "Cuarto del Rey" if "Cuarto del Rey" in pistas_por_visitar:
            $ lugar_actual = "Cuarto del Rey"
            $ pistas_por_visitar.remove(lugar_actual)
            jump mostrar_pista
        "Cocina Real" if "Cocina Real" in pistas_por_visitar:
            $ lugar_actual = "Cocina Real"
            $ pistas_por_visitar.remove(lugar_actual)
            jump mostrar_pista
        "Biblioteca" if "Biblioteca" in pistas_por_visitar:
            $ lugar_actual = "Biblioteca"
            $ pistas_por_visitar.remove(lugar_actual)
            jump mostrar_pista
        "Pasillo del Castillo" if "Pasillo del Castillo" in pistas_por_visitar:
            $ lugar_actual = "Pasillo del Castillo"
            $ pistas_por_visitar.remove(lugar_actual)
            jump mostrar_pista
        "Laboratorio" if "Laboratorio" in pistas_por_visitar:
            $ lugar_actual = "Laboratorio"
            $ pistas_por_visitar.remove(lugar_actual)
            jump mostrar_pista

label mostrar_pista:
    $ pista_actual = historia_activa["pistas"][lugar_actual]

    narrator "Te diriges a [lugar_actual]."

    $ descripcion = pista_actual.get("descripcion", [])
    python:
        narrar_lineas(descripcion)

    if pista_actual.get("es_escena"):
        narrator olor_por_arma[arma]

    if pista_actual.get("personaje"):
        $ hablante = personajes_obj[pista_actual["personaje"]]
        if pista_actual.get("arma_en_sala"):
            $ hablante("Me parece que vi a alguien usar [arma] pero no estoy seguro de eso.")
        if pista_actual.get("asesino_visto"):
            $ hablante("Me parece que vi a [culpable] fuera de su lugar de trabajo, solo no digas nada de eso.")
        $ hablar_lineas(hablante, pista_actual.get("dialogo_extra", []))

    narrator "Anotas las pistas y decides continuar investigando."
    jump explorar_castillo

# MENU 1: ELEGIR PERSONAJE
label elige_personaje:
    "Quien crees que es el culpable?"
    menu:
        "Espadachin" :
            $ eleccion_personaje ="Espadachin"
            jump elige_arma
        "Curandero" :
            $ eleccion_personaje ="Curandero"
            jump elige_arma
        "Cocinero" :
            $ eleccion_personaje = "Cocinero"
            jump elige_arma
        "Bibliotecaria":
            $ eleccion_personaje = "Bibliotecaria"
            jump elige_arma
        "Bufon":
            $ eleccion_personaje = "Bufon"
            jump elige_arma

# MENU 2: ELEGIR ARMA
label elige_arma:
    "Que arma crees que uso?"
    menu:
        "Espada":
            $ eleccion_arma = "Espada"
            jump elige_lugar
        "Veneno":
            $ eleccion_arma = "Veneno"
            jump elige_lugar
        "Cuchillo de Carnicero":
            $ eleccion_arma = "Cuchillo de Carnicero"
            jump elige_lugar
        "Conjuro de Muerte":
            $ eleccion_arma = "Conjuro de Muerte"
            jump elige_lugar
        "Daga del Dragon":
            $ eleccion_arma = "Daga del Dragon"
            jump elige_lugar

# MENU 3: ELEGIR LUGAR
label elige_lugar:
    "En que lugar crees que ocurrio el crimen?"
    menu:
        "Cuarto del Rey":
            $ eleccion_lugar = "Cuarto del Rey"
            jump resultado_deduccion
        "Cocina Real":
            $ eleccion_lugar = "Cocina Real"
            jump resultado_deduccion
        "Biblioteca":
            $ eleccion_lugar = "Biblioteca"
            jump resultado_deduccion
        "Pasillo del Castillo":
            $ eleccion_lugar = "Pasillo del Castillo"
            jump resultado_deduccion
        "Laboratorio":
            $ eleccion_lugar = "Laboratorio"
            jump resultado_deduccion

# RESULTADO
label resultado_deduccion:
    scene black
    with fade

    narrator "Has tomado tu decision..."
    narrator "Los guardias reunen a los sospechosos en el salon del trono."

    if eleccion_personaje == culpable and eleccion_arma == arma and eleccion_lugar == lugar:
        narrator "Increible! Has resuelto el caso a la perfeccion."
        narrator "El verdadero culpable era el [culpable], usando [arma] en el [lugar]."
        narrator "El consejo real te honra como el mejor detective del reino."
    else:
        narrator "Tu deduccion fue incorrecta..."
        narrator "El verdadero culpable era el [culpable], usando [arma] en el [lugar]."
        narrator "El crimen se resolvio, pero no gracias a ti."

    narrator "Ahora, conoce el destino del asesino..."
    jump mostrar_historia

# FINALES
label mostrar_historia:
    $ resolucion = historia_activa.get("resolucion", [])
    python:
        narrar_lineas(resolucion)
    return
