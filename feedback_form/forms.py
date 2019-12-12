from django import forms

'''from feedback_form.models import Question_txt, MultipleChoice, Evaluation, EvaluationAnswer
from django.forms.models import inlineformset_factory'''

'''class SurveyForm(forms.ModelForm):
    """ Render and process a form based on the Page model. """
    class Meta:
        model = Question_txt
        fields = [
            'question_text'
        ]

AnswerFormSet = inlineformset_factory(Evaluation, 
        EvaluationAnswer, exclude=('question',), 
        extra=0, can_delete=False)'''
