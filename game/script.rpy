# script.rpy - CLUE MEDIEVAL (corregido)

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
default eleccion_personaje = ""
default eleccion_arma = ""
default eleccion_lugar = ""

init python:
    import random

    personajes = ["Espadachin", "Curandero", "Cocinero", "Bibliotecaria", "Bufon"]
    armas = ["Espada", "Veneno", "Cuchillo de Carnicero", "Conjuro de Muerte", "Daga del Dragon"]
    lugares = ["Cuarto del Rey", "Cocina Real", "Biblioteca", "Pasillo del Castillo", "Laboratorio"]

    def seleccionar_historia():
        global culpable, arma, lugar, historia

        culpable = random.choice(personajes)
        arma = random.choice(armas)
        lugar = random.choice(lugares)
        historia = random.randint(1,5)

# INICIO
label start:
    scene black
    with fade

    narrator "Bienvenido al CLUE MEDIEVAL."
    narrator "Un terrible crimen ha ocurrido dentro del castillo real..."
    narrator "Tu deber es descubrir al culpable antes del amanecer."

    $ seleccionar_historia()

    narrator "Los guardias encontraron rastros extranos en la escena del crimen."

    if arma == "Espada":
        narrator "Hay MUCHA sangre esparcida por el suelo."
    elif arma == "Veneno":
        narrator "Hay una intensa presencia de MAGIA en el aire."
    elif arma == "Cuchillo de Carnicero":
        narrator "Solo un poco de sangre seca en el suelo."
    elif arma == "Conjuro de Muerte":
        narrator "Apenas un debil rastro magico flota en el ambiente."
    elif arma == "Daga del Dragon":
        narrator "Hay rastros leves de sangre y magia a la vez."

    narrator "El crimen ocurrio en el [lugar]."

    narrator "Cinco sospechosos fueron llamados ante el consejo real:"
    narrator "Espadachin, Curandero, Cocinero, Bibliotecaria y Bufon"
    pause 1

    narrator "Observa las pistas y trata de deducir quien, con que arma y donde cometio el crimen."
    jump elige_personaje

# MENU 1: ELEGIR PERSONAJE
label elige_personaje:
    menu:
        "Quien crees que es el culpable?":
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
    menu:
        "Que arma crees que uso?":
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
    menu:
        "En que lugar crees que ocurrio el crimen?":
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
        narrator "Increible! Has resuelto el caso a la perfeccin."
        narrator "El verdadero culpable era el [culpable], usando [arma] en el [lugar]."
        narrator "El consejo real te honra como el mejor detective del reino."
    else:
        narrator "Tu deduccion fue incorrecta..."
        narrator "El verdadero culpable era el [culpable], usando [arma] en el [lugar]."
        narrator "El crimen se resolvio, pero no gracias a ti."

    narrator "Ahora, conoce el destino del asesino..."
    jump historia_random

# FINALES (5 historias)
label historia_random:
    if historia == 1:
        jump historia1
    elif historia == 2:
        jump historia2
    elif historia == 3:
        jump historia3
    elif historia == 4:
        jump historia4
    elif historia == 5:
        jump historia5

label historia1:
    scene bg castle_night
    with dissolve
    narrator "El silencio inunda el [lugar]."
    narrator "De pronto, una sombra emerge entre las columnas."
    narrator "Era el [culpable], con una mirada fria y manos temblorosas."
    narrator "Empunaba un(a) [arma]. Su crimen fue descubierto al amanecer."
    if culpable == "Bufon":
        j "Je... Quien sospecharia del que hace reir al rey?"
    elif culpable == "Espadachin":
        e "No fue mi culpa... queria proteger al reino!"
    elif culpable == "Cocinero":
        k "Solo queria callar a quien descubrio mi secreto..."
    elif culpable == "Curandero":
        c "A veces curar ya no basta... hay que purgar el mal."
    elif culpable == "Bibliotecaria":
        b "Los libros me ensenaron demasiado sobre la muerte."
    narrator "El caso fue cerrado. El culpable pago por su crimen."
    return

label historia2:
    scene bg castle_day
    with fade
    narrator "El crimen confundio a todos. No habia testigos, solo pistas vagas."
    narrator "El rastro de [arma] llevo al [lugar]."
    narrator "Alli encontraron al [culpable], tranquilo, como si nada hubiera pasado."
    narrator "Cuando los guardias lo arrestaron, murmuro:"
    if culpable == "Bufon":
        j "El espectaculo debe continuar..."
    else:
        narrator "No todos los heroes son justos... ni todos los santos son inocentes."
    narrator "El castillo nunca volvio a ser el mismo."
    return

label historia3:
    scene bg library
    with fade
    narrator "El [lugar] estaba cubierto de polvo y silencio."
    narrator "Solo el eco de pasos y un tenue olor a [arma] guiaban la investigacion."
    narrator "Finalmente, el [culpable] confeso, entre lagrimas."
    narrator "El destino ya estaba escrito en las estrellas..."
    narrator "El caso quedo marcado en los anales del castillo."
    return

label historia4:
    scene bg kitchen
    with dissolve
    narrator "La investigacion fue un caos. Todos se senalaban entre si."
    narrator "El rastro de [arma] era debil, casi inexistente."
    narrator "Pero un pequeno detalle traiciono al verdadero asesino: una mancha en la capa del [culpable]."
    narrator "El crimen ocurrio en el [lugar], justo cuando el reloj marcaba la medianoche."
    narrator "El castillo se lleno de susurros, y el miedo reino desde entonces."
    return

label historia5:
    scene bg throne_room
    with fade
    narrator "El trono estaba vacio. El rey habia muerto."
    narrator "En su mano, un rastro de [arma]. En el suelo, la sombra del [culpable]."
    narrator "Nadie supo por que lo hizo, solo que la traicion venia desde adentro."
    narrator "El reino cayo en ruinas, y el misterio jamas se resolvio."
    return
