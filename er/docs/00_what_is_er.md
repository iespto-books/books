# Qué es el diagrama de Entidad - Relación (ER)

El modelo Entidad–Relación es una herramienta para el modelo de datos, propuesta por Peter Chen en 1976, la cual facilita la representación gráfica de:

1. **Entidades**: Son los "objetos" o "conceptos" del mundo real sobre los que queremos guardar información. Se representan con **rectángulos**.

    * Ejemplos: Cliente, Producto, Venta, Empleado.

2. **Atributos**: Son las características o propiedades de una entidad. Se representan con **óvalos** conectados a la entidad.

    * Ejemplos: El "Nombre", "DNI" o "Email" de la entidad Cliente.

3. **Relaciones**: Es el vínculo que une a dos o más entidades, describiendo cómo interactúan. Se representan con rombos.

    * Ejemplo: Un Cliente **compra** un Producto.

4. **Cardinalidades**: La cardinalidad define cuántas instancias de una entidad pueden asociarse con instancias de otra.

    * **Uno a Uno (1:1)**: Un usuario tiene un único perfil (y viceversa).
    * **Uno a Muchos (1:N)**: Un cliente puede realizar muchos pedidos, pero cada pedido pertenece a un solo cliente.
    * **Muchos a Muchos (N:M)**: Un estudiante puede inscribirse en muchos cursos, y un curso puede tener muchos estudiantes.

El Modelo Entidad-Relación (E-R) es el paso previo e imprescindible antes de crear tablas en una base de datos. Su función principal es organizar las ideas de forma conceptual, sin preocuparse todavía por el software o el código técnico.

El proceso de creación de una base de datos sigue una secuencia clara:

1. Necesidad: El cliente define qué información necesita almacenar.
2. Modelo Entidad-Relación (E-R): Se representa conceptualmente la información mediante entidades y relaciones.
3. Modelo Relacional: El modelo conceptual se transforma en tablas, claves primarias y foráneas.
4. SQL: Se implementa físicamente la base de datos en un sistema gestor mediante sentencias SQL.

```mermaid
flowchart LR
    A["`**Necesidad**`" <br />El cliente explica qué quiere guardar]
    B["`**Modelo E-R**`" <br />Boceto con entidades y relaciones]
    C["`**Modelo Relacional**`" <br />Tablas, claves primarias y foráneas]
    D["`**SQL**`" <br />Implementación en el sistema gestor]

    A --> B --> C --> D
```
