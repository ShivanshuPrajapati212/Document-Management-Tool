from django import template

register = template.Library()

@register.filter
def file_type(value):
    image_extensions = ['jpg', 'jpeg', 'png', 'gif']
    document_extensions = ['doc', 'docx', 'pdf', 'txt']
    code_extensions = ['py', 'java', 'cpp', 'html', 'css', 'js']
    # Add more extensions as needed
    
    file_extension = value.split('.')[-1].lower()
    
    if file_extension in image_extensions:
        return 'image'
    elif file_extension in document_extensions:
        return 'document'
    elif file_extension in code_extensions:
        return 'code'
    else:
        return 'other'