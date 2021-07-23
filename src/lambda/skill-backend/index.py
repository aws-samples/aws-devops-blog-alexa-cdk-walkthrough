import logging
import datetime

from ask_sdk_core.skill_builder import SkillBuilder
from ask_sdk_core.dispatch_components import (
    AbstractRequestHandler,
    AbstractRequestInterceptor,
    AbstractResponseInterceptor)
import ask_sdk_core.utils as ask_utils
from ask_sdk_core.handler_input import HandlerInput
from ask_sdk_model import Response

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


class TellTimeHandler(AbstractRequestHandler):
    """Handler for Skill Launch and TellTime Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return (ask_utils.is_request_type("LaunchRequest")(handler_input) or
                ask_utils.is_intent_name("TellTimeIntent")(handler_input))

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        logger.info("In TellTimeHandler")

        current_time = datetime.datetime.utcnow().time()
        hour = current_time.strftime('%I').strip('0')
        minute = current_time.strftime('%M')
        ampm = current_time.strftime('%p')

        return (
            handler_input.response_builder
            .speak(f"Hello! It is currently {hour}:{minute} {ampm} U.T.C.")
            .response
        )

class RequestLogger(AbstractRequestInterceptor):
    """Log all Alexa requests."""
    def process(self, handler_input):
        # type: (HandlerInput) -> None
        logger.debug("Alexa Request: {}".format(
            handler_input.request_envelope.request))

class ResponseLogger(AbstractResponseInterceptor):
    """Log all Alexa responses."""
    def process(self, handler_input, response):
        # type: (HandlerInput, Response) -> None
        logger.debug("Alexa Response: {}".format(response))


sb = SkillBuilder()

sb.add_request_handler(TellTimeHandler())

sb.add_global_request_interceptor(RequestLogger())
sb.add_global_response_interceptor(ResponseLogger())

handler = sb.lambda_handler()
