import pygame
import pytest
from level import Level
from settings import level_map, screen_width, screen_height, tile_size


@pytest.fixture
def level_instance():
    mock_screen = pygame.Surface((screen_width, screen_height))
    level = Level(level_map, mock_screen)
    return level


def test_loading_level(level_instance):
    test_map = [
        "XXXXX",
        "XP XX",
        "XXXXX",
    ]
    level_instance.loading_level(test_map)
    assert len(level_instance.tiles.sprites()) == 13


def test_bordure_x_left_movement(level_instance):
    player_mock = pygame.sprite.Sprite()
    player_mock.rect = pygame.Rect(0, 0, 10, 10)
    player_mock.rect.centerx = 0
    player_mock.direction = pygame.math.Vector2(-1, 0)
    level_instance.player.sprite = player_mock
    level_instance.bordure_x()
    assert player_mock.v == 0


def test_bordure_x_right_movement(level_instance):
    player_mock = pygame.sprite.Sprite()
    player_mock.rect = pygame.Rect(0, 0, 10, 10)
    player_mock.rect.centerx = screen_width
    player_mock.direction = pygame.math.Vector2(1, 0)
    level_instance.player.sprite = player_mock
    level_instance.bordure_x()
    assert player_mock.v == 0


def test_collision_hori_left_movement(level_instance):
    test_map = [
        "XXXXX",
        "XP XX",
        "XXXXX",
    ]
    level_instance.loading_level(test_map)

    initial_player_position = level_instance.player.sprite.rect.topleft

    level_instance.player.sprite.direction = pygame.math.Vector2(-1, 0)
    level_instance.collision_hori()

    final_player_position = level_instance.player.sprite.rect.topleft

    assert final_player_position == initial_player_position


def test_collision_hori_right_movement(level_instance):
    test_map = [
        "XXXXX",
        "X PXX",
        "XXXXX",
    ]
    level_instance.loading_level(test_map)

    initial_player_position = level_instance.player.sprite.rect.topright

    level_instance.player.sprite.direction = pygame.math.Vector2(1, 0)
    level_instance.collision_hori()

    final_player_position = level_instance.player.sprite.rect.topright

    assert final_player_position == initial_player_position


def test_collision_ver_down_movement(level_instance):
    test_map = [
        "  P  ",
        "     ",
        "XXXXX",
    ]
    level_instance.loading_level(test_map)
    while level_instance.player.sprite.rect.bottom != 2 * tile_size:
        level_instance.collision_ver()
    assert True
