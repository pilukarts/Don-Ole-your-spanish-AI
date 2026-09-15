from django.shortcuts import render
from django.views.decorators.http import require_http_methods

from .content import AUDIENCES, LESSON, LEVELS


def home(request):
    return render(request, "learning/home.html", {"levels": LEVELS, "audiences": AUDIENCES})


@require_http_methods(["GET", "POST"])
def lesson(request):
    level = request.GET.get("level", "A1").upper()
    audience = request.GET.get("audience", "jovenes")
    if level not in LEVELS:
        level = "A1"
    if audience not in AUDIENCES:
        audience = "jovenes"

    score = None
    if request.method == "POST":
        score = sum(
            request.POST.get(f"question_{index}") == str(question["answer"])
            for index, question in enumerate(LESSON["questions"])
        )

    return render(request, "learning/lesson.html", {
        "lesson": LESSON,
        "level": level,
        "audience": AUDIENCES[audience],
        "audience_key": audience,
        "score": score,
        "total": len(LESSON["questions"]),
    })

