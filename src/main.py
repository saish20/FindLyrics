import streamlit as st
import lyricsgenius

# Step 1: Install the lyricsgenius library and obtain an API token from the Genius website
# !pip install lyricsgenius

# Step 2: Set up the API client
genius = lyricsgenius.Genius("YOUR_ACCESS_TOKEN_HERE",timeout=100)

# Create the Streamlit app
def app():
    # Set the app title and description
    st.set_page_config(page_title='Lyrics Search', page_icon=':microphone:')
    st.title('Lyrics Search')
    st.write('This app allows you to search for the lyrics of any song on Genius.')
    
    # Get user input for song title and artist name
    song_title = st.text_input('Enter the song title:', '')
    artist_name = st.text_input('Enter the artist name:', '')
    
    # Define function to search for and retrieve lyrics
    def get_lyrics(title, artist):
        search_results = genius.search_song(title, artist)
        if search_results is not None:
            lyrics = search_results.lyrics
            return lyrics
        else:
            return "Could not find lyrics for the specified song and artist."
    
    # Display lyrics on search button click
    if st.button('Search'):
        lyrics = get_lyrics(song_title, artist_name)
        st.write('Lyrics:')
        st.write(lyrics)

if __name__ == '__main__':
    app()
