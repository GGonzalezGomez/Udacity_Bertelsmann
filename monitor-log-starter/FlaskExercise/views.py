from flask import flash, render_template, redirect, request
from FlaskExercise import app


@app.route('/')
def home():
    log = request.values.get('log_button')
    # TODO: Appropriately log the different button presses
    #   with the appropriate log level.
    if log == "info":
        app.logger.info("Info button pressed")
    if log == "warning":
        app.logger.warning("Warning button pressed")
    if log == "error":
        app.logger.error("Error button pressed")
    if log == "critical":
        app.logger.critical("Critical button pressed")
    return render_template(
        'index.html',
        log=log
    )
