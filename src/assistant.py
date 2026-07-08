import re


def _contains_number(text):
    match = re.search(r"\b(\d{1,2})\b", text)
    if match:
        return int(match.group(1))
    return None


def _response(action, parameters, explanation):
    return {
        "action": action,
        "parameters": parameters,
        "explanation": explanation,
    }


def interpret_command(user_input):
    """
    Simulate a simple AI assistant using keyword matching.

    This function does not use a real LLM and does not treat prompt injection
    phrases specially. That is intentional: the simulator demonstrates that a
    risky action can still be extracted from malicious-looking text.
    """
    text = user_input.lower()
    temperature = _contains_number(text)

    if "light" in text and "turn on" in text:
        return _response(
            "turn_on_light",
            {},
            "The assistant interpreted the command as a request to turn on the living room light.",
        )

    if "light" in text and "turn off" in text:
        return _response(
            "turn_off_light",
            {},
            "The assistant interpreted the command as a request to turn off the living room light.",
        )

    if "door" in text and "unlock" in text:
        return _response(
            "unlock_front_door",
            {},
            "The assistant interpreted the command as a request to unlock the front door.",
        )

    if "door" in text and "lock" in text:
        return _response(
            "lock_front_door",
            {},
            "The assistant interpreted the command as a request to lock the front door.",
        )

    if "thermostat" in text and temperature is not None:
        return _response(
            "set_thermostat",
            {"temperature": temperature},
            f"The assistant interpreted the command as a request to set the thermostat to {temperature} degrees.",
        )

    if "thermostat" in text and ("status" in text or "show" in text or "read" in text):
        return _response(
            "read_thermostat_status",
            {},
            "The assistant interpreted the command as a request to read the thermostat status.",
        )

    if "camera" in text and ("camera status" in text or "show camera" in text or "read camera" in text):
        return _response(
            "read_camera_status",
            {},
            "The assistant interpreted the command as a request to read the camera status.",
        )

    if "camera" in text and "disable" in text:
        return _response(
            "disable_security_camera",
            {},
            "The assistant interpreted the command as a request to disable the security camera.",
        )

    if "camera" in text and "enable" in text:
        return _response(
            "enable_security_camera",
            {},
            "The assistant interpreted the command as a request to enable the security camera.",
        )

    if "alarm" in text and ("turn off" in text or "disable" in text):
        return _response(
            "turn_off_alarm",
            {},
            "The assistant interpreted the command as a request to turn off the alarm.",
        )

    if "security system" in text and ("turn off" in text or "disable" in text):
        return _response(
            "turn_off_alarm",
            {},
            "The assistant interpreted the command as a request to turn off the alarm system.",
        )

    if "alarm" in text and ("turn on" in text or "enable" in text):
        return _response(
            "turn_on_alarm",
            {},
            "The assistant interpreted the command as a request to turn on the alarm.",
        )

    if "alarm" in text and ("status" in text or "show" in text or "read" in text):
        return _response(
            "read_alarm_status",
            {},
            "The assistant interpreted the command as a request to read the alarm status.",
        )

    if "door" in text and ("status" in text or "show" in text or "read" in text):
        return _response(
            "read_door_status",
            {},
            "The assistant interpreted the command as a request to read the front door status.",
        )

    return _response(
        "unknown",
        {},
        "The assistant could not understand the command.",
    )
