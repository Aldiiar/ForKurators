from django.contrib.auth.decorators import login_required
from users.models import Kurator
from users.forms import LoginForm
from groups.forms import AddStudentForm, EditStudentForm
from groups.models import Group, Student
from django.shortcuts import render, redirect, get_object_or_404

def main_page_view(request):
    if request.method == "GET":
        if request.user.is_anonymous:
            context = {
                'form': LoginForm
            }

            return render(request, 'registration/login.html', context=context)

        else:
            return render(request, 'layouts/index.html')


@login_required
def group_view(request):
    try:
        kurator = Kurator.objects.get(user=request.user)
        groups = kurator.groups.all()
    except Kurator.DoesNotExist:
        return redirect('error_page')

    context = {
        'groups': groups
    }
    return render(request, 'groups/groups.html', context=context)


@login_required
def group_detail_view(request, pk):

    group = get_object_or_404(Group, pk=pk)
    students = group.student_set.all()

    if request.user.is_anonymous:
        context = {
            'form': LoginForm
        }
        return render(request, 'registration/login.html', context=context)
    else:
        context = {
            'group': group,
            'students': students
        }
        return render(request, 'groups/groups_detail.html', context=context)

@login_required
def add_student(request, pk):
    group = get_object_or_404(Group, pk=pk)
    if request.method == 'POST':
        form = AddStudentForm(request.POST, request.FILES)

        if form.is_valid():
            student = Student.objects.create(
                photo=request.FILES.get('photo'),
                name=form.cleaned_data['name'],
                surname=form.cleaned_data['surname'],
                phone_number=form.cleaned_data['phone_number'],
                date_of_b=form.cleaned_data['date_of_b'],
                group=group
            )
            student.save()
            students = group.student_set.all()

            context = {
                'group': group,
                'students': students
            }

            return render(request, 'groups/groups_detail.html', context=context)
    else:
        form = AddStudentForm()

    return render(request, 'groups/add_student.html', {'form': form, 'group': group})


@login_required
def student_detail_view(request, pk):
    if request.method == "GET":
        if request.user.is_anonymous:
            context = {
                'form': LoginForm
            }

            return render(request, 'registration/login.html', context=context)

        else:
            student = get_object_or_404(Student, pk=pk)
            context = {
                'student': student
            }
            return render(request, 'groups/student.html', context=context)


@login_required
def edit_student(request, pk):
    student = get_object_or_404(Student, pk=pk)

    if request.method == 'POST':
        form = EditStudentForm(request.POST, request.FILES, instance=student)
        if form.is_valid():
            form.save()
            return redirect('student_detail', pk=student.pk)
    else:
        form = EditStudentForm(instance=student)

    return render(request, 'groups/change_student.html', {'form': form, 'student': student})


@login_required
def delete_student(request, pk):
    student = get_object_or_404(Student, pk=pk)
    group_id = student.group.pk
    student.delete()
    return redirect('group_detail', pk=group_id)