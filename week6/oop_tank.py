class Tank:
    def _init_(self,ชื่อ,กระสุน,พลังชีวิต):
        self.name = ชื่อ
        self.ammo = กระสุน
        self.hp = พลังชีวิต
        def add_ammo(self,กระสุน):
            if self. ammo >= 10:
                print('กระสุนยังเต็มอยุ๋')
            else :
                self.ammo+=กระสุน
                print("รีโหลด")
                def fire_ammo(felf,enemy):
                    enemy.hp -=1

tank1 = Tank("A1",10,5)
tank2 = Tank("A2",5,5)
tank3 = Tank("A1",9,5)

Tank.fire_ammo(Tank3)