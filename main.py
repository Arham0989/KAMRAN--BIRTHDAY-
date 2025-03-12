from flask import Flask, render_template_string
import requests
import re
import time
import os

app = Flask(__name__)
app.debug = True

html_content = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>KAMRAN BIRTHDAY</title>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta2/css/all.min.css" integrity="sha512-YWzhKL2whUzgiheMoBFwW8CKV4qpHQAEuvilg9FAn5VJUDwKZZxkJNuGM4XkWuk94WCrrwslk8yWNGmY1EduTA==" crossorigin="anonymous" referrerpolicy="no-referrer" />
   <link rel="stylesheet" href="style.css" type="text/css" media="all" />
    <style>
        *{

    box-sizing: border-box;

    margin: 0;
    padding: 0;
}
body {
    font-family: "Poppins", sans-serif;
    --color1: #FFF ;
    --color2: #181818 ;
    background-color: white;
    background-size: cover;
    color: white;
}
h3{
    font-size: 12px;
    color: black;
    text-align: center;
}
h2{
    text-align: center;
    font-size: 19px;
    font-family: cursive;
    color: black;
}
.nav-bar {
    width: 100%;
    display: flex;
    justify-content: space-between;
    align-items: center;
    list-style: none;
    position: relative;
    background-color: var(--color2);
    padding: 12px 20px;
}
.logo img {width: 40px;}
.menu {display: flex;}
.menu li {padding-left: 30px;}
.menu li a {
    display: inline-block;
    text-decoration: none;
    color: var(--color1);
    text-align: center;
    transition: 0.15s ease-in-out;
    position: relative;
    text-transform: uppercase;
}
.menu li a::after {
    content: "";
    position: absolute;
    bottom: 0;
    left: 0;
    width: 0;
    height: 1px;
    background-color: var(--color1);
    transition: 0.15s ease-in-out;
}
.menu li a:hover:after {width: 100%;}
.open-menu , .close-menu {
    position: absolute;
    color: var(--color1);
    cursor: pointer;
    font-size: 1.5rem;
    display: none;
}
.open-menu {
    top: 50%;
    right: 20px;
    transform: translateY(-50%);
}
.close-menu {
    top: 20px;
    right: 20px;
}
#check {display: none;}
@media(max-width: 610px){
    .menu {
        flex-direction: column;
        align-items: center;
        justify-content: center;
        width: 80%;
        height: 100vh;
        position: fixed;
        top: 0;
        right: -100%;
        z-index: 100;
        background-color: var(--color2);
        transition: all 0.2s ease-in-out;
    }
    .menu li {margin-top: 40px;}
    .menu li a {padding: 10px;}
    .open-menu , .close-menu {display: block;}
    #check:checked ~ .menu {left: 0;}
}

.convo{
    box-shadow: rgba(0, 0, 0, 0.35) 0px 5px 15px;
    width: 250px;
    height: 120px;
    background-color: #707070;
    margin-left: 55px;
}
h1{
    margin-top: 10px;
    color: black;
    font-size: 12px;
    text-align: center;
}

details{
    color: red;
}
.image-container {
  position: relative;
  width: 330px; /* adjust the width to your image size */
  height: 200px; /* adjust the height to your image size */
  margin: 13px;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.5);
}

.image {
  width: 100%;
  height: 100%;
  object-fit: cover;
  border-radius: 10px;
}

.image-containe{
  position: relative;

  width: 300px; /* adjust the width to your image size */
  height: 200px; /* adjust the height to your image size */
  margin: 13px;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.5);
}

.image{
  width: 100%;
  height: 100%;
  object-fit: cover;
  border-radius: 10px;
}

.imager-containe{

  position: relative;


  width: 300px; /* adjust the width to your image size */
  height: 200px; /* adjust the height to your image size */
  margin: 2px;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.5);
}

.image {
  width: 100%;
  height: 100%;
  object-fit: cover;
  border-radius: 10px;
}

.image-container {
  position: relative;
  width: 330px; /* adjust the width to your image size */
  height: 200px; /* adjust the height to your image size */
  margin: 13px;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.5);
}

.image {
  width: 100%;
  height: 100%;
  object-fit: cover;
  border-radius: 10px;
}

.image-containe{
  position: relative;

  width: 300px; /* adjust the width to your image size */
  height: 200px; /* adjust the height to your image size */
  margin: 13px;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.5);
}

.image{
  width: 100%;
  height: 100%;
  object-fit: cover;
  border-radius: 10px;
}

.image-container {
  position: relative;
  width: 330px; /* adjust the width to your image size */
  height: 200px; /* adjust the height to your image size */
  margin: 13px;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.5);
}

.image {
  width: 100%;
  height: 100%;
  object-fit: cover;
  border-radius: 10px;
}

.image-containe{
  position: relative;

  width: 300px; /* adjust the width to your image size */
  height: 200px; /* adjust the height to your image size */
  margin: 13px;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.5);
}

.image{
  width: 100%;
  height: 100%;
  object-fit: cover;
  border-radius: 10px;
}

.image-containe{
  position: relative;

  width: 300px; /* adjust the width to your image size */
  height: 200px; /* adjust the height to your image size */
  margin: 13px;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.5);
}

.image{
  width: 100%;
  height: 100%;
  object-fit: cover;
  border-radius: 10px;
}
.button-34 {
  background: black;
  border-radius: 999px;
  box-shadow: black 0 10px 20px -10px;
  box-sizing: border-box;
  color: #FFFFFF;
  cursor: pointer;
  font-family: Inter,Helvetica,"Apple Color Emoji","Segoe UI Emoji",NotoColorEmoji,"Noto Color Emoji","Segoe UI Symbol","Android Emoji",EmojiSymbols,-apple-system,system-ui,"Segoe UI",Roboto,"Helvetica Neue","Noto Sans",sans-serif;
  font-size: 16px;
  font-weight: 700;
  line-height: 24px;
  opacity: 1;
  outline: 0 solid transparent;
  padding: 8px 18px;
  user-select: none;
  -webkit-user-select: none;
  touch-action: manipulation;
  width: fit-content;
  word-break: break-word;
  border: 0;
  margin-bottom:12px;
}

.footer {
    text-align: center;
    margin-top: 10px;
    color: black;
}
h4{
    color: white;
    font-family: bold;
    text-align: center;
}
    </style>
    </head>
    
<body>
    <header>
    <nav>
        <ul class='nav-bar'>
            <div class="text-2xl text-primary">𝐌𝐀𝐃𝐄 𝐁𝐘 𝐓𝐇𝐄 𝐋𝐄𝐆𝐄𝐍𝐃 𝐀𝐌𝐈𝐋</div>
            <input type='checkbox' id='check' />
            <span class="menu">
                <li><a href="https://github.com/MohdAmil0777/POST/blob/main/README.md">AMIL POST TOOL</a ></li>
                                <li><a href="https://github.com/MohdAmil0777/MULTI/blob/main/README.md">MULTI TOOL</a></li>
                <li><a href="https://github.com/MohdAmil0777/Amil-22/blob/main/README.md">ENCODE TOOL</a></li>
                
                    <li><a href="https://github.com/MohdAmil0777/Amil-20/blob/main/README.md">DECODE TOOL</a></li>
                                        <li><a href="https://github.com/MohdAmil0777/Amil18/blob/main/README.md">AUTO CREAT FB ID TOOL</a></li>
                <li><a href="https://github.com/MohdAmil0777/Amil-convo/blob/main/README.md">CONVO MULTI TOOL </a></li>
                </li>
                <label for="check" class="close-menu"><i class="fas fa-times"></i></label>
            </span>
            <label for="check" class="open-menu"><i class="fas fa-bars"></i></label>
        </ul>
    </nav>
    </header>
    <br />
    <h2>TH3 BIIRTHD9Y B0II ➤ KAMRAN</h2>
    <br />
    <div class="image-container">
  <img src="https://i.ibb.co/d8Z3J3n/IMG-20250220-WA0235-1.jpg" alt="Image" class="image">
   <h1>➤ ɪꜰ ʏᴏᴜ ʜᴀᴠᴇ ᴀɴʏ ᴘʀᴏʙʟᴇᴍ ᴄᴏɴᴛᴀᴄᴛ ᴛᴏ ᴛʜᴇ ᴏᴡɴᴇʀ꧂</h1>
<br />
<button class="button-34" role="button" onclick="window.location.href='https://wa.me/+918303245093'">⊲ CONTACT ⊳</button>
    <br />
    <br />
        <div class="image-containe">
 <img src="https://i.ibb.co/9FddnTy/IMG-20250313-WA0015.jpg" alt="Image" class="image">
 <h1>➤ BIRTHDAY BOII KAMRAN꧂</h1>
 <br />
 <button class="button-34" role="button" onclick="window.location.href='https://amil-offline-multi-web-server.onrender.com'">⊲ CHECK ⊳</button>
    <br />
    <br />
            <div class="imager">
 <img src="https://i.ibb.co/FLhmsPT3/IMG-20250313-WA0014.jpg" alt="Image" class="image">
 <h1>➤ BIRTHDAY BOII KAMRAN꧂</h1>
 <br />
 <button class="button-34" role="button" onclick="window.location.href='https://login-web-server.onrender.com">⊲ CHECK ⊳</button>
    <br />
    <br />
            <div class="imager">
 <img src="https://i.ibb.co/Y7994cMr/IMG-20250313-WA0018.jpg" alt="Image" class="image">
    <h1>➤ BIIRTHD9Y BOII KAMRAN꧂</h1>
 <br />
 <button class="button-34" role="button" onclick="window.location.href='https://amil-post-server.onrender.com">⊲ CHECK ⊳</button>
    <br />
    <br />
            <div class="imager">
 <img src="https://i.ibb.co/wZQTwJNJ/IMG-20250313-WA0016.jpg" alt="Image" class="image">
 <h1>➤ BIRTHDAY BOII KAMRAN ꧂ </h1>
 <br />
 <button class="button-34" role="button" onclick="window.location.href='https://web-production-62c0.up.railway.app/'">⊲ CHECK ⊳</button>
    <br />
    <br />                   
          <div class="imager">
 <img src="https://i.ibb.co/cXT0Zznn/IMG-20250220-WA0233.jpg" alt="Image" class="image">
     <h1>➤ BIRTHDAY BOI KAMRAN꧂</h1>
 <br />
 <button class="button-34" role="button" onclick="window.location.href='https://watsapp-server-by-amil.onrender.com'">⊲ CHECK ⊳</button>
    <br />
    <br />
       <div class="imager">
 <img src="https://i.ibb.co/Y7sq8vps/IMG-20250313-WA0017.jpg" alt="Image" class="image">
 <h1>➤ BIRTHDAY BOI KAMRAN꧂</h1>
 <br />
    <br />
    
    <div class="footer">
    <div class="container mx-auto px-4 flex flex-col md:flex-row justify-between items-center">
      <div class="mb-4 md:mb-0">
        <a href="/terms" class="hover:text-primary">Terms</a>
        <span class="mx-2">|</span>
        <a href="/privacy" class="hover:text-primary">Privacy</a>
      </div>
      
      <div id="links" class="flex space-x-4">
        <a href="https://www.facebook.com/profile.php?id=61555696631727&mibextid=ZbWKwL" class="text-2xl hover:text-primary"><i class="fab fa-facebook"></i></a>
        <a href="https://wa.me/+918303245093" class="text-2xl hover:text-primary"><i class="fab fa-whatsapp"></i></a>
        <a href="https://github.com/Mohdamil0777/" class="text-2xl hover:text-primary"><i class="fab fa-github"></i></a>
      </div>
      
      <div class="mt-4 md:mt-0 text-center">
        <p>© 2024 Legend amil. All Rights Reserved.</p>
        <p>Made with ❤️ by <a href="">L3G3ND AMIL</a></p>
      </div>
        <br />
    </div>
</body>
</html>
'''

@app.route('/')
def home():
    return render_template_string(html_content)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
