Gestión del Estado en Vue.js

Índice
Gestión del Estado en Vue.js	1
Introducción	1
Uso de ref	1
¿Qué es?	1
¿Para qué se usa?	2
Ejemplo práctico	2
Otros ejemplos	2
Uso de reactive	2
¿Qué es?	2
¿Para qué se usa?	3
Ejemplo práctico	3
Otros ejemplos	3
Uso de computed	3
¿Qué es?	3
¿Para qué se usa?	4
Ejemplo práctico	4
Otros ejemplos	4
Uso de watch	4
¿Qué es?	4
¿Para qué se usa?	4
Ejemplo práctico	5
Otros ejemplos	5
Comparativa rápida	5

	
Introducción
	Aprenderemos sobre la gestión del estado en Vue.js utilizando ref, reactive, computed y watch. La reactividad es el núcleo de Vue.js y permite que la interfaz de usuario responda automáticamente a los cambios en los datos.

Uso de ref
¿Qué es?
    • ref crea una referencia reactiva a un valor primitivo o a un objeto. Es una función proporcionada por la Composition API de Vue.js.
    • El valor de la referencia se almacena en su propiedad .value.
      
¿Para qué se usa?
    • Para manejar valores reactivamente en variables simples como números, cadenas o booleanos.
    • Es útil cuando se necesita una variable reactiva que puede ser fácilmente pasada entre funciones o componentes.
Ejemplo práctico
<template>
  <button @click="increment">
    Pulsado {{ count }} veces
  </button>
</template>

<script setup>
import { ref } from 'vue'

const count = ref(0)

const increment = () => {
  count.value++
}
</script>

En el Template

<p>{{ count }}</p>
<button @click="increment">Incrementar</button>

Otros ejemplos
    1. Crear una variable reactiva simple:
       Ejemplo: const count = ref(0);
       
    2. Vincular la variable a la interfaz:
       Ejemplo: <button @click='count++'>{{ count }}</button>
       
    3. Actualizar dinámicamente el valor de ref:
       Ejemplo: count.value = 10;
       
Uso de reactive
¿Qué es?
    • reactive convierte un objeto completo en un objeto reactivo, permitiendo que todas sus propiedades sean observadas para cambios.
    • A diferencia de ref, no necesita .value para acceder a las propiedades.
¿Para qué se usa?
    • Para manejar estructuras más complejas, como objetos o arreglos.
    • Proporciona una forma natural de trabajar con datos estructurados.
Ejemplo práctico
<template>
  <div>
    <p>Framework: {{ state.name }}</p>
    <p>Versión: {{ state.version }}</p>
    <button @click="updateVersion">Actualizar versión</button>
  </div>
</template>

<script setup>
import { reactive } from 'vue'

const state = reactive({
  name: 'Vue.js',
  version: 3,
})

const updateVersion = () => {
  state.version = 4
}
</script>

		En el Template
<p>{{ state.name }} v{{ state.version }}</p>
<button @click="updateVersion">Actualizar Versión</button>
Otros ejemplos
    1. Crear un objeto reactivo:
       Ejemplo: const state = reactive({ name: 'Vue.js', version: 3 });
       
    2. Actualizar propiedades del objeto:
       Ejemplo: state.version = 4;
       
    3. Vincular propiedades del objeto reactivo a la interfaz:
       Ejemplo: <p>{{ state.name }} v{{ state.version }}</p>

Uso de computed
¿Qué es?
    • computed es una función que devuelve un valor calculado basado en otras variables reactivas.
    • Se utiliza para derivar estados o datos que dependen de otras variables.
¿Para qué se usa?
    • Para realizar cálculos reactivos que se actualizan automáticamente cuando cambian los datos subyacentes.
    • Reduce la necesidad de escribir funciones manuales para actualizar valores derivados.
Ejemplo práctico
<template>
  <div>
    <p>Count: {{ count }}</p>
    <p>Double: {{ doubleCount }}</p>
    <button @click="count++">Incrementar</button>
  </div>
</template>

<script setup>
import { ref, computed } from 'vue'

const count = ref(2)

const doubleCount = computed(() => count.value * 2)
</script> 	

En el Template

<p>Original: {{ count }}</p>
<p>Doble: {{ doubleCount }}</p>
Otros ejemplos
    1. Crear una propiedad computada:
       Ejemplo: const doubleCount = computed(() => count.value * 2);
       
    2. Usar computed en la interfaz:
       Ejemplo: <p>Doble: {{ doubleCount }}</p>
       
    3. Combinar computed con otros métodos:
       Ejemplo: const formatted = computed(() => `${state.name} ${state.version}`);

Uso de watch
¿Qué es?
    • watch permite observar cambios en variables reactivas y ejecutar una función cuando se detecta un cambio.
    • A diferencia de computed, no devuelve un valor sino que realiza una acción en respuesta al cambio.
¿Para qué se usa?
    • Para realizar efectos secundarios cuando cambian los datos, como llamar a una API, registrar datos o validar formularios.
    • Es útil cuando se necesita un seguimiento de cambios más granular.
Ejemplo práctico
<template>
  <div>
    <p>Count: {{ count }}</p>
    <button @click="increment">Incrementar</button>
  </div>
</template>

<script setup>
import { ref, watch } from 'vue'

const count = ref(0)

watch(count, (newVal, oldVal) => {
  console.log(`El valor cambió de ${oldVal} a ${newVal}`)
})

const increment = () => {
  count.value++
}
</script>

En el Template

<p>{{ count }}</p>
<button @click="increment">Incrementar</button>
Otros ejemplos
    1. Observar cambios en una variable:
       Ejemplo: watch(count, (newVal, oldVal) => console.log(newVal, oldVal));
       
    2. Observar cambios en un objeto reactivo:
       Ejemplo: watch(() => state.version, (newVal) => console.log(newVal));
       
    3. Usar watch con una función personalizada:
       Ejemplo: watch(() => state.name, () => fetchData());

Comparativa rápida

Concepto	¿Qué controla?	¿Cuándo usuarlo?
ref	Valor simple o único	Para valores individuales reactivos, como números, cadenas o booleanos.
reactive	Objetos/estructuras	Para objetos complejos o arreglos que necesitan ser reactivos.
computed	Valores derivados	Para cálculos reactivos basados en otras variables reactivas. 
watche	Efectos secundarios	Para ejecutar código en respuesta a cambios en variables reactivas (llamar APIs, guardar datos, realizar validaciones, etc.).

