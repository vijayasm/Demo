from flask import Flask
 
app = Flask(__name__)
 
@app.route("/")
def home():
    return """
    <html>
    <head>
        <title>CI/CD Demo</title>
 
        <style>
 
        body{
            margin:0;
            height:100vh;
            background: linear-gradient(270deg,#ff6b6b,#4ecdc4,#45b7d1,#96c93d);
            background-size: 800% 800%;
            animation: bgmove 12s infinite;
            font-family: Arial;
            overflow:hidden;
        }
 
        @keyframes bgmove{
            0%{background-position:0% 50%}
            50%{background-position:100% 50%}
            100%{background-position:0% 50%}
        }
 
        .scroll-text{
            position:absolute;
            top:20px;
            white-space:nowrap;
            font-size:40px;
            font-weight:bold;
            color:white;
            animation: moveText 10s linear infinite;
        }
 
        @keyframes moveText{
            0%{left:100%}
            100%{left:-100%}
        }
 
        .ball{
            width:60px;
            height:60px;
            background:red;
            border-radius:50%;
            position:absolute;
            animation: bounce 4s infinite;
        }
 
        @keyframes bounce{
            0%{top:200px; left:0}
            50%{top:400px; left:80%}
            100%{top:200px; left:0}
        }
 
        .square{
            width:50px;
            height:50px;
            background:yellow;
            position:absolute;
            top:60%;
            animation: moveSquare 6s infinite;
        }
 
        @keyframes moveSquare{
            0%{left:0}
            50%{left:90%}
            100%{left:0}
        }
 
        </style>
 
    </head>
 
    <body>
 
        <div class="scroll-text">
        CI/CD Pipeline working successfully 🚀
        </div>
 
        <div class="ball"></div>
 
        <div class="square"></div>
 
    </body>
    </html>
    """
 
app.run(host="0.0.0.0", port=5000)
