from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtform.validators import DataRequired

class DJPlaylistForm(FlaskForm):
    title = StringField('Title' , validators=[DataRequired()])
    description = TextAreaField('Description')
    submit = SubmitField('Create Playlist')

@app.route('/create-dj-playlist' , methods=['GET', 'POST'])
def create_dj_playlist():
    form = DJPlaylistForm()
    if form.validate_on_submit()
    playlist = DJPlaylist(title=form.title.data, description=form.description.data)
    db.session.add(playlist)
    db.session.commit()
    return redirect('/')
    return render_template('create_dj_playlist.html', form=form)