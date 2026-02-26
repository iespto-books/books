Analizando la estructura del proyecto Vue+Vite+JS
Índice
Estructura de carpetas	1
1.- Entrada al proyecto: index.html	2
2.- El fichero main.js	2
3.- El fichero App.vue	2
3.1.- Template de App.vue	3
3.2.- Script de App.vue	3
3.3.- Style de App.vue	3
4.- El componente ButtonAutoCount.vue	3
4.1.- Script del componente	4
4.2.- Template del componente	4
Resumen	5

Estructura de carpetas
    • node_modules: estan todos los ficheros de dependencia del proyecto.
    • Carpeta cypress: librería para los test en el front
    • Carpeta public: el fichero principal de la aplicación index.html y el icono favicon
    • Carpeta src: donde se construye la aplicación
    • Carpeta router: en el encontrarás la configuración donde asociamos url y componente al que se dirige.
    • App.vue : dentro de la carpeta src. 
    • main.js: dentro de src. Es el primer fichero que se ejecuta. Le indica a Vite cómo crear el proyecto Vue en función del archivo "App.vue"
    • Carpeta src/assets: almacena todos los archivos multimedia, documentos, etc.
    • Carpeta components: se guardan los componentes de la aplicación.
    • Por fuera tenemos los archivos de configuración: .gitignore, babel.config.js, jsconfig.json, package.json. Vue.config.js, etc.



1.- Entrada al proyecto: index.html
	En el body se carga el script que carga el JS:



	El fichero es el main.js dentro de la carpeta src.
2.- El fichero main.js
	El fichero main.js se encuentra dentro de src.
	En el importamos el proyecto Vue, las hojas de estilo, el componente App.vue, router y Pinia (para poder compartir datos/estructuras en todo el proyecto).
Creamos la aplicación con createApp(App).
Luego hacemos “use” de Pinia y router.
Finalmente se monta la aplicación en el elemento con id “app”.

3.- El fichero App.vue
	El fichero App.vue se encuentra dentro de src.
	Este fichero sigue la estructura SFC: <template>, <script> y <style>


3.1.- Template de App.vue
	Contiene el html que se “pintará”. 
<template>
  <h1>You did it!</h1>
  <p>
    Visit <a href="https://vuejs.org/" target="_blank" rel="noopener">vuejs.org</a> to read the
    documentation
  </p>
  <ButtonAutoCount />
</template>

	En el código se observa los enlaces de dos imágenes y un componente:
	<ButtonAutoCount />
	Dicho componente se encuentra en la carpeta src/components y se importará en la sección <script> de App.vue.

3.2.- Script de App.vue
	En este caso se importa el componente ButtonAutoCount de src/components.
<script setup lang="ts">
    import ButtonAutoCount from './components/ButtonAutoCount.vue'
</script>
3.3.- Style de App.vue
	Se define los estilos dentro de la etiqueta <style scoped>. En este caso no aplico.
	La palabra "scoped" indica que los estilos definidos dentro de esa etiqueta solo afectarán al componente en el que se declaran. No se aplicarán globalmente a otros elementos de la aplicación, lo que evita problemas de colisión de estilos y facilita el mantenimiento de tu código.
	Existe el fichero general de CSS dentro de la carpeta src que define los estilos genéricos.
4.- El componente ButtonAutoCount.vue
	El componente ButtonAutoCount.vue se encuentra dentro de src/components.
	Por convención el nombre del componente empieza por mayúscula y con estilo Camell.
	Sigue la estructura SFC.
	Veamos cada parte del componente:


4.1.- Script del componente
<script setup lang="ts">
   import { ref } from 'vue'

   const count = ref(0)
</script>

<script setup> 
	En Vue 3, la etiqueta <script setup> es una forma simplificada y optimizada de definir la lógica de un componente cuando se utiliza la Composition API. Se introdujo para hacer que el código sea más conciso y fácil de escribir. Es más eficiente en términos de rendimiento porque el código se preprocesa de manera más optimizada por Vue.
	Otras mejoras:
    • Código más breve y con menos repeticiones
    • Capacidad para declarar props y eventos emitidos usando TypeScript puro
    • Mejor rendimiento en tiempo de ejecución (la plantilla se compila en una función de renderizado en el mismo ámbito, sin un proxy intermedio)
    • Mejor rendimiento de inferencia de tipos IDE (menos trabajo para que el servidor de lenguaje extraiga los tipos del código)

import {ref} from “vue”;
	ref es una función que convierte un valor en una referencia reactiva. Cuando se utiliza ref, Vue detecta automáticamente los cambios en el valor y actualiza la interfaz de usuario en consecuencia.
	¿Por qué se usa ref? Permite que Vue haga un seguimiento de los cambios y actualice la interfaz en tiempo real. Y es útil para definir variables reactivas dentro de la lógica de la Composition API, proporcionando una estructura más organizada para componentes complejos.

const count = ref(0);
	Definimos la variable count como reactiva (ref) inicializada a 0.

4.2.- Template del componente
<template>
  <div>
    <button data-test="btn-auto-count" @click="count++">Pulsado {{ count }} veces</button>
  </div>
</template>





<button data-test="btn-auto-count" @click="count++">Pulsado {{ count }} veces</button>

	data-test="btn-auto-count"
	Creamos un dataset para localizar mejor el botón para hacer test

	type="button" 
	Se define un botón:

            @click="count++" 
	Evento click de Vue (@click es la abreviatura de v-on:click)
	V-on es un escuchador de eventos, véase más en la página oficial.
	En el evento click incremenamos la variable count, definida en el script. También podemos 	llamar a funciones.

	Pulsado {{ count }} veces</button>
	Y en el texto del mismo botón visualizamos la variable count por medio de interpolación.

Resumen
	Los componentes son importados dentro del script donde se desee usar e incrustado en el Template integrándolo como si fuese un elemento html.
