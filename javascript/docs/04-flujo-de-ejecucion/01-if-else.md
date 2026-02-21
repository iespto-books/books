---
title: "Condicional IF‑ELSE"
duration: "4 min"
---

# Condicional IF‑ELSE en JavaScript

La estructura `if … else` permite ejecutar bloques de código según una condición booleana.

```js
if (condición) {
  // código si la condición es verdadera
} else {
  // código si la condición es falsa
}
```

Puedes encadenar varios `else if` para múltiples casos:

```js
if (a > b) {
  console.log('a es mayor');
} else if (a < b) {
  console.log('b es mayor');
} else {
  console.log('a y b son iguales');
}
```

> En JavaScript la condición se evalúa como **truthy** o **falsy**.
