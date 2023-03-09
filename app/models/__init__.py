import datetime


class PersonalExperience:
    def __init__(self, current_work_here: bool, start: datetime.date, company_name: str, description: str, end: datetime.date | None) -> None:
        self.current_work_here = current_work_here
        self.start = start
        self.company_name = company_name
        self.description = description
        self.end = end


class PersonalInformation:
    def __init__(self, your_name: str, your_skills: list[str]):
        self.your_name = your_name
        self.your_skills = your_skills


class PromptRequest:
    def __init__(self, personal_information: PersonalInformation):
        self.personal_information = personal_information