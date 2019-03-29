# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import logging
import requests
import json
from rasa_core_sdk import Action
from rasa_core_sdk.events import  UserUtteranceReverted

logger = logging.getLogger(__name__)


class ActionJoke(Action):
    def name(self):
        # define the name of the action which can then be included in training stories
        return "action_joke"

    def run(self, dispatcher, tracker, domain):
        # what your action should do
        request = json.loads(requests.get('https://api.chucknorris.io/jokes/random').text)  # make an api call
        joke = request['value']  # extract a joke from returned json response
        dispatcher.utter_message(joke)  # send the message back to the user
        return []

class ActionDefaultFallback(Action):

    def name(self):
        return "action_default_fallback"

    def run(self, dispatcher, tracker, domain):

        # Fallback caused by Core
        dispatcher.utter_template('utter_default', tracker)
        # If doesn't return UserUtteranceReverted event
        # The next predictions of your bot may become inaccurate, 
        # as it is very likely that the fallback action is not present in your stories.
        return [UserUtteranceReverted()]
