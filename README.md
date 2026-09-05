# Bitey Trainer

**Capacidad interna de Bitey IA para entrenamiento, evaluación, validación y evolución de inteligencia.**

Bitey Trainer no es una aplicación, no es un canal web/Android y no es un segundo cerebro. Forma parte de las capacidades internas de Bitey IA y puede entrenar y validar capacidades especializadas que utilizan sus módulos, incluido JobIA.

## Posición en la arquitectura

```text
                         BITEY IA
                    inteligencia general
                           │
                    BITEY TRAINER
             entrenamiento · evaluación
                validación · evolución
                           │
              capacidades validadas
                           ▼
                         JOBIA
                módulo de empleo/trabajo
                           │
                    contrato jobia-v1
                      ┌────┴────┐
                      ▼         ▼
                  JobIA-Web JobIA-app
                     Web      Android
                    canal       canal
```

`Bitey IA Web` es el canal web de Bitey IA. `JobIA-Web` y `JobIA-app` son canales de JobIA. Trainer no controla directamente ninguna interfaz.

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
- aprendizaje a partir de feedback y regresiones.

## Contrato con JobIA

```text
Definir → Implementar → Probar → Medir → Mejorar
        → Validar → Publicar capacidad → JobIA consume
```

JobIA es el módulo/backend especializado de empleo y expone sus capacidades a sus canales web y Android. Trainer no crea un segundo backend público ni duplica la API de los canales.

## Relación bidireccional

- **Bitey IA → JobIA:** cuando una solicitud necesita conocimiento o acciones especializadas de empleo/trabajo.
- **JobIA → Bitey IA:** cuando necesita razonamiento general, orquestación, memoria, herramientas, selección de modelos o políticas generales.
- **Bitey Trainer → JobIA:** aporta capacidades entrenadas/validadas y evaluación especializada.

Las integraciones se realizan mediante contratos versionados y APIs, nunca acoplando las interfaces web entre sí.

## Seguridad

- Sin secretos de proveedores en código.
- Datos aislados por cuenta/tenant.
- Autorización en backend.
- Sin exposición automática de datos privados de JobIA.
- Ninguna automatización debe suplantar al usuario ni saltarse evaluaciones, identidad o términos de plataformas.

## Principio

> **Bitey IA es el sistema general. Bitey Trainer es una capacidad interna para entrenar y validar. JobIA es el módulo especializado de empleo. JobIA-Web y JobIA-app son sus canales web y Android. Bitey IA Web es el canal web de Bitey IA.**
