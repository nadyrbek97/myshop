from .cart import Cart


def cart(request):
    return {'cart': Cart(request)}
    # The cart context processor will be executed every time
    # a template is rendered using Django's RequestContext.
    # The cart variable will be set in the context of your templates
    """
    Context processors
        A context processor is a Python function that takes the request object
        as an argument and returns a dictionary that gets added to the
        request context. They come in handy when you need to make
        something available globally to all templates.
        By default, when you create a new project using the startproject
        command, your project contains the following template context
        processors, in the context_processors option inside the TEMPLATES setting:
        : This sets the boolean debug
        and sql_queries variables in the context representing the list of
        SQL queries executed in the request.
        django.template.context_processors.debug
        : This sets the request
        django.template.context_processors.request
        variable in the context.
        : This sets the user
        django.contrib.auth.context_processors.auth
        variable in the request.
        : This sets a messages
        variable in the context containing all messages that have
        been generated using the messages framework.
    """