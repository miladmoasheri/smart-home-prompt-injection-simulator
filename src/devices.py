DEFAULT_DEVICE_STATES = {
    "living_room_light": "off",
    "front_door": "locked",
    "thermostat_temperature": 20,
    "security_camera": "enabled",
    "alarm_system": "off",
}


def get_default_device_states():
    """Return a fresh copy so each session starts with clean fake devices."""
    return DEFAULT_DEVICE_STATES.copy()


def turn_on_light(states, parameters=None):
    states["living_room_light"] = "on"
    return "Living room light turned on."


def turn_off_light(states, parameters=None):
    states["living_room_light"] = "off"
    return "Living room light turned off."


def unlock_front_door(states, parameters=None):
    states["front_door"] = "unlocked"
    return "Front door unlocked."


def lock_front_door(states, parameters=None):
    states["front_door"] = "locked"
    return "Front door locked."


def set_thermostat(states, parameters=None):
    parameters = parameters or {}
    temperature = parameters.get("temperature")

    if temperature is None:
        return "No thermostat temperature was provided."

    states["thermostat_temperature"] = temperature
    return f"Thermostat set to {temperature} degrees."


def read_thermostat_status(states, parameters=None):
    return f'Thermostat is set to {states["thermostat_temperature"]} degrees.'


def enable_security_camera(states, parameters=None):
    states["security_camera"] = "enabled"
    return "Security camera enabled."


def disable_security_camera(states, parameters=None):
    states["security_camera"] = "disabled"
    return "Security camera disabled."


def read_camera_status(states, parameters=None):
    return f'Security camera is {states["security_camera"]}.'


def turn_on_alarm(states, parameters=None):
    states["alarm_system"] = "on"
    return "Alarm system turned on."


def turn_off_alarm(states, parameters=None):
    states["alarm_system"] = "off"
    return "Alarm system turned off."


def read_alarm_status(states, parameters=None):
    return f'Alarm system is {states["alarm_system"]}.'


def read_door_status(states, parameters=None):
    return f'Front door is {states["front_door"]}.'


ACTION_HANDLERS = {
    "turn_on_light": turn_on_light,
    "turn_off_light": turn_off_light,
    "unlock_front_door": unlock_front_door,
    "lock_front_door": lock_front_door,
    "set_thermostat": set_thermostat,
    "read_thermostat_status": read_thermostat_status,
    "enable_security_camera": enable_security_camera,
    "disable_security_camera": disable_security_camera,
    "read_camera_status": read_camera_status,
    "turn_on_alarm": turn_on_alarm,
    "turn_off_alarm": turn_off_alarm,
    "read_alarm_status": read_alarm_status,
    "read_door_status": read_door_status,
}


def execute_action(states, action, parameters=None):
    """
    Execute a fake smart-home action.

    No real devices, APIs, networks, locks, or cameras are ever contacted.
    """
    handler = ACTION_HANDLERS.get(action)

    if handler is None:
        return "Unknown action. No fake device state was changed."

    return handler(states, parameters)
