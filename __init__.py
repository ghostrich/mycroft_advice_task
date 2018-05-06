# Copyright 2016 Mycroft AI, Inc.
#
# This file is part of Mycroft Core.
#
# Mycroft Core is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Mycroft Core is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Mycroft Core.  If not, see <http://www.gnu.org/licenses/>.

from adapt.intent import IntentBuilder

from mycroft.skills.core import MycroftSkill
from mycroft.util.log import getLogger
import requests

__author__ = 'wiebke'

LOGGER = getLogger(__name__)


class AdviceSkill(MycroftSkill):
    def __init__(self):
        super(AdviceSkill, self).__init__(name="AdviceSkill")

    def initialize(self):
    
		advice_intent = IntentBuilder("AdviceIntent"). \
            require("AdviceKeyword").build()
        self.register_intent(advice_intent, self.handle_advice_intent)   
        
         
        

    def handle_advice_intent(self, message):
		url = 'http://api.adviceslip.com/advice'
		r = requests.get(url)
		json_output = r.json()
		#print (json_output['slip']['advice'])
        self.speak("Some advice: {}".format(json_output['slip']['advice']))

    def stop(self):
        pass


def create_skill():
    return AdviceSkill()
