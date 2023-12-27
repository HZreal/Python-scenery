"""
链路追踪 opentelemetry
doc: https://opentelemetry.io/docs/instrumentation/python/getting-started/

pip install opentelemetry-api
pip install opentelemetry-sdk
pip install 'flask<3' 'werkzeug<3'
pip install opentelemetry-distro
opentelemetry-bootstrap -a install

"""

# from random import randint
# from flask import Flask, request
# import logging
#
# app = Flask(__name__)
# logging.basicConfig(level=logging.INFO)
# logger = logging.getLogger(__name__)
#
#
# @app.route("/rolldice")
# def roll_dice():
#     player = request.args.get('player', default=None, type=str)
#     result = str(roll())
#     if player:
#         logger.warn("%s is rolling the dice: %s", player, result)
#     else:
#         logger.warn("Anonymous player is rolling the dice: %s", result)
#     return result
#
#
# def roll():
#     return randint(1, 6)


"""
链路信息输出到控制台
export OTEL_PYTHON_LOGGING_AUTO_INSTRUMENTATION_ENABLED=true
opentelemetry-instrument \
    --traces_exporter console \
    --metrics_exporter console \
    --logs_exporter console \
    --service_name dice-server \
    flask run -p 8080

"""

##############################################################################
# from random import randint
# from flask import Flask
#
# from opentelemetry import trace
#
# # Acquire a tracer
# tracer = trace.get_tracer("diceroller.tracer")
#
# app = Flask(__name__)
#
#
# @app.route("/rolldice")
# def roll_dice():
#     return str(roll())
#
#
# def roll():
#     # This creates a new span that's the child of the current one
#     with tracer.start_as_current_span("roll") as rollspan:
#         res = randint(1, 6)
#         rollspan.set_attribute("roll.value", res)
#         return res


"""
export OTEL_PYTHON_LOGGING_AUTO_INSTRUMENTATION_ENABLED=true
opentelemetry-instrument \
    --traces_exporter console \
    --metrics_exporter console \
    --logs_exporter console \
    --service_name dice-server \
    flask run -p 8080

"""

##############################################################################
# These are the necessary import declarations
from opentelemetry import trace
from opentelemetry import metrics

from random import randint
from flask import Flask, request
import logging

# Acquire a tracer
tracer = trace.get_tracer("diceroller.tracer")
# Acquire a meter.
meter = metrics.get_meter("diceroller.meter")

# Now create a counter instrument to make measurements with
roll_counter = meter.create_counter(
    "dice.rolls",
    description="The number of rolls by roll value",
)

app = Flask(__name__)
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


@app.route("/rolldice")
def roll_dice():
    # This creates a new span that's the child of the current one
    with tracer.start_as_current_span("roll") as roll_span:
        player = request.args.get('player', default=None, type=str)
        result = str(roll())
        roll_span.set_attribute("roll.value", result)
        # This adds 1 to the counter for the given roll value
        roll_counter.add(1, {"roll.value": result})
        if player:
            logger.warn("{} is rolling the dice: {}", player, result)
        else:
            logger.warn("Anonymous player is rolling the dice: %s", result)
        return result


def roll():
    return randint(1, 6)

"""
export OTEL_PYTHON_LOGGING_AUTO_INSTRUMENTATION_ENABLED=true
opentelemetry-instrument \
    --traces_exporter console \
    --metrics_exporter console \
    --logs_exporter console \
    --service_name dice-server \
    flask run -p 8080

"""
