from flask import Flask

app = Flask(__name__)

@app.route('/')
def display_html():
    html_content = """
    <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Title Page</title>
</head>
<body>
    <h1>Dating Site</h1>
    <p>This is a simple page to be updated soon</p>
    <div>
        <a href="https://i.ibb.co/H2n8N2m/Dating-Anonymized.png">
            <img src="https://i.ibb.co/H2n8N2m/Dating-Anonymized.png" alt="Dating-Anonymized" border="0" />
        </a>
    </div>
    <script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>
    <script>
        // JavaScript code goes here
    </script>
    <button onclick="updateDataFrameContent()">Update DataFrame</button>
</body>
</html>

    """
    return html_content

if __name__ == '__main__':
    app.run(debug=True)
