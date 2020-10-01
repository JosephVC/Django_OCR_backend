# Django_OCR_backend

The DRF back end to my OCR project, the front end being done in React.

  

More specifically, the front end will initially be a form taking a title, description, and a pdf file. This will then be submitted to the back end to be OCR'd by an external library, OCRmyPDF.

  

## Follow the Tutorial

I've set up a tutorial on creating both the front and back end on [Medium](https://medium.com/@josephvcardenas/pdf-ocr-via-react-django-rest-framework-and-heroku-part-1-set-up-and-starting-on-the-back-end-7932626dc040).  The tutorial will expand to match expanded features of the application itself.  

## Using the Web App
The front end of the web application is [hosted](https://ocr-app-frontend.herokuapp.com/) on Heroku.  The list of files is tied to the [Django REST Framework](https://www.django-rest-framework.org/) back end, which itself is sending our uploaded files to an Amazon S3 bucket.

### Uploading a file
The front end uses a simple upload form and asks for a simple title and description.  

### Viewing uploaded files
The file we upload is OCR'd via the back end, with the resulting file being stored in an S3 bucket. The Django back end keeps a list of each file and its corresponding title and description, with this list being mirrored on the front end.  The latter allows the user to see and download what they've uploaded.  **Future updates** to the front end will allow for greater functionality, such as grid views, visual previews of PDFs, as well as selection and editing of PDFs.

## Using the App Locally
We'll need to clone the [front end repo](https://github.com/JosephVC/React_OCR_frontend) in order to upload files.  

### Prepare the Front End
Make sure `UploadForm.js` points to `localhost:8000` rather than the Heroku-hosted backend (this is only if we want to keep both front and back ends local). Do the same with `FileList.js`.  

### Prepare the Back End
Ensure your `ALLOWED_HOSTS` settings allow `localhost` in addition to `.herokuapp.com`.  Also make sure to set `DEBUG` to `True` as you are not running the app in production. 

### Start Up the Front End
Run `npm start` from within the front end repo that was just cloned.  