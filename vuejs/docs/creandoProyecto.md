# Proyecto Vue JS en Visual Studio Code

## Confirmacion de version de Node

Antes de crear un proyecto Vue, conviene comprobar que tu version de Node.js es compatible con la version actual de Vue.

![Requisitos de Node en la documentacion oficial](img/creandoProyecto/100000000000038F000000FD80C17F5B.png)

Para consultar tu version instalada, ejecuta:

```bash
node --version
```

Si tu version es inferior a la recomendada, actualiza Node.js antes de continuar para evitar errores durante la creacion o ejecucion del proyecto.

## Creando un proyecto ejemplo con npm

Puedes iniciar un proyecto Vue con npm o con el CLI de Vue.

### Opcion 1: npm (recomendada)

```bash
npm init vue@latest
```

### Opcion 2: Vue CLI

```bash
vue create proyectoBaseVue
```

Durante el asistente interactivo:

1. Se solicita el nombre del proyecto. En este ejemplo: `proyectoBaseVue`.

![Nombre del proyecto](img/creandoProyecto/10000000000001E6000000B4D824A2E3.png)

2. Se solicita el `package name`. Puedes dejar el valor por defecto.

![Package name por defecto](img/creandoProyecto/10000000000001F0000000FF85371BAA.png)

3. Se muestra el menu para elegir caracteristicas. Marca las que vayas a usar.

![Seleccion de caracteristicas](img/creandoProyecto/100000000000042E000000E5DB265790.png)

4. Se pregunta por caracteristicas experimentales. En este ejemplo, no se marca ninguna.

![Caracteristicas experimentales](img/creandoProyecto/10000000000004B30000005B12F9233D.png)

5. Se pregunta por plantilla base o de ejemplo. En este caso, se elige proyecto en blanco.

![Proyecto en blanco](img/creandoProyecto/100000000000023E0000004ECC403543.png)

6. El asistente genera la estructura inicial del proyecto.

![Estructura base creada](img/creandoProyecto/10000000000000C8000001F906703970.png)

7. Al finalizar, se muestran los comandos para instalar dependencias y levantar la app.

![Comandos finales del asistente](img/creandoProyecto/1000000000000260000000E8C1C0F82F.png)

8. Una vez ejecutado, el servidor de desarrollo indica URL y puerto para abrir la aplicacion.

![Servidor de desarrollo levantado](img/creandoProyecto/10000000000002F7000000A48F02FFFA.png)

9. Abre la URL indicada para verificar que el proyecto funciona.

![Aplicacion Vue ejecutandose en navegador](img/creandoProyecto/100000000000016B000000C9F4FA6EFB.png)
