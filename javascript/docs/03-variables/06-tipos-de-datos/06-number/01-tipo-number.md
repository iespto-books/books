---
title: "Tipo Number"
duration: "5 min"
---

# Tipo Number en JavaScript

`Number` es el tipo primitivo que representa **todos los números**, enteros y de punto flotante, utilizando la representación IEEE‑754 de doble precisión.

## Características principales

- **Ordenamiento**: Los números pueden compararse con los operadores de comparación.
- **Precisión**: Hasta 53 bits de precisión manteniendo exactitud para enteros de hasta `2^53 - 1`.
- **NaN**: Representa un resultado no numérico (`Number.isNaN(value)`).
- **Infinity / -Infinity**: Representan valores fuera del rango numérico.

## Creación

```js
let entero = 42;            // entero
let decimal = 3.14;          // número con punto flotante
let notANumber = NaN;        // no es un número válido
let infinito = Infinity;    // valor infinito
```

## Métodos útiles de `Number`

| Método | Descripción |
|--------|--------------|
| `Number.isNaN(val)` | Detecta `NaN` sin coerción |
| `Number.isFinite(val)` | Verifica que no sea `Infinity` ni `NaN` |
| `Number.isInteger(val)` | Comprueba si es entero |
| `Number.parseInt(str)` | Convierte cadena a entero (similar a `parseInt`) |
| `Number.parseFloat(str)` | Convierte cadena a número de punto flotante |
| `Math.round(num)` | Redondea al entero más cercano |
| `Math.floor(num)` | Redondea hacia abajo |
| `Math.ceil(num)` | Redondea hacia arriba |

## Operaciones aritméticas

```js
let a = 5 + 3;      // suma → 8
let b = 10 - 2;     // resta → 8
let c = 4 * 2;      // multiplicación → 8
let d = 16 / 2;     // división → 8
let e = 2 ** 3;      // exponenciación → 8
let f = 17 % 3;      // módulo → 2
```

## Biblioteca `Math`

El objeto global `Math` ofrece funciones matemáticas avanzadas (`Math.max`, `Math.min`, `Math.random`, `Math.sqrt`, etc.) que operan sobre valores `Number`.
