# Variables y tipos en JavaScript

En esta unidad veremos:

- `let`, `const` y `var`.
- Tipos primitivos (`string`, `number`, `boolean`, `null`, `undefined`, `symbol`, `bigint`).
- Conversión de tipos.

```js
"use strict";

const centro = "CIFP X";
let grupo = "2º DAW";
let plazas = "25";

const plazasNum = Number(plazas);
console.log(typeof plazas, typeof plazasNum);
