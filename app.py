@app.route('/remove-song/<int:playlist_id>/<int:song_id>', methods=['POST'])
def remove_song(playlist_id, song_id):
    playlist = DJPlaylist.query.get(playlist_id)
    song = Song.query.get(song_id)
    db.session.delete(song)
    db.session.commit()
    flash('Song removed from playlist!', 'success')
    return redirect(url_for('view_playlist', playlist_id=playlist.id))
