# Bitey Trainer

**Bitey Trainer es un modelo/capacidad interna de Bitey IA Web para entrenamiento, evaluación, validación y evolución de inteligencia especializada.**

No es una aplicación, no es un cliente, no sustituye a JobIA y no controla directamente JobIA-Web ni JobIA-app. Su origen y autoridad pertenecen a Bitey IA Web.

## Posición en la arquitectura

```text
                         BITEY IA WEB
                  inteligencia general / núcleo
                           │
                           │ contiene
                           ▼
                    BITEY TRAINER
             modelo/capacidad de entrenamiento
             evaluación · validación · evolución
                           │
                capacidades especializadas
                           ▼
                         JOBIA
                backend/producto de empleo
                           │
                  contrato versionado
                     jobia-v1 / API
                    ┌──────┴──────┐
                    ▼             ▼
                JobIA-Web      JobIA-app
                  web            Android
```

Bitey IA Web y JobIA mantienen identidades de producto separadas. Bitey Trainer no crea una segunda web ni un segundo cerebro independiente.

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

El flujo es:

```text
Definir → Implementar → Probar → Medir → Mejorar
        → Validar → Publicar capacidad/contrato → JobIA consume
```

JobIA es el backend/producto especializado de empleo y expone sus capacidades a JobIA-Web y JobIA-app. Trainer no debe crear un segundo backend público ni duplicar la API de los clientes.

## Relación bidireccional

- **Bitey IA Web → JobIA:** cuando una solicitud necesita conocimiento o acciones especializadas de empleo/trabajo.
- **JobIA → Bitey IA Web:** cuando necesita razonamiento general, orquestación, memoria, herramientas, selección de modelos o políticas generales.
- **Bitey Trainer → JobIA:** aporta capacidades entrenadas/validadas y evaluación especializada.

Las integraciones deben realizarse mediante contratos versionados y APIs, nunca acoplando las interfaces web entre sí.

## Seguridad

- Sin secretos de proveedores en código.
- Datos aislados por cuenta/tenant.
- Autorización backend.
- Sin exposición automática de datos privados de JobIA.
- Ninguna automatización debe suplantar al usuario ni saltarse evaluaciones, identidad o términos de plataformas.

## Principio

> **Bitey IA Web es el sistema general; Bitey Trainer es una capacidad/modelo interno de Bitey para entrenar y validar; JobIA es la especialidad de empleo; JobIA-Web y JobIA-app son productos/clientes independientes de JobIA.**
