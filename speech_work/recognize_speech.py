# system
import azure.cognitiveservices.speech as speech_sdk
import logging
import os
import asyncio

# user
from config import set_logger
from utils import make_move

set_logger()


class RecognizeSpeech:
    def __init__(self) -> None:
        self.speech_key, self.service_region = (
            os.environ.get("AZURE_COGNITIVE_SERVICE_KEY"),
            os.environ.get("AZURE_COGNITIVE_SERVICE_REGION"),
        )
        self.speech_config = speech_sdk.SpeechConfig(
            subscription=self.speech_key, region=self.service_region
        )

        # Creates a recognizer with the given settings
        self.speech_recognizer = speech_sdk.SpeechRecognizer(
            speech_config=self.speech_config
        )

    @staticmethod
    def clean_up(text: str):
        # remove whitespaces and the period at the end
        return text.strip().lower()[0:-1]

    async def start_recognizing(self):
        logging.info("Starting the recognition...")

        while True:
            # need to make this async to do multiple commands
            result = self.speech_recognizer.recognize_once()

            try:
                # Checks result.
                if result.reason == speech_sdk.ResultReason.RecognizedSpeech:
                    recognized_text = self.clean_up(result.text)
                    logging.info(f"Raw - Recognized: {recognized_text}")
                    if recognized_text == "stop":
                        logging.warning("Exiting the process!!")
                        os._exit(0)

                    # make the move with pyautogui
                    await make_move(recognized_text)

                elif result.reason == speech_sdk.ResultReason.NoMatch:
                    logging.info(
                        "No speech could be recognized: {}".format(
                            result.no_match_details
                        )
                    )
                elif result.reason == speech_sdk.ResultReason.Canceled:
                    cancellation_details = result.cancellation_details
                    logging.info(
                        "Speech Recognition canceled: {}".format(
                            cancellation_details.reason
                        )
                    )
                    if (
                        cancellation_details.reason
                        == speech_sdk.CancellationReason.Error
                    ):
                        logging.info(
                            "Error details: {}".format(
                                cancellation_details.error_details
                            )
                        )

            except Exception as e:
                logging.error(f"Exception occurred - {e}")


if __name__ == "__main__":
    recognize_speech_obj = RecognizeSpeech()
    asyncio.run(recognize_speech_obj.start_recognizing())
