from mycroft import MycroftSkill, intent_file_handler


class LectureSubjects(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('subjects.lecture.intent')
    def handle_subjects_lecture(self, message):
        self.speak_dialog('subjects.lecture')


def create_skill():
    return LectureSubjects()

