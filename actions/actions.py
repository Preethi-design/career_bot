# from typing import Any, Text, Dict, List, Union, Optional


# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher
# from rasa_sdk.forms import FormAction
# class professionalcourse(Action):

#     def name(self) -> Text:
#         return "proffesional_course"

#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

#         # dispatcher.utter_message(text="Hello World!")

#         # return []
#         gt = {
#             "attachment": {
#                 "type": "template",
#                 "payload": {
#                     "template_type": "generic",
#                     "elements": [
#                         {
#                             "title": "Proffessional Course",
#                             # "image_url":"https://www.trawell.in/admin/images/upload/486072642MarineDrive_Main.jpg",
#                             # "subtitle": "Marine Drive is a buzzing waterfront district known for the Marine Walkway, popular for evening strolls,..",
#                             "buttons": [
#                                 {
#                                     "type": "postback",
#                                     "payload": "/pc_be",
#                                     "title": "BE"
#                                 },
#                                {
#                                     "type": "postback",
#                                     "payload": "/pc_medical",
#                                     "title": "Medical"
#                                 },  
#                             ]
#                         }
#                     ]
                    
#                         }
#             }
#         }
#         dispatcher.utter_button_message(gt)
#         return []