# Analizando la estructura de un proyecto
# Vite + Vue + JS

Guia para entender la organizacion basica de un proyecto Vue y el papel de sus archivos principales.

## Estructura de carpetas

- `node_modules`: dependencias del proyecto.
- `cypress`: configuracion y pruebas end-to-end en frontend.
- `public`: recursos publicos como `index.html` y `favicon`.
- `src`: codigo fuente principal de la aplicacion.
- `src/router`: definicion de rutas (URL -> componente).
- `src/assets`: imagenes, documentos y otros recursos.
- `src/components`: componentes reutilizables.
- `src/App.vue`: componente raiz de la app.
- `src/main.js`: punto de entrada principal.
- Archivos de configuracion en raiz: `.gitignore`, `package.json`, `jsconfig.json`, etc.

## 1. Entrada al proyecto: `index.html`

`index.html` es el archivo inicial que carga la aplicacion.

- En el `body` se encuentra el contenedor donde Vue monta la app.
- Tambien carga el script principal que apunta a `src/main.js`.

## 2. El fichero `main.js`

`main.js` arranca la aplicacion Vue.

Funciones principales:

- Importar Vue y el componente raiz `App.vue`.
- Importar estilos globales.
- Registrar plugins como Router y Pinia.
- Montar la app en el elemento con id `app`.

Ejemplo tipico:

```js
import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import { createPinia } from 'pinia'

const app = createApp(App)
app.use(createPinia())
app.use(router)
app.mount('#app')
```

## 3. El fichero `App.vue`

`App.vue` es el componente raiz y sigue el formato SFC (Single File Component):

- `<template>`: estructura visual.
- `<script>` o `<script setup>`: logica del componente.
- `<style>`: estilos del componente.

### 3.1 Template de `App.vue`

El template define el HTML renderizado por Vue.

Ejemplo:

```vue
<template>
  <h1>You did it!</h1>
  <p>
    Visit <a href="https://vuejs.org/" target="_blank" rel="noopener">vuejs.org</a>
    to read the documentation
  </p>
  <ButtonAutoCount />
</template>
```

En este caso se usa el componente `<ButtonAutoCount />`, que vive en `src/components`.

### 3.2 Script de `App.vue`

En el script se importan componentes y dependencias.

```vue
<script setup lang="ts">
import ButtonAutoCount from './components/ButtonAutoCount.vue'
</script>
```

### 3.3 Style de `App.vue`

- `<style scoped>` aplica estilos solo al componente actual.
- Evita colisiones con estilos de otros componentes.
- Los estilos globales suelen estar en archivos CSS de `src`.

## 4. El componente `ButtonAutoCount.vue`

Este componente tambien sigue la estructura SFC.

### 4.1 Script del componente

```vue
<script setup lang="ts">
import { ref } from 'vue'

const count = ref(0)
</script>
```

Notas importantes:

- `<script setup>` simplifica y optimiza el uso de Composition API.
- `ref` crea una variable reactiva.
- `count` se inicializa en `0` y cambia en tiempo real en la UI.

### 4.2 Template del componente

```vue
<template>
  <div>
    <button data-test="btn-auto-count" @click="count++">
      Pulsado {{ count }} veces
    </button>
  </div>
</template>
```

Elementos clave:

- `data-test="btn-auto-count"`: ayuda a localizar el boton en pruebas.
- `@click="count++"`: escucha click y aumenta el contador.
- `{{ count }}`: interpolacion para mostrar el valor reactivo.

## Resumen

La app Vue arranca en `index.html` y `main.js`, usa `App.vue` como raiz y se compone de componentes en `src/components`. Con `ref` y eventos como `@click`, la interfaz se actualiza de forma reactiva y sencilla.
