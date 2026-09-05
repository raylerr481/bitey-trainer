# Bitey Trainer

**Bitey Trainer es el motor interno de entrenamiento, evaluación y validación de inteligencia de JobIA dentro de Bitey IA Web.**

No es una aplicación ni un cliente. No controla JobIA-Web ni JobIA-app.

## Posición en la arquitectura

```text
                         BITEY IA WEB
                    inteligencia general
                           │
              Cognitive Core / políticas
                           │
                    ┌──────▼──────┐
                    │    JobIA    │
                    │ backend     │
                    │ empleo      │
                    └──────┬──────┘
                           ▲
                           │ capacidades validadas
                           │
                    Bitey Trainer
                  entrenamiento/evaluación
                           │
                 ┌─────────┴─────────┐
                 ▼                   ▼
            JobIA-Web           JobIA-app
             cliente               cliente
```

## Responsabilidad

Trainer desarrolla y valida capacidades especializadas como:

- descubrimiento y normalización de oportunidades;
- detección de duplicados y oportunidades obsoletas;
- matching por habilidades transferibles;
- idioma, ubicación y modalidad;
- análisis de compensación;
- clasificación HUMAN/BITEY/HYBRID;
- scoring, ranking y explicaciones;
- preparación de CV/propuestas/aplicaciones;
- evaluación de respuestas de IA;
- aprendizaje a partir de feedback.

## Contrato con JobIA

El flujo es:

```text
Definir → Implementar → Probar → Medir → Mejorar
        → Validar → Publicar contrato → JobIA consume
```

JobIA es el backend de producto y expone las capacidades a los clientes. Trainer no debe crear un segundo backend público ni duplicar la API de los clientes.

## Relación con Bitey IA Web

Bitey IA Web es el sistema general y conserva la autoridad sobre razonamiento general, memoria, selección de herramientas/modelos y políticas. Trainer aporta inteligencia especializada para empleo.

## Seguridad

- Sin secretos de proveedores en código.
- Datos aislados por cuenta/tenant.
- Autorización backend.
- Sin exposición automática de datos privados de JobIA.
- Ninguna automatización debe suplantar al usuario ni saltarse evaluaciones, identidad o términos de plataformas.

## Principio

> **Bitey IA Web coordina; Bitey Trainer entrena y valida; JobIA ejecuta el contrato de empleo; JobIA-Web y JobIA-app presentan el producto al usuario.**
