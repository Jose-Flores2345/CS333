import unittest
import pygame
from additions import draw_board, draw_pieces, check_options
from additions import check_king, check_queen, check_bishop, check_rook, check_pawn, check_knight
from additions import check_valid_moves, draw_valid, draw_captured, draw_check
from chess.additions import winner


class TestChessIntegration(unittest.TestCase):

    def setUp(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 900))
        self.white_pieces = ['pawn', 'rook']
        self.white_locations = [(0, 0), (1, 0)]
        self.black_pieces = ['pawn', 'bishop']
        self.black_locations = [(0, 7), (2, 7)]
        self.turn = 0

    def tearDown(self):
        pygame.quit()

    def test_draw_board_and_pieces_integration(self):
        surface = pygame.Surface((800, 900))
        draw_board(surface, self.turn)
        draw_pieces(surface, self.white_pieces, self.white_locations, self.black_pieces, self.black_locations, self.turn)

    def test_check_options_integration(self):
        selection = 0
        destination = (0, 1)
        self.white_locations[selection] = destination
        actual_moves = check_options(self.white_pieces, self.white_locations, self.turn)
        expected_moves = [
            [],
            [(1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0), (7, 0)],
        ]

        self.assertEqual(actual_moves, expected_moves)

    def test_check_king_integration(self):
        position = (4, 0)
        actual_moves = check_king(position, 'white', self.white_locations, self.black_locations)
        expected_moves = [(3, 0), (5, 0), (3, 1), (4, 1), (5, 1)]
        self.assertEqual(actual_moves, expected_moves)

    def test_check_queen_integration(self):
        position = (3, 3)
        actual_moves = check_queen(position, 'black', self.white_locations, self.black_locations)
        expected_moves = [(2, 2), (1, 1), (0, 0), (4, 2), (5, 1), (6, 0), (2, 4), (1, 5), (0, 6), (4, 4), (5, 5),
                          (6, 6), (3, 2), (3, 1), (3, 0), (3, 4), (3, 5), (3, 6), (3, 7), (2, 3), (1, 3), (0, 3),
                          (4, 3), (5, 3), (6, 3), (7, 3)]
        self.assertEqual(actual_moves, expected_moves)

        def test_check_bishop_integration(self):
            position = (3, 3)
            actual_moves = check_bishop(position, 'white', self.white_locations, self.black_locations)
            expected_moves = [(2, 2), (1, 1), (0, 0), (4, 2), (5, 1), (6, 0), (2, 4), (1, 5), (0, 6), (4, 4), (5, 5),
                              (6, 6)]
            self.assertEqual(actual_moves, expected_moves)

        def test_check_rook_integration(self):
            position = (3, 3)
            actual_moves = check_rook(position, 'white', self.white_locations, self.black_locations)
            expected_moves = [(3, 2), (3, 1), (3, 0), (3, 4), (3, 5), (3, 6), (3, 7), (2, 3), (1, 3), (0, 3), (4, 3),
                              (5, 3), (6, 3), (7, 3)]
            self.assertEqual(actual_moves, expected_moves)

        def test_check_pawn_integration(self):
            position = (3, 1)
            actual_moves = check_pawn(position, 'white', self.white_locations, self.black_locations)
            expected_moves = [(3, 2)]
            self.assertEqual(actual_moves, expected_moves)

        def test_check_knight_integration(self):
            position = (3, 3)
            actual_moves = check_knight(position, 'white', self.white_locations, self.black_locations)
            expected_moves = [(1, 2), (1, 4), (2, 1), (2, 5), (4, 1), (4, 5), (5, 2), (5, 4)]
            self.assertEqual(actual_moves, expected_moves)

        def setUp(self):
            global turn_step, white_options, black_options, selection, white_pieces, white_locations, black_pieces, black_locations, captured_pieces_white, captured_pieces_black, piece_list, counter
            turn_step = 0
            white_options = [[(3, 3), (4, 4)], [(2, 2), (5, 5)]]
            black_options = [[(3, 4), (4, 3)], [(2, 5), (5, 2)]]
            selection = 0
            white_pieces = ['king', 'queen']
            white_locations = [(3, 3), (4, 4)]
            black_pieces = ['king', 'queen']
            black_locations = [(3, 4), (4, 3)]
            captured_pieces_white = []
            captured_pieces_black = []
            piece_list = ['king', 'queen', 'rook', 'bishop', 'knight', 'pawn']
            counter = 10

        def test_check_valid_moves_integration(self):
            global selection
            selection = 1
            valid_moves = check_valid_moves()
            expected_moves = [(2, 2), (5, 5)]
            self.assertEqual(valid_moves, expected_moves)

        def test_draw_valid_integration(self):
            global selection
            selection = 0
            valid_moves = [(3, 3), (4, 4)]
            draw_valid(valid_moves)
        def test_draw_captured_integration(self):
            draw_captured()
        def test_draw_check_integration(self):
            draw_check()

        from unittest.mock import MagicMock

        # Mocking pygame functions for the purpose of testing
        pygame.draw = MagicMock()
        pygame.blit = MagicMock()
        pygame.mouse = MagicMock()

        # Mocking game state
        turn_step = 0
        white_locations = [(1, 0), (3, 0), (5, 0), (7, 0), (0, 1), (2, 1), (4, 1), (6, 1)]
        black_locations = [(0, 7), (2, 7), (4, 7), (6, 7), (1, 6), (3, 6), (5, 6), (7, 6)]
        white_pieces = ['pawn', 'pawn', 'pawn', 'pawn', 'rook', 'knight', 'bishop', 'queen']
        black_pieces = ['pawn', 'pawn', 'pawn', 'pawn', 'rook', 'knight', 'bishop', 'queen']
        white_moved = [False, False, False, False, False, False, False, False]
        black_moved = [False, False, False, False, False, False, False, False]
        check = False
        font = MagicMock()

        # Mocking screen
        screen = MagicMock()

        def draw_game_over():
            pass  # Mocking the function for testing purposes

        def check_ep(old_coords, new_coords):
            pass  # Mocking the function for testing purposes

        def check_castling():
            pass  # Mocking the function for testing purposes

        def draw_castling(moves):
            pass  # Mocking the function for testing purposes

        def check_promotion():
            pass  # Mocking the function for testing purposes

        def draw_promotion():
            pass  # Mocking the function for testing purposes

        class TestChessFunctions(unittest.TestCase):

            def test_draw_game_over(self):
                draw_game_over()
                pygame.draw.rect.assert_called_once()
                pygame.blit.assert_any_call(font.render(f'{winner} won the game!', True, 'white'), (210, 210))
                pygame.blit.assert_any_call(font.render(f'Press ENTER to Restart!', True, 'white'), (210, 240))

            def test_check_ep(self):
                old_coords = (0, 1)
                new_coords = (0, 3)
                ep_coords = check_ep(old_coords, new_coords)
                self.assertEqual(ep_coords, (0, 2))

            def test_check_castling(self):
                castle_moves = check_castling()
                self.assertEqual(castle_moves, [])

            def test_draw_castling(self):
                moves = [((4, 0), (7, 0)), ((4, 0), (0, 0))]
                draw_castling(moves)
                pygame.draw.circle.assert_any_call(screen, 'red', (7 * 100 + 50, 0 * 100 + 70), 8)
                pygame.blit.assert_any_call(font.render('king', True, 'black'), (7 * 100 + 30, 0 * 100 + 70))
                pygame.draw.circle.assert_any_call(screen, 'red', (0 * 100 + 50, 0 * 100 + 70), 8)
                pygame.blit.assert_any_call(font.render('rook', True, 'black'), (0 * 100 + 30, 0 * 100 + 70))
                pygame.draw.line.assert_any_call(screen, 'red', (7 * 100 + 50, 0 * 100 + 70),
                                                 (7 * 100 + 50, 0 * 100 + 70), 2)

            def test_check_promotion(self):
                white_promotion, black_promotion, promote_index = check_promotion()
                self.assertEqual(white_promotion, False)
                self.assertEqual(black_promotion, False)
                self.assertEqual(promote_index, 100)

            def test_draw_promotion(self):
                draw_promotion()
                pygame.draw.rect.assert_called_once_with(screen, 'dark gray', [800, 0, 200, 420])
                pygame.draw.rect.assert_called_once_with(screen, 'red', [800, 0, 200, 420], 8)


if __name__ == '__main__':
    unittest.main()
