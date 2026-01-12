import pytest

from src.alien.alien_decorator import PersonalShield, CombatShield, AlienDecorator
from src.alien.alien import Alien 

@pytest.fixture
def alien_base():
    """
    Crea un alien con mucha vida para las pruebas.
    Usamos 100 de vida para que las restas sean fáciles de verificar.
    """
    return Alien(x=0, y=0, level_health=100)


def test_decorator_delegates_attributes(alien_base):
    """
    Verifica que el AlienDecorator actúa como un espejo
    Si toco al decorador, debo estar tocando al alien real.
    """
    # Envolvemos al alien en un decorador genérico
    decorator = AlienDecorator(alien_base)
    
    # 1. Probamos lectura (Getters)
    assert decorator.x == 0
    assert decorator.level_health == 100
    
    # 2. Probamos escritura (Setters)
    # Movemos el decorador...
    decorator.x = 50
    # ... y el alien de dentro debe haberse movido
    assert alien_base.x == 50

def test_decorator_delegates_methods(alien_base):
    """Verifica que los métodos (teleport, is_alive) pasan al original."""
    decorator = AlienDecorator(alien_base)
    
    decorator.teleport(10, 20)
    assert alien_base.x == 10
    assert alien_base.y == 20
    
    assert decorator.is_alive() is True


def test_personal_shield_reduces_damage(alien_base):
    """
    El escudo personal tiene protección 1.
    Si recibe 5 de daño -> Pasan 4.
    """
    shield = PersonalShield(alien_base)
    
    shield.hit(5)
    
    assert alien_base.level_health == 96
    assert shield.durability == 4

def test_personal_shield_breaks(alien_base):
    """
    El escudo tiene 5 de durabilidad.
    Tras 5 golpes, el 6º golpe debe entrar entero.
    """
    shield = PersonalShield(alien_base)
    
    for _ in range(5):
        shield.hit(2) 
    
    assert alien_base.level_health == 95
    assert shield.durability == 0
    
    shield.hit(2)
    
    assert alien_base.level_health == 93 # 95 - 2


def test_combat_shield_reduces_heavy_damage(alien_base):
    """
    El escudo de combate tiene protección 5.
    Si recibe 20 de daño -> Pasan 15.
    """
    shield = CombatShield(alien_base)
    
    shield.hit(20)
    
    # Vida esperada: 100 - 15 = 85
    assert alien_base.level_health == 85
    assert shield.durability == 19


def test_bug_curacion_evitado(alien_base):
    """
    Verifica que `max(0, ...)` funciona.
    Escenario:
    - Escudo Combate (Protección 5)
    - Ataque débil (Daño 2)
    
    Cálculo sin protección: 2 - 5 = -3 (Curaría 3 puntos).
    Cálculo correcto: max(0, -3) = 0.
    """
    shield = CombatShield(alien_base)
    
    # Golpeamos con daño menor a la protección
    shield.hit(2)
    
    # La vida NO debe subir a 103. Debe quedarse en 100.
    assert alien_base.level_health == 100
    
    # Pero la durabilidad SÍ debe bajar
    assert shield.durability == 19