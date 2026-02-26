---
title: Introducción
---

# Introducción a Vue.js

Vue.js es un framework frontend progresivo orientado a la construcción de interfaces reactivas y aplicaciones SPA.
En su versión moderna (Vue 3), implementa un sistema de reactividad basado en `Proxy`, con seguimiento fino de dependencias (`track`) y disparo de efectos (`trigger`), lo que permite actualizaciones eficientes del árbol de componentes sin manipulación manual del DOM.

Referencia oficial: [Vue Guide - Introduction](https://vuejs.org/guide/introduction.html).

## Arquitectura de componentes

Su arquitectura gira en torno a componentes encapsulados, normalmente definidos como `Single File Components` (SFC) cuyos ficheros tienen extensión `.vue` y donde plantilla, lógica y estilos coexisten de forma cohesionada.
El compilador de plantillas transforma sintaxis declarativa en funciones de render optimizadas, y el runtime se encarga del proceso de patching sobre un Virtual DOM.

Referencia oficial: [Vue Guide - Single-File Components](https://vuejs.org/guide/scaling-up/sfc.html).

## Ecosistema técnico

En el ecosistema de Vue destacan:

- [`Vue Router`](https://router.vuejs.org/): enrutamiento declarativo y lazy loading de vistas.
- [`Pinia`](https://pinia.vuejs.org/): store reactivo, tipable y modular para estado global.
- [`Vite`](https://vite.dev/): bundler/dev server de baja latencia (ESM nativo + HMR rápido).
- [`Nuxt`](https://nuxt.com/): capa superior para SSR, SSG e híbridos con enfoque full-stack.

## Modelos de desarrollo

A nivel de diseño de software, Vue ofrece dos modelos principales:

- `Options API`: organiza el componente por opciones (`data`, `methods`, `computed`, `watch` y hooks de ciclo de vida), separando responsabilidades por tipo y está plenamente soportada en Vue 3.
- `Composition API`: organiza la lógica con primitivas reactivas y composables; la documentación la presenta como especialmente útil para reutilización y TypeScript.

Referencias oficiales: [Vue Guide - Essentials](https://vuejs.org/guide/essentials/component-basics.html), [Vue Guide - Composition API](https://vuejs.org/guide/extras/composition-api-faq.html).

### Modelo mental

- `Options API`: separa responsabilidades por tipo de opción dentro del componente.
- `Composition API`: permite agrupar responsabilidades por feature o dominio, normalmente mediante composables.

### Cuándo usar cada una

#### Casos recomendados para `Options API`

- Componentes con lógica acotada (por ejemplo, vistas CRUD simples).
- Bases de código heredadas de Vue 2/2.7 que migran gradualmente a Vue 3.
- Equipos que prefieren una estructura guiada por opciones dentro de cada componente.

#### Casos recomendados para `Composition API`

- Componentes con estado y efectos complejos.
- Escenarios con reutilización explícita de lógica entre módulos (auth, filtros, paginación, sockets, etc.).
- Proyectos con TypeScript y arquitectura orientada a dominio.

### Cuál es mejor

No existe una respuesta universal. En Vue 3:

- La documentación oficial muestra ambas como válidas en Vue 3, con diferentes trade-offs de organización.
- En práctica, `Composition API` se usa con frecuencia para lógica reutilizable/avanzada y `Options API` sigue siendo habitual en componentes más directos.

### Rendimiento y mantenibilidad

- Ambas APIs comparten el runtime y el sistema de reactividad de Vue 3.
- Las diferencias de rendimiento entre APIs suelen ser menores que el impacto de decisiones de diseño (watchers excesivos, renders innecesarios o estado mal segmentado).

### Reutilización de lógica

- En `Options API`, la reutilización tradicional con mixins puede reducir trazabilidad y provocar colisiones de nombres.
- En `Composition API`, los composables (`useXxx`) hacen explícitas las dependencias y mejoran la separación de responsabilidades.

### TypeScript y experiencia de desarrollo

- `Composition API` con `<script setup>` ofrece mejor inferencia de tipos y ergonomía en escenarios complejos.
- `Options API` también admite TypeScript, pero su inferencia suele ser menos expresiva en casos avanzados.

Referencias oficiales: [Vue Guide - TypeScript](https://vuejs.org/guide/typescript/overview.html), [Vue Guide - Composition API with TypeScript](https://vuejs.org/guide/typescript/composition-api.html).

### Estrategia de adopción

- Ambas APIs pueden convivir en la misma base de código.
- En migraciones, ambas pueden coexistir y adoptarse de forma incremental.
- Conviene priorizar cambios con retorno claro de mantenibilidad o reutilización.

## Conclusión

En términos prácticos, la documentación y el ecosistema de Vue 3 muestran un framework apto tanto para integración incremental en sistemas existentes como para aplicaciones frontend modernas.

## Referencias oficiales

- [Vue Documentation](https://vuejs.org/guide/introduction.html)
- [Vue API Reference](https://vuejs.org/api/)
- [Vue Router Documentation](https://router.vuejs.org/guide/)
- [Pinia Documentation](https://pinia.vuejs.org/)
- [TypeScript con Vue](https://vuejs.org/guide/typescript/overview.html)
