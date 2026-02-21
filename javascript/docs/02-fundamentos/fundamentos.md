---
title: "Fundamentos"
duration: "6 artículos"
---

# Fundamentos

## Nuestro primer programa *(3 min)*

```javascript
// hola-mundo.js
console.log('¡Hola, Mundo!');
```
Guarda el archivo y ejecútalo con `node hola-mundo.js` o inclúyelo en una página HTML.

## Cómo ejecutar JavaScript *(4 min)*

| Entorno | Forma de ejecución |
|---------|----------------------|
| Navegador | `<script src="app.js"></script>` o código inline `<script> … </script>` |
| Node.js | `node archivo.js` |
| REPL | `node` → prompt interactivo |
| Herramientas | VS Code *Run Code*, *Debugger*, extensiones como **Quokka** |

## Sintaxis básica *(5 min)*

- **Sentencias** terminan en `;` (opcional). 
- **Bloques** `{ … }` agrupan sentencias.
- **Identificadores** pueden contener letras, `$`, `_` y números (no iniciar con número).

```js
let nombre = 'Ana';
const PI = 3.1415;
```

## Comentarios *(2 min)*

```js
// Comentario de una línea
/* Comentario
   multilínea */
```

## Consola *(6 min)*

| Método | Uso |
|--------|-----|
| `console.log()` | Imprime información |
| `console.error()` | Mensajes de error |
| `console.table()` | Muestra arrays/objetos como tabla |
| `console.group()` / `console.groupEnd()` | Agrupa logs |

```js
console.log('Valor:', 42);
console.error('¡Error!');
```

## Objetos globales *(3 min)*

- `window` (navegador) – contiene `document`, `fetch`, `setTimeout`, etc.
- `global` (Node) – equivalente a `window`.
- `globalThis` – referencia universal al objeto global.
- `console`, `JSON` – herramientas de logging y serialización.

## Expresiones y operadores *(≈ 8 artículos)*

### Operadores de asignación *(4 min)*
```js
let a = 10;
a += 5; // a = 15
a **= 2; // a = 225
```

### Operadores aritméticos *(2 min)*
`+ - * / % ** ++ --`

### Operadores de comparación *(3 min)*
```js
0 == false   // true (coerción)
0 === false // false (estricto)
```

### Operadores lógicos *(3 min)*
```js
true && false // false
true || false // true
!true          // false
```

### Operador spread `...` *(5 min)*
```js
const nums = [1,2,3];
const copia = [...nums, 4];
const obj = { a:1, b:2 };
const nuevo = { ...obj, c:3 };
```

### Nullish coalescing `??` *(2 min)*
```js
let valor = null;
let definitivo = valor ?? 'default'; // 'default'
```

### Optional chaining `?.` *(4 min)*
```js
let usuario = { perfil: { nombre: 'Ana' } };
console.log(usuario?.perfil?.nombre); // 'Ana'
console.log(usuario?.contacto?.email); // undefined
```

### Precedencia *(4 min)*
Orden de evaluación: `()`, `**`, `* / %`, `+ -`, comparaciones, `== != === !==`, `&&`, `||`, `??`, `?:`, asignaciones, `,`.
