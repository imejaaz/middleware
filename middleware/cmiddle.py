from django.http import HttpResponse
class middlewareClass1:

    def __init__(self, get_response):
        self.get_response = get_response
        print("this is initial print 1")


        
    def __call__(self, request):
        print("this is before views 1")
        response = self.get_response(request)
        print("this is after views 1")


        return response 

    def process_template_response(self, request, response):
        print("this is template  middleware")
        response.context_data['name'] = 'Mudassar'
        return response



        
    def process_exception(self,request, exception):
        print("this is exception method")
        exp = exception
        print(exp)
        return HttpResponse(exp)

    def process_view(request, *a, **b):
        print("exactly before vies")
        return HttpResponse("process retyurn")
        return HttpResponse("process view return")
        return None
        print("after process view")



    
 
    

    
