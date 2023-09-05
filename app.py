from flask import Flask, render_template, request, jsonify
#   # Import your video downloader function

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/download', methods=['POST'])
def download():
    try:
        from video_downloader import video_downloader
        
        youtube_link = request.form['videoURL']
        video = video_downloader(youtube_link)
        response = {'success': True, 'message': f'"{video}" downloaded successfully!'}
    except Exception as e:
        response = {'success': False, 'message': f'Failed to download video: {str(e)}'}
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)
