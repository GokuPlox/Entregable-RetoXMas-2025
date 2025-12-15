# Entregable-RetoXMas-2025
Entregable de Backend


requisitos_

Tener instalado Git y Docker Desktop
lod datos estan harcodeados en el docker compose.

una vez clonado, dentro del proyecto en la temrinal 
ejecutar (de a 1)
docker-compose up --build -d
docker-compose ps  (este para chequear que haya algo funcionando)

en el navegador ir a http://localhost:8000/docs

yo pude chquear si se generaba correctamenete el jwt desde https://www.jwt.io/
pero claude tmb tiene una forma de validarlo mediante entradas a la consola. 
a dewmas en swagger si te registras y logueas te da un token que podes poner arriba  la derecha un bloqeusito que dice authorize

Cuando actualizar un dato de la tabla con update, tenes q borrrar los campos q no vas a actualizar, si dejas "email" = "string" te va a ctualizar el mail a la palabra string, cositas..


La base de datos se inicializa automáticamente con 4 usuarios de prueba:

| Usuario | Email | Contraseña | Estado |
|---------|-------|------------|--------|
| Eli1 | user@example.com | password123 | activo |
| Eli3 | user3@example.com | password123 | activo |
| string | user20@example.com | password123 | activo |
| Eli5 | user5@example.com | password123 | activo |

**Nota**: Estos usuarios se crean automáticamente solo si la base de datos está vacía. Puedes usar cualquiera de ellos para probar el login y las funcionalidades protegidas de la API. (gracias sonnet)

al terminar solo 

docker-compose down -v