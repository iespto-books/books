Aspectos de Vue - Props y Emit

Índice
Paso de parámetros de Padre a Hijo (Props)	2
¿Qué son las Props?	2
¿Cómo se usa?	2
Ejemplo 1: Paso de una Variable	2
Ejemplo 2: Paso de un Objeto	3
Ejemplo 3: Paso de Varios Parámetros	3
Paso de parámetros de Hijo a Padre (Emit)	3
¿Qué es y cómo se usa?	3
Ejemplo 1: Paso de una Variable	4
Ejemplo 2: Paso de un Objeto	4
Ejemplo 3: Paso de Varios Parámetros	5

Paso de parámetros de Padre a Hijo (Props)
En Vue.js, el paso de parámetros de padre a hijo (Props) es una forma de enviar datos desde un componente padre a un componente hijo. Las props son atributos que se definen en el componente hijo y se pasan desde el componente padre, permitiendo a los componentes comunicarse y compartir datos.

¿Qué son las Props?
Las props son la forma en que los componentes Vue pueden recibir datos de sus componentes padres.
Se definen en el componente hijo y se pasan desde el componente padre como atributos del componente.
Las props pueden ser de cualquier tipo, como valores primitivos (números, cadenas, booleanos), objetos, arreglos, funciones, etc.

¿Cómo se usa?
    1. Declarar Props en el Componente Hijo: Se utiliza `defineProps` (en la Composition API) o se define un objeto `props` (en la Options API) para especificar qué props espera el componente hijo.
    2. Pasar Props desde el Componente Padre: Se pasan como atributos al componente hijo en el template del componente padre.

Ejemplo 1: Paso de una Variable

Componente Hijo (ChildComponent.vue)	Componente Padre (ParentComponent.vue)
<template>
<p>Mensaje: {{ message }}</p>
</template>	<template>
<ChildComponent message="Hola desde el padre" />
</template>
<script setup>
const props = defineProps({ message: String
});
</script>	<script setup>
import ChildComponent from './ChildComponent.vue';
</script>
Explicación: Se pasa una variable de tipo `String` llamada `message` desde el componente padre al hijo.
Ejemplo 2: Paso de un Objeto

Componente Hijo (ChildComponent.vue)	Componente Padre (ParentComponent.vue)
<template>
<p>Nombre: {{ user.name }}</p>
<p>Edad: {{ user.age }}</p>
</template>	<template>
<ChildComponent :user="{ name: 'Juan', age: 30 }" />
</template>
<script setup>
const props = defineProps({ user: Object
});
</script>	<script setup>
import ChildComponent from './ChildComponent.vue';
</script>
Explicación: Se pasa un objeto `user` que contiene las propiedades `name` y `age` desde el componente padre al hijo.
Ejemplo 3: Paso de Varios Parámetros

Componente Hijo (ChildComponent.vue)	Componente Padre (ParentComponent.vue)
<template>
<p>Título: {{ title }}</p>
<p>Descripción: {{ description }}</p>
<p>Puntuación: {{ rating }}</p>
</template>

<script setup>
const props = defineProps({ title: String,
description: String,
rating: Number
});
</script>	<template>
<ChildComponent title="Vue Props"
description="Aprender a pasar props en Vue"
:rating="4.5"
/>
</template>

<script setup>
import ChildComponent from './ChildComponent.vue';
</script>
Explicación: Se pasan múltiples props (`title`, `description` y `rating`) desde el componente padre al hijo.

Paso de parámetros de Hijo a Padre (Emit)
En Vue.js, el paso de parámetros de hijo a padre es una forma de enviar datos desde un componente hijo hacia un componente padre. Esto se logra mediante la emisión de eventos personalizados desde el componente hijo y la captura de estos eventos en el componente padre. Esta comunicación permite que el componente hijo notifique al padre sobre cambios o acciones que necesiten atención.

¿Qué es y cómo se usa?
    1. En el componente hijo, se emite un evento con emit utilizando defineEmits.
    2. En el componente padre, se escucha este evento y se ejecuta una función para manejar los datos enviados.
Ejemplo 1: Paso de una Variable

Componente Hijo (ChildComponent.vue)	Componente Padre (ParentComponent.vue)
<template>
<button @click="sendMessage">Enviar Mensaje</button>
</template>
<script setup lang="ts">
const emit = defineEmits<{
  'send-message': [string]
}>()
const sendMessage = () => {
  emit('send-message', 'Hola desde el hijo')
}
</script>	<template>
// (3)
<ChildComponent @send-message="handleMessage" />
<p>{{ message }}</p> // (6)
</template>

<script setup>
import { ref } from 'vue';
import ChildComponent from './ChildComponent.vue';

const message = ref('');
const handleMessage = (msg: string) => {
  message.value = msg
};
</script>

Explicación: Se emite un evento `send-message` con un mensaje desde el componente Hijo. El componente Padre escucha este evento y actualiza la variable `message`.

Ejemplo 2: Paso de un Objeto

Componente Hijo (ChildComponent.vue)	Componente Padre (ParentComponent.vue)
<template>
<button @click="sendUserData">Enviar Datos de Usuario</button> // (1)
</template>

<script setup>
const emit = defineEmits(); // (5)

const sendUserData = () => { // (2)
const user = { name: 'Juan', age: 30 }; // (3)
// Emitimos un evento con un objeto `user`
emit('send-user', user); // (4)
};
</script>	<template>
<ChildComponent @send-user="handleUser" /> // (6)
<p>Nombre: {{ user.name }}</p> // (10)
<p>Edad: {{ user.age }}</p>	// (10)
</template>

<script setup>
import { ref } from 'vue';
import ChildComponent from './ChildComponent.vue'; const user = ref({ name: '', age: 0 }); // (8)
const handleUser = (userData) => {	// (7)
// Capturamos y asignamos el objeto `user` al recibir el evento
user.value = userData; // (9)
};
</script>

Explicación: Se emite un evento `send-user` con un objeto `user` desde el hijo. El componente padre captura el evento y actualiza el objeto `user`.
Ejemplo 3: Paso de Varios Parámetros

Componente Hijo (ChildComponent.vue)	Componente Padre (ParentComponent.vue)
<template>
<button @click="sendMultipleData">Enviar Múltiples Datos</button> // (1)
</template>

<script setup>
const emit = defineEmits(); // (5)

const sendMultipleData = () => { // (2) const title = 'Vue.js'; // (3)
const description = 'Pasar múltiples datos de hijo a padre'; // (3)
const rating = 5; // (3)
// Emitimos un evento con varios parámetros
emit('send-data', title, description, rating); // (4)
};
</script>	<template>
<ChildComponent @send-data="handleData" /> // (6)
<p>Título: {{ title }}</p> // (10)
<p>Descripción: {{ description }}</p> // (10)
<p>Puntuación: {{ rating }}</p> // (10)
</template>
<script setup>
import { ref } from 'vue';
import ChildComponent from './ChildComponent.vue';

const title = ref('');	// (8) const description = ref(''); // (8) const rating = ref(0);   // (8)

const handleData = (t, d, r) => { // (7)
// Capturamos y asignamos el título
title.value = t; // (9)
// Capturamos y asignamos la descripción
description.value = d;	// (9)
// Capturamos y asignamos la puntuación
rating.value = r;	// (9)
};
</script>

Explicación: Se emite un evento `send-data` con múltiples parámetros (un título, una descripción y una puntuación). El componente padre captura estos datos y actualiza las variables correspondientes.
