import pygame
from settings import *
from support import *
from item import Item
from cooldown import Cooldown


class Player(pygame.sprite.Sprite):
    def __init__(self, pos, group, collision_sprites):
        super().__init__(group)

        # general setup
        self.import_assets()
        self.status = ANIMATION.DOWN_IDLE
        self.frame_index = 0

        self.image = self.animations[self.status][self.frame_index]
        self.rect = self.image.get_rect(center=pos)
        self.z = LAYERS['main']

        # cooldowns
        self.cooldowns = {
            'tool switch': Cooldown(200)
        }

        # movement
        self.direction = pygame.math.Vector2()
        self.position = pygame.math.Vector2(self.rect.center)
        self.speed = SPEED

        # collision
        self.hitbox = self.rect.copy().inflate((-126, -70))
        self.collision_sprites = collision_sprites

        self.items = [
            Item("apple", 2),
            Item("hoe", 1, True),
            Item("axe", 1),
        ]

    def import_assets(self):
        self.animations = {
            ANIMATION.UP_IDLE: [],
            ANIMATION.DOWN_IDLE: [],
            ANIMATION.LEFT_IDLE: [],
            ANIMATION.RIGHT_IDLE: [],
            ANIMATION.UP: [],
            ANIMATION.DOWN: [],
            ANIMATION.LEFT: [],
            ANIMATION.RIGHT: []
        }

        for animation in self.animations:
            filePath = "assets/character/" + animation.value
            self.animations[animation] = import_folder(filePath)

    def input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_w]:
            self.direction.x = -1
            self.direction.y = -0.5
            self.status = ANIMATION.UP

        elif keys[pygame.K_s]:
            self.direction.x = 1
            self.direction.y = 0.5
            self.status = ANIMATION.DOWN

        elif keys[pygame.K_a]:
            self.direction.x = -1
            self.direction.y = 0.5
            self.status = ANIMATION.LEFT

        elif keys[pygame.K_d]:
            self.direction.x = 1
            self.direction.y = - 0.5
            self.status = ANIMATION.RIGHT

        elif keys[pygame.K_LEFT] and not self.cooldowns['tool switch'].active:

            self.cooldowns['tool switch'].activate()
            self.handle_change_tool_click('previous')

        elif keys[pygame.K_RIGHT] and not self.cooldowns['tool switch'].active:

            self.cooldowns['tool switch'].activate()
            self.handle_change_tool_click('next')

        else:
            self.direction.x = 0
            self.direction.y = 0

    def handle_change_tool_click(self, changeTo):
        selected_item_index = next(
            (i for i, item in enumerate(self.items) if item.selected), None)

        if selected_item_index is not None:
            self.items[selected_item_index].selected = False

            if changeTo == 'next':
                new_index = (selected_item_index + 1) % len(self.items)
            elif changeTo == 'previous':
                new_index = (selected_item_index - 1) % len(self.items)
            else:
                new_index = selected_item_index

            self.items[new_index].selected = True

    def animate(self, dt):
        self.frame_index += 4 * dt
        if self.frame_index >= len(self.animations[self.status]):
            self.frame_index = 0

        self.image = self.animations[self.status][int(self.frame_index)]

    def update_cooldowns(self):
        for cooldown in self.cooldowns.values():
            cooldown.update()

    def collision(self, direction):

        for sprite in self.collision_sprites:
            if hasattr(sprite, 'hitbox'):
                if sprite.hitbox.colliderect(self.hitbox):
                    if direction == 'horizontal':
                        if self.direction.x > 0:  
                            self.hitbox.right = sprite.hitbox.left
                        if self.direction.x < 0: 
                            self.hitbox.left = sprite.hitbox.right

                        self.rect.centerx = self.hitbox.centerx
                        self.position.x = self.hitbox.centerx

                    if direction == 'vertical':
                        if self.direction.y > 0: 
                            self.hitbox.bottom = sprite.hitbox.top
                        if self.direction.y < 0: 
                            self.hitbox.top = sprite.hitbox.bottom

                        self.rect.centery = self.hitbox.centery
                        self.position.y = self.hitbox.centery

    def move(self, dt):
        if self.direction.magnitude() > 0:
            self.direction = self.direction.normalize()

        self.position.x += self.direction.x * self.speed * dt
        self.hitbox.centerx = round(self.position.x)
        self.rect.centerx = round(self.position.x)
        self.collision('horizontal')

        self.position.y += self.direction.y * self.speed * dt
        self.hitbox.centery = round(self.position.y)
        self.rect.centery = round(self.position.y)
        self.collision('vertical')

    def get_status(self):

        if self.direction.magnitude() == 0:
            new_status_str = self.status.value.split('_')[0] + '_idle'
            self.status = ANIMATION(new_status_str)

    def update(self, dt):
        self.input()
        self.get_status()
        self.move(dt)
        self.animate(dt)
        self.update_cooldowns()
