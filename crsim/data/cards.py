class Giant:
    def __init__(self):
        # Basic attributes
        self.name = "Giant"
        self.cost = 5
        self.hp = 3968
        self.speed = 45
        self.count = 1
        self.transport = "Ground"
        self.type = "Troop"

        # Attack
        self.attack_type = "Single Target"
        self.target_type = "Buildings"
        
        self.damage = 253
        self.attack_speed = 1.5
        self.range = 1.2

        # Others
        self.deploy_time = 1.0
        

class MiniPEKKA:
    def __init__(self):
        # Basic attributes
        self.name = "Mini P.E.K.K.A"
        self.cost = 4
        self.hp = 1390
        self.speed = 90
        self.count = 1
        self.transport = "Ground"
        self.type = "Troop"
        

        # Attack
        self.attack_type = "Single Target"
        self.target_type = "Ground"
        
        self.damage = 755
        self.attack_speed = 1.6
        self.range = 0.8

        # Others
        self.deploy_time = 1.0

class Knight:
    def __init__(self):
        # Basic attributes
        self.name = "Knight"
        self.cost = 3
        self.hp = 1766
        self.speed = 60
        self.count = 1
        self.type = "Troop"
        self.transport = "Ground"

        # Attack
        self.attack_type = "Single Target"
        self.target_type = "Ground"

        self.damage = 202
        self.attack_speed = 1.2
        self.range = 1.2

        # Others
        self.deploy_time = 1.0
        

class Archers:
    def __init__(self):
        # Basic attributes
        self.name = "Archers"
        self.cost = 3
        self.hp = 304
        self.speed = 75
        self.count = 2
        self.transport = "Ground"
        self.type = "Troop"

        # Attack
        self.attack_type = "Single Target"
        self.target_type = "Air, Ground"
        
        self.damage = 112
        self.attack_speed = 0.9
        self.range = 5

        self.projectile_speed = 600

        # Others
        self.deploy_time = 1.0
        

class Minions:
    def __init__(self):
        # Basic attributes
        self.name = "Minions"
        self.cost = 3
        self.hp = 230
        self.count = 3
        self.speed = 90
        self.transport = "Air"
        self.type = "Troop"

        # Attack
        self.attack_type = "Single Target"
        self.target_type = "Air, Ground"
        
        self.damage = 107
        self.attack_speed = 1.2
        self.range = 2.5

        self.projectile_speed = 1000

        # Others
        self.deploy_time = 1.0

class Musketeer:
    def __init__(self):
        # Basic attributes
        self.name = "Musketeer"
        self.cost = 4
        self.hp = 721
        self.speed = 60
        self.count = 1
        self.transport = "Ground"
        self.type = "Troop"

        # Attack
        self.attack_type = "Single Target"
        self.target_type = "Air, Ground"
        
        self.damage = 217
        self.attack_speed = 1
        self.range = 6

        self.projectile_speed = 1000

        # Others
        self.deploy_time = 1.0

class Arrows:
    def __init__(self):
        # Basic attributes
        self.name = "Arrows"
        self.cost = 3
        self.speed = 1100
        self.count = 3
        self.type = "Spell"

        # Attack
        self.attack_type = "Area Damage"
        self.target_type = "Air, Ground"
        
        self.damage = 122
        self.crown_tower_damage = 31
        self.attack_speed = 0.5
        self.radius = 3.5

        # Others
        self.deploy_time = 0

class Fireball:
    def __init__(self):
        # Basic attributes
        self.name = "Fireball"
        self.cost = 4
        self.speed = 600
        self.count = 1
        self.type = "Spell"

        # Attack
        self.attack_type = "Area Damage"
        self.target_type = "Air, Ground"
        
        self.damage = 688
        self.crown_tower_damage = 159
        self.attack_speed = 0.5
        self.radius = 2.5

        # Others
        self.deploy_time = 0