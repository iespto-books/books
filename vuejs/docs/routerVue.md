# Vue Router

Guia basica para enrutar aplicaciones Vue SPA (Single Page Application).

## 1. Introduccion

Vue Router es la libreria oficial de Vue para manejar navegacion entre vistas sin recargar la pagina.

## 2. Instalacion

En muchos proyectos con Vite ya viene integrado. Si no:

```bash
npm install vue-router
```

## 3. Configuracion basica

Archivo `src/router.js`:

```js
import { createRouter, createWebHistory } from 'vue-router'
import Home from './components/Home.vue'
import About from './components/About.vue'

const routes = [
  { path: '/', component: Home },
  { path: '/about', component: About },
]

const router = createRouter({
  history: createWebHistory(),
  routes,
})

export default router
```

Archivo `src/main.js`:

```js
import { createApp } from 'vue'
import App from './App.vue'
import router from './router'

createApp(App).use(router).mount('#app')
```

## 4. Uso de `<router-link>` y `<router-view>`

### Navegacion con `<router-link>`

```vue
<template>
  <nav>
    <router-link to="/">Home</router-link>
    <router-link to="/about">About</router-link>
  </nav>
</template>
```

### Render dinamico con `<router-view>`

```vue
<template>
  <div>
    <Navbar />
    <router-view />
  </div>
</template>
```

## 5. Rutas con parametros

Definicion de ruta dinamica:

```js
const routes = [
  { path: '/user/:id', component: UserProfile },
]
```

Acceso al parametro en componente:

```vue
<template>
  <h1>Usuario ID: {{ $route.params.id }}</h1>
</template>
```

## 6. Redirecciones y rutas no encontradas

```js
{ path: '/home', redirect: '/' }
{ path: '/:pathMatch(.*)*', component: NotFound }
```

## 7. Anidacion de rutas

Configuracion:

```js
const routes = [
  {
    path: '/dashboard',
    component: Dashboard,
    children: [
      { path: 'stats', component: Stats },
      { path: 'settings', component: Settings },
    ],
  },
]
```

Vista anidada:

```vue
<template>
  <div>
    <h1>Dashboard</h1>
    <router-link to="/dashboard/stats">Stats</router-link>
    <router-link to="/dashboard/settings">Settings</router-link>
    <router-view />
  </div>
</template>
```

## 8. Proteccion de rutas (Route Guards)

Guardia global:

```js
router.beforeEach((to, from, next) => {
  if (to.path === '/protected' && !isLoggedIn()) {
    next('/login')
  } else {
    next()
  }
})
```

## 9. Meta fields

Puedes agregar metadata a las rutas para reglas de acceso u otra logica:

```js
const routes = [
  { path: '/admin', component: Admin, meta: { requiresAuth: true } },
]

router.beforeEach((to, from, next) => {
  if (to.meta.requiresAuth && !isLoggedIn()) {
    next('/login')
  } else {
    next()
  }
})
```

## 10. Transiciones entre rutas

```vue
<template>
  <transition name="fade">
    <router-view />
  </transition>
</template>

<style>
.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.5s;
}

.fade-enter,
.fade-leave-to {
  opacity: 0;
}
</style>
```

## 11. Rutas dinamicas avanzadas con `props`

Definicion de ruta pasando parametros como props:

```js
const routes = [
  { path: '/user/:id', component: UserProfile, props: true },
]
```

Componente `UserProfile`:

```vue
<template>
  <h1>Usuario ID: {{ id }}</h1>
</template>

<script setup>
defineProps(['id'])
</script>
```
