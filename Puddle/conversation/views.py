from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from .models import Conversation, ConversationMessage
from Item.models import Item
from .forms import ConversationMessageForm

@login_required
def new_conversation(request, item_pk):  # sourcery skip: remove-redundant-if
    item = get_object_or_404(Item, pk=item_pk)

    if item.created_by == request.user:
        return redirect('dashboard:index')

    conversations = Conversation.objects.filter(item=item).filter(members__in=[request.user.id])

    if conversations:
        pass # redirect to the conversatin page
    
    if request.method == 'POST':
        form = ConversationMessageForm(request.POST)

        if form.is_valid():
            return _extracted_from_new_conversation_13(item, request, form, item_pk)
    else:
        form = ConversationMessageForm()

    return render(request, 'conversation/new.html', {
        'form':form
    })


# TODO Rename this here and in `new_conversation`
# Helper function for new_conversation
def _extracted_from_new_conversation_13(item, request, form, item_pk):
    conversation = Conversation.objects.create(item=item)
    conversation.members.add(request.user)
    conversation.members.add(item.created_by)
    conversation.save()

    conversation_message = form.save(commit=False)
    conversation_message.conversation = conversation
    conversation_message.created_by = request.user
    conversation_message.save()

    return redirect('item:detail', pk=item_pk)



@login_required
def inbox(request):
    conversations = Conversation.objects.filter(members__in=[request.user.id])

    return render(request, 'conversation/inbox.html', {'conversations':conversations})


@login_required
def detail(request, pk):
    conversation = Conversation.objects.filter(members__in=[request.user.id]).get(pk=pk)

    return render(request, 'conversation/detail.html', {'conversation':conversation})