Imagina que tienes una caja llena de diferentes tipos de frutas, y quieres averiguar la mejor manera de separarlas usando las características más obvias: color, tamaño o tipo de fruta. Los árboles de decisión son como un juego de "20 preguntas" que usas para clasificar las frutas basándote en estas características. Cada pregunta te lleva por un camino que te acerca más a saber qué fruta tienes en la mano.

La "importancia de una característica" es básicamente cuán buena es una pregunta para ayudarte a separar las frutas de manera efectiva. Si preguntar por el color te lleva rápidamente a identificar la fruta, entonces el color es una característica muy importante.

Para entender cómo se decide esto, necesitamos hablar sobre dos conceptos: la entropía y la ganancia de información.

- **Entropía**: Es una forma de medir el "desorden" o cuán mezcladas están las frutas en tu caja. Si todas las frutas son iguales (digamos, todas manzanas), no hay desorden. Pero si tienes una mezcla de manzanas, bananas y uvas, hay más desorden. Matemáticamente, la entropía se calcula usando la probabilidad de encontrar cada tipo de fruta en tu caja.

- **Ganancia de información**: Es cuánto "desorden" reduces (o cuánta información ganas) cuando eliges una característica para separar las frutas. Si después de preguntar por el color, las frutas quedan perfectamente agrupadas por tipo, has ganado mucha información y has reducido mucho el desorden.

Entonces, en los árboles de decisión, ordenamos las características (como color, tamaño, tipo) por cuánta ganancia de información proporcionan. La que más reduce el desorden y nos ayuda a clasificar las frutas más rápidamente es considerada la más importante. Y esa es, en esencia, cómo los árboles de decisión deciden qué camino tomar primero: preguntando primero por las características más reveladoras.

Una de las formas más habituales de medir esta importancia es la ganancia de la información o pequeñas variaciones sobre este concepto.