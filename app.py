from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen

class MainMenuScreen(Screen):
    pass


class AlphabetMenuScreen(Screen):
    pass

class VowelScreen(Screen):
    pass

class ConsonantScreen(Screen):
    pass





class VideoAScreen(Screen):
    pass

class VideoBScreen(Screen):
    pass

class VideoCScreen(Screen):
    pass

class VideoDScreen(Screen):
    pass

class VideoEScreen(Screen):
    pass

class VideoFScreen(Screen):
    pass

class VideoGScreen(Screen):
    pass

class VideoHScreen(Screen):
    pass

class VideoIScreen(Screen):
    pass

class VideoJScreen(Screen):
    pass

class VideoKScreen(Screen):
    pass

class VideoLScreen(Screen):
    pass

class VideoMScreen(Screen):
    pass

class VideoNScreen(Screen):
    pass

class VideoOScreen(Screen):
    pass

class VideoPScreen(Screen):
    pass

class VideoQScreen(Screen):
    pass

class VideoRScreen(Screen):
    pass

class VideoSScreen(Screen):
    pass

class VideoTScreen(Screen):
    pass

class VideoUScreen(Screen):
    pass

class VideoVScreen(Screen):
    pass

class VideoWScreen(Screen):
    pass

class VideoXScreen(Screen):
    pass

class VideoYScreen(Screen):
    pass

class VideoZScreen(Screen):
    pass






class LearningNumbers_1_25(Screen):
    pass

class LearningNumbers_26_50(Screen):
    pass

class LearningNumbers_51_75(Screen):
    pass

class LearningNumbers_76_100(Screen):
    pass




class LearningCharacter(Screen):
    pass


class LearningWords(Screen):
    pass


class LearningPhrases(Screen):
    pass


class LearningParagrahp(Screen):
    pass


class ElearningApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(MainMenuScreen(name='main_menu'))

        sm.add_widget(LearningCharacter(name="learning_characters"))
        sm.add_widget(LearningWords(name="learning_words"))
        sm.add_widget(LearningPhrases(name="learning_phrases"))
        sm.add_widget(LearningParagrahp(name="learning_paragraphs"))
        
        
        
        sm.add_widget(AlphabetMenuScreen(name='alphabet_menu'))
        sm.add_widget(VowelScreen(name ="vowel_menu"))
        sm.add_widget(ConsonantScreen(name = "consonant_menu"))
        
        sm.add_widget(VideoAScreen(name='video_a'))
        sm.add_widget(VideoBScreen(name='video_b'))
        sm.add_widget(VideoAScreen(name='video_c'))
        sm.add_widget(VideoBScreen(name='video_d'))
        sm.add_widget(VideoAScreen(name='video_e'))
        sm.add_widget(VideoBScreen(name='video_f'))
        sm.add_widget(VideoAScreen(name='video_g'))
        sm.add_widget(VideoBScreen(name='video_h'))
        sm.add_widget(VideoAScreen(name='video_i'))
        sm.add_widget(VideoBScreen(name='video_j'))
        sm.add_widget(VideoAScreen(name='video_k'))
        sm.add_widget(VideoBScreen(name='video_l'))
        sm.add_widget(VideoAScreen(name='video_m'))
        sm.add_widget(VideoBScreen(name='video_n'))
        sm.add_widget(VideoAScreen(name='video_o'))
        sm.add_widget(VideoBScreen(name='video_p'))
        sm.add_widget(VideoAScreen(name='video_q'))
        sm.add_widget(VideoBScreen(name='video_r'))
        sm.add_widget(VideoAScreen(name='video_s'))
        sm.add_widget(VideoBScreen(name='video_t'))
        sm.add_widget(VideoAScreen(name='video_u'))
        sm.add_widget(VideoBScreen(name='video_v'))
        sm.add_widget(VideoBScreen(name='video_w'))
        sm.add_widget(VideoAScreen(name='video_x'))
        sm.add_widget(VideoBScreen(name='video_y'))
        sm.add_widget(VideoBScreen(name='video_z'))
        
        sm.add_widget(LearningNumbers_1_25(name='learning_numbers_1_25'))
        sm.add_widget(LearningNumbers_26_50(name='learning_numbers_26_50'))
        sm.add_widget(LearningNumbers_51_75(name='learning_numbers_51_75'))
        sm.add_widget(LearningNumbers_76_100(name='learning_numbers_76_100'))
        
        return sm