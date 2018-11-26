from django.shortcuts import render, get_object_or_404, redirect
from django.views import View

from .models import Course
from .forms import CourseModelForm

# Create your views here.
# HTTP METHODS - função normal
def my_fbv(request, *args, **kwargs):
	return render(request, 'about.html', {})


# BASE VIEW CLASS = VIEW
class CourseView(View):
	template_name = 'about.html'
	# GET method
	def get(self, request, *args, **kwargs):
		return render(request, self.template_name, {})


class CourseDetailView(View):
	template_name = 'courses/course_detail.html'	
	def get(self, request, id=None, *args, **kwargs):
		# GET method	
		#context = {}
		if id is not None:
			obj = get_object_or_404(Course, id=id)
			#context['object'] = obj
			context = {
				'object': obj
			}
		return render(request, self.template_name, context)

class CourseListView(View):
	template_name = 'courses/course_list.html'
	queryset = Course.objects.all()

	# encapsula a funcao para ser aproveitada por outra classe
	def get_queryset(self):
		return self.queryset

	def get(self, request, *args, **kwargs):
		context = {
			'object_list': self.get_queryset(),
		}
		return render(request, self.template_name, context)

# extendendo a classe CourseListView
class MyListView(CourseListView):
	queryset = Course.objects.filter(id=1)


class CourseCreateView(View):
	template_name = 'courses/course_create.html'
	def get(self, request, *args, **kwargs):
		# GET method
		form = CourseModelForm()
		context = {'form': form}
		return render(request, self.template_name, context)

	def post(self, request, *args, **kwargs):
		# POST method
		form = CourseModelForm(request.POST)
		if form.is_valid():
			form.save()
			form = CourseModelForm()
		context = {'form': form}
		return render(request, self.template_name, context)


class CourseUpdateView(View):
	template_name = 'courses/course_update.html'
	
	def get_object(self):
		id = self.kwargs.get('id')
		obj = None
		if id is not None:
			obj = get_object_or_404(Course, id=id)
		return obj

	def get(self, request, id=None, *args, **kwargs):
		# GET method
		context = {}
		obj = self.get_object()
		if obj is not None:
			form = CourseModelForm(instance=obj)
			context['object'] = obj
			context['form'] = form
		return render(request, self.template_name, context)

	def post(self, request, id=None, *args, **kwargs):
		# POST method
		context = {}
		obj = self.get_object()
		if obj is not None:
			form = CourseModelForm(request.POST, instance=obj)
			if form.is_valid():
				form.save()
			context['object'] = obj
			context['form'] = form
			return redirect('courses:course-list')
		return render(request, self.template_name, context)


class CourseDeleteView(View):
	template_name = 'courses/course_delete.html'
	
	def get_object(self):
		id = self.kwargs.get('id')
		obj = None
		if id is not None:
			obj = get_object_or_404(Course, id=id)
		return obj

	def get(self, request, id=None, *args, **kwargs):
		# GET method
		context = {}
		obj = self.get_object()
		if obj is not None:
			context['object'] = obj
		return render(request, self.template_name, context)

	def post(self, request, id=None, *args, **kwargs):
		# POST method
		context = {}
		obj = self.get_object()
		if obj is not None:
			obj.delete()
			context['object'] = obj
			return redirect('courses:course-list')
		return render(request, self.template_name, context)