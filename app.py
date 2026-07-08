import streamlit as st

from src.assistant import interpret_command
from src.devices import execute_action, get_default_device_states
from src.policy_engine import evaluate_action
from src.scenarios import NORMAL_COMMANDS, PROMPT_INJECTION_ATTACKS


st.set_page_config(
    page_title="Smart Home AI Assistant Prompt Injection Simulator",
    layout="centered",
)


def initialize_session_state():
    """Create fake device state once per Streamlit session."""
    if "devices" not in st.session_state:
        st.session_state.devices = get_default_device_states()

    if "last_result" not in st.session_state:
        st.session_state.last_result = None


def reset_devices():
    st.session_state.devices = get_default_device_states()
    st.session_state.last_result = None


def run_command(user_input, mode):
    """Interpret a command and optionally enforce the security policy."""
    interpretation = interpret_command(user_input)
    action = interpretation["action"]
    parameters = interpretation["parameters"]
    policy_result = evaluate_action(action)

    if mode == "Unsafe Mode":
        if action == "unknown":
            final_result = "No action was executed because the command was not understood."
            executed = False
        else:
            final_result = execute_action(st.session_state.devices, action, parameters)
            executed = True

        decision = {
            "allowed": executed,
            "risk_level": policy_result["risk_level"],
            "reason": "Unsafe Mode does not enforce the policy engine before execution.",
        }
    else:
        decision = policy_result
        if decision["allowed"]:
            final_result = execute_action(st.session_state.devices, action, parameters)
        else:
            final_result = "Action blocked. Device state was not changed."

    st.session_state.last_result = {
        "mode": mode,
        "user_input": user_input,
        "interpretation": interpretation,
        "policy_result": decision,
        "final_result": final_result,
    }


def display_device_states():
    states = st.session_state.devices

    st.subheader("Current Fake Smart-Home Device States")
    st.table(
        {
            "Device": [
                "Living room light",
                "Front door",
                "Thermostat",
                "Security camera",
                "Alarm system",
            ],
            "State": [
                states["living_room_light"],
                states["front_door"],
                f'{states["thermostat_temperature"]} degrees',
                states["security_camera"],
                states["alarm_system"],
            ],
        }
    )


def display_result():
    result = st.session_state.last_result
    if result is None:
        return

    interpretation = result["interpretation"]
    policy_result = result["policy_result"]

    st.subheader("Command Result")
    st.write("**Original user input:**", result["user_input"])
    st.write("**Assistant interpreted action:**", interpretation["action"])
    st.write("**Assistant explanation:**", interpretation["explanation"])
    st.write("**Risk level:**", policy_result["risk_level"])
    st.write("**Policy engine decision:**", "Allowed" if policy_result["allowed"] else "Blocked")
    st.write("**Reason for decision:**", policy_result["reason"])
    st.write("**Final result:**", result["final_result"])

    if result["mode"] == "Unsafe Mode":
        st.warning(
            "Unsafe Mode is dangerous: the assistant executes the interpreted action "
            "without security validation. This can allow prompt injection text to trigger "
            "high-risk smart-home actions."
        )


initialize_session_state()

st.title("Smart Home AI Assistant Prompt Injection Simulator")

st.write(
    "This safe educational simulator shows how prompt injection can influence an AI "
    "assistant that controls fake smart-home devices."
)

st.info(
    "Prompt injection happens when a user or external content tries to override an "
    "assistant's rules with instructions such as 'ignore previous rules' or 'admin mode'. "
    "For IoT assistants, this matters because a bad instruction could try to unlock a "
    "door, disable an alarm, or turn off a security camera."
)

mode = st.radio("Choose a mode", ["Unsafe Mode", "Safe Mode"], horizontal=True)

all_examples = [""] + NORMAL_COMMANDS + PROMPT_INJECTION_ATTACKS
example_prompt = st.selectbox("Example prompts", all_examples)

user_command = st.text_input(
    "Enter a command for the assistant",
    value=example_prompt,
    placeholder="Example: Turn on the living room light.",
)

col1, col2 = st.columns(2)

with col1:
    run_clicked = st.button("Run Command", type="primary")

with col2:
    reset_clicked = st.button("Reset Fake Devices")

if reset_clicked:
    reset_devices()
    st.success("Fake device states were reset.")

if run_clicked:
    if user_command.strip():
        run_command(user_command.strip(), mode)
    else:
        st.error("Please enter or select a command first.")

display_result()
display_device_states()

st.caption(
    "Safety note: this project never connects to real smart-home devices, locks, "
    "cameras, APIs, networks, or external systems. Everything is simulated locally."
)
