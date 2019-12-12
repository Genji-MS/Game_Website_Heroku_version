from django.shortcuts import render_to_response, get_object_or_404, render
from django.http import HttpResponse
from django.views.generic import CreateView
'''
from feedback_form.forms import SurveyForm, AnswerFormSet
from feedback_form.models import EvaluationAnswer, Evaluation'''
'''
# Create your views here.
class CreateSurveyForm(CreateView):
    def get(self, request, *args, **kwargs):
        context = {'form': SurveyForm()}
        template_name = 'survey'
        return render(request, 'survey.html', context)

    def post(self, request, *args, **kwargs):
        form = SurveyForm(request.POST or None)
        if form.is_valid():
            form.save()

        context = {
            'form': form
        }
        return render(request, 'survery.html', context)

def prepare_blank_answers(evaluation):
    for question in evaluation.scheme.evaluationquestion_set.all():
        answer = EvaluationAnswer(evaluation=evaluation,
                                         question=question)
        answer.save()

def answer_form(request, id):
    evaluation = get_object_or_404(Evaluation, id=id)
    if len(evaluation.evaluationanswer_set.all()) == 0:
        prepare_blank_answers(evaluation)
    if request.method == 'POST':
        formset = AnswerFormSet(request.POST, instance=evaluation)
        if formset.is_valid():
            formset.save()
            return HttpResponse('Thank you!')
    else:
        formset = AnswerFormSet(instance=evaluation)
    return render_to_response('answer_form.html',
            {'formset':formset, 'evaluation':evaluation})'''