# Django_OCR_backend

The DRF back end to my OCR project, the front end being done in React.

  

More specifically, the front end will initially be a form taking a title, description, and a pdf file. This will then be submitted to the back end to be OCR'd by an external library, OCRmyPDF.

  

## Follow the Tutorial

I've set up a tutorial on creating both the front and back end on [Medium](https://medium.com/@josephvcardenas/pdf-ocr-via-react-django-rest-framework-and-heroku-part-1-set-up-and-starting-on-the-back-end-7932626dc040).  The tutorial will expand to match expanded features of the application itself.  

## Using the Web App
The front end of the web application is [hosted](https://ocr-app-frontend.herokuapp.com/) on Heroku.  The list of files is tied to the [Django REST Framework](https://www.django-rest-framework.org/) back end, which itself is sending our uploaded files to an Amazon S3 bucket.
