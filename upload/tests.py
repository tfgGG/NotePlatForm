from django.test import TestCase
'''
# Create your tests here.
def detail(request,note_id):
    # TODO: Change to RESTFUL in the future
    notelist= NoteList.objects.filter(noteid = note_id).order_by("list_num")
    message = Message.objects.all()
    if request.method == "POST":
        message = request.POST['message']

        num=(Message.objects.all().count()) + 1

        unit = Message.objects.create(id=num,note_id=note_id
        ,message=message)
        unit.save()
    return render(request,'upload/detail_note.html',{"notelist":notelist,"noteid":note_id,"message":message})
'''