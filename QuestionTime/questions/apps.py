from django.apps import AppConfig


class QuestionsConfig(AppConfig):
    name = 'questions'

    def ready(self) -> None:
        import questions.signals
