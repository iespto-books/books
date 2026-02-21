---
title: "Variables"
duration: "5 artículos"
---

# Variables

## Variables *(5 min)*
En JavaScript existen tres formas de declarar variables:

| Declaración | Ámbito | Reasignable |
|-------------|--------|--------------|
| `var` | función o global | sí |
| `let` | bloque (`{}`) | sí |
| `const` | bloque | **no** (solo la referencia) |

```js
let contador = 0;
contador = 10; // ok

const PI = 3.14;
PI = 3.1415; // TypeError
```

## Constantes *(3 min)*
Aunque `const` impide la reasignación de la **referencia**, el contenido de objetos y arrays sigue siendo mutable.

```js
const CONFIG = { modo: 'dev' };
CONFIG.modo = 'prod'; // permitido
```
Usa `Object.freeze()` para obtener inmovilidad real.

## Ámbito de una variable *(2 min)*
- **Global**: disponible en todo el script (`window` / `globalThis`).
- **Funcional**: creado con `var` dentro de una función.
- **Bloque**: creado con `let`/`const` dentro de `{}` (incluye bucles, `if`, `try`).

```js
function demo(){
  var x = 1; // función
  if(true){
    let y = 2; // bloque
    const z = 3; // bloque
  }
  console.log(x); // 1
  // console.log(y); // ReferenceError
}
```

## Coerción de tipos *(6 min)*
JavaScript convierte automáticamente entre tipos en contextos numéricos, booleanos o de cadena.

| Operación | Resultado |
|-----------|----------|
| `'5' + 1` | `'51'` (concatenación) |
| `'5' - 1` | `4` (coerción a número) |
| `!!0` | `false` |
| `Boolean('')` | `false` |
| `null == undefined` | `true` |
| `null === undefined` | `false` |

**Buenas prácticas**: usa `===` y conversiones explícitas (`Number()`, `String()`, `Boolean()`).

```js
let suma = Number('10') + 5; // 15
```

## La antigua `var` *(6 min)*
- **Hoisting**: la declaración se eleva al inicio del scope, pero la asignación no.
- **Ámbito de función**: `var` no respeta bloques (`if`, `for`).

```js
console.log(a); // undefined (hoisted)
var a = 10;
```
Recomendación: **evitar `var`** y usar `let`/`const`.

## Tipos de datos *(≈ 4 artículos)*

### Tipos primitivos *(3 min)*
| Tipo | Descripción |
|------|-------------|
| `Number` | Números de punto flotante (IEEE‑754) |
| `String` | Cadenas Unicode (inmutables) |
| `Boolean` | `true` / `false` |
| `BigInt` | Enteros arbitrariamente grandes (`123n`) |
| `Symbol` | Valores únicos e inmutables |
| `null` | Valor nulo explícito |
| `undefined` | Valor no definido |

### `null` y `undefined` *(2 min)*
- `null`: asignado intencionalmente para indicar ausencia de valor.
- `undefined`: valor por defecto de variables no inicializadas, parámetros no pasados o propiedades inexistentes.

```js
let a; // undefined
a = null; // ahora es null
```

### `Symbol` *(4 min)*
```js
const ID = Symbol('id');
const obj = { [ID]: 123 };
```
Cada `Symbol()` es único, incluso con la misma descripción. Se usa para crear claves privadas o para protocolos (e.g., `Symbol.iterator`).

### Boolean *(2 artículos)*
#### Tipo Boolean *(2 min)*
Solo dos valores posibles: `true` y `false`. Utilizado en estructuras de control, comparaciones y lógica.

#### Falsy y Truthy *(3 min)*
| Falsy | Truthy (cualquier otro valor) |
|-------|------------------------------|
| `false` | `'texto'` |
| `0` | `42` |
| `-0` | `{}` |
| `0n` | `[]` |
| `""` (cadena vacía) | `function(){}` |
| `null` | `null` |
| `undefined` | `undefined` |
| `NaN` | `NaN` |

### Number *(3 artículos)*
#### Tipo Number *(5 min)*
Representa **todos** los números (enteros y decimales). Usa **IEEE‑754 double‑precision**, lo que implica limitaciones (p.ej., `0.1 + 0.2 !== 0.3`).

```js
let entero = 42;
let decimal = 3.14;
```

#### Métodos útiles de Number *(3 min)*
| Método | Ejemplo |
|--------|---------|
| `Number.isNaN(value)` | `Number.isNaN(NaN) // true` |
| `Number.isInteger(value)` | `Number.isInteger(5) // true` |
| `Number.parseInt(str)` | `Number.parseInt('10px') // 10` |
| `Number.parseFloat(str)` | `Number.parseFloat('3.14em') // 3.14` |
| `Number.isFinite(value)` | `Number.isFinite(Infinity) // false` |

#### Biblioteca Math *(5 min)*
| Método | Descripción |
|--------|-------------|
| `Math.max(...nums)` | Máximo |
| `Math.min(...nums)` | Mínimo |
| `Math.round(num)` | Redondeo al entero más cercano |
| `Math.floor(num)` | Redondeo hacia abajo |
| `Math.ceil(num)` | Redondeo hacia arriba |
| `Math.random()` | Número pseudo‑aleatorio en `[0,1)` |
| `Math.pow(base, exp)` | Potencia (`base ** exp`) |
| `Math.sqrt(x)` | Raíz cuadrada |
| `Math.abs(x)` | Valor absoluto |
| `Math.sin`, `Math.cos`, `Math.tan` | Funciones trigonométricas |

### String *(4 artículos)*
#### Tipo String *(2 min)*
Cadenas de texto Unicode, inmutables. Se pueden crear con comillas simples `'...'`, dobles `"..."` o backticks `` `...` `` (template literals).

#### Métodos útiles de String *(7 min)*
| Método | Ejemplo |
|--------|----------|
| `charAt(index)` | `"hola".charAt(1) // 'o'` |
| `includes(sub)` | `"hello".includes('ell') // true` |
| `startsWith(sub)` | `"test".startsWith('te') // true` |
| `endsWith(sub)` | `"test".endsWith('st') // true` |
| `indexOf(sub)` | `"abc".indexOf('b') // 1` |
| `slice(start, end)` | `"abcdef".slice(1,4) // 'bcd'` |
| `substring(start, end)` | igual que `slice` sin índices negativos |
| `trim()` | `"  hola ".trim() // 'hola'` |
| `padStart/End` | `"5".padStart(3,'0') // '005'` |
| `repeat(n)` | `"ab".repeat(3) // 'ababab'` |

#### Template literals *(4 min)*
Usan backticks `` `...` `` y permiten **interpolación** y **multilínea**.

```js
let nombre = 'Ana';
let edad = 30;
let mensaje = `Hola ${nombre},
 tienes ${edad} años.`;
```

### Regex *(3 min)*
```js
let patron = /ab+c/i; // i = case‑insensitive
let texto = 'aaabC';
console.log(patron.test(texto)); // true
```
Métodos principales: `test`, `exec`, `match`, `replace`, `search`, `split`. Flags: `g`, `i`, `m`, `u`, `y`.
