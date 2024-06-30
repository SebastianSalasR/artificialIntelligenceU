<h1> Aprendizaje no supervisado </h1>
	
	I) La diferencia entre estos modelos de aprendizaje es que el supervisado contiene etiquetas en los datos mostrado cual es la respuesta correcta, mientras que el no supervisado no tiene estas etiquetas, lo que significa que tendra que agrupar datos (en clusters por ejemplo) e identificar patrones.

	II) Los datos ocupados para entrenar modelos mediante un aprendizaje supervisados son datos etiquetados, es decir, que cada instancia de dato tiene una etiqueta o salida conocida que el modelo intenta predecir. En cnotraste, el modelo de aprendizaje no supervisado no hay etiquedas.
	
	III) Ventajas del aprendizaje supervisado: 

		Precisión: el aprendizaje supervisado es capaz de proporcionar predicciones altamente precisas y confiables, ya que utiliza un conjunto de datos etiquetados y supervisados para entrenar un modelo. Esto significa que el modelo aprende a partir de ejemplos claros y precisos.
	
		Clasificación: también se puede utilizar para clasificar los datos en diferentes categorías, lo que permite a los usuarios analizar y entender mejor los datos.
		
		Eficiencia: este método es más eficiente que otros métodos de aprendizaje automático, ya que utiliza un conjunto de datos etiquetados y supervisados para entrenar el modelo, lo que significa que el modelo aprende más rápido.

		Ventajas del aprendisaje no supervisado:

		Descubrimiento de patrones: El aprendizaje no supervisado puede ayudar a descubrir patrones ocultos en los datos que no son evidentes a simple vista. Esto puede ser útil para identificar tendencias, comportamientos o relaciones entre variables.
		
		Exploración de datos: también permite explorar y analizar grandes conjuntos de datos de manera eficiente y efectiva. Esto puede ayudar a identificar problemas y oportunidades que no se habían considerado anteriormente.
		
		Reducción de costes: El aprendizaje no supervisado puede ser más rentable que el aprendizaje supervisado, ya que no requiere la creación y etiquetado de grandes conjuntos de datos de entrenamiento.
		
		Flexibilidad: A su vez, es más flexible que el aprendizaje supervisado, ya que no requiere la especificación de objetivos específicos de aprendizaje o la definición de una función de pérdida.

	IV)

<h1> 2 </h1>

	El análisis de componentes principales (PCA por sus siglas en inglés, Principal Component Analysis) es una técnica estadística utilizada para reducir la dimensionalidad de un conjunto de datos mientras se conserva la mayor cantidad posible de su variabilidad.La idea fundamental detrás del PCA es transformar un conjunto de variables correlacionadas en un conjunto de variables no correlacionadas llamadas componentes principales.
	Las dos primeras componentes principales cumplen la propiedad de que son las variables con mayor varianza de todas las variables.

<h1> 4 k-means</h1>
	
	i)  Una estrategia común para definir el número de grupos en un algoritmo de agrupamiento es la observación visual de cómo se distribuyen los datos cuando se asignan a diferentes números de grupos. Esto puede lograrse mediante técnicas como gráficos de dispersión o visualizaciones de los clusters resultantes. Sin embargo, este enfoque puede ser subjetivo y dependiente del observador. 

	ii) El método del codo es una técnica popular para determinar el número óptimo de clusters en algoritmos de agrupamiento, como K-means. Consiste en trazar el número de clusters en el eje X y la suma de cuadrados dentro de los clusters (WSS, por sus siglas en inglés) en el eje Y. A medida que aumentamos el número de clusters, es de esperar que WSS disminuya, ya que los clusters tienden a ser más compactos. Sin embargo, en algún punto, agregar más clusters ya no proporciona una reducción significativa en WSS, lo que resulta en un "codo" en el gráfico. El punto en el que se observa este codo se considera un buen candidato para el número óptimo de clusters, ya que agregar más clusters no mejora significativamente la calidad del agrupamiento.

<h1> 5 </h1>

	i)  1- Escoger un numero k de clusters
		2- Select k puntos de forma random
		3- Calcular la distancia entre cada punto y el centroide, asigne cada punto de data al cluster mas cercano.
		4- Calcular el centroide (posicion promedia) de cada cluster.
		5- Repetir pasos 3-4 hasta que los clusters con cambien o se haya llegado al numero maximo de iteraciones.