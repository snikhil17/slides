# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

# from tkinter import Button
# from typing import Any, Text, Dict, List

# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher


# class ActionBadFeeling(Action):

#     def name(self) -> Text:
#         return "action_hello_world"

#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

#         buttons = [
#             {"payload":'/more_specific{"feelings":"anxiety"}', "title": "anxiety"}, 
#             {"payload":'/more_specific{"feelings":"stressed"}', "title": "stressed"},  
#             {"payload":'/more_specific{"feelings":"sad"}', "title": "sad"},  
#             {"payload":'/more_specific{"feelings":"hopeless"}', "title": "hopeless"}
#         ]
#         dispatcher.utter_message(text="I'm sorry to hear you're not doing well today. It's not always easy to discuss, but can you tell me what has got you feeling down?", buttons = buttons)

#         return []
# from rasa_core_sdk import Action
# from rasa_core_sdk.events import Restarted

# class ActionRestarted(Action):
#     """This is for restarting the chat"""

#     def name(self):
#         return "action_restart"

#     def run(self, dispatcher, tracker, domain):
#         return [Restarted()]