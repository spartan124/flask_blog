from flask import Blueprint, render_template, request, flash, redirect, url_for
from ..forms import ContactForm
from ..models import ContactUs
from ..utils import save_to_db

pages = Blueprint('pages', __name__, template_folder='templates')

@pages.route('/about', methods=['GET', 'POST'])
def about():
    return render_template('about.html')


@pages.route('/contact', methods=['GET', 'POST'])
def contact_us():
    form = ContactForm()

    if request.method == 'POST':
        fullname = request.form.get('fullname')
        email = request.form.get('email')
        subject = request.form.get('subject')
        message = request.form.get('message')

        try:
            contact = ContactUs(fullname=fullname, email=email,
                            subject=subject, message=message)
            save_to_db(contact)
            

            flash("Message Sent Successfully")
        except:
            print('Very long traceback error')
        return redirect(url_for('pages.contact_us'))

    return render_template('contact.html', form=form)
