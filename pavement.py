from paver.easy import *
from paver.setuputils import setup
from paver.tasks import BuildFailure

setup(
    name = "django-recaptcha-comments",
    version = "1",
    author = "Bill Mill",
    author_email = "bill.mill@gmail.com",
    description = "An application to make it easy for django sites to require reCAPTCHA on comments",
    long_description = open("README.md").read(),
    license = "BSD",
    url = "http://github.com/llimllib/django-recaptcha-comments",
    packages = [
        "recaptcha_comments",
        "recaptcha_comments.templatetags",
    ],
    classifiers = [
        "Development Status :: 3 - Alpha",
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "License :: Freely Distributable",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Framework :: Django",
    ]
)

@task
def builddocs():
    try:
        sh("pycco recaptcha_comments/[a-z]*.py")
        sh("pycco recaptcha_comments/templatetags/[a-z]*.py")
    except BuildFailure:
        print "error building docs, make sure you have pycco installed if you want to build them. Skipping."

@task
@needs('generate_setup', 'minilib', 'setuptools.command.sdist', "builddocs")
def sdist():
    """Overrides sdist to make sure that our setup.py is generated."""
    pass
