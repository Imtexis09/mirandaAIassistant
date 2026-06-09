import asyncio
from config.settings import load_config
from ai.llm_manager import OpenAIProvider, OllamaProvider
from automation.system import DesktopAutomation, SecurityManager

class MirandaCore:
    def __init__(self, llm_provider, automation_engine):
        # Inyección de dependencias
        self.llm = llm_provider
        self.automation = automation_engine
        self.context = [] # Memoria a corto plazo en RAM (MVP)

    async def process_user_input(self, user_text: str) -> str:
        # 1. Parseo básico de intención (En producción, usar LLM para clasificación)
        if user_text.lower().startswith("abre "):
            app_name = user_text.lower().replace("abre ", "").strip()
            try:
                success = self.automation.execute_command("open_app", app_name)
                return f"Abriendo {app_name}..." if success else f"No pude abrir {app_name}."
            except PermissionError as e:
                return str(e)

        # 2. Conversación normal
        response = await self.llm.generate_response(user_text, self.context)
        
        # 3. Actualizar memoria corto plazo
        self.context.append({"role": "user", "content": user_text})
        self.context.append({"role": "assistant", "content": response})
        
        # Mantener solo los últimos 10 mensajes
        if len(self.context) > 10:
            self.context = self.context[-10:]
            
        return response

# --- Configuración e Inicialización ---
async def main():
    config = load_config()
    
    # Switch entre Local y Cloud sin alterar MirandaCore
    if config.mode == "LOCAL":
        llm = OllamaProvider(model_name="llama3")
    else:
        llm = OpenAIProvider(api_key=config.openai_api_key)
        
    security = SecurityManager()
    automation = DesktopAutomation(security)
    
    miranda = MirandaCore(llm, automation)
    
    print("Miranda Beta Inicializada. Escribe 'salir' para terminar.")
    while True:
        user_input = input("Tú: ")
        if user_input.lower() == 'salir':
            break
        response = await miranda.process_user_input(user_input)
        print(f"Miranda: {response}")

if __name__ == "__main__":
    asyncio.run(main())