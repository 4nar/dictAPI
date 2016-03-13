from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets
from dictionary.serializers import WordSerializer, ShortWordSerializer
from dictionary.models import Word
from rest_framework import generics
import copy

class WordViewSet(generics.ListAPIView):
	queryset = Word.objects.all()
	serializer_class = WordSerializer

class WordDetail(generics.RetrieveAPIView):
	queryset = Word.objects.all()
	serializer_class = WordSerializer

class LangView(generics.ListAPIView):
	serializer_class = WordSerializer
	lookup_url_kwarg = "language"
	def get_queryset(self):
		language = self.kwargs.get(self.lookup_url_kwarg)
		queryset = Word.objects.filter(language=language)
		start = self.request.query_params.get('title__istartswith', None)
		startswith_list = []
		listOfobj = []
		listOfobj_ = []
		if start is not None:
			start = start.lower()

			for t in Word.objects.all():
				i = 0
				if t.title.startswith(start):
					startswith_list.append(t.title)
			for x in startswith_list:
				listOfobj.append(Word.objects.all().filter(title=x))

			for x in listOfobj:
				for y in x:
					listOfobj_.append(y)

			
			return sorted(listOfobj_, key=lambda Word: Word.title)
		return queryset
		


class LangDetailed(generics.RetrieveAPIView):
	serializer_class = WordSerializer
	queryset = Word.objects.all()
	multiple_lookup_fields = ["pk","language"]
	def get_object(self):
	    queryset = self.get_queryset()
	    filter = {}
	    for field in self.multiple_lookup_fields:
	        filter[field] = self.kwargs[field]
	    obj = get_object_or_404(queryset, **filter)
	    self.check_object_permissions(self.request, obj)
	    t_lang = self.request.query_params.get('translate', None)
	    if t_lang is not None:
	    	return obj
	    	# print(newobj)

	   		
	    return obj




		



		
