from django.shortcuts import render
from django.shortcuts import redirect

from .forms import SevenForm

UP_TO = 7


def _get_pairs(number_list):
    # Filter numbers
    numbers = [int(number) for number in number_list.split(',')]

    numbers = sorted(list(set(numbers)))

    head_pointer = 0
    tail_pointer = len(numbers) - 1

    # Get unique pairs
    pairs = []
    while head_pointer < tail_pointer:
        head = numbers[head_pointer]
        tail = numbers[tail_pointer]
        pair_sum = head + tail

        if pair_sum == UP_TO:
            pairs.append((head, tail))
            head_pointer = head_pointer + 1
            tail_pointer = tail_pointer - 1

        elif pair_sum < UP_TO:
            head_pointer = head_pointer + 1

        elif pair_sum > UP_TO:
            tail_pointer = tail_pointer - 1

    return pairs


def index(request):
    return redirect('seven')


def seven(request):
    if request.method == 'POST':
        form = SevenForm(request.POST)
        if form.is_valid():
            return render(request, 'seven/result.html', {'pairs': _get_pairs(form.cleaned_data['numbers'])})
    else:
        form = SevenForm()

    return render(request, 'seven/index.html', {'form': form})