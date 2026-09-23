from django import forms

from books.models import Comment


class CommentForm(forms.ModelForm):
	class Meta :
		model = Comment
		fields = ['text' , 'recommend']  # 👈 اینجا شد text
		labels = {
			'text' : 'متن نظر شما' ,  # 👈 اینجا شد text
		}
		widgets = {
			'text' : forms.Textarea(attrs = {  # 👈 اینجا هم شد text
				'rows' : 4 ,
				'placeholder' : 'نظر خود را بنویسید...' ,
			}) ,
		}

#