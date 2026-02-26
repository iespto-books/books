# Props y Emits en Vue

Guia practica para comunicar componentes en Vue:

- De padre a hijo con `props`.
- De hijo a padre con `emit`.

## 1) Paso de datos de Padre a Hijo (`props`)

### Que son las props

Las `props` son la forma estandar de enviar datos desde un componente padre a uno hijo.

- Se definen en el componente hijo.
- Se pasan como atributos desde el padre.
- Admiten tipos simples y complejos (String, Number, Object, Array, etc.).

### Como se usan

1. En el hijo se declaran con `defineProps`.
2. En el padre se pasan como atributos del componente hijo.

### Ejemplo 1: pasar una variable

Componente hijo (`ChildComponent.vue`):

```vue
<template>
  <p>Mensaje: {{ message }}</p>
</template>

<script setup>
defineProps({
  message: String,
})
</script>
```

Componente padre (`ParentComponent.vue`):

```vue
<template>
  <ChildComponent message="Hola desde el padre" />
</template>

<script setup>
import ChildComponent from './ChildComponent.vue'
</script>
```

### Ejemplo 2: pasar un objeto

Componente hijo (`ChildComponent.vue`):

```vue
<template>
  <p>Nombre: {{ user.name }}</p>
  <p>Edad: {{ user.age }}</p>
</template>

<script setup>
defineProps({
  user: Object,
})
</script>
```

Componente padre (`ParentComponent.vue`):

```vue
<template>
  <ChildComponent :user="{ name: 'Juan', age: 30 }" />
</template>

<script setup>
import ChildComponent from './ChildComponent.vue'
</script>
```

### Ejemplo 3: pasar varios parametros

Componente hijo (`ChildComponent.vue`):

```vue
<template>
  <p>Titulo: {{ title }}</p>
  <p>Descripcion: {{ description }}</p>
  <p>Puntuacion: {{ rating }}</p>
</template>

<script setup>
defineProps({
  title: String,
  description: String,
  rating: Number,
})
</script>
```

Componente padre (`ParentComponent.vue`):

```vue
<template>
  <ChildComponent
    title="Vue Props"
    description="Aprender a pasar props en Vue"
    :rating="4.5"
  />
</template>

<script setup>
import ChildComponent from './ChildComponent.vue'
</script>
```

## 2) Paso de datos de Hijo a Padre (`emit`)

### Que es y como se usa

Cuando el hijo necesita notificar algo al padre, emite eventos personalizados.

1. El hijo define eventos con `defineEmits`.
2. El padre escucha esos eventos con `@evento="handler"`.

### Ejemplo 1: emitir una variable

Componente hijo (`ChildComponent.vue`):

```vue
<template>
  <button @click="sendMessage">Enviar mensaje</button>
</template>

<script setup lang="ts">
const emit = defineEmits<{
  'send-message': [string]
}>()

const sendMessage = () => {
  emit('send-message', 'Hola desde el hijo')
}
</script>
```

Componente padre (`ParentComponent.vue`):

```vue
<template>
  <ChildComponent @send-message="handleMessage" />
  <p>{{ message }}</p>
</template>

<script setup lang="ts">
import { ref } from 'vue'
import ChildComponent from './ChildComponent.vue'

const message = ref('')

const handleMessage = (msg: string) => {
  message.value = msg
}
</script>
```

### Ejemplo 2: emitir un objeto

Componente hijo (`ChildComponent.vue`):

```vue
<template>
  <button @click="sendUserData">Enviar datos de usuario</button>
</template>

<script setup>
const emit = defineEmits(['send-user'])

const sendUserData = () => {
  const user = { name: 'Juan', age: 30 }
  emit('send-user', user)
}
</script>
```

Componente padre (`ParentComponent.vue`):

```vue
<template>
  <ChildComponent @send-user="handleUser" />
  <p>Nombre: {{ user.name }}</p>
  <p>Edad: {{ user.age }}</p>
</template>

<script setup>
import { ref } from 'vue'
import ChildComponent from './ChildComponent.vue'

const user = ref({ name: '', age: 0 })

const handleUser = (userData) => {
  user.value = userData
}
</script>
```

### Ejemplo 3: emitir varios parametros

Componente hijo (`ChildComponent.vue`):

```vue
<template>
  <button @click="sendMultipleData">Enviar multiples datos</button>
</template>

<script setup>
const emit = defineEmits(['send-data'])

const sendMultipleData = () => {
  const title = 'Vue.js'
  const description = 'Pasar multiples datos de hijo a padre'
  const rating = 5

  emit('send-data', title, description, rating)
}
</script>
```

Componente padre (`ParentComponent.vue`):

```vue
<template>
  <ChildComponent @send-data="handleData" />
  <p>Titulo: {{ title }}</p>
  <p>Descripcion: {{ description }}</p>
  <p>Puntuacion: {{ rating }}</p>
</template>

<script setup>
import { ref } from 'vue'
import ChildComponent from './ChildComponent.vue'

const title = ref('')
const description = ref('')
const rating = ref(0)

const handleData = (t, d, r) => {
  title.value = t
  description.value = d
  rating.value = r
}
</script>
```

## Resumen rapido

- `props`: datos entran al componente hijo.
- `emit`: eventos salen del hijo hacia el padre.
- Regla practica: estado baja por `props`, eventos suben por `emit`.
