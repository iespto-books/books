# Pinia en Vue 3

Guia basica para crear y usar stores con Pinia en una aplicacion Vue.

Referencia oficial: [Pinia Documentation](https://pinia.vuejs.org/).

## Introduccion

Pinia es la libreria oficial de gestion de estado para Vue.

- Permite compartir estado entre componentes.
- Centraliza logica de negocio.
- Funciona muy bien con Composition API y TypeScript.

Referencia oficial: [Why Pinia?](https://pinia.vuejs.org/introduction.html).

## Instalacion

Si no se instalo durante la creacion del proyecto:

```bash
npm install pinia
```

Referencia oficial: [Getting Started](https://pinia.vuejs.org/getting-started.html).

## Registrar Pinia en `main.js`

Referencia oficial: [Installation](https://pinia.vuejs.org/getting-started.html#installation).

```js
import { createApp } from 'vue'
import { createPinia } from 'pinia'
import App from './App.vue'

const app = createApp(App)
const pinia = createPinia()

app.use(pinia)
app.mount('#app')
```

## Que es un store

Un store es una entidad global que contiene estado y logica.

En Pinia, de forma general:

- Estado: datos reactivos compartidos.
- Getters: valores derivados.
- Actions: funciones que modifican el estado.

Referencia oficial: [Core Concepts](https://pinia.vuejs.org/core-concepts/).

Usalo para datos que se comparten en muchas partes de la app (por ejemplo, usuario autenticado o carrito).

## Definir un store con Composition API

Archivo: `src/stores/counter.js`

Referencia oficial: [Defining a Store (Setup Stores)](https://pinia.vuejs.org/core-concepts/#defining-a-store).

```js
import { defineStore } from 'pinia'
import { ref, computed } from 'vue'

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

  return { count, name, doubleCount, increment, decrement }
})
```

Resumen:

- `ref()` -> estado
- `computed()` -> getters
- `function` -> actions

## Definir el store en TypeScript

Referencia oficial: [TypeScript](https://pinia.vuejs.org/core-concepts/state.html#typescript).

Archivo: `src/stores/counter.ts`

```ts
import { defineStore } from 'pinia'
import { ref, computed } from 'vue'

export const useCounterStore = defineStore('counter', () => {
  const count = ref<number>(0)
  const name = ref<string>('Usuario')

  const doubleCount = computed(() => count.value * 2)

  function increment() {
    count.value++
  }

  function decrement() {
    count.value--
  }

  function randomize() {
    count.value = Math.round(100 * Math.random())
  }

  return { count, name, doubleCount, increment, decrement, randomize }
})
```

Si usas `<script setup>`, recuerda `lang="ts"` en los componentes TypeScript.

## Uso del store en un componente padre

Referencia oficial: [Using the Store](https://pinia.vuejs.org/core-concepts/outside-component-usage.html).

Archivo: `src/components/ParentComponent.vue`

```vue
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
import { useCounterStore } from '@/stores/counter'
import ChildComponent from './ChildComponent.vue'

const counter = useCounterStore()
</script>
```

## Uso del store en un componente hijo

Referencia oficial: [State and Getters usage](https://pinia.vuejs.org/core-concepts/state.html).

Archivo: `src/components/ChildComponent.vue`

```vue
<template>
  <div>
    <h2>Componente Hijo</h2>
    <p>Valor del contador desde el hijo: {{ counter.count }}</p>
    <button @click="counter.increment">Incrementar desde el hijo</button>
  </div>
</template>

<script setup>
import { useCounterStore } from '@/stores/counter'

const counter = useCounterStore()
</script>
```

## Compartir store entre ramas distintas

Aunque los componentes no esten en la misma rama directa, pueden leer y modificar el mismo store.

Referencia oficial: [Stores outside components](https://pinia.vuejs.org/core-concepts/outside-component-usage.html).

```text
App.vue
├── BranchA.vue
│   └── ComponentA.vue
└── BranchB.vue
    └── ComponentB.vue
```

Componente A (incrementa):

```vue
<template>
  <div>
    <h2>Componente A (Rama A)</h2>
    <p>Contador compartido: {{ counter.count }}</p>
    <button @click="counter.increment">Incrementar</button>
  </div>
</template>

<script setup>
import { useCounterStore } from '@/stores/counter'

const counter = useCounterStore()
</script>
```

Componente B (decrementa):

```vue
<template>
  <div>
    <h2>Componente B (Rama B)</h2>
    <p>Contador compartido: {{ counter.count }}</p>
    <button @click="counter.decrement">Decrementar</button>
  </div>
</template>

<script setup>
import { useCounterStore } from '@/stores/counter'

const counter = useCounterStore()
</script>
```

## Consideraciones de uso

- Usa store solo para estado compartido real.
- Mantener estado local en componente cuando no se comparte mejora claridad.
- Evita reactividad innecesaria para reducir renders y mantener rendimiento.

## Referencias oficiales

- [Pinia Documentation](https://pinia.vuejs.org/)
- [Getting Started](https://pinia.vuejs.org/getting-started.html)
- [Core Concepts](https://pinia.vuejs.org/core-concepts/)
- [Defining Stores](https://pinia.vuejs.org/core-concepts/#defining-a-store)
- [State](https://pinia.vuejs.org/core-concepts/state.html)
- [Getters](https://pinia.vuejs.org/core-concepts/getters.html)
- [Actions](https://pinia.vuejs.org/core-concepts/actions.html)
