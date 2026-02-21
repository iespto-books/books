---
title: Introducción
---

# Introducción a Vue.js

Vue.js es un framework frontend progresivo orientado a la construcción de interfaces reactivas y aplicaciones SPA.
En su versión moderna (Vue 3), implementa un sistema de reactividad basado en `Proxy`, con seguimiento fino de dependencias (`track`) y disparo de efectos (`trigger`), lo que permite actualizaciones eficientes del árbol de componentes sin manipulación manual del DOM.

## Arquitectura de componentes

Su arquitectura gira en torno a componentes encapsulados, normalmente definidos como `Single File Components` (`.vue`), donde plantilla, lógica y estilos coexisten de forma cohesionada.
El compilador de plantillas transforma sintaxis declarativa en funciones de render optimizadas, y el runtime se encarga del proceso de patching sobre un Virtual DOM.

## Modelos de desarrollo

A nivel de diseño de software, Vue ofrece dos modelos principales:

- `Options API`: útil para adopción gradual y código guiado por convenciones.
- `Composition API`: más adecuada para lógica compleja, reutilización mediante composables y mejor tipado con TypeScript.

## Ecosistema técnico

En el ecosistema de Vue destacan:

- `Vue Router`: enrutamiento declarativo y lazy loading de vistas.
- `Pinia`: store reactivo, tipable y modular para estado global.
- `Vite`: bundler/dev server de baja latencia (ESM nativo + HMR rápido).
- `Nuxt`: capa superior para SSR, SSG e híbridos con enfoque full-stack.

## Options API vs Composition API

### Qué son

- `Options API`: organiza un componente por opciones (`data`, `computed`, `methods`, `watch` y hooks de ciclo de vida), separando responsabilidades por tipo.
- `Composition API`: organiza por feature o lógica de dominio usando `setup()`, `ref`, `reactive`, `computed`, `watch` y composables reutilizables.

### Modelo mental

- `Options API`: enfoque declarativo guiado por convención; suele ser más directo en componentes pequeños o medianos.
- `Composition API`: enfoque componible/funcional; facilita extraer y compartir lógica compleja entre componentes.

### Cuándo usar cada una

#### Casos recomendados para `Options API`

- Componentes simples o formularios CRUD con baja complejidad transversal.
- Equipos con onboarding inicial en Vue o bases heredadas de Vue 2/2.7.
- Escenarios donde prima la claridad inmediata del componente.

#### Casos recomendados para `Composition API`

- Componentes con estado complejo, múltiples efectos y reglas de negocio.
- Necesidad de reutilizar lógica entre módulos (auth, filtros, paginación, sockets, etc.).
- Proyectos con TypeScript estricto, pruebas unitarias de lógica y arquitectura por dominio.

### Cuál es mejor

No existe una respuesta universal. En Vue 3:

- Para escalabilidad, mantenibilidad y TypeScript en proyectos complejos, `Composition API` suele ser superior.
- Para simplicidad de arranque y componentes de baja complejidad, `Options API` puede resultar más rápida de adoptar.

### Rendimiento y mantenibilidad

- Ambas APIs comparten el runtime y el sistema de reactividad de Vue 3.
- Las diferencias de rendimiento suelen ser menores frente a decisiones de diseño (watchers excesivos, renders innecesarios o estado mal segmentado).

### Reutilización de lógica

- En `Options API`, la reutilización tradicional con mixins puede reducir trazabilidad y provocar colisiones de nombres.
- En `Composition API`, los composables (`useXxx`) hacen explícitas las dependencias y mejoran la separación de responsabilidades.

### TypeScript y experiencia de desarrollo

- `Composition API` con `<script setup>` ofrece mejor inferencia de tipos y ergonomía en escenarios complejos.
- `Options API` también admite TypeScript, pero su inferencia suele ser menos expresiva en casos avanzados.

### Estrategia de adopción

- Ambas APIs pueden convivir en la misma base de código.
- En migraciones, es habitual mantener componentes estables en `Options API` y aplicar `Composition API` en módulos nuevos o de mayor complejidad.
- Evita reescrituras masivas sin retorno claro; prioriza migración incremental guiada por valor de negocio.

## Conclusión

En términos prácticos, Vue ofrece una buena relación entre ergonomía, rendimiento y mantenibilidad, siendo adecuado tanto para integración incremental en sistemas legacy como para arquitecturas frontend modernas completas.
