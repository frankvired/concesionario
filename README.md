# AutoCore Enterprise Ecosystem 🏎️
(VERISON ACTUAL MUY BASICA)
**AutoCore** es una plataforma integral de gestión para concesionarios diseñada bajo una arquitectura de microservicios. El sistema automatiza todo el ciclo de venta: desde la gestión de inventario inteligente hasta la generación automática de contratos legales y comunicación con el cliente.

## 🏗️ Arquitectura del Sistema

El proyecto está diseñado siguiendo el principio de **Separación de Responsabilidades (SoC)**, dividiéndose en tres bloques independientes:

1.  **Frontend (The Showcase):** SPA desarrollada en **React + TypeScript** enfocada en la experiencia de usuario (UX) y el rendimiento.
2.  **Backend Core (The Brain):** API REST desarrollada con **Django + PostgreSQL** que gestiona la lógica de negocio, jerarquías corporativas y seguridad.
3.  **Automation Microservice (The Worker):** Servicio asíncrono con **FastAPI** encargado de tareas pesadas como generación de PDFs, envío de correos y web scraping.



---

## 🚀 Características Principales (MVP)

### 🏢 Gestión Empresarial (B2B)
- **Modelo de Usuario Corporativo:** Estructura jerárquica con roles (Ventas, IT, Gerencia), asignación de mentores (Buddy System) y gestión por sedes/oficinas.
- **Dashboard de Salud de Inventario:** Panel administrativo avanzado para comerciales con KPIs sobre rotación de stock y rentabilidad.

### 🛒 Experiencia de Cliente (B2C)
- **Catálogo Inteligente:** Buscador avanzado de vehículos con filtrado dinámico.
- **Reserva con Expiración Automática:** Sistema de reserva de vehículos con validez de 48h para optimizar el stock.

### ⚙️ Automatización
- **Generación de Contratos:** Creación dinámica de documentos PDF tras la confirmación de reserva.
- **Notificaciones Automatizadas:** Envío de documentación legal vía email mediante integración con servicios de mensajería.

---

## 🛠️ Stack Tecnológico

| Tecnología | Propósito |
| :--- | :--- |
| **React (Vite)** | Interfaz de usuario reactiva y tipado con TypeScript. |
| **Django (DRF)** | API robusta, ORM, autenticación y panel de administración. |
| **FastAPI** | Microservicio de alta velocidad para tareas en segundo plano. |
| **PostgreSQL** | Base de datos relacional para garantizar integridad de datos. |
| **Docker** | Contenerización de todo el ecosistema (Docker Compose). |

---

## 📋 Planificación (Scrum)

El desarrollo se divide en tres hitos principales:
- [ ] **Fase 1:** Core Backend. Modelado de usuarios, inventario y API inicial.
- [ ] **Fase 2:** Frontend & Integración. Catálogo reactivo y conexión con el sistema de reservas.
- [ ] **Fase 3:** Automatización & DevOps. Generación de PDFs, servicios de email y despliegue con Docker.

---

## 🚀 Instalación y Uso (Próximamente)

