#from django.shortcuts import render

#from django.http import HttpResponse, HttpResponseRedirect
from django.http import HttpResponse, HttpResponseRedirect

#from django.template import loader

from django.http import Http404
from django.shortcuts import get_object_or_404, render

from django.urls import reverse

from django.views import generic


from .models import Choice, Question

from django.utils import timezone

#def index(request):
#    return HttpResponse("Hola, mundo. You're at the polls index.")

#def detail(request, question_id):
#    return HttpResponse("Estás viendo la pregunta %s." % question_id)

#def results(request, question_id):
#    response = "Estás viendo los resultados de la  pregunta %s."
#    return HttpResponse(response % question_id)



class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    #def get_queryset(self):
    #    return Question.objects.order_by('-pub_date')[:5]

    def get_queryset(self):
         return Question.objects.filter(
            pub_date__lte=timezone.now()
        ).order_by('-pub_date')[:5]

class DetailView(generic.DetailView):

    model = Question
    template_name = 'polls/detail.html'
    def get_queryset(self):
        return Question.objects.filter(pub_date__lte=timezone.now())


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "No has seleccionado una alternativa",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))






#def results(request, question_id):
#    question = get_object_or_404(Question, pk=question_id)
#    return render(request, 'polls/results.html', {'question': question})

#def vote(request, question_id):
 #   return HttpResponse("Estás votando sobre la pregunta %s." % question_id)

#def index(request):
#    latest_question_list = Question.objects.order_by('-pub_date')[:5]
#    template = loader.get_template('polls/index.html')
#    context = {
#        'latest_question_list': latest_question_list,
#    }
#    return HttpResponse(template.render(context, request))


#def index(request):
#    latest_question_list = Question.objects.order_by('-pub_date')[:5]
#    context = {'latest_question_list': latest_question_list}
#    return render(request, 'polls/index.html', context)

#def detail(request, question_id):
#    question = get_object_or_404(Question, pk=question_id)
#    return render(request, 'polls/detail.html', {'question': question})