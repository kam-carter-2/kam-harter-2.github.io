<!DOCTYPE html>
 <html lang="en">
 <head>
   <meta charset="UTF-8" />
   <meta name="viewport" content="width=device-width, initial-scale=1.0" />
   <title>HelpHub - Connect with Charities</title>
   <style>
     /* Basic Reset */
     * { margin: 0; padding: 0; box-sizing: border-box; }
 
     body {
       font-family: Arial, sans-serif;
       background-color: #f2f7f5;
       color: #333;
       line-height: 1.6;
     }
 
     nav {
       background-color: #00796b;
       padding: 10px 20px;
       display: flex;
       justify-content: space-between;
       align-items: center;
     }
 
     nav a {
       color: #fff;
       text-decoration: none;
       margin: 0 10px;
       font-weight: bold;
     }
 
     nav a:hover {
       text-decoration: underline;
     }
 
     header {
       background: url('https://images.unsplash.com/photo-1488521787991-ed7bbaae773c?fit=crop&w=1200&q=80') no-repeat center center/cover;
       color: white;
       height: 300px;
       display: flex;
       flex-direction: column;
       justify-content: center;
       align-items: center;
       text-align: center;
       padding: 20px;
     }
 
     header h1 {
       font-size: 3rem;
       margin-bottom: 10px;
     }
 
     header p {
       font-size: 1.5rem;
     }
 
     .section {
       padding: 40px 20px;
       max-width: 1200px;
       margin: auto;
     }
 
     .charity-grid {
       display: grid;
       grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
       gap: 20px;
     }
 
     .charity-card {
       background: #ffffff;
       padding: 20px;
       border: 1px solid #ccc;
       border-radius: 10px;
       text-align: center;
     }
 
     .charity-card h3 {
       margin-bottom: 10px;
     }
 
     .charity-card p {
       margin-bottom: 15px;
     }
 
     .charity-card button {
       background-color: #00796b;
       color: white;
       padding: 10px 20px;
       border: none;
       border-radius: 5px;
       cursor: pointer;
     }
 
     .charity-card button:hover {
       background-color: #004d40;
     }
 
     .charity-profile {
       background: white;
       padding: 20px;
       border-radius: 10px;
     }
 
     .form {
       margin-top: 20px;
     }
 
     .form input, .form textarea {
       width: 100%;
       padding: 10px;
       margin-bottom: 10px;
       border: 1px solid #ccc;
       border-radius: 5px;
     }
 
     .form button {
       background-color: #00796b;
       color: white;
       border: none;
       padding: 10px 20px;
       cursor: pointer;
       border-radius: 5px;
     }
 
     footer {
       background-color: #004d40;
       color: white;
       text-align: center;
       padding: 15px 0;
       margin-top: 40px;
     }
 
     @media (max-width: 600px) {
       header h1 {
         font-size: 2rem;
       }
       header p {
         font-size: 1.2rem;
       }
     }
   </style>
 </head>
 
 <body>
 
   <!-- Navigation Bar -->
   <nav>
     <div><a href="#">HelpHub</a></div>
     <div>
       <a href="#home">Home</a>
       <a href="#charities">Find Charities</a>
       <a href="#contact">Contact Us</a>
       <a href="#">Login</a>
       <a href="#">Sign Up</a>
     </div>
   </nav>
 
   <!-- Homepage -->
   <header id="home">
     <h1>Welcome to HelpHub</h1>
     <p>Connecting Volunteers with Local Charities</p>
   </header>
 
   <div class="section">
     <h2>About HelpHub</h2>
     <p>HelpHub is a platform that connects passionate volunteers with local charities and community initiatives. Find opportunities to make a difference in your community today!</p>
   </div>
 
   <div class="section">
     <h2>Explore</h2>
     <div style="text-align:center;">
       <button onclick="location.href='#charities'">Find Charities Near You</button>
       <button onclick="location.href='#contact'">Volunteer Now</button>
     </div>
   </div>
 
   <!-- Charities List Page -->
   <div class="section" id="charities">
     <h2>Find Charities</h2>
     <div class="charity-grid">
       <div class="charity-card">
         <h3>Green Earth Foundation</h3>
         <p>Fighting for a greener tomorrow.</p>
         <button onclick="location.href='#charity1'">Learn More</button>
       </div>
       <div class="charity-card">
         <h3>Hope for All</h3>
         <p>Providing shelter and care for the homeless.</p>
         <button onclick="location.href='#charity2'">Learn More</button>
       </div>
       <div class="charity-card">
         <h3>Bright Future</h3>
         <p>Supporting education for underprivileged children.</p>
         <button onclick="location.href='#charity3'">Learn More</button>
       </div>
     </div>
   </div>
 
   <!-- Charity Profile Pages -->
   <div class="section" id="charity1">
     <div class="charity-profile">
       <h2>Green Earth Foundation</h2>
       <p>Our mission is to protect natural environments through education, conservation, and activism. Join us in making the Earth greener!</p>
       <button onclick="location.href='#contact'">Volunteer Now</button>
     </div>
   </div>
 
   <div class="section" id="charity2">
     <div class="charity-profile">
       <h2>Hope for All</h2>
       <p>Hope for All is committed to helping the homeless community with shelter, food, and counseling services. Volunteers are the heart of our work!</p>
       <button onclick="location.href='#contact'">Volunteer Now</button>
     </div>
   </div>
 
   <div class="section" id="charity3">
     <div class="charity-profile">
       <h2>Bright Future</h2>
       <p>Bright Future focuses on educational outreach programs for children in need. Be a mentor, tutor, or supporter today!</p>
       <button onclick="location.href='#contact'">Volunteer Now</button>
     </div>
   </div>
 
   <!-- Contact Form Section -->
   <div class="section" id="contact">
     <h2>Volunteer Now</h2>
     <form class="form">
       <input type="text" placeholder="Your Name" required />
       <input type="email" placeholder="Your Email" required />
       <input type="tel" placeholder="Your Phone Number" required />
       <textarea rows="4" placeholder="Tell us how you want to help..." required></textarea>
       <button type="submit">Submit</button>
     </form>
   </div>
 
   <! Footer >
   <footer>
     <p>HelpHub &copy; 2025 | Privacy Policy | Contact Us</p>
   </footer>
 
 </body>
 </html>