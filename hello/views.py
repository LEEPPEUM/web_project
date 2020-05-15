from django.shortcuts import render

# Create your views here.

# from django.http import HttpResponse
# def home(request):
#     return HttpResponse("Hello, Django!")


# # age02 문자로 취급됨. 205로 출력 되버리기 때문에 int라는 function을 이용하여 숫자로 처리되기 함.
# from django.http import JsonResponse

# def home(request):
#     name01 = request.GET['name']
#     age02 = request.GET['age']
#     # requestDict = request.GET
#     result = int(age02) + 5
#     requestDict = {'result_response':result}
#     return JsonResponse(requestDict)


# import pickle
# from django.http import JsonResponse

# class Class_3:
#     def __init__(self, x1=0, x2=2):
#         self.x1 = x1
#         self.x2 = x2
#     def calculate(self):
#         return self.x1 + self.x2
# c3 = Class_3()
# c3.calculate()
# # pickle.dump(c3, open("./c3.pkl", "wb"))
# # c3_pkl = pickle.load(open("./c3.pkl", "rb"))
# # c3_pkl.calculate()

# def home(request):
#     first01 = request.GET.get('first')
#     second02 = request.GET.get('second')
#     c3_pkl = pickle.load(open("./c3.pkl", "rb"))
#     result = c3_pkl.calculate()
#     requestDict = {'result_response':result}
#     return JsonResponse(requestDict)





import pickle
from django.http import JsonResponse

class Class_3:
    def __init__(self, x1=0, x2=2):
        self.x1 = x1
        self.x2 = x2
    def calculate(self):
        return self.x1 + self.x2
c3 = Class_3(30,32)
c3.calculate()
print(c3.calculate())
# pickle.dump(c3, open("./c3.pkl", "wb"))
# c3_pkl = pickle.load(open("./c3.pkl", "rb"))
# c3_pkl.calculate()

def home(request):
    first01 = request.GET['first']
    second02 = request.GET['second']
    c3_pkl = pickle.load(open("./c3.pkl", "rb"))
    c3_pkl = Class_3(int(first01),int(second02))
    result = c3_pkl.calculate()
    requestDict = {'result_response':result}
    return JsonResponse(requestDict)