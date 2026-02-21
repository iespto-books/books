---
title: "El tipo String"
duration: "2 min"
---

# El tipo String en JavaScript

Un **String** es una secuencia de caracteres Unicode. Es inmutable; cualquier operación devuelve una nueva cadena.

## Creación

```js
const s1 = 'Hola';            // comillas simples
const s2 = "Mundo";           // comillas dobles
const s3 = `Template ${s1}`; // template literals, permite interpolación
```

## Propiedades

- `s.length` – número de caracteres.

## Métodos principales

| Método | Ejemplo |
|--------|---------|
| `charAt(i)` | `'abc'.charAt(1) // 'b'` |
| `includes(sub)` | `'hola'.includes('ol') // true` |
| `startsWith(sub)` | `'test'.startsWith('te') // true` |
| `endsWith(sub)` | `'test'.endsWith('st') // true` |
| `indexOf(sub)` | `'abc'.indexOf('b') // 1` |
| `slice(a,b)` | `'abcdef'.slice(1,4) // 'bcd'` |
| `trim()` | `'  hola '.trim() // 'hola'` |
| `padStart/End` | `'5'.padStart(3,'0') // '005'` |
| `repeat(n)` | `'ab'.repeat(3) // 'ababab'` |

## Template literals

```js
let nombre = 'Ana';
let edad = 30;
let mensaje = `Hola ${nombre}, tienes ${edad} años.`;
```

Los *template literals* permiten interpolar variables y crear cadenas multilínea.
