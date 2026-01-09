import pytest
# Asumimos que tu archivo se llama 'aliens.py'
from src.alien.alien import Alien, new_aliens_collection

@pytest.fixture
def alien_default():
    """Crea un alien en (0,0) con vida por defecto (3)."""
    return Alien(0, 0)

@pytest.fixture
def alien_strong():
    """Crea un alien fuerte con 10 de vida."""
    return Alien(10, 20, level_health=10)

def test_inicializacion_correcta(alien_default):
    """Verifica que se guardan las coordenadas y la vida."""
    assert alien_default.x == 0
    assert alien_default.y == 0
    assert alien_default.level_health == 3
    assert alien_default.is_alive() is True

def test_contador_aumenta():
    """
    Verifica que la variable de clase 'counter_alien' sube.
    NOTA: Como los tests corren en desorden, comparamos el "antes" y el "después".
    """
    count_antes = Alien.counter_alien
    _ = Alien(5, 5)
    count_despues = Alien.counter_alien
    
    assert count_despues == count_antes + 1

def test_hit_recibe_dano(alien_default):
    """Un golpe básico quita 1 de vida."""
    vida_inicial = alien_default.level_health
    alien_default.hit()
    assert alien_default.level_health == vida_inicial - 1

def test_hit_dano_personalizado(alien_default):
    """Un golpe fuerte quita más vida."""
    alien_default.hit(level_damage=2)
    assert alien_default.level_health == 1

def test_muerte_alien(alien_default):
    """Si la vida llega a 0, is_alive devuelve False."""
    alien_default.hit(3) # Tiene 3 de vida, le quitamos 3
    assert alien_default.level_health == 0
    assert alien_default.is_alive() is False

def test_teleport(alien_default):
    """El alien cambia de coordenadas instantáneamente."""
    alien_default.teleport(100, -50)
    assert alien_default.x == 100
    assert alien_default.y == -50


def test_collision_true():
    """Dos aliens en la misma coordenada chocan."""
    a1 = Alien(5, 5)
    a2 = Alien(5, 5)
    assert a1.collision(a2) is True

def test_collision_false():
    """Dos aliens en distinta coordenada NO chocan."""
    a1 = Alien(0, 0)
    a2 = Alien(10, 10)
    assert a1.collision(a2) is False


def test_new_aliens_collection():
    """La función crea una lista de objetos Alien correctamente."""
    posiciones = [(0, 0), (10, 20), (-5, 5)]
    
    flota = new_aliens_collection(posiciones)
    
    # 1. Comprobamos longitud
    assert len(flota) == 3
    
    # 2. Comprobamos que son objetos Alien
    assert isinstance(flota[0], Alien)
    
    # 3. Comprobamos que los datos coinciden
    assert flota[1].x == 10
    assert flota[1].y == 20
    assert flota[2].x == -5

def test_collection_vacia():
    """Si la lista de tuplas está vacía, devuelve lista vacía."""
    assert new_aliens_collection([]) == []