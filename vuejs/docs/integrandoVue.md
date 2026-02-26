# Integrando Vue

## 1. Desde CDN

Puedes usar Vue directamente desde un CDN mediante una etiqueta `script`:

```html
<script src="https://unpkg.com/vue@3/dist/vue.global.js"></script>
```

En este ejemplo se usa `unpkg`, pero también puedes utilizar otros CDN que publiquen paquetes de npm (por ejemplo, `jsdelivr` o `cdnjs`). También puedes descargar el archivo y servirlo localmente.

Cuando se utiliza Vue desde un CDN no hay paso de compilación. Esto simplifica la configuración y encaja bien para mejorar HTML estático o integrarlo con un backend existente. Como contrapartida, no podrás usar sintaxis de Componentes de Archivo único (SFC).

### Usando la compilación global

El enlace anterior carga la compilación global de Vue, donde las APIs de alto nivel quedan disponibles como propiedades del objeto global `Vue`.

```html
<script src="https://unpkg.com/vue@3/dist/vue.global.js"></script>

<div id="app">{{ message }}</div>

<script>
  const { createApp, ref } = Vue

  createApp({
    setup() {
      const message = ref('Hola Vue!')
      return { message }
    }
  }).mount('#app')
</script>
```

### Usando el modulo de construcción ES

La mayoría de navegadores modernos soportan módulos ES de forma nativa, por lo que Vue puede cargarse también como módulo.

```html
<script type="importmap">
{
  "imports": {
    "vue": "https://unpkg.com/vue@3/dist/vue.esm-browser.js"
  }
}
</script>

<div id="app">{{ message }}</div>

<script type="module">
  import { createApp, ref } from 'https://unpkg.com/vue@3/dist/vue.esm-browser.js'

  createApp({
    setup() {
      const message = ref('Hola Vue!')
      return { message }
    }
  }).mount('#app')
</script>
```

Con `script type="importmap"` le indicas al navegador desde donde resolver las importaciones.

## 2. Usando npm para crear una aplicación de Vue

Asegúrate de tener instalada una versión actualizada de Node.js y situarte en el directorio donde quieras crear el proyecto.

```bash
npm create vue@latest
```

Este comando instala y ejecuta `create-vue`, la herramienta oficial de scaffolding de Vue. Durante el proceso se te preguntara por opciones como TypeScript o soporte de pruebas.

Una vez creado el proyecto, sigue las instrucciones del asistente para instalar dependencias e iniciar el servidor de desarrollo.

Los componentes de ejemplo generados por defecto usan `Composition API` y `script setup`.

## Pluggins de Vue para Visual Studio Code

Configuración recomendada de extensiones para VS Code:

- `Vue (Official)` - `vuejs.org`
- `Vue 3 Snippets` - `hollowtree`
- `Vue VSCode Snippets` - `sarah.drasner`

## Componentes de archivo único (SFC)

Un Single File Component (SFC o en español Componente de archivo único) es un archivo `.vue` que agrupa tres bloques:

- `template`: contenido HTML
- `script`: logica del componente
- `style`: estilos CSS

Este formato facilita el desarrollo en proyectos grandes porque mejora la organización y la mantenibilidad del código.

Ventajas practicas:

- Mejor gestión de plantillas y componentes a medida que crece el proyecto.
- Flujo de desarrollo moderno con servidor local.
- Actualización inmediata al guardar cambios (HMR), sin recargar manualmente.
- Es el enfoque habitual en aplicaciones Vue reales.

Los SFC no se ejecutan directamente en el navegador: necesitas un entorno de compilación que transforme los `.vue` en recursos que el navegador pueda interpretar.

### Proyecto Composition API sin formato SFC

Este ejemplo se puede ejecutar directamente en un archivo HTML con Vue 3 cargado por CDN.

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Vue Composition API Example</title>
  <script src="https://unpkg.com/vue@3"></script>
</head>
<body>
  <div id="app">
    <p>{{ message }}</p>
    <button @click="increment">Click Count: {{ count }}</button>
  </div>

  <script>
    const { createApp, ref } = Vue

    createApp({
      setup() {
        const message = ref('Hello, Vue with Composition API!')
        const count = ref(0)

        function increment() {
          count.value++
        }

        return { message, count, increment }
      }
    }).mount('#app')
  </script>
</body>
</html>
```

### Proyecto Composition API con formato SFC

Este ejemplo usa un componente `.vue` con `template`, `script setup` y `style`.

Para que funcione, debes usar un servidor de desarrollo (por ejemplo, Vite). No basta con abrir `index.html` directamente, porque necesitas compilación de `.vue` y resolución de módulos.

```bash
npm create vite@latest my-vue-app --template vue
cd my-vue-app
npm install
npm run dev
```

Estructura básica:

```text
/project-root
  /src
    Hola.vue
    main.js
  index.html
```

`index.html`:

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Vue App</title>
</head>
<body>
  <div id="app"></div>
  <script type="module" src="/src/main.js"></script>
</body>
</html>
```

`main.js`:

```js
import { createApp } from 'vue'
import Hola from './Hola.vue'

createApp(Hola).mount('#app')
```

`Hola.vue`:

```vue
<template>
  <div>
    <p>{{ message }}</p>
    <button @click="increment">Click Count: {{ count }}</button>
  </div>
</template>

<script setup>
import { ref } from 'vue'

const message = ref('Hello, Vue with Composition API and SFC!')
const count = ref(0)

function increment() {
  count.value++
}
</script>

<style scoped>
button {
  margin-top: 10px;
  padding: 5px 10px;
  font-size: 16px;
}
</style>
```
