#importing the required libraries
import streamlit as st
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap
import numpy as np
from matplotlib.pyplot import specgram
import librosa
import librosa.display
from matplotlib import ticker, cm
import sys, os
import IPython.display as idisp
from IPython.display import Audio
import io
from PIL import Image
from scipy.io import wavfile
import streamlit as st


# Building the functions for the following visuals that I plan to show to the user:

def plot_audio_player(audio_data, sample_rate):
    '''

    :param audio_data: The audio file
    :param sample_rate: The default sampling rate which is the samples taken per second of the audio
    :return: Returns the audio file where you can hear the audio inside the script
    '''
    virtualfile = io.BytesIO()
    wavfile.write(virtualfile, rate=sample_rate, data=audio_data)

    return virtualfile

def plot_waveplot(y,sr):
    '''
    :param y: This is the data file
    :param sr: This is the sampling rate
    :return: Returns the wavelength of the inputted emotion's audio file
    '''
    fig, ax = plt.subplots()

    img = librosa.display.waveshow(y, sr=sr, x_axis="time", ax=ax)

    return plt.gcf()

def plot_spectogram(y, sr):
    '''
    :param y: This is the data file
    :param sr: This is the sampling rate
    :return: Returns the plotted spectogram of the emotion's audio file
    '''
    spectogram = librosa.feature.melspectrogram(y=y, sr=sr, n_mels=128, fmax=8000)
    spectogram = librosa.power_to_db(spectogram)

    img = librosa.display.specshow(spectogram, y_axis='mel', x_axis='time')
    plt.title('Mel Spectogram')
    plt.colorbar(img,format='%+2.0f dB')

    return plt.gcf()

def plot_emotion(emotion):
    '''
    :param emotion: Takes in the emotion, the user selects from the dropdown menu on the interface
    :return: Returns the visualization of the circle (with density) representing the selected emotion
    '''
    fig, ax = plt.subplots(figsize=(10, 4))
    if emotion == 'Achievement':
        n = 100
        inner_radius = 1
        outer_radius = 2
        center_x = 1
        center_y = 2
        glow_color = '#66CD00'

        center_color = '#458B00'
        xmin = center_x - outer_radius
        xmax = center_x + outer_radius

        ymin = center_y - outer_radius
        ymax = center_y + outer_radius
        x, y = np.meshgrid(np.linspace(xmin, xmax, n), np.linspace(ymin, ymax, n))
        r = np.sqrt((x - center_x) ** 2 + (y - center_y) ** 2)
        z = np.where(r < inner_radius, np.nan, np.clip(outer_radius - r, 0, np.inf))
        cmap = LinearSegmentedColormap.from_list('', ['#FFFFFF00', glow_color])
        cmap.set_bad(center_color)
        ax = plt.imshow(z, cmap=cmap, extent=[xmin, xmax, ymin, ymax], origin='lower', zorder=3) # move the other circle on top of the first
        plt.axis('off')
        #st.pyplot(fig)
    if emotion == 'Surprise':
        n = 100
        inner_radius = 1
        outer_radius = 2
        center_x = 1
        center_y = 2
        glow_color = '#FFD700'

        center_color = '#EEEE00'
        xmin = center_x - outer_radius
        xmax = center_x + outer_radius
        ymin = center_y - outer_radius
        ymax = center_y + outer_radius
        x, y = np.meshgrid(np.linspace(xmin, xmax, n), np.linspace(ymin, ymax, n))
        r = np.sqrt((x - center_x) ** 2 + (y - center_y) ** 2)
        z = np.where(r < inner_radius, np.nan, np.clip(outer_radius - r, 0, np.inf))
        cmap = LinearSegmentedColormap.from_list('', ['#FFFFFF00', glow_color])
        cmap.set_bad(center_color)
        ax = plt.imshow(z, cmap=cmap, extent=[xmin, xmax, ymin, ymax], origin='lower', zorder=3)
        plt.axis('off')
    if emotion == 'Fear':
        n = 100
        inner_radius = 1
        outer_radius = 2
        center_x = 1
        center_y = 2
        glow_color = '#FF00FF'

        center_color = '#FF34B3'
        xmin = center_x - outer_radius
        xmax = center_x + outer_radius
        ymin = center_y - outer_radius
        ymax = center_y + outer_radius
        x, y = np.meshgrid(np.linspace(xmin, xmax, n), np.linspace(ymin, ymax, n))
        r = np.sqrt((x - center_x) ** 2 + (y - center_y) ** 2)
        z = np.where(r < inner_radius, np.nan, np.clip(outer_radius - r, 0, np.inf))
        cmap = LinearSegmentedColormap.from_list('', ['#FFFFFF00', glow_color])
        cmap.set_bad(center_color)
        ax = plt.imshow(z, cmap=cmap, extent=[xmin, xmax, ymin, ymax], origin='lower', zorder=3)
        plt.axis('off')
    if emotion == 'Anger':
        n = 100
        inner_radius = 1
        outer_radius = 2
        center_x = 1
        center_y = 2
        glow_color = '#FF0000'

        center_color = '#EE4000'
        xmin = center_x - outer_radius
        xmax = center_x + outer_radius
        ymin = center_y - outer_radius
        ymax = center_y + outer_radius
        x, y = np.meshgrid(np.linspace(xmin, xmax, n), np.linspace(ymin, ymax, n))
        r = np.sqrt((x - center_x) ** 2 + (y - center_y) ** 2)
        z = np.where(r < inner_radius, np.nan, np.clip(outer_radius - r, 0, np.inf))
        cmap = LinearSegmentedColormap.from_list('', ['#FFFFFF00', glow_color])
        cmap.set_bad(center_color)
        ax = plt.imshow(z, cmap=cmap, extent=[xmin, xmax, ymin, ymax], origin='lower', zorder=3)
        plt.axis('off')
    if emotion == 'Pain':
        n = 100
        inner_radius = 1
        outer_radius = 2
        center_x = 1
        center_y = 2
        glow_color = '#87CEFF'

        center_color = '#4876FF'
        xmin = center_x - outer_radius
        xmax = center_x + outer_radius
        ymin = center_y - outer_radius
        ymax = center_y + outer_radius

        # meshgrid for turning the radius values into an array to plot the outer circle grid.
        x, y = np.meshgrid(np.linspace(xmin, xmax, n), np.linspace(ymin, ymax, n))

        r = np.sqrt((x - center_x) ** 2 + (y - center_y) ** 2)
        z = np.where(r < inner_radius, np.nan, np.clip(outer_radius - r, 0, np.inf))
        cmap = LinearSegmentedColormap.from_list('', ['#FFFFFF00', glow_color])
        cmap.set_bad(center_color)
        ax = plt.imshow(z, cmap=cmap, extent=[xmin, xmax, ymin, ymax], origin='lower', zorder=3)
        plt.axis('off')

def plot_data(y, sr):
    '''
    :param y: This is again the data file extracted from the uploaded audio file
    :param sr: The specified sampling rate
    :return: Returns the four visualizations(audio, waveplot, spectogram and the corresponding visual of the circle) in four columns
    '''
    columns = [1, 1, 1, 1]

    col1, col2, col3, col4 = st.columns(columns)
    with col1:
        st.markdown('**Audio File:**')
        st.audio(plot_audio_player(y, sr))
    with col2:
        st.markdown('**Audio Waveplot:**')
        st.pyplot(plot_waveplot(y, sr))
    with col3:
        st.markdown('**Audio Spectogram**')
        st.pyplot(plot_spectogram(y, sr))
    with col4:
        st.markdown('Emotion: '+ emotion)
        st.pyplot(plot_emotion(emotion))



def load_audio_sample(file):
    '''
    :param file: Takes in the input audio file and assigns the associated data (y) and the sampling rate for the audio.
    :return: The data and the updated data with the assigned sampling rate.
    '''
    y, sr = librosa.load(file, sr=22050) # the default sampling rate

    return y, sr

def visualize_data(audio_emotion):
    '''
    :param audio_emotion: The variable which checks if an audio file has been uploaded or not and if it's been then plot the associated visualizations.
    :return:Returns the visualizations of the audio as defined in the function plot_data()
    '''
    if audio_emotion is not None:
        y, sr = librosa.load(audio_emotion)
    plot_data(y, sr)

def main():
    st.title("Visualizing Emotions Audio Data")
    st.write('''This assignment's goal is to visualise the different emotions by using the sound audio files. The dataset used to build this can be found on this [link](https://zenodo.org/record/4066235#.YzWH-3Yzaw4)''')
    image = Image.open(r'C:\Users\PC\PycharmProjects\empathic_DV\2022-09-28 21_31_34-Data Visualization and Feelings - Scientific American Blog Network.png')
    col1, col2, col3 = st.columns([0.2, 0.4, 0.2])
    col2.image(image, use_column_width=True)
    #st.image(image)

    global emotion
    emotion = st.sidebar.selectbox('Which emotion would you like to test?',
                    ('Fear', 'Pain', 'Anger', 'Surprise', 'Achievement'))
    st.write('You selected:', emotion)

    st.sidebar.markdown("Upload your audio file here:")
    global file
    file = st.sidebar.file_uploader(label="",
                                    type=['.wav', '.mp3'])
    if st.sidebar.button("Visualize"):
        visualize_data(audio_emotion = file)


if __name__ == "__main__":
    st.set_page_config(layout='wide')
    st.set_option('deprecation.showPyplotGlobalUse', False)
    main()







