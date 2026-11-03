# Publicación y Pull Requests en GitHub

## Estado del paquete
Este paquete conserva un historial **Git local** verificable con ramas, commits y merges; **no** contiene un Pull Request de GitHub y no acredita publicación remota.

## Publicar en un repositorio nuevo
1. Ingrese en https://github.com/new con su cuenta real de GitHub.
2. Cree un repositorio **vacío** llamado `sistema-turnos-almuerzo` (sin README, .gitignore ni licencia, ya vienen en el paquete). Recomendación: privado hasta que el equipo decida si lo hace público.
3. Extraiga el ZIP conservando la carpeta oculta `.git`. Abra una terminal en su directorio.
4. Ejecute los siguientes comandos (reemplace `USUARIO` por su cuenta real):

```bash
git remote add origin https://github.com/USUARIO/sistema-turnos-almuerzo.git
git push -u origin main
git push origin feature/asignacion-turnos feature/control-cupos feature/pruebas
git push origin --tags
```

> Si Git solicita autenticación, use Git Credential Manager o una clave de acceso apropiada. No publique tokens en archivos.

## Cómo demostrar un Pull Request genuino
Las ramas locales **ya se fusionaron en main**, por lo que GitHub no permitirá abrir un PR nuevo de esas mismas ramas con cambios pendientes (el diff sería vacío). Para una demostración reproducible, haga lo siguiente después de subir el repo:

```bash
git switch main
git pull origin main
git switch -c feature/mejora-documentacion
printf '
## Control de cambios
Se revisó el procedimiento de GitHub.
' >> docs/MANUAL_USUARIO.md
git add docs/MANUAL_USUARIO.md
git commit -m "docs: ampliar procedimiento de uso"
git push -u origin feature/mejora-documentacion
```

En GitHub abra **Compare & pull request** para `feature/mejora-documentacion` hacia `main`, incluya un título descriptivo, revise el diff y seleccione **Merge pull request**. Capture la pantalla del PR fusionado, el historial de commits, las ramas y el repositorio; al final ejecute `git switch main && git pull origin main` para descargar el merge realizado remotamente.

## Evidencias recomendadas
- Página principal: `https://github.com/USUARIO/sistema-turnos-almuerzo`
- Ramas: `https://github.com/USUARIO/sistema-turnos-almuerzo/branches`
- Commits: `https://github.com/USUARIO/sistema-turnos-almuerzo/commits/main/`
- Pull Requests: `https://github.com/USUARIO/sistema-turnos-almuerzo/pulls?q=is%3Apr+is%3Amerged`
- Versiones: `https://github.com/USUARIO/sistema-turnos-almuerzo/tags`

Reemplace `USUARIO` por el propietario real; **estas URL son plantillas hasta publicar el repositorio**.
