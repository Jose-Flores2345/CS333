import unittest
import pygame
from additions import draw_board, draw_pieces, check_options
from additions import check_king, check_queen, check_bishop, check_rook, check_pawn, check_knight
from additions import check_valid_moves, draw_valid, draw_captured, draw_check
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

if __name__ == '__main__':
    unittest.main()
