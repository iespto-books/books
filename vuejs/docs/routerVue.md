Vue Router
Índice
0. Introducción......................................................................................................................................2
1. Instalación.........................................................................................................................................2
2. Configuración básica....................................................................................................................... .2
3. Uso de `<router-link>` y `<router-view>`....................................................................................... .3
Navegación con `<router-link>`..................................................................................................... .3
Mostrar contenido dinámico con `<router-view>`...........................................................................3
4. Rutas con parámetros...................................................................................................................... .3
5. Redirecciones y rutas no encontradas...............................................................................................4
6. Anidación de rutas........................................................................................................................... .4
7. Protección de rutas (Route Guards)..................................................................................................4
8. Meta fields....................................................................................................................................... .5
9. Transiciones entre rutas................................................................................................................... .5
10. Rutas dinámicas avanzadas........................................................................................................... .5

1


0. Introducción
Vue Router es la biblioteca oficial de Vue.js para manejar el enrutamiento en aplicaciones
SPA (Single Page Application). Permite a los desarrolladores definir rutas y asociarlas con
componentes para crear experiencias de usuario dinámicas y fluidas.

1. Instalación
Si estás usando un proyecto con Vite o Vue CLI, Vue Router generalmente está incluido. Si no,
instálalo con npm:
npm install vue-router

2. Configuración básica
Configuración de un archivo `router.js`:
// src/router.js
import { createRouter, createWebHistory } from 'vue-router';
import Home from './components/Home.vue';
import About from './components/About.vue';
const routes = [
{ path: '/', component: Home },
{ path: '/about', component: About },
];
const router = createRouter({
history: createWebHistory(),
routes,
});
export default router;
Importar el enrutador en `main.js`:
// src/main.js
import { createApp } from 'vue';
import App from './App.vue';
import router from './router';
createApp(App).use(router).mount('#app');

2


3. Uso de `<router-link>` y `<router-view>`
Navegación con `<router-link>`
Se utiliza para cambiar entre rutas sin recargar la página.
<template>
<nav>
<router-link to="/">Home</router-link>
<router-link to="/about">About</router-link>
</nav>
</template>

Mostrar contenido dinámico con `<router-view>`
Coloca `<router-view>` donde deseas renderizar los componentes según la ruta activa.
<template>
<div>
<Navbar />
<router-view />
</div>
</template>

4. Rutas con parámetros
Se pueden pasar parámetros dinámicos a través de la URL.
Configurar rutas con parámetros:
const routes = [
{ path: '/user/:id', component: UserProfile },
];
Acceder a parámetros en el componente:
<template>
<div>
<h1>Usuario ID: {{ $route.params.id }}</h1>
</div>
</template>

3


5. Redirecciones y rutas no encontradas
Redirección:
{ path: '/home', redirect: '/' }
Rutas no encontradas (`404`):
{ path: '/:pathMatch(.*)*', component: NotFound }

6. Anidación de rutas
Permite crear subrutas dentro de componentes.
Configuración de rutas anidadas:
const routes = [
{
path: '/dashboard',
component: Dashboard,
children: [
{ path: 'stats', component: Stats },
{ path: 'settings', component: Settings },
], }, ];
Uso de `<router-view>` anidado:
<template>
<div>
<h1>Dashboard</h1>
<router-link to="/dashboard/stats">Stats</router-link>
<router-link to="/dashboard/settings">Settings</router-link>
<router-view />
</div>
</template>

7. Protección de rutas (Route Guards)
Se pueden usar para restringir el acceso a rutas específicas.
Ejemplo de guardia global:
router.beforeEach((to, from, next) => {
if (to.path === '/protected' && !isLoggedIn()) {
next('/login');
} else {
next();
}
});
4


8. Meta fields
Las rutas pueden incluir campos personalizados para añadir lógica adicional.
Ejemplo con meta:
const routes = [
{ path: '/admin', component: Admin, meta: { requiresAuth: true } },
];
router.beforeEach((to, from, next) => {
if (to.meta.requiresAuth && !isLoggedIn()) {
next('/login');
} else {
next();
}
});

9. Transiciones entre rutas
Se pueden usar animaciones CSS para transiciones.
Ejemplo con `transition`:
<template>
<transition name="fade">
<router-view />
</transition>
</template>
<style>
.fade-enter-active, .fade-leave-active {
transition: opacity 0.5s;
}
.fade-enter, .fade-leave-to {
opacity: 0;
}
</style>

10. Rutas dinámicas avanzadas
Renderización condicional con `props`:
const routes = [
{ path: '/user/:id', component: UserProfile, props: true },
];

5


Componente `UserProfile`:
<template>
<div>
<h1>Usuario ID: {{ id }}</h1>
</div>
</template>
<script setup>
defineProps(['id']);
</script>

6


