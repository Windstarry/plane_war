
class Settings(object):

    def __init__(self):
        #设置屏幕参数
        self.screen_width = 480
        self.screen_height = 700
        #设置背景图像
        self.bg_image = 'images/background.png'
        #设置飞船图像位置
        self.ship_image = 'images/me2.png'
        self.bullet_image = 'images/bullet1.png'
        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        #游戏相关参数初始化
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 3
        self.alien_speed_factor = 0.5
        self.alien_points = 1
        #设置移动方向,1表示右移，-1表示左移
        self.fleet_direction = 1
    
    def increase_speed(self):
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale
        self.alien_points *= int(self.alien_points*self.score_scale)