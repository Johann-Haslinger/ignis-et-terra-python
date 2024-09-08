import pygame
from settings import *
from cooldown import Cooldown
from item_slot import ItemSlot


INVENTORY_SIZE = (590, 475)
INVENTORY_POSITION = (
    (SCREEN_WIDTH - INVENTORY_SIZE[0]) / 2, (SCREEN_HEIGHT - INVENTORY_SIZE[1]) / 2)
GRAY_1 = (40, 40, 40)
GRAY_2 = (60, 60, 60)


BLACK = (0, 0, 0)
WHITE = (255, 255, 255)


class Inventory:
    def __init__(self):
        self.visible = False
        self.item_slots = []

        self.cool_downs = {
            "visibility change": Cooldown(200)
        }

        self.setup_item_slots()

    def setup_item_slots(self):
        for i in range(5):
            for j in range(4):
                x = INVENTORY_POSITION[0] + 15 + 115 * i
                y = INVENTORY_POSITION[1] + 15 + 115 * j
                self.item_slots.append(ItemSlot((x, y), i + j * 5))

    def draw_inventory_box(self, screen):
        if self.visible:
            rect_surface = pygame.Surface(
                (SCREEN_WIDTH, SCREEN_HEIGHT), pygame.SRCALPHA)

            rect_surface.fill((0, 0, 0, 40))
            screen.blit(rect_surface, (0, 0))

            pygame.draw.rect(
                screen, (30, 30, 30), (INVENTORY_POSITION, INVENTORY_SIZE), 0, 20)

    def input(self):
        pressed_keys = pygame.key.get_pressed()

        if pressed_keys[pygame.K_e] and not self.cool_downs['visibility change'].active:
            self.cool_downs["visibility change"].activate()
            self.visible = not self.visible

    def update_cooldowns(self):
        for cool_down in self.cool_downs.values():
            cool_down.update()

    def draw_item_slots(self, screen,  player):
        if not self.visible:
            return

        for slot in self.item_slots:
            slot_item = None

            if len(player.items) > slot.index:
                slot_item = player.items[slot.index]

            slot.draw(screen, slot_item)

    def update(self, player, screen):
        self.input()
        self.draw_inventory_box(screen)
        self.update_cooldowns()
        self.draw_item_slots(screen, player)


