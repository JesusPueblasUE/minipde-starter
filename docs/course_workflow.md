# Flujo de trabajo del curso

## Remotos

Cada estudiante tendrá dos repositorios remotos:

- `origin`: repositorio personal;
- `upstream`: repositorio del profesor.

## Actualización de la rama principal

```powershell
git switch main
git pull origin main
git fetch upstream
git merge upstream/main
git push origin main