import subprocess
import os
from core.interfaces import IAutomationEngine

class SecurityManager:
    def __init__(self):
        # En el futuro, esto se carga de SQLite
        self.allowed_apps = ["notepad", "calc", "brave", "code"]
        
    def is_action_allowed(self, action: str) -> bool:
        return action.lower() in self.allowed_apps

class DesktopAutomation(IAutomationEngine):
    def __init__(self, security_manager: SecurityManager):
        self.security = security_manager

    def execute_command(self, action: str, target: str) -> bool:
        if action == "open_app":
            if self.security.is_action_allowed(target):
                try:
                    # Implementación cross-platform básica
                    if os.name == 'nt': # Windows
                        subprocess.Popen(target)
                    else: # Linux/Mac (requiere adaptar el nombre del binario)
                        subprocess.Popen(target)
                    return True
                except Exception as e:
                    print(f"Error abriendo aplicación: {e}")
                    return False
            else:
                raise PermissionError(f"Acción no autorizada: abrir {target}")
        return False