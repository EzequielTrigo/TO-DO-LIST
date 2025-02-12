from polls.models import Question, Choice
from django.template import loader
from django.shortcuts import get_object_or_404, render
from django.db.models import F
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from .models import Choice, Question

#def index(request):
#    latest_question_list = Question.objects.order_by("-pub_date")[:5]
#    output = ", ".join([q.question_text + " (id=" + str(q.id) + ")" for q in latest_question_list])
#    return HttpResponse(output)

#def index(request):
#    latest_question_list = Question.objects.order_by("-pub_date")[:5]
#    template = loader.get_template("polls/index.html")
#    context = {
#        "latest_question_list": latest_question_list,
#    }
#    return HttpResponse(template.render(context, request))

#def index(request):
#    latest_question_list = Question.objects.order_by("-pub_date")[:5]
#    context = {"latest_question_list": latest_question_list}
#    return render(request, "polls/index.html", context)

class IndexView(generic.ListView):
    template_name = "polls/index.html"
    context_object_name = "latest_question_list"

    def get_queryset(self):
        """Return the last five published questions."""
        latest_question_list = Question.objects.filter(pub_date__lte=timezone.now()).order_by("-pub_date")[:5]
        return latest_question_list
    
    def get_context_data(self, **kwargs):
        # Obtén el contexto predeterminado de la clase padre
        context = super().get_context_data(**kwargs)
        # Agrega más datos al contexto
        context["hola"]="funciona bien?¿"
        context["total_questions"] = Question.objects.count()
        return context

#def detail(request, question_id):
#    question = get_object_or_404(Question, pk=question_id)
#    return render(request, "polls/detail.html", {"question": question})

class DetailView(generic.DetailView):
    model = Question
    template_name = "polls/detail.html"

    def get_queryset(self):
        """
        Excludes any questions that aren't published yet.
        """
        return Question.objects.filter(pub_date__lte=timezone.now())
#def results(request, question_id):
#    question = get_object_or_404(Question, pk=question_id)
#    return render(request, "polls/Results.html", {"question": question})

class ResultsView(generic.DetailView):
    model = Question
    template_name = "polls/results.html"

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(
            request,
            "polls/detail.html",
            {
                "question": question,
                "error_message": "You didn't select a choice.",
            },
        )
    else:
        selected_choice.votes = F("votes") + 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse("polls:results", args=(question.id,)))