from typing import Self
class Alien():
    x : float = 0
    y : float =0 
    # valor por defecto
    level_health : int = 3
    counter_alien = 0 

    def __init__(self,x:float, y:float, level_health:int=3)->None:
        self.x= x
        self.y= y
        self.level_health= level_health
        Alien.counter_alien+=1
    

    def hit(self, level_damage:int=1)->None:
        self.level_health-=level_damage

    def is_alive(self)-> bool:
        return self.level_health>0
    
    def teleport(self, x_tp:float, y_tp:float)-> None:
        self.x= x_tp
        self.y= y_tp

    def collision(self, object_coll: Self)-> bool:
        if self.x == object_coll.x and self.y==object_coll.y:
            return True
        
        return False

def new_aliens_collection(start_positions: list[tuple[int, int]]) -> list[Alien]:
        return [Alien(x,y) for x, y in start_positions]

