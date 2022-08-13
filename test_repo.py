import unittest
from SeeGitHubRepos import GitHubRepo


class GetRepoTest(unittest.TestCase):
  
   
    case_1 = [(1, 'randomDot'),
            (2, 'birthday'),
            (3, 'Facebook-Clone'),
            (4, 'zsanal'),
            (5, 'OlguD'),
            (6, 'Survey-Form'),
            (7, 'JUST-HTML-CV'),
            (8, 'Circle'),
            (9, 'Guessing-Game'),
            (10, 'Password-Generator'),
            (11, 'random-wordlist'),
            (12, 'mathematical-operations-with-function')]

    case_2 = [(1, 'tetris-js'),
            (2, 'twitter_login_yt'),
            (3, 'facebook_login_yt'),
            (4, 'ytb_snake_js'),
            (5, 'ytb_tree2_js'),
            (6, 'ytb_tree_js'),
            (7, 'estimating-pi'),
            (8, 'cs319-spring22-git-lab'),
            (9, 'matrix-faces'),
            (10, 'ytb_matrix_js'),
            (11, 'ytb_firework_js'),
            (12, 'ytb_snake_py'),
            (13, 'ytb_purple_rain'),
            (14, 'Ballerina-3D-Clone'),
            (15, 'electricliaraclar.com'),
            (16, 'nextjs-blog'),
            (17, 'Tricky-Track-3D-Clone'),
            (18, 'CS353-Project'),
            (19, 'rocket_lander_unity'),
            (20, 'multiplayer-game-with-javascript'),
            (21, 'personalwebsite'),
            (22, 'opencv'),
            (23, 'netflix-clone'),
            (24, 'Basic-unity-game'),
            (25, 'CS102-tutorial-assignment'),
            (26, 'mobilegame'),
            (27, 'snake-game'),
            (28, 'articleFocuser')] 
    
    def test_1(self):
        get_repo = GitHubRepo("OlguD")
        self.assertEqual(get_repo.fetchRepo(), self.case_1)

    def test_2(self):
        get_repo = GitHubRepo("servetgulnaroglu")
        self.assertEqual(get_repo.fetchRepo(), self.case_2)


if __name__ == '__main__':
    unittest.main()
