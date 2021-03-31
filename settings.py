
class Settings(object):

    def __init__(self):
        #设置屏幕参数
        self.screen_width = 480
        self.screen_height = 700
        self.bg_color=(224,224,224)
        #设置背景图像
        self.bg_image = 'images/background.png'
        #设置图像位置
        self.ship_image = 'images/me2.png'
        self.bullet_image = 'images/bullet1.png'
        self.alien_image = 'images/enemy1.png'
        self.initialize_dynamic_settings()
        self.bullet_allowed = 6
        #设置最高分保存文件
        self.high_score_file = "high_score.json"
        self.ship_limit = 2
        #设置游戏加速
        self.speedup_scale = 1.1
        self.score_scale = 1.1

    def initialize_dynamic_settings(self):
        #游戏相关参数初始化
        self.ship_speed_factor = 0.3
        self.bullet_speed_factor = 3
        self.alien_speed_factor = 0.5
        self.alien_allowed = 4
        self.alien_points = 1
        #设置移动方向,1表示右移，-1表示左移
        self.fleet_direction = 1
    
    def increase_speed(self):
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale
        self.alien_allowed += 2
        self.alien_points *= int(self.alien_points*self.score_scale)