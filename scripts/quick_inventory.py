import pygame

QUICK_INVENTORY_POSITION = (40, 621)
BOX_SIZE = (76, 76)


class QuickInventory:
    def __init__(self):
        self.selected_item = None

    def draw(self, screen):

        box_position = (
            QUICK_INVENTORY_POSITION[0] - 10, QUICK_INVENTORY_POSITION[1] - 10)

        pygame.draw.rect(screen, (0, 0, 0), (box_position, BOX_SIZE), 0, 10)

        image = self.selected_item.image
        scaled_image = pygame.transform.scale(
            image, (image.get_width() * 3.5, image.get_height() * 3.5))

        screen.blit(scaled_image, QUICK_INVENTORY_POSITION)

    def find_selected_item(self, player):
        for item in player.items:
            if item.selected:
                self.selected_item = item
                break

    def update(self, player, screen):
        self.find_selected_item(player)
        self.draw(screen)
