Pinia
Índice
Introducción	1
Instalación	1
Registrando Pinia en el main.js	1
¿Qué es un Almacén?	1
Definir un Almacén	2
Uso del store por en componente padre	3
Acceso al store por en componente hijo	3
Consideraciones de uso	5

	
Introducción
	Pinia es una librería de almacenes para Vue que te permite compartir el estado entre los distintos componentes.

	Vamos a usar como ejemplo el uso de un contador. Este podrá ser incrementado y decrementado desde el store creado.
Instalación
	Con vue@latest podemos elegir la instalación de Pinia. Si no, lo podemos instalar manualmente con: npm install pinia

Registrando Pinia en el main.js
	Importamos Pinia y le damos uso, por ejemplo en el App.vue:

App.vue
import { createApp } from 'vue'
import { createPinia } from 'pinia'
import App from './App.vue'

const app = createApp(App)
const pinia = createPinia()


app.use(pinia)
app.mount('#app')

	Ahora crearemos un almacén de Pinia.
¿Qué es un Almacén?
	Es una entidad que contiene el estado y la lógica de negocio. Es como si fuese un componente que está siempre ahí y todos los demás pueden leerlo y escribirlo. 
	Tiene tres conceptos, el estado, getters y acciones (relacionado con la sintaxis Option API) y estos conceptos son equivalentes a datos, propiedades computadas y métodos de los componentes (relacionado con la sintaxis Composition API).

	Un almacén debería contener datos que pudiesen ser accesibles a lo largo de una aplicación. Esto incluye los datos que son usados en muchos sitios, como por ejemplo información del usuario que se está mostrando en la barra de navegación, así como datos que necesiten ser conservados entre páginas, como por ejemplo un formulario muy complejos con muchos pasos.

Definir un Almacén
	Un almacén se define usando defineStore() y que requiere el uso de un nombre único como primer parámetro usando la sintaxis Composition API.

Definiendo el store en /src/store/counter.js
// stores/counter.js
import { defineStore } from 'pinia';

export const useCounterStore = defineStore('counter', () => {
  const count = ref(0)
  const name = ref('Eduardo')
  const doubleCount = computed(() => count.value * 2)
  function increment() {
    count.value++
  }
  function decrement() {
    count.value--
  }

  return { count, name, doubleCount, increment, decrement}
})

    • ref() se convierten state en propiedades
    • computed() se convierte en getters
    • function() se convierte en actions	
      
	El store se podría definir como un fichero typescript, tal como sigue:

Definiendo el store en /src/store/counter.ts
import { defineStore } from 'pinia'
import { ref, computed } from 'vue'

export const useCounterStore = defineStore('counter', () => {
  // Estado (ref)
  const count = ref<number>(0)
  const name = ref<string>('Usuario')

  // Getters (computed)
  const doubleCount = computed(() => count.value * 2)

  // Acciones (funciones)
  function increment() {
    count.value++
  }

  function randomize() {
    count.value = Math.round(100 * Math.random())
  }

  function decrement() {
    count.value--
  }

  // Devolver lo que se quiere exponer
  return { count, name, doubleCount, increment, decrement, randomize }
})

	Recordando añadir lang=”ts” en el <script setup> de los componentes.
Uso del store por en componente padre
	Veamos como el componente padre interactúa con el store.
Definiendo el componente padre en /src/components/ParentComponent.vue
<!-- ParentComponent.vue -->
<template>
  <div>
    <h1>Contador</h1>
    <p>Contador actual: {{ counter.count }}</p>
    <p>Doble del contador: {{ counter.doubleCount }}</p>
    <button @click="counter.increment">Incrementar</button>
    <button @click="counter.decrement">Decrementar</button>
    <ChildComponent />
  </div>
</template>
<script setup>
import { useCounterStore } from '@/stores/counter';
import ChildComponent from './ChildComponent.vue';

const counter = useCounterStore();
</script>

Acceso al store por en componente hijo

Definiendo el componente hijo en /src/components/ChildComponent.vue
<!-- ChildComponent.vue -->
<template>
  <div>
    <h2>Componente Hijo</h2>
    <p>Valor del contador desde el hijo: {{ counter.count }}</p>
    <button @click="counter.increment">Incrementar desde el hijo</button>
  </div>
</template>

<script setup>
import { useCounterStore } from '@/stores/counter';
const counter = useCounterStore();
</script>

	En este ejemplo el padre e hijo están en la misma rama. Pero con Pinia es posible el acceso al store aún estando en diferente rama, por ejemplo:

App.vue
├── BranchA.vue
│   └── ComponentA.vue
└── BranchB.vue
    └── ComponentB.vue

	Haciendo uso del mismo store, App.vue se declara como:


App.vue
<template>
  <div>
    <h1>Aplicación Principal</h1>
    <BranchA />
    <BranchB />
  </div>
</template>

<script setup>
import BranchA from './BranchA/ComponentA.vue';
import BranchB from './BranchB/ComponentB.vue';
</script>

	Declaramos ComponenteA.vue para incrementar el contador.

ComponenteA.vue
<template>
  <div>
    <h2>Componente A (Rama A)</h2>
    <p>Contador compartido: {{ counter.count }}</p>
    <button @click="counter.increment">Incrementar</button>
  </div>
</template>

<script setup>
import { useCounterStore } from '@/stores/counter';

const counter = useCounterStore();
</script>

	Declaramos ComponenteB.vue para decrementar el contador.

ComponenteB.vue
<template>
  <div>
    <h2>Componente B (Rama B)</h2>
    <p>Contador compartido: {{ counter.count }}</p>
    <button @click="counter.decrement">Decrementar</button>
  </div>
</template>
<script setup>
import { useCounterStore } from '@/stores/counter';

const counter = useCounterStore();
</script>
Consideraciones de uso
	Usa el store para datos que realmente necesiten ser compartidos.

	Si usas Pinia extensivamente, asegúrate de optimizar las reactividades para evitar actualizaciones innecesarias.
