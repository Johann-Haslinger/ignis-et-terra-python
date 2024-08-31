from os import walk
import pygame

def import_folder(path):
	surface_list = []

	for _, __, img_files in walk(path):
		for image in img_files:
			full_path = path + '/' + image
			image_surf = pygame.image.load(full_path).convert_alpha()
			surface_list.append(image_surf)

	return surface_list

def import_folder_dict(path):
	surafce_dict = {}

	for _, __, img_files in walk(path):
		for image in img_files:
			full_path = path + '/' + image
			image_surf = pygame.image.load(full_path).convert_alpha()
			surafce_dict[image.split('.')[0]] = image_surf

	return surafce_dict


def iso_to_pixel(iso_x, iso_y):
    # Beispielwerte für Offset und Skalierung. Diese müssen an deine spezifische Karte angepasst werden.
    TILE_SIZE = 64
    offset_x = 800
    offset_y = 600

    pixel_x = (iso_x + iso_y) * (TILE_SIZE // 2) + offset_x
    pixel_y = (iso_x - iso_y) * (TILE_SIZE // 4) + offset_y

    return pixel_x, pixel_y

def pixel_to_iso(pixel_x, pixel_y):
    TILE_SIZE = 64
    offset_x = 0
    offset_y = 0

    iso_x = (pixel_x - offset_x) // (TILE_SIZE // 2) - (pixel_y - offset_y) // (TILE_SIZE // 4)
    iso_y = (pixel_y - offset_y) // (TILE_SIZE // 4) - iso_x

    return iso_x, iso_y
