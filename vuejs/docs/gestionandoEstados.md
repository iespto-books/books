# Gestion del Estado en Vue.js

Guia practica para entender y usar `ref`, `reactive`, `computed` y `watch` en Vue 3.

## Introduccion

La reactividad es el nucleo de Vue.js. Gracias a ella, la interfaz se actualiza automaticamente cuando cambian los datos.

En esta guia veras:

- `ref`: para valores simples reactivos.
- `reactive`: para objetos y estructuras complejas.
- `computed`: para valores derivados.
- `watch`: para ejecutar efectos secundarios al detectar cambios.

## Uso de `ref`

### Que es

`ref` crea una referencia reactiva a un valor (numero, texto, booleano u objeto).

- El valor se guarda en `.value` dentro del script.
- En el template, Vue desenvuelve ese valor automaticamente.

### Para que se usa

- Manejar valores simples reactivos.
- Compartir una variable reactiva entre funciones o composables.

### Ejemplo practico

```vue
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
```

Uso directo en template:

```vue
<p>{{ count }}</p>
<button @click="increment">Incrementar</button>
```

### Otros ejemplos

1. Crear una variable reactiva: `const count = ref(0)`
2. Enlazarla en la UI: `<button @click="count++">{{ count }}</button>`
3. Actualizar su valor: `count.value = 10`

## Uso de `reactive`

### Que es

`reactive` convierte un objeto completo en reactivo.

- Observa cambios en todas sus propiedades.
- No requiere `.value` para acceder a sus campos.

### Para que se usa

- Trabajar con objetos o arrays reactivos.
- Mantener estructuras de datos mas naturales en el codigo.

### Limitaciones


### Ejemplo practico

```vue
<template>
  <div>
    <p>Framework: {{ state.name }}</p>
    <p>Version: {{ state.version }}</p>
    <button @click="updateVersion">Actualizar version</button>
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
```

Uso directo en template:

```vue
<p>{{ state.name }} v{{ state.version }}</p>
<button @click="updateVersion">Actualizar version</button>
```

### Otros ejemplos

1. Crear objeto reactivo: `const state = reactive({ name: 'Vue.js', version: 3 })`
2. Actualizar propiedad: `state.version = 4`
3. Mostrar en interfaz: `<p>{{ state.name }} v{{ state.version }}</p>`

## Uso de `computed`

### Que es

`computed` devuelve un valor calculado a partir de otros datos reactivos.

- Se recalcula cuando cambian sus dependencias.
- Evita repetir logica derivada en el template.

### Para que se usa

- Calculos reactivos automaticos.
- Mantener el template limpio y expresivo.

### Ejemplo practico

```vue
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
```

Uso directo en template:

```vue
<p>Original: {{ count }}</p>
<p>Doble: {{ doubleCount }}</p>
```

### Otros ejemplos

1. `const doubleCount = computed(() => count.value * 2)`
2. `<p>Doble: {{ doubleCount }}</p>`
3. `const formatted = computed(() => `${state.name} ${state.version}`)`

## Uso de `watch`

### Que es

`watch` observa cambios en una o mas fuentes reactivas y ejecuta una funcion cuando cambian.

- No devuelve un valor derivado.
- Sirve para efectos secundarios.

### Para que se usa

- Llamadas a API.
- Validaciones.
- Persistencia de datos.
- Logs y trazas.

### Ejemplo practico

```vue
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
  console.log(`El valor cambio de ${oldVal} a ${newVal}`)
})

const increment = () => {
  count.value++
}
</script>
```

Uso directo en template:

```vue
<p>{{ count }}</p>
<button @click="increment">Incrementar</button>
```

### Otros ejemplos

1. `watch(count, (newVal, oldVal) => console.log(newVal, oldVal))`
2. `watch(() => state.version, (newVal) => console.log(newVal))`
3. `watch(() => state.name, () => fetchData())`

## Comparativa rapida

| Concepto    | Que controla         | Cuando usarlo |
|-------------|----------------------|---------------|
| `ref`       | Valor simple         | Para valores individuales (numero, texto, booleano). |
| `reactive`  | Objetos / estructuras| Para objetos complejos o arrays reactivos. |
| `computed`  | Valores derivados    | Para calculos en base a otros datos reactivos. |
| `watch`     | Efectos secundarios  | Para reaccionar a cambios (API, validaciones, persistencia). |
