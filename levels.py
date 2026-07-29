from Class import *
levels = {
    1: {0: Player(250, 400),
        
        1:{1: Object(600, 400, 200, 200),
            2: Object(300, 350, 200, 20),
            3: Object(150, 200, 50, 800),
            4: Object(390, 350, 20, 300)},

        2: {1: Object(600, 400, 200, 200),
            2: Object(300, 350, 200, 20),
            3: Object(150, 200, 50, 800),
            4: Object(390, 0, 20, 350)},

        3: Teleporter(0, 550, 200, 50),
        4: [
            Spike(725, 350, "up"),
            Spike(500, 20, "down"),
            Spike(550, 20, "down"),
            Spike(600, 20, "down"),
            Spike(200, 200, "right"),
            Spike(100, 200, "left"),
            Spike(20, 50, "right")
            ],
        5: [
            Spike(500, 20, "down"),
            Spike(550, 20, "down"),
            Spike(600, 20, "down"),
            Spike(725, 350, "up")
            ]
    },
    2: {0: Player(250, 400),
        1: {1: Object(600, 400, 200, 200),
            2: Object(300, 100, 200, 20),
            3: Object(150, 200, 50, 800),
            4: Object(390, 350, 20, 300)},
        2: {1: Object(600, 400, 200, 200),
            2: Object(300, 350, 200, 20),
            3: Object(150, 200, 50, 800),
            4: Object(390, 0, 20, 350)},
        3: Teleporter(0, 550, 200, 50),
        4: [
            Spike(400, 40, "up"),
            Spike(500, 40, "down"),    
            Spike(600, 40, "left"),
            Spike(700, 40, "right")
            ]
    }
}