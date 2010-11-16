from distutils.core import setup

setup(
    name = "django-recaptcha-comments",
    version = "1.0",
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
