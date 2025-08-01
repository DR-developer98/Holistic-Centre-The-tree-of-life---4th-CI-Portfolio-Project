<img src="images-README/logo-the-tree-of-life.png" style="width: 25%" alt="Holisit centre The tree of life logo">

<h1 style="color: gold">Holistic centre - The tree of life</h1>
<p>Welcome to the official website of the Holistic centre "The tree of life". Get to see the faces and to learn more about the treatments of this wellness centre, located in the very pittoresque town of Kromme-ellebogenstad (Dutch for "Crooked-elbows town"). The website is designed:</p>
<ul>
<li>for the business owner, serving the purpose of enabling the appointment booking process and making it as straightforward as possible;</li>
<li>the visitor and the prospective customers, enabling them to see the faces of the centre and getting them acquainted with the business offer;</li>
<li>the customers, enabling them to manage their appointments;</li>
<li>the website administrator, allowing them to manage the content of the website.</li>
</ul>

<h2>User stories</h2>
<ol>
<li>As a Site admin, I can add, edit or delete the centre's employees' profiles, so that I can keep the employees list up to date;</li>
<li>As a customer, I can view the list of treatments with their price, so that I can choose the one that's most suitable to me within my buget;</li>
<li>As a Site admin, I can add, inspect, delete or edit treatments from the list, so that I can manage the website content</li>
<li>As a Prospective customer, I can get in touch with the holistic centre, so that I can ask questions;</li>
<li>As a Site admin, I can store the sent in enquiries by potential customers in the database, so that I can review them;</li>
<li>As a Site admin, I can mark the sent in enquiries as "processed", so that I can see how many I still need to process</li>
<li>As the business owner, I want a prominent "Make an appointment button" on the website, so that my prospective customers can easily make an appointment and I can increase my clientele;</li>
<li>As a Site user, I can register an account, so that I can make an appointment</li>
<li>As a logged in user, I can create, view, update, and delete my own appointments, so that I have full control over my treatment schedule and can manage my time effectively;</li>
</ol>
<p>For the implementation of these user stories, I used the following project (<a href="https://github.com/users/DR-developer98/projects/7/views/1" target="_blank">Holistic centre "The tree of life" User stories</a>) as a backlog.</p>

<h2 style="color: darkorange">Wireframes</h2>
<img src="images-README/Tree-of-life-wireframes.png">
<br>
<p>Link to repository: <a href="https://github.com/DR-developer98/Holistic-Centre-The-tree-of-life---4th-CI-Portfolio-Project" target="_blank">Holistic-Centre-The-tree-of-life---4th-CI-Portfolio-Project
</a></p>
<p>Link to deployed project: <a href="" target="_blank">Holistic centre "The tree of life"</a></p>


<h2 style="color: darkorange">Features</h2>

<h3 style="color: gold">Future implementations</h3>
<p>In the future, the following features can be added to this application:</p>
<ul>
<li>An "About us" page, with some background information about each employee; this app can be furthered enhanced by adding a "Make an appointment" button that prepopulates the appointment form with the name of the employee, in this way enabling the user to make an appointment with preferred employee;</li>
<li>In the home page under each employee, a "Get to know them" button can be added, which links to the "About us" page, so that the website visitors would be directly forwarded to the presentation/background text of the selected employee;</li>
<li>In the treatment page, a "Make an appointment" button could be added for each treatment, which - when clicked - would redirect the visitor to the appointment form and populate the "treatment"-field with the selected item;</li>
<li>Django logic could be added to the base template to include a "Scheduled appointment" navlink, only visible for the logged in Employee-user, similar to the current "My appointments" page, where the employee would have access to the list of appointments booked with them. This section would allow the employee to modify the appointment or to delete it. To finish it off, one could consider integrating a notification system to informt the user about the change and the reason for the change.</li>
<li>For the purpose of this project, I decided not to further refine the time selection field of the appointment form. In future enhancements, one can definitely consider tailoring the time and date selection to the duration of the selected treatment and to the employees' schedules. This could be achieved by wiring the form to the employee's Google Calendar.</li>
</ul>

<h2 style="color: darkorange">Testing</h2>
<p>For the testing part, including fixed bugs, please refer to <a href="TESTING.md">TESTING.md</a></p>

<h2 style="color: darkorange">Deployment</h2>

<h2 style="color: darkorange">Credits</h2>
<h3>Content</h3>
<ul>
<li><a href="https://copilot.microsoft.com/chats/GB3BA3usiipHcgySkE9RN" target="_blank">Microsoft Copilot</a> was used for some debugging, incorporation of widgets in the make an appointment form and tweaking of some models and views. For detailed source referencing, please see code.</li>
<li>The "I think, therefore I blog" Code Institute Project was also referenced for - amongst others - the sign in, sign up and sign out html templates and for linking the cancel appointment button to the modal. The exact code sections that were built in this way are indicated in detail in the code.</li>
<li><a href="https://stackoverflow.com/" target="_blank">Stackoverflow</a> was consulted for - amongst others - building the TimeOut function for the fade out effect on Django messages. Detailed referencing can be found in the code.</li>
</ul>


<h3 style="color: gold">Used technologies and media</h3>
<ul>
<li>The website logo, the images of the employees and the treatments were created with <a href="https://copilot.microsoft.com/chats/GB3BA3usiipHcgySkE9RN" target="_blank">Microsoft Copilot</a></li>
<li>The hero-images in the home page, treatments, get in touch and make an appointment page were created using <a href="https://leonardo.ai/" target="_blank">Leonardo.AI</a></li>
<li></li>
<li>Django (Python) was used for building and managing the project and its different apps;</li>
<li>HTML was used for the templates' structure;</li>
<li>CSS was used for the styling and the buttons hover effects;</li>
<li>JavaScript was used for handling the appointment edit and cancel functions;</li>
</ul>

