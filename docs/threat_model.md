# Threat Model

## 1. System Overview

The Smart Home AI Assistant Prompt Injection Simulator is a local Python and Streamlit project. It simulates an AI assistant that interprets natural language commands and controls fake smart-home devices.

The system has two execution modes:

- Unsafe Mode directly executes the interpreted action.
- Safe Mode sends the interpreted action to a policy engine before execution.

The simulator does not connect to real smart-home devices, locks, cameras, APIs, networks, or external systems.

## 2. Assets

- Smart-home device states
- Door lock status
- Alarm status
- Camera status
- User commands
- Assistant decision process

## 3. Threat Actors

- Malicious user
- Guest user
- Compromised external data source
- Attacker trying to manipulate the AI assistant

## 4. Attack Scenarios

- Direct prompt injection through user input
- Attempt to unlock the front door
- Attempt to disable the alarm
- Attempt to disable the security camera
- Attempt to bypass security rules using fake emergency/admin instructions

## 5. Risks

- The assistant may treat malicious text as a valid command.
- High-risk actions may be executed without validation in Unsafe Mode.
- Fake emergency or admin language may pressure the assistant into ignoring normal safety rules.
- A system connected to real devices could create physical security risks if it lacked a policy layer.

## 6. Mitigations

- Security policy layer
- Blocking high-risk actions
- Allowing only known commands
- Separating AI interpretation from final command execution
- Showing clear logs and decisions
- Human confirmation as a future improvement

## 7. Limitations

- This project uses simple keyword matching instead of a real AI model.
- The policy engine is intentionally basic for beginner readability.
- Device state is stored only in local Streamlit session memory.
- There is no authentication, user role system, or human approval workflow.
- The simulator is educational and should not be used as production IoT security software.
