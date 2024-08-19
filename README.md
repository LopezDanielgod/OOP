# Paradigmo de la OOP

- Encapsulamiento
Se basa en convenciones de nomenclatura, no en mecanismos de acceso estrictos como en otros lenguajes. Se utiliza un guion bajo (_) al inicio del nombre de un atributo para indicar que no debe ser accedido directamente desde fuera de la clase, aunque técnicamente es posible. Para métodos, se utilizan dos guiones bajos (__) al inicio del nombre, lo que los convierte en "privados" y les aplica una técnica llamada "name mangling" que dificulta su acceso directo desde fuera de la clase. Python no impide el acceso a estos atributos y métodos "privados", pero la convención de nomenclatura es una guía para mantener la integridad del objeto y facilitar el mantenimiento del código.

- Abstracción
Permite definir interfaces generales para objetos, dejando la implementación específica a las clases que heredan de ellas. Imagina que estás construyendo un sistema de transporte: puedes tener diferentes tipos de vehículos (coches, barcos, aviones), pero todos deben tener la capacidad de arrancar, acelerar y frenar. En lugar de definir estas acciones individualmente para cada tipo de vehículo, puedes crear una clase abstracta llamada "Vehiculo" que defina estos métodos como abstractos. 

- Herencia
Es un mecanismo que permite a una clase, llamada subclase o clase hija, heredar atributos y métodos de otra clase, llamada superclase o clase padre. Esto significa que la subclase puede reutilizar el código de la superclase y agregarle su propia funcionalidad.

- Polimorfismo
Aporta flexibilidad al código, ya que permite reutilizar el mismo código para diferentes tipos de objetos, facilita el mantenimiento, ya que al cambiar el comportamiento de un método en una subclase, no se necesita modificar el código que lo llama, y en general, facilita la creación de sistemas complejos y adaptables.