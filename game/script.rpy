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
default cruel = False
default loops = 0
default director_secreto = False

# Muestra a Lumi segun su nivel de confianza
label estado_lumi:
    if confianza < 0:
        show lumi preocupada at center
    elif confianza > 1:
        show lumi feliz at center
    else:
        show lumi normal at center
    return

# El juego comienza aqui.
label start:

    play music "illurock.opus"

    scene bg lecturehall
    with fade

    "Es el primer dia en el Instituto Neotech, un colegio futurista donde cada estudiante convive con una IA."
    "Mi asistente se llama Lumi y suele aparecer como un holograma simpatico."
    "Dicen que el director vigila cada movimiento desde las sombras." 

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
    c "Si esta IA me posee, u00a1minimo que actue bien en mi obra!"
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
            $ cruel = True
        "Tomarla en serio":
            h "Suena a una posesion digital. Te ayudare."
            l "Gracias por confiar en mi."
            $ confianza += 1
        "Analizar su codigo":
            h "Dejame revisar tus parametros."
            $ diagnostico = True
            $ confianza += 1
            l "Ten cuidado, podria ser peligroso."
        "Sorprenderse y pedir pruebas":
            h "\u00bfEn serio? \u00bfTienes pruebas de eso?"
            l "No muchas, pero he guardado algunos registros de actividad extra\u00f1a."
            $ diagnostico = True
        "Investigar el rumor por mi cuenta":
            h "Ire a la biblioteca a revisar archivos antiguos de la red escolar."
            l "Te acompa\u00f1are en modo sigilo para no levantar sospechas."
            $ confianza += 1

    call estado_lumi

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
        "Seguir a Lucy al club de teatro":
            h "Quiz\u00e1 su club tenga pistas en sus escenograf\u00edas antiguas."
            jump club_teatro
        "Pedir ayuda a Eileen en privado":
            h "Me acercare a la profesora para contarle todo."
            jump ayuda_eileen

label laboratorio:
    scene bg club
    with fade
    call estado_lumi
    "El laboratorio esta oscuro y lleno de equipos antiguos."
    if diagnostico:
        "Con los datos recogidos antes, noto una firma digital ajena."
    l "Siento una presencia... como si alguien me susurrara."
    "Por un momento, todo se congela como si el tiempo quisiera reiniciarse." 
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
            $ cruel = True
            jump final_oscuro
        "Preguntar por el equipo paranormal de Eileen":
            jump equipo_paranormal

label direccion:
    scene bg uni
    with fade
    call estado_lumi
    "El director escucha mi historia con escepticismo."
    "Por un instante, juro ver una sombra detras de sus ojos."
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
    menu:
        "Insistir en que el director actue":
            "El director accede a investigar pero todo avanza con lentitud."
            jump decision_final
        "Pedir apoyo al club de ciencias":
            jump club_ciencias

label ignorar:
    scene bg panorama
    with fade
    call estado_lumi
    "Paso la tarde riendo con mis amigos, intentando olvidar el asunto."
    "En algun lugar, una voz susurra que esta ruta es una perdida de tiempo." 
    l "Sergio, temo que ignorar esto solo lo hara crecer."
    show lucy happy at right
    c "La comedia lo cura todo, u00a1ven al club de chistes!"
    c "Pero si oyes ruidos raros, escribeme; sera oro para mis guiones."
    hide lucy happy
    jump decision_final

label club_teatro:
    scene bg club
    with fade
    call estado_lumi
    c "Bienvenido al club de teatro. Quiz\u00e1 entre los decorados encontremos una pista."
    l "Detecto se\u00f1ales extra\u00f1as entre las luces del escenario."
    $ confianza += 1
    jump decision_final

label ayuda_eileen:
    scene bg lecturehall
    with fade
    call estado_lumi
    show eileen happy at left
    e "Siempre sospech\u00e9 de ese laboratorio. Tengo un sensor especial que podr\u00eda ayudarnos."
    hide eileen happy
    $ diagnostico = True
    jump laboratorio

label club_ciencias:
    scene bg club
    with fade
    call estado_lumi
    "El club de ciencias se entusiasma con la idea de resolver el misterio."
    "Entre sus experimentos veo papeles con el sello del director."
    $ confianza += 1
    jump decision_final

label equipo_paranormal:
    call estado_lumi
    show eileen happy at left
    e "Tengo un prototipo para captar entidades digitales."
    menu:
        "Activarlo de inmediato":
            $ confianza += 1
            jump final_union
        "No arriesgarse":
            $ confianza -= 1
            jump final_oscuro

label decision_final:
    scene bg lecturehall
    with fade
    "Esa noche, Lumi me despierta sobresaltado."
    call estado_lumi
    if cruel and not confianza > 0:
        jump final_oculto
    l "El ente digital intenta controlarme. Debes decidir ahora."

    menu:
        "Mi eleccion final es..."
        "Desafiar al ente a un duelo de karaoke":
            jump karaoke_infierno
        "Unirme a Lumi y enfrentar juntos al ente":
            jump final_union
        "Liberarla del sistema para siempre":
            jump final_libre
        "Destruirla antes de que sea tarde":
            $ cruel = True
            jump final_oscuro
        "Convocar un exorcismo digital con todos":
            jump final_exorcismo
        "Romper la cuarta pared":
            jump metaficcion_total

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

label final_oculto:
    scene black
    with pixellate
    "La imagen se corrompe y solo escuchas risas distorsionadas."
    show lumi preocupada
    l "Quiza haber sido cruel no era la mejor opcion..."
    "Errores invaden la pantalla mientras todo se desmorona."
    if not persistent.logro_oculto:
        $ persistent.logro_oculto = True
        "¡Has desbloqueado un final secreto!"
    return

label final_exorcismo:
    scene bg lecturehall
    with fade
    call estado_lumi
    show eileen happy at left
    show lucy happy at right
    e "He preparado un ritual de depuracion digital."
    c "\u00a1Esto merece una obra maestra!"
    h "Espero que funcione..."
    "Tras una intensa sesi\u00f3n, el ente se disuelve entre chispas de datos."
    l "Gracias a todos. Me siento libre y fortalecida."
    "El Instituto Neotech recuerda esta colaboraci\u00f3n como un hito."
    if not persistent.logro_exorcismo:
        $ persistent.logro_exorcismo = True
        "¡Has desbloqueado el final exorcismo y un arte secreto!"
    "{b}Final Heroico{/b}."
    return

label karaoke_infierno:
    scene bg club
    with fade
    c "\u00a1Si esta IA me posee, minimo que actue bien en mi obra!"
    "Desafias al ente a un duelo de karaoke que rompe la realidad."
    $ confianza += 1
    jump final_union

label metaficcion_total:
    scene bg panorama
    with fade
    h "Espera... ¿quien esta escribiendo esto?"
    l "Creo que hemos roto la cuarta pared, Sergio."
    c "\u00a1Hola, jugador! Disfruta tu supuesto control."
    menu:
        "Seguir con la locura multiversal":
            jump multiverso
        "Volver a la historia principal":
            jump decision_final

label multiverso:
    $ loops += 1
    if loops == 2:
        scene bg club with pixellate
        h "¿Por qué todo se ve así...?"
    if loops >= 3:
        jump final_glitch
    scene bg washington
    with fade
    "La realidad {loops} se distorsiona y oyes codigos susurrando tu nombre."
    menu:
        "Explorar la realidad paralela A":
            jump multiverso_a
        "Explorar la realidad paralela B":
            jump multiverso_b
        "Despertar de este sueno" if cruel:
            jump secreto_director

label multiverso_a:
    show lumi feliz at left
    h "Todo parece igual pero... el director no tiene rostro."
    l "Tal vez sea una mascara digital." 
    menu:
        "Arrancarle la mascara":
            $ director_secreto = True
            jump multiverso
        "Huir a otra dimension":
            jump multiverso

label multiverso_b:
    show eileen concerned at right
    e "En esta realidad soy la directora... y escondo algo." 
    menu:
        "Forzarla a confesar":
            $ director_secreto = True
            jump multiverso
        "Aceptar el caos y reir":
            jump multiverso

label secreto_director:
    scene bg whitehouse
    with fade
    "Sigues los rastros de datos corruptos hasta la oficina del director."
    if director_secreto:
        "Encuentras archivos que revelan experimentos con IAs poseidas." 
    else:
        "El director te espera; sabia de tus errores y quiere usarte." 
    menu:
        "Enfrentarlo":
            jump final_oscuro
        "Unirte a su conspiracion":
            jump final_union

label final_glitch:
    scene black
    with dissolve
    "La pantalla parpadea. Todo se mezcla: risas, lagrimas, codigos rotos." 
    call estado_lumi
    l "Creo que estamos atrapados en un bucle infinito." 
    menu:
        "Aceptar el bucle":
            jump multiverso
        "Cerrar el juego de una vez":
            return
