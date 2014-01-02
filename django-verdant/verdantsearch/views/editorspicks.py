from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from verdantsearch import models, forms


@login_required
def index(request):
    # Select only queries with editors picks
    queries = models.Query.objects.filter(editors_picks__isnull=False).distinct()
    return render(request, 'verdantsearch/editorspicks/index.html', {
        'queries': queries,
    })


@login_required
def add(request):
    if request.POST:
        # Get queries
        query_form = forms.QueryForm(request.POST)
        if query_form.is_valid():
            query = models.Query.get(query_form['query_string'].value())

            # Save editors picks
            editors_pick_formset = forms.EditorsPickFormSet(request.POST, instance=query)

            if editors_pick_formset.is_valid():
                editors_pick_formset.save()

                return redirect('verdantsearch_editorspicks_index')
        else:
            editors_pick_formset = forms.EditorsPickFormSet()
    else:
        query_form = forms.QueryForm()
        editors_pick_formset = forms.EditorsPickFormSet()

    return render(request, 'verdantsearch/editorspicks/add.html', {
        'query_form': query_form,
        'editors_pick_formset': editors_pick_formset,
    })


@login_required
def edit(request, query_id):
    query = get_object_or_404(models.Query, id=query_id)

    if request.POST:
        editors_pick_formset = forms.EditorsPickFormSet(request.POST, instance=query)

        if editors_pick_formset.is_valid():
            editors_pick_formset.save()

            return redirect('verdantsearch_editorspicks_index')
    else:
        editors_pick_formset = forms.EditorsPickFormSet(instance=query)

    return render(request, 'verdantsearch/editorspicks/edit.html', {
        'editors_pick_formset': editors_pick_formset,
        'query': query,
    })


@login_required
def delete(request, query_id):
    query = get_object_or_404(models.Query, id=query_id)

    if request.POST:
        query.editors_picks.all().delete()
        return redirect('verdantsearch_editorspicks_index')

    return render(request, 'verdantsearch/editorspicks/confirm_delete.html', {
        'query': query,
    })