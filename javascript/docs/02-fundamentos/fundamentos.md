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

Los operadores de asignación combinan una operación con la asignación de un valor a una variable.

| Operador | Significado |
|----------|--------------|
| `=` | Asignación simple |
| `+=` | Suma y asigna |
| `-=` | Resta y asigna |
| `*=` | Multiplica y asigna |
| `/=` | Divide y asigna |
| `%=` | Módulo y asigna |
| `**=` | Exponenciación y asigna |

Ejemplo:
```js
let a = 5;
a += 3; // a = 8
```

### Operadores aritméticos *(2 min)*

Los operadores aritméticos permiten realizar cálculos numéricos básicos.

| Operador | Nombre | Ejemplo |
|----------|--------|---------|
| `+` | Suma | `5 + 3 // 8` |
| `-` | Resta | `5 - 2 // 3` |
| `*` | Multiplicación | `4 * 2 // 8` |
| `/` | División | `10 / 2 // 5` |
| `%` | Módulo (resto) | `10 % 3 // 1` |
| `**` | Exponenciación | `2 ** 3 // 8` |
| `++` | Incremento | `let i = 0; i++; // i = 1` |
| `--` | Decremento | `let i = 5; i--; // i = 4` |

> Cada operador tiene su precedencia (p.ej., `**` > `*`/`/` > `+`/`-`).


### Operadores de comparación *(3 min)*

Los operadores de comparación devuelven un **booleano** (`true` o `false`). Se usan para decidir flujos de control.

| Operador | Significado |
|----------|-------------|
| `==` | Igualdad (con coerción) |
| `===` | Igualdad estricta |
| `!=` | Desigualdad (con coerción) |
| `!==` | Desigualdad estricta |
| `<` `>` `<=` `>=` | Comparación numérica |

Ejemplo:

```js
5 == '5'   // true (coerción)
5 === '5' // false (tipo diferente)
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
