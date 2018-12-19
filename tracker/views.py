from django.shortcuts import render, HttpResponse, redirect
from django.shortcuts import get_object_or_404
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from .forms import SignUpForm
from django.contrib.auth.models import Group

#from .models import Recipe, Step, Ingredient, Chef, User, Like
from .models import Clinic, Dentist, Patient, Announcement, Stat
from .forms import newRecipeForm
from django.conf import settings

from . import MAX_STEPS, MAX_INGREDIENTS

# Create your views here.

@login_required
def index(request):
    account_type = request.user.groups.all()[0].name

    if account_type == "Patient":

        dentist = Patient.objects.get(user=request.user).dentist

        announcements = Announcement.objects.filter(dentist=dentist).order_by('-date_sent')[:10]

        return render(request, 'tracker/patient_dashboard.html', {'dentist' : dentist, 'announcements' : announcements})
    else:
        return render(request, 'tracker/dentist_dashboard.html', {})

def privacy(request):
    return HttpResponse("Privacy page")


def register(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            clinic = form.fields['clinic']
            if form.fields['account_type'] == "patient":
                Patient.objects.create(user=user, clinic=clinic)
            else:
                Dentist.objects.create(user=user, clinic=clinic)
            g = Group.objects.get(name=form.fields['account_type'])
            g.user_set.add(user)
            login(request, user)
            return redirect('index')
    else:
        form = SignUpForm()
        form.fields['account_type'].initial = 'patient'
    return render(request, 'registration/register.html', {'form': form})

def logstats(request):
    return render(request, 'tracker/patient_log_stats.html', {})

def trackstats(request):

    patient = Patient.objects.get(user=request.user)

    stats = Stat.objects.filter(patient=patient).order_by('-date_logged')[:7]

    return render(request, 'tracker/patient_track_stats.html', {'stats' : stats})

def information(request):
    return render(request, 'tracker/patient_information.html', {})

def stat(request, stat_id):

    stat = Stat.objects.get(id=stat_id)

    return render(request, 'tracker/patient_stat.html', {'stat' : stat})


def contact(request):

    dentist = Patient.objects.get(user=request.user).dentist

    clinic = Patient.objects.get(user=request.user).clinic

    return render(request, 'tracker/patient_contact.html', {'dentist' : dentist, 'clinic' : clinic})

def discussion(request):
    return render(request, 'tracker/patient_discussion.html', {})

def health(request):
    return render(request, 'tracker/patient_health.html', {})

def pubannouncement(request):
    return HttpResponse("Publish Announcement")

def requests(request):
    return HttpResponse("Requests")

def quizzes(request):
    return HttpResponse("Quizzes")

@login_required
def newrecipe(request):
    # TODO:: Authentication required
    if request.method == "POST":
        form = newRecipeForm(request.POST, request.FILES)
        if form.is_valid():
            recipe_title = form.cleaned_data.get('recipe_title')
            recipe_category = form.cleaned_data.get('recipe_category')
            recipe_diet_req = form.cleaned_data.get('recipe_diet_req')
            recipe_servings = form.cleaned_data.get('recipe_servings')
            recipe_duration = form.cleaned_data.get('recipe_duration')
            recipe_image = form.cleaned_data.get('recipe_image')

            steps = {}

            ingredient = {}
            iquantity = {}

            for i in range(MAX_STEPS):
                steps['step_'+str(i)] = form.cleaned_data.get('step_'+str(i))

            for i in range(MAX_INGREDIENTS):
                ingredient['ingredients_'+str(i)] = form.cleaned_data.get('ingredient_'+str(i))
                iquantity['iquantity_'+str(i)] = form.cleaned_data.get('iquantity_'+str(i))

            Recipe.objects.create(recipe_text=recipe_title, recipe_category=recipe_category, recipe_diet_req=recipe_diet_req, servings=recipe_servings, duration=recipe_duration, image_path=recipe_image,  chef=request.user.chef)
            this_recipes = Recipe.objects.get(recipe_text=recipe_title)
            for i in range(MAX_STEPS):
                if steps['step_'+str(i)] is not None:
                    Step.objects.create(step_number=(i+1), contents=steps['step_'+str(i)], recipe=this_recipes)
            for i in range(MAX_INGREDIENTS):
                if ingredient['ingredients_'+str(i)] is not None:
                    Ingredient.objects.create(quantity = iquantity['iquantity_'+str(i)], ingredient_name=ingredient['ingredients_'+str(i)], recipe=this_recipes)

            # Save data in DB
            return redirect('index')
    else:
        form = newRecipeForm()
    return render(request, 'tracker/new_recipes.html', {'form': form})

@login_required
def submitrecipe(request):
    return HttpResponse("Submit Recipe View")
#    try:
        # Get form information
        # equest.POST['serves']
#    except (KeyError, Choice.DoesNotExist):
        # Display errors (form not filled properly)
#    else:
        # Put form data in the database

        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        # Redirect to recipe pagef
        # return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))

def recipe(request, recipe_id):
    try:
        recipe = Recipe.objects.get(pk=recipe_id)
        chef = Chef.objects.get(user=recipe.chef.user)
        steps_list = Step.objects.filter(recipe_id=recipe_id)
        ingredients_list = Ingredient.objects.filter(recipe_id=recipe_id)

        context = {
            'recipe' : recipe,
            'chef' : chef,
            'steps_list': steps_list,
            'ingredients_list': ingredients_list,
        }

    except Recipe.DoesNotExist:
        raise Http404("Recipe or user does not exist")
    return render(request, 'tracker/recipe_details.html', context)


def userpage(request, username):
    try:
        chef = User.objects.get(username=username).chef

        user_recipes = Recipe.objects.filter(chef=chef).order_by('-like_count')
        liked_recipes = Like.objects.filter(chef=chef)

        context = {
            'chef' : chef,
            'user_recipes' : user_recipes,
            'liked_recipes' : liked_recipes,
        }

    except Recipe.DoesNotExist:
        raise Http404("User does not exist")
    return render(request, 'tracker/display_user.html', context)
