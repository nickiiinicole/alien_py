"""
Módulo de sistemas de defensa (Escudos) para Aliens.

Este módulo implementa el patrón de diseño **Decorator** para añadir
funcionalidades de protección a la clase base :class:`Alien` sin modificar
su código original.

Incluye la clase base abstracta :class:`AlienDecorator` y dos implementaciones:
:class:`PersonalShield` y :class:`CombatShield`.
"""
from src.alien.alien import Alien

class AlienDecorator(Alien):
    """Clase base para todos los decoradores de Alien (Wrapper).

    Implementa el patrón Decorator envolviendo una instancia de :class:`Alien`
    y delegando todas las llamadas a métodos y accesos a atributos al objeto envuelto.
    Hereda de Alien para mantener la compatibilidad de tipo (Polimorfismo).

    Attributes:
        _wrappee (Alien): La instancia original del Alien que está siendo decorada.
    """

    def __init__(self, wrappee: Alien):
        """Inicializa el decorador.

        Args:
            wrappee: La instancia de Alien a envolver.
        """
        # No llamamos a super().__init__ porque no queremos inicializar un nuevo estado
        # de Alien (como incrementar el contador global), solo queremos envolver uno existente.
        self._wrappee = wrappee

    # --- DELEGACIÓN DE ATRIBUTOS (Getters/Setters) ---
    # Es fundamental delegar los atributos de posición y salud al objeto original
    # para que el escudo "siga" al alien.

    @property
    def x(self) -> float:
        """float: Coordenada X del alien envuelto."""
        return self._wrappee.x
    
    @x.setter
    def x(self, val: float):
        self._wrappee.x = val

    @property
    def y(self) -> float:
        """float: Coordenada Y del alien envuelto."""
        return self._wrappee.y
    
    @y.setter
    def y(self, val: float):
        self._wrappee.y = val

    @property
    def level_health(self) -> int:
        """int: Salud actual del alien envuelto."""
        return self._wrappee.level_health
    
    @level_health.setter
    def level_health(self, val: int):
        self._wrappee.level_health = val

    # --- MÉTODOS DELEGADOS ---

    def hit(self, level_damage: int = 1) -> None:
        """Aplica daño al alien envuelto.

        Args:
            level_damage: Cantidad de daño a aplicar.
        """
        self._wrappee.hit(level_damage)
    
    def is_alive(self) -> bool:
        """Comprueba si el alien envuelto sigue vivo.

        Returns:
            True si la salud > 0, False en caso contrario.
        """
        return self._wrappee.is_alive()
    
    def teleport(self, x_tp: float, y_tp: float) -> None:
        """Teletransporta al alien envuelto.

        Args:
            x_tp: Nueva coordenada X.
            y_tp: Nueva coordenada Y.
        """
        self._wrappee.teleport(x_tp, y_tp)

    def collision(self, object_coll) -> bool:
        """Detecta colisiones delegando en el alien envuelto.

        Args:
            object_coll: Objeto con el que comprobar la colisión.

        Returns:
            True si hay colisión, False si no.
        """
        return self._wrappee.collision(object_coll)


class PersonalShield(AlienDecorator):
    """Escudo Deflector Personal.

    Este escudo reduce el daño recibido en 1 punto por impacto mientras tenga durabilidad.
    Tiene una durabilidad limitada.

    Attributes:
        durability (int): Puntos de durabilidad restantes del escudo (empieza en 5).
        protection (int): Cantidad de daño que reduce por golpe (fijo en 1).
    """

    def __init__(self, wrappee: Alien):
        """Inicializa el escudo personal envolviendo a un alien.

        Args:
            wrappee: El alien al que se le aplica el escudo.
        """
        super().__init__(wrappee)
        self.durability = 5
        self.protection = 1

    def hit(self, level_damage: int = 1) -> None:
        """Gestiona el impacto recibido reduciendo el daño si el escudo está activo.

        Lógica del escudo:
        1. Si tiene durabilidad, calcula el daño reducido.
        2. Usa ``max(0, ...)`` para evitar que el daño negativo cure al alien.
        3. Reduce la durabilidad en 1 punto.
        4. Pasa el daño final al alien envuelto.

        Args:
            level_damage: Daño bruto recibido antes de aplicar el escudo.
        """
        if self.durability > 0:
            print(f"Escudo Personal activo! Durabilidad restante: {self.durability}")
            
            # EXPLICACIÓN DEL MAX(0, ...):
            # Si el daño es 2 y la protección es 5 -> 2 - 5 = -3.
            # Si pasamos -3 al alien, le estaríamos sumando vida (curándolo).
            # max(0, -3) obliga a que el daño mínimo sea 0 (ni daño ni cura).
            final_damage = max(0, level_damage - self.protection)
            
            self.durability -= 1
            
            self._wrappee.hit(final_damage)
        else:
            print("¡Escudo Personal roto! Daño completo.")
            # Si no hay escudo, el golpe pasa directo
            self._wrappee.hit(level_damage)


class CombatShield(AlienDecorator):
    """Escudo Deflector de Combate.

    Versión avanzada del escudo con mayor protección y durabilidad.
    Reduce el daño en 5 puntos.

    Attributes:
        durability (int): Puntos de durabilidad restantes (empieza en 20).
        protection (int): Cantidad de daño que reduce (fijo en 5).
    """

    def __init__(self, wrappee: Alien):
        """Inicializa el escudo de combate.

        Args:
            wrappee: El alien a proteger.
        """
        super().__init__(wrappee)
        self.durability = 20
        self.protection = 5

    def hit(self, level_damage: int = 1) -> None:
        """Aplica la reducción de daño de combate.

        Args:
            level_damage: Daño bruto recibido.
        """
        if self.durability > 0:
            print(f"Escudo de Combate resistiendo! Durabilidad: {self.durability}")
            
            final_damage = max(0, level_damage - self.protection)
            
            self.durability -= 1
            self._wrappee.hit(final_damage)
        else:
            self._wrappee.hit(level_damage)
