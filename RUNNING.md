# Ejecutando TUXNetwork

Este documento describe cómo ejecutar el prototipo inicial de TUXNetwork, un blockchain de capa 1 diseñado para transacciones sin costo (requiere 100 TUX en stake). **Advertencia:** Este es un prototipo de desarrollo y no debe usarse para minería real ni distribución de TUX en una red activa.

## Estado Actual
- Versión: Prototipo 0.1 (simulación local).
- Objetivo: Demostrar el bloque génesis, consenso híbrido (PoW Lite + PoS), y transacciones básicas.
- Red Real: La testnet está planeada para julio 2025; este código no está conectado a una red activa.

## Requisitos
- **Python:** 3.9 o superior (probado con 3.12.6).
- **Sistema Operativo:** macOS, Linux o Windows.
- **Hardware:** CPU básica (probado en un Core 2 Duo 2 GHz con 6 GB RAM).

## Instrucciones
1. **Clona el Repositorio:**
   ```bash
   git clone https://github.com/MrTuxio/TUXNetwork.git
   cd TUXNetwork
   ```
2. **Ejecuta el Prototipo:**
   ```bash
   python3 tuxnetwork.py
   ```
3. **Salida Esperada:**
   - Creación del bloque génesis con un preminado de 800,000 TUX (0.8% del suministro total).
   - Simulación de 3 nodos locales, cada uno añadiendo un bloque con 3 transacciones.

## Advertencias de Seguridad
- **Prohibido Minar TUX:** Este código es una simulación local y no representa la red final. Cualquier intento de minar o generar TUX con este prototipo no será reconocido en la testnet o mainnet oficial. El preminado de 800,000 TUX está hardcodeado y no debe duplicarse.
- **No Modificar ni Redistribuir:** Alterar el código para "inyectar" TUX u otros fines sin permiso del equipo de desarrollo viola la licencia GPLv3 y no tendrá validez en la red oficial.
- **Uso Autorizado:** Este prototipo es solo para pruebas locales y demostración. No lo ejecutes en un entorno público o conectado sin autorización explícita.

## Seguridad Futura
- La red real implementará:
  - **Criptografía:** Firmas digitales y claves públicas/privadas para validar transacciones y preminado.
  - **Consenso Seguro:** Mecanismos para prevenir minería no autorizada o manipulación del suministro.
- Este prototipo evolucionará para incluir estas medidas antes de la testnet.

## Contribuir
- Revisa el [Whitepaper](Whitepaper.md) para detalles técnicos.
- Envía feedback o ideas vía issues en GitHub.
- **Nota:** No desarrolles forks para minería sin coordinar con el equipo.

---
Última actualización: Febrero 22, 2025
