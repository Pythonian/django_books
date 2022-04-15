from django.shortcuts import get_object_or_404, render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import Story, Chapter
from .forms import (
    StoryForm, ChapterForm, StoryDeleteForm, ChapterDeleteForm)


def create_story(request):
    if request.method == 'POST':
        form = StoryForm(request.POST, request.FILES)
        if form.is_valid():
            story = form.save(commit=False)
            story.author = request.user
            story.save()
            messages.success(
                request, 'Story created. Now add some chapters to your story below.')
            return redirect('story:change_story', story.pk)
    else:
        form = StoryForm()

    return render(
        request, 'story/create.html',
        {'form': form, 'create': True})


def change_story(request, pk):
    story = get_object_or_404(Story, pk=pk)
    if request.method == 'POST':
        form = StoryForm(
            request.POST, request.FILES,
            instance=story)
        if form.is_valid():
            form.save()
            messages.success(
                request, 'Story successfully updated.')
            return redirect('story:change_story', story.pk)
    else:
        form = StoryForm(instance=story)

    return render(
        request, 'story/create.html',
        {'form': form, 'story': story})


def add_chapter(request, pk):
    story = get_object_or_404(
        Story, pk=pk, author=request.user)
    if request.method == 'POST':
        form = ChapterForm(request.POST)
        if form.is_valid():
            chapter = form.save(commit=False)
            chapter.story = story
            chapter.save()
            messages.success(
                request,
                f'You have successfully added chapter {chapter.order}.')
            return redirect('story:change_story', story.pk)
    else:
        form = ChapterForm()
    return render(
        request, 'story/chapter_form.html',
        {'story': story, 'form': form, 'create': True})


def update_chapter(request, story_pk, chapter_pk):
    story = get_object_or_404(
        Story, pk=story_pk, author=request.user)
    chapter = get_object_or_404(Chapter, pk=chapter_pk, story=story)
    if request.method == 'POST':
        form = ChapterForm(request.POST, instance=chapter)
        if form.is_valid():
            form.save()
            messages.success(
                request, f'You"ve successfully updated chapter {chapter.pk}.')
            return redirect('story:change_story', story.pk)
    else:
        form = ChapterForm(instance=chapter)
    return render(
        request, 'story/chapter_form.html',
        {'story': story, 'form': form, 'chapter': chapter})


@login_required
def delete_chapter(request, story_pk, chapter_pk):
    story = get_object_or_404(
        Story, pk=story_pk, author=request.user)
    chapter = get_object_or_404(Chapter, pk=chapter_pk, story=story)
    if request.method == 'POST':
        form = ChapterDeleteForm(request.POST, instance=chapter)
        if form.is_valid():
            chapter.delete()
            messages.success(
                request, "Chapter successfully deleted.")
            return redirect('story:change_story', story.pk)
    else:
        form = ChapterDeleteForm(instance=chapter)
    return render(
        request, 'story/chapter_delete.html',
        {'story': story, 'form': form, 'chapter': chapter})


def story_detail(request, slug):
    story = get_object_or_404(Story, slug=slug)
    session_key = 'viewed_story_{}'.format(story.pk)
    if not request.session.get(session_key, False):
        story.impressions += 1
        story.save()
        request.session[session_key] = True

    return render(
        request, 'story/detail.html',
        {'story': story})


@login_required
def story_delete(request, pk):
    story = get_object_or_404(Story, pk=pk, author=request.user)
    if request.method == 'POST':
        form = StoryDeleteForm(request.POST, instance=story)
        if form.is_valid():
            story.delete()
            messages.success(
                request, "Story successfully deleted.")
            return redirect('stories')
    else:
        form = StoryDeleteForm(instance=story)
    return render(
        request, 'story/delete.html',
        {'story': story, 'form': form})
