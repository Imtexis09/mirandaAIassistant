import pytest
from automation.system import DesktopAutomation, SecurityManager

def test_security_manager_allows_notepad():
    sm = SecurityManager()
    assert sm.is_action_allowed("notepad") == True

def test_security_manager_blocks_unknown():
    sm = SecurityManager()
    assert sm.is_action_allowed("format_c") == False

def test_automation_raises_permission_error():
    sm = SecurityManager()
    auto = DesktopAutomation(sm)
    with pytest.raises(PermissionError):
        auto.execute_command("open_app", "powershell")