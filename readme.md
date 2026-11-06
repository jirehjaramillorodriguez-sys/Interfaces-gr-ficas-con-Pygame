Biblioteca: Pygame
¿Qué es la biblioteca seleccionada y cuál es su propósito principal?
Pygame, a diferencia de otras bibliotecas, te da control total sobre la ejecución del programa.
Pygame es una biblioteca gratuita, de código abierto y multiplataforma para el desarrollo de aplicaciones multimedia como videojuegos usando Python. Usa la librería Simple DirectMedia Layer (SDL) y otras librerías populares para abstraer las funciones más comunes, haciendo que escribir estos programas sea una tarea más intuitiva.

En pocas palabras, podemos decir que Pygame es una biblioteca que nos permite programar videouegos con python.

¿Qué tipo de aplicaciones permite desarrollar?
Pygame permite aplicaciones como Juegos 2D, simulaciones y apps interactivas con dibujos. 

¿Cómo se instala y qué requisitos necesita?
Para instalar pygame-ce, primero asegúrese de tener Python (y pip) instalados y disponibles en su PATH. Luego, ejecute el siguiente comando en su terminal o símbolo del sistema:

"pip install pygame-ce"
Tenga en cuenta que en algunas plataformas es posible que deba usar pip3en lugar de pip.
En algunos casos en el sistema operativo de Linux puede aparecer error, para ello se recomienda usar venv.

¿Cuáles son sus principales componentes o elementos gráficos?
Entre sus tantos componentes o elementos gráficos, a continuación de presentan algunos que considero más relevantes o más usados:
pygame.BufferProxy
Una vista de protocolo de matriz de píxeles de superficie

pygame.Color
Representación del color.

pygame.cursors
Cargando y compilando imágenes de cursor.

pygame.display
Configure la superficie de visualización.

pygame.draw
Dibujar formas simples como líneas y elipses sobre superficies.

pygame.evento
Gestionar los eventos entrantes procedentes de diversos dispositivos de entrada y de la plataforma de ventanas.

pygame.ejemplos
Diversos programas que demuestran el uso de módulos individuales de Pygame.

pygame.font
Cargando y renderizando fuentes TrueType.

pygame.freetype
Módulo pygame mejorado para la carga y representación de fuentes tipográficas.

pygame.gfxdraw
Funciones de dibujo con suavizado de bordes.

pygame.image
Carga, guardado y transferencia de superficies.

pygame.joystick
Gestionar los dispositivos joystick.

pygame.key
Administrar el dispositivo de teclado.

pygame.locals
Constantes de Pygame.

pygame.mixer
Cargar y reproducir sonidos

pygame.mouse
Gestiona el ratón y la pantalla.

pygame.mixer.music
Reproduce pistas de música en streaming.

pygame
Funciones de alto nivel para gestionar Pygame.

pygame.PixelArray
Manipular los datos de píxeles de la imagen.

pygame.scrap
Acceso nativo al portapapeles.

¿Cómo maneja los eventos del usuario, por ejemplo, los clics del mouse o las pulsaciones del teclado?
Pygame maneja los eventos con un bucle principal que en cada vuelta revisa la lista de eventos con pygame.event.get(). Cada evento tiene un tipo que dice qué pasó. Para el ejemplo del contador, se detecta el evento MOUSEBUTTONDOWN y se revisa con collidepoint si el clic cayó dentro del botón. Si cayó dentro, se ejecuta el método que le suma 1 al contador y se vuelve a dibujar la pantalla con el nuevo número.

¿Qué ventajas y limitaciones presenta frente a Tkinter?
Pygame no funciona exactamente como Tkinter. En Tkinter tú le dices a un botón: "cuando te hagan clic, ejecuta esta función" y te olvidas. Tkinter se queda esperando por ti.Mientras que en Pygame tú eres el que tiene que estar preguntando todo el tiempo si pasó algo.
En tkinter hay cosas predeterminadas, mientras que en Pygame tú puedes dibujar las cosas, colocarle el color, forma, tamaño, etc.
Pygame está hecho para juegos pues se puede dibujar 60 veces por segundo.
Con Pygame también podemos manejar sónido.
Tkinter es como más simple en comparación con Pygame, pero con Tkinter no ha que dar tantos detalles, sino que al especificar el obeto se crea sin necesidad de adecuarlo tanto.

Referencias:
https://pypi.org/project/pygame/
https://www.pygame.org/docs/#tutorials-reference-label
https://www.pygame.org/docs/ref/event.html



Explicación del funcionamiento:
Voy a hacer una aplicación pequeña con Pygame que muestra un contador en 0. Cuando hago clic en un botón que yo dibujé, el contador sube 1 y se muestra el número nuevo en la pantalla.

Cómo se crea la ventana o pantalla principal:
Voy a crear una ventana de 800 x 600, en esta irá toda la info que necesito:
con screen creamos nuestra ventana e indicamos las medidas en el parentessis
screen = pygame.display.set_mode((800, 600))

Para que se mantenga abierta la ventana vamos a colocar este código:
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
De esta forma, cuando la acción sea darle x a la ventana, se va a cerrar esta.
Y con esta línea cerramos completamente la funcionalidad:
pygame.quit()

Cómo se crean y muestran los componentes gráficos:
Cuando creamos la ventana, esta es automáticamente negra, pero si queremos darle color, vamos a ir dentro del while a especificar este color asi:
screen.fill("purple")
Ahora vamos a crear nuestro botón a través de la creación de un rectángulo y a ese le damos forma:
boton = pygame.Rect(300, 250, 200, 100)
pygame.draw.rect(screen, "red", boton)
los números nos indican los pixeles dónde se ubica el botón, en este caso está en todo el medio de la ventana. Además la palabra red, indica el color del mismo.
Por último, para poder mostrar eso que hemos "dibujado" debemos mostrar esto a través de una línea de código:
pygame.display.flip()
Es decir, para dibujar en la pantalla usamos fill y para mostrar usamos flip.

Bueno ahora vamos a escribir algo en la ventana para que el usuario pueda conocer la funcionalidad de nuestro botón:
Nuestra fuente la creamos asi:
fuente = pygame.font.Font(None, 50)

Qué evento implementó y cómo se detecta:
texto_contador = fuente.render(f"Contador: {contador}", True, "white")
con esta linea vamos a poder mostrar nuestro contador que vamos a crear más adelante, este va a colocar el número correspondiente al contador, dónde se menciona este. El white le da el color al mismo.
Ahora, para que este contador nos sirva y pueda aumentar, es necesario que antes del while coloquemos:
contador = 0
porque si no colocamos esta línea va a ser una variable vacía
También tenemos que pegar luego esta información para que se muestre, de esta forma:
screen.blit(texto_contador, (300, 100))
con blit pegamos y los números son como las coordenadas de su ubicación.
Y por último, vamos a agregar la palabra sumar para hacer referencia al funcionamiento de la ventana.
texto_boton = fuente.render("SUMAR", True, "white")
screen.blit(texto_boton, (350, 280))

Qué función o método responde al evento:
Para que este botón funcione y pueda aumentar el contador cada vez que presionemos, tenemos ahora que en el for que ya teníamos antes, añadir un nuevo condicional if, con este componente: MOUSEBUTTONDOWN, que nos indica que por cada pulsación del mouse continua funcionando y luego: if boton.collidepoint(event.pos), que nos permite saber si la pulsación del mouse fue dentro del botoncito que ya habíamos creado, y si sí pasa esto pasamos a sumar 1 al contador de esta forma: contador = contador + 1

Cómo se modifica la interfaz después de la interacción:
Después de cada interacción con el botón, programamos para que el contador pueda mostrar cómo sube este, primeramente declarando la variable contador que contendrá la cantidad de veces que pulsamos el mouse, luego mediante nuestro fuente.render mostramos este resultado que va aumentando. De esta forma es como si se redibujara la ventanita pero con el nuevo número.

Reto adicional: agregar clases de poo