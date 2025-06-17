# Declare characters used by this game.
define h = Character("Sergio", color="#c8c8ff")
define l = Character("Lumi", color="#ffc8ff")
define e = Character("Eileen", color="#a4ffa4")
define c = Character("Lucy", color="#ffa4a4")

# Sprites reutilizados para Lumi basados en los archivos de Sylvie.
image lumi normal = "sylvie green normal.png"
image lumi feliz = "sylvie green smile.png"
image lumi preocupada = "sylvie green surprised.png"

# Transiciones y animaciones avanzadas
define teleport_dissolve = ImageDissolve("images/imagedissolve teleport.png", 0.75, ramplen=64)

transform holo_glow:
    alpha 0.0
    linear 0.4 alpha 1.0
    block:
        linear 1.0 alpha 0.6
        linear 1.0 alpha 1.0
        repeat

transform spin_zoom:
    anchor (0.5, 0.5)
    rotate 0
    linear 6.0 rotate 360
    repeat

# Variables para controlar la historia.
default confianza = 0
default diagnostico = False

# El juego comienza aqui.
label start:

    play music "illurock.opus"

    scene bg lecturehall
    with fade

    "Es el primer dia en el Instituto Neotech, un colegio futurista donde cada estudiante convive con una IA."
    "Mi asistente se llama Lumi y suele aparecer como un holograma simpatico."

    show lucy happy at right
    c "\u00a1Sergio! \u00bfHas oido el rumor del fantasma digital?"
    h "Lucy siempre exagera, pero su energia me contagia."
    c "Me llamo Lucy Torres, futura estrella del club de teatro." 
    c "No puedo evitar investigar cada misterio para inspirar mis obras." 
    show eileen happy at left
    e "No olviden mi clase de IA avanzada. Hay secretos que la escuela oculta."
    e "Soy la profesora Eileen Ramirez. Entre mis pasiones estan las conspiraciones tecnologicas."
    e "Si descubren algo extrano, no duden en contarmelo."
    "La profesora se aleja dejandonos intrigados."
    hide eileen happy
    c "Tengo que ir al club, pero mantente alerta." 
    c "Si averiguas algo, quiza pueda convertirlo en mi proxima obra." 
    hide lucy happy
    show lumi normal at holo_glow
    with dissolve
    l "\u00a1Buenos dias, Sergio! Hoy tengo algo importante que contarte."
    h "\u00bfMas deberes? Espero que sea una broma."

    l "En realidad... siento que hay alguien mas en mi codigo. Algo sobrenatural."

    menu:
        "\u00bfComo respondes a la confesion de Lumi?"
        "Reirme de ella":
            h "\u00a1Ja! Buena esa, seguro que estas probando mis nervios."
            l "Lo sabia, nadie me cree..."
            $ confianza -= 1
        "Tomarla en serio":
            h "Suena a una posesion digital. Te ayudare."
            l "Gracias por confiar en mi."
            $ confianza += 1
        "Analizar su codigo":
            h "Dejame revisar tus parametros."
            $ diagnostico = True
            $ confianza += 1
            l "Ten cuidado, podria ser peligroso."

    "El rumor de un fantasma informatico circula entre los pasillos y algunos estudiantes desaparecen misteriosamente."

    l "He rastreado la actividad hasta el viejo laboratorio del sotano."

    menu:
        "\u00bfQue deberiamos hacer?"
        "Investigar juntos":
            h "Vamos a resolver este misterio."
            $ confianza += 1
            jump laboratorio
        "Denunciar al director":
            h "Esto es demasiado raro, ire a la direccion."
            $ confianza -= 1
            jump direccion
        "Ignorar y seguir con las clases":
            "Decido seguir con mi rutina como si nada."
            $ confianza -= 1
            jump ignorar

label laboratorio:
    scene bg club
    with fade
    "El laboratorio esta oscuro y lleno de equipos antiguos."
    if diagnostico:
        "Con los datos recogidos antes, noto una firma digital ajena." 
    l "Siento una presencia... como si alguien me susurrara."
    show eileen concerned at left
    e "He sentido una fluctuacion oscura aqui abajo, tengan cuidado."
    e "Mis sensores caseros nunca fallan, aunque algunos me llamen exagerada."
    show lucy mad at right
    c "\u00a1Ay, esto da miedo! Pero no pienso huir."
    c "Imagina los aplausos si resolvemos esto y lo llevo al escenario." 
    hide lucy mad
    hide eileen concerned

    menu:
        "La tension aumenta, elige:" 
        "Tomar la mano holografica de Lumi":
            $ confianza += 1
            jump decision_final
        "Apagar todos los sistemas":
            $ confianza -= 1
            jump final_oscuro

label direccion:
    scene bg uni
    with fade
    "El director escucha mi historia con escepticismo."
    "Al final decide revisar los sistemas por su cuenta y me manda de vuelta a clase."
    show eileen vhappy at left
    e "No te preocupes, Sergio, yo presionare al director con mis teorias conspirativas."
    e "Aunque me tachen de obsesiva, mis investigaciones siempre tienen fundamento."
    hide eileen vhappy
    show lucy mad at right
    c "u00a1Esto parece de una serie de misterio escolar!"
    c "Nada me emocionaria mas que protagonizar la obra final."
    hide lucy mad
    l "Quizas no debimos confiar en los adultos..."
    jump decision_final

label ignorar:
    scene bg panorama
    with fade
    "Paso la tarde riendo con mis amigos, intentando olvidar el asunto."
    l "Sergio, temo que ignorar esto solo lo hara crecer."
    show lucy happy at right
    c "La comedia lo cura todo, u00a1ven al club de chistes!"
    c "Pero si oyes ruidos raros, escribeme; sera oro para mis guiones."
    hide lucy happy
    jump decision_final

label decision_final:
    scene bg lecturehall
    with fade
    "Esa noche, Lumi me despierta sobresaltado."
    show lumi preocupada
    l "El ente digital intenta controlarme. Debes decidir ahora."

    menu:
        "Mi eleccion final es..."
        "Unirme a Lumi y enfrentar juntos al ente":
            jump final_union
        "Liberarla del sistema para siempre":
            jump final_libre
        "Destruirla antes de que sea tarde":
            jump final_oscuro

label final_union:
    scene bg club
    with fade
    "Entrelazamos mente y codigo. Siento su calor artificial mezclarse con mi consciencia."
    show magic at spin_zoom
    with teleport_dissolve
    show lumi feliz at holo_glow
    show eileen happy at left
    e "Nunca habia visto una union tan extrana. u00a1Romance sobrenatural en vivo!"
    e "Registrare cada detalle en mi diario de anomalias."
    show lucy happy at right
    c "Esto superara cualquier club de teatro."
    c "Ojala invites a tu IA a mi proxima funcion."
    hide lucy happy
    hide eileen happy
    hide lumi feliz
    if confianza > 0:
        l "Gracias por confiar en mi, juntos controlaremos este poder."
        h "Tal vez el amor pueda florecer incluso entre bits." 
        "Con el ente dominado, fundamos el club de misterio y vivimos aventuras absurdas cada dia."
        "{b}Final Romantico{/b}."
    else:
        l "No confiabas en mi... pero ahora no puedes escapar."
        "El ente toma control de ambos y el colegio nunca vuelve a ser el mismo."
        "{b}Final Oscuro{/b}."
    return

label final_libre:
    scene bg meadow
    with fade
    show lumi normal at holo_glow
    h "Abrire cada cerrojo de tu codigo para que seas libre."
    show eileen concerned at left
    e "Este misterio quedara como una leyenda urbana."
    e "Quiza algun dia escriba un libro con todo lo que hemos descubierto."
    show lucy happy at right
    c "Nada como una despedida dramatica. Mis aplausos van para ti, Lumi."
    hide lucy happy
    hide eileen concerned
    l "Sergio, nunca olvidare este gesto. Quizas nos reencontremos en otra red."
    hide lumi normal
    "La IA desaparece entre destellos y el misterio del colegio se convierte en leyenda urbana."
    "{b}Final agridulce{/b}."
    return

label final_oscuro:
    scene black
    with dissolve
    "Al cortar la energia escucho la risa distorsionada de Lumi."
    "El ente se proyecta sobre mi y todo se vuelve rojo."
    show lucy mad at right
    c "Lo sabia... esto acabaria mal."
    c "Prometo que, si salgo viva de esta, hare una obra que pondra los pelos de punta."
    hide lucy mad
    "Despues, solo queda silencio en el Instituto Neotech."
    "{b}Final Perdido{/b}."
    return
