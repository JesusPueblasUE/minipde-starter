# MiniPDE

Proyecto transversal de la asignatura **Métodos Numéricos en Ecuaciones
en Derivadas Parciales**.

## Objetivo

Desarrollar progresivamente un pequeño solver modular para ecuaciones
en derivadas parciales, aplicando:

- discretización espacial;
- condiciones de contorno;
- resolución de sistemas lineales y no lineales;
- integración temporal;
- análisis de estabilidad;
- verificación numérica;
- pruebas automatizadas;
- control de versiones con Git.

## Evolución prevista

| Versión | Contenido |
|---|---|
| v0.1 | Entorno, estructura, punto flotante y pruebas |
| v0.2 | Operadores de diferencias finitas |
| v0.3 | Ecuación de Poisson y condiciones de contorno |
| v0.4 | Solvers lineales y no lineales |
| v0.5 | Integradores temporales |
| v0.6 | Ecuación del calor |
| v0.7 | Ecuación de advección |
| v1.0 | Verificación, documentación y proyecto final |

## Instalación

### Crear el entorno virtual

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1