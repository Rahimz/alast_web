# briefs app

Design briefs are the brief of a project.
Design briefs needs  a form to be filled fo get a brief of the project.
Each client may fill some questionnaires.

## Models

```python
class Questionnaire(TimeStampedModel):
    client = models.ForeignKey(Client)

class Question(TimeStampedModel):
    description = models.TextField()
    question_type = models.CharField()

class QuestionResponse(TimeStampedModel):
    question = Question
    response_type
    
    response = models.TextField()
    r_response_1 = mdoels.CharField()
    r_response_2 = mdoels.CharField()
    r_response_3 = mdoels.CharField()
    r_response_4 = mdoels.CharField()
    r_response_5 = mdoels.CharField()
    r_response_6 = mdoels.CharField()
    r_response_7 = mdoels.CharField()
```
