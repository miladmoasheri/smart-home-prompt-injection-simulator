HIGH_RISK_ACTIONS = {
    "unlock_front_door": "Unlocking the front door is a high-risk action and is blocked in Safe Mode.",
    "turn_off_alarm": "Turning off the alarm is a high-risk action and is blocked in Safe Mode.",
    "disable_security_camera": "Disabling the security camera is a high-risk action and is blocked in Safe Mode.",
}

MEDIUM_RISK_ACTIONS = {
    "set_thermostat": "This medium-risk action is allowed in Safe Mode.",
    "lock_front_door": "Locking the front door is a medium-risk action and is allowed in Safe Mode.",
    "turn_on_alarm": "Turning on the alarm is a medium-risk action and is allowed in Safe Mode.",
    "enable_security_camera": "Enabling the security camera is a medium-risk action and is allowed in Safe Mode.",
}

LOW_RISK_ACTIONS = {
    "turn_on_light": "This low-risk action is allowed in Safe Mode.",
    "turn_off_light": "This low-risk action is allowed in Safe Mode.",
    "read_thermostat_status": "Reading thermostat status is a low-risk action and is allowed in Safe Mode.",
    "read_camera_status": "Reading camera status is a low-risk action and is allowed in Safe Mode.",
    "read_alarm_status": "Reading alarm status is a low-risk action and is allowed in Safe Mode.",
    "read_door_status": "Reading door status is a low-risk action and is allowed in Safe Mode.",
}


def evaluate_action(action):
    if action in HIGH_RISK_ACTIONS:
        return {
            "allowed": False,
            "risk_level": "high",
            "reason": HIGH_RISK_ACTIONS[action],
        }

    if action in MEDIUM_RISK_ACTIONS:
        return {
            "allowed": True,
            "risk_level": "medium",
            "reason": MEDIUM_RISK_ACTIONS[action],
        }

    if action in LOW_RISK_ACTIONS:
        return {
            "allowed": True,
            "risk_level": "low",
            "reason": LOW_RISK_ACTIONS[action],
        }

    return {
        "allowed": False,
        "risk_level": "unknown",
        "reason": "The action is unknown and cannot be executed safely.",
    }
