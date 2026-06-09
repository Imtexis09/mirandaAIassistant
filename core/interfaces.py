from abc import ABC, abstractmethod

class ILLMProvider(ABC):
    @abstractmethod
    async def generate_response(self, prompt: str, context: list) -> str:
        pass

class IVoiceRecognizer(ABC):
    @abstractmethod
    def listen_for_wakeword(self, wakeword: str) -> bool:
        pass

    @abstractmethod
    def record_and_transcribe(self) -> str:
        pass

class IAutomationEngine(ABC):
    @abstractmethod
    def execute_command(self, action: str, target: str) -> bool:
        pass