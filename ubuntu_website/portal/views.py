from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from .models import ServiceRequest, Opportunity, Application
from .forms import RegisterForm, ServiceRequestForm, OpportunityForm, ApplicationForm

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('dashboard')
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})

@login_required
def dashboard(request):
    user = request.user
    if user.role == 'client':
        requests = ServiceRequest.objects.filter(client=user)
        opps = Opportunity.objects.all()
        return render(request, 'dashboard_client.html', {'requests': requests, 'opps': opps, 'user': user})
    elif user.role == 'agent':
        requests = ServiceRequest.objects.filter(agent=user) | ServiceRequest.objects.filter(agent__isnull=True)
        return render(request, 'dashboard_agent.html', {'requests': requests, 'user': user})
    else:
        requests = ServiceRequest.objects.all()
        opps = Opportunity.objects.all()
        apps = Application.objects.all()
        return render(request, 'dashboard_admin.html', {'requests': requests, 'opps': opps, 'apps': apps, 'user': user})

@login_required
def create_request(request):
    if request.method == 'POST':
        form = ServiceRequestForm(request.POST)
        if form.is_valid():
            r = form.save(commit=False)
            r.client = request.user
            r.save()
            return redirect('dashboard')
    else:
        form = ServiceRequestForm()
    return render(request, 'create_request.html', {'form': form})

@login_required
def update_request(request, pk):
    req = get_object_or_404(ServiceRequest, pk=pk)
    if request.method == 'POST':
        status = request.POST.get('status')
        req.status = status
        req.agent = request.user
        req.save()
        return redirect('dashboard')
    return render(request, 'update_request.html', {'req': req})

@login_required
def create_opportunity(request):
    if request.method == 'POST':
        form = OpportunityForm(request.POST)
        if form.is_valid():
            o = form.save(commit=False)
            o.posted_by = request.user
            o.save()
            return redirect('dashboard')
    else:
        form = OpportunityForm()
    return render(request, 'create_opportunity.html', {'form': form})

@login_required
def apply_opportunity(request, pk):
    opp = get_object_or_404(Opportunity, pk=pk)
    if request.method == 'POST':
        form = ApplicationForm(request.POST)
        if form.is_valid():
            a = form.save(commit=False)
            a.opportunity = opp
            a.applicant = request.user
            a.save()
            return redirect('dashboard')
    else:
        form = ApplicationForm()
    return render(request, 'apply.html', {'form': form, 'opp': opp})

@login_required
def review_application(request, pk):
    app = get_object_or_404(Application, pk=pk)
    if request.method == 'POST':
        app.status = request.POST.get('status')
        app.save()
        return redirect('dashboard')
    return render(request, 'review.html', {'app': app})

# Create your views here.
