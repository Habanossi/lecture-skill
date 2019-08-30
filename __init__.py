import datetime
from adapt.intent import IntentBuilder
from mycroft import intent_handler
from mycroft.skills.core import MycroftSkill
from mycroft.util.log import getLogger

__author__ = 'viljanen'

LOGGER = getLogger(__name__)


class LectureSkill(MycroftSkill):



    def __init__(self):
        super(LectureSkill, self).__init__(name="LectureSkill")



    @intent_handler(IntentBuilder("LectureIntent").require("LectureKeyword").require("SubjectKeyword"))



    def handle_lecture_intent(self, message):

        f = open("/opt/mycroft/skills/lecture-subjects-skill/dates.txt", "r")     #open textfile
        dateFound = False
        lectureNumber = 0
        line = f.readline()
        g = open("/opt/mycroft/skills/lecture-subjects-skill/settings.txt", "r")     #open textfile
        line2 = g.readline()
        if line2[0] == "0":
            self.speak_dialog("default")
            dateFound = True
        g.close()
        while(line and not dateFound):                 #while right date hasn't been found and there is lines in the textfile, the program will read new lines from textfile
            lectureNumber += 1         #for each line the lectureNumber will go up
            y = int(line[0:4])         #yyyy
            m = int(line[4:6])         #mm
            d = int(line[6:8])	       #dd
            date = datetime.date(y, m, d)
            if datetime.date.today() == date:    #check if date is today, speak accordingly
                self.speak_dialog("lecture" + str(lectureNumber))
                dateFound = True
            line = f.readline()

        if not dateFound:       #"no lecture today" if no date is found
            self.speak_dialog("nolecture")



        f.close()                      #close textfile


    @intent_handler(IntentBuilder("SettingsIntent").require("LectureKeyword").require("SettingsKeyword").require("ChangeKeyword"))

    def handle_settings_intent(self, message):

            f = open("/opt/mycroft/skills/lecture-subjects-skill/settings.txt", "r")     #open textfile
            line = f.readline()
            f.close()
            f  = open("/opt/mycroft/skills/lecture-subjects-skill/settings.txt", "w")     #open textfile
            if line[0] == "1":
                    f.write("0")
                    self.speak_dialog("defset")
            else:
                    f.write("1")
                    self.speak_dialog("specset")

            f.close()                      #close textfile


    @intent_handler(IntentBuilder("Dialog1Intent").require("DialogKeyword1"))

    def handle_dialog1_intent(self, message):

        self.speak_dialog("dialogAns1")


    @intent_handler(IntentBuilder("Dialog2Intent").require("DialogKeyword2"))

    def handle_dialog2_intent(self, message):

        self.speak_dialog("dialogAns2")

    @intent_handler(IntentBuilder("Dialog3Intent").require("DialogKeyword3"))

    def handle_dialog3_intent(self, message):

        self.speak_dialog("dialogAns3")


    @intent_handler(IntentBuilder("Dialog4Intent").require("DialogKeyword4"))

    def handle_dialog4_intent(self, message):

        self.speak_dialog("dialogAns4")


    @intent_handler(IntentBuilder("Dialog5Intent").require("DialogKeyword5"))

    def handle_dialog5_intent(self, message):

        self.speak_dialog("dialogAns5")





    def stop(self):
        pass




def create_skill():
    return LectureSkill()
