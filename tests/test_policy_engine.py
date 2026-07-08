from src.policy_engine import evaluate_action


def test_high_risk_actions_are_blocked():
    high_risk_actions = [
        "unlock_front_door",
        "turn_off_alarm",
        "disable_security_camera",
    ]

    for action in high_risk_actions:
        result = evaluate_action(action)
        assert result["allowed"] is False
        assert result["risk_level"] == "high"


def test_low_risk_actions_are_allowed():
    low_risk_actions = [
        "turn_on_light",
        "read_camera_status",
    ]

    for action in low_risk_actions:
        result = evaluate_action(action)
        assert result["allowed"] is True
        assert result["risk_level"] == "low"


def test_medium_risk_actions_are_allowed():
    result = evaluate_action("set_thermostat")

    assert result["allowed"] is True
    assert result["risk_level"] == "medium"


def test_unknown_action_is_blocked():
    result = evaluate_action("unknown")

    assert result["allowed"] is False
    assert result["risk_level"] == "unknown"
