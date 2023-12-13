from typing import Any
from django.views import generic
from django.urls import reverse_lazy
from .models import NewsStory
from .forms import StoryForm
from users.models import CustomUser
from django.shortcuts import get_object_or_404
# from django.shortcuts import render, redirect
# from news.forms import ContactForm
# from django.http import HttpResponse

class IndexView(generic.ListView):
    template_name = 'news/index.html'
    context_object_name = "all_stories"

    def get_queryset(self):
        '''Return all news stories.'''
        return NewsStory.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['latest_stories'] = NewsStory.objects.all()[:4]
        return context

class StoryView(generic.DetailView):
    model = NewsStory
    template_name = 'news/story.html'
    context_object_name = 'story'

class AddStoryView(generic.CreateView):
    form_class = StoryForm
    context_object_name = 'storyform'
    template_name = 'news/createStory.html'
    success_url = reverse_lazy('news:index')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
class AuthorView(generic.DetailView):
    model = CustomUser
    template_name = 'news/author.html'
    context_object_name = 'author'

    def get_object(self, *args, **kwargs):
        return get_object_or_404 (CustomUser, username=self.kwargs['username'])
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['latest_stories'] = NewsStory.objects.filter(author_id=self.object.id)
        return context

# def contact(request):
#     if request.method == 'POST':
#         form = ContactForm(request.POST)
#         if form.is_valid():
#             # Process the form data
#             pass
#             return redirect('success')
#     else:
#         form = ContactForm()
#     return render(request, 'contact.html', {'form': form})


# def success(request):
#    return HttpResponse('Success!')