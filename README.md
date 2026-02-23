# Instalación, uso y despliegue

Se hace uso de [Zensical](https://zensical.org) para crear el sitio web estático.

Se recomienda leer el [get-started](https://zensical.org/docs/get-started/) de [Zensical](https://zensical.org).

# Crear nuevo libro

Para crear un nuevo libro debemos 

1. Ubicarnos en la carpeta books

```bash
cd books
```

2. Crear una nueva carpeta con el nombre del libro

```bash
mkdir new-concept-book
```

3. Crear `zensical.toml` y alojar el contenido dentro de la carpeta `docs`

```
mkdir -p new-concept-book/docs
touch new-concept-book/docs/index.md
touch new-concept-book/zensical.toml
```

Como mínimo en `zensical.toml` estamos generando:

```toml
[project]
site_name = "Nombre del libro"
site_description = "Descripción"

[project.theme]
language = "es"
```

Para acceder a los libros tras el despliegue automático de github-actions con rama `main` debemos acceder a la url: https://iespto-books.github.io/books/new-concept-book

# Serve en local

Para ver en local el estado de tu libro con los cambios, ubicarse en la carpeta del libro y ejecutar:

```bash
uv run zensical serve
```
