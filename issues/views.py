from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Issue
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

class IssueListView(LoginRequiredMixin, ListView):
    model = Issue
    template_name = 'issues/list.html'
    context_object_name = 'issues'
    ordering = ['-created_at']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['todo_issues'] = Issue.objects.filter(status=Issue.Status.TODO).order_by('-created_at')
        context['inprogress_issues'] = Issue.objects.filter(status=Issue.Status.IN_PROGRESS).order_by('-created_at')
        context['done_issues'] = Issue.objects.filter(status=Issue.Status.DONE).order_by('-created_at')
        return context

class IssueDetailView(LoginRequiredMixin, DetailView):
    model = Issue
    template_name = 'issues/detail.html'

class IssueCreateView(LoginRequiredMixin, CreateView):
    model = Issue
    template_name = 'issues/new.html'
    fields = ['summary', 'description', 'status', 'priority', 'assignee']
    success_url = reverse_lazy('list')

    def form_valid(self, form):
        form.instance.reporter = self.request.user
        return super().form_valid(form)

class IssueUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Issue
    template_name = 'issues/edit.html'
    fields = ['summary', 'description', 'status', 'priority', 'assignee']
    success_url = reverse_lazy('list')

    def form_valid(self, form):
        form.instance.reporter = self.request.user
        return super().form_valid(form)

    def test_func(self):
        issue = self.get_object()
        return self.request.user == issue.reporter

class IssueDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Issue
    template_name = 'issues/delete.html'
    success_url = reverse_lazy('list')

    def test_func(self):
        issue = self.get_object()
        return self.request.user == issue.reporter
