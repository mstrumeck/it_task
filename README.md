<h1>User manual.</h2>
<p> You can use the fibonacci transformer function via localhost/fib/<num> endpoint,
where 'num' is your number to transform.</p>

<h2>Deployment manual</h2>
<p>You can easily deploy application via Dockerfile. Please, make sure you have properly
installed and configured Docker, including docker.daemon, dns adresses and - if needed - proxy.
<p>Firstly, you have to go to folder with 'Dockerfile' and build the image with:</p>
<b>docker build -t 'your_name_of_app' .</b>
<p>After that you can run server with:</p>
<b>docker run -p 80:80 -t 'your_name_of_app'</b>

<h1>Grading application manual.</h1>

<p>Each web application should be evaluated according to <a href=https://12factor.net/>Twelve-Factor app</a>.
However, in the case of Fibonacci sequencer application, these rules might be too complex - 
application is doing only one specific task and uses no database, user validation,
complex logic and similar. For this reason, I've decided to implement my grading system.

<h2>Grading points</h2>

- Tools selection - good application should be built on a suitable technology stack. In the case of that
task, I've decided to use Flask instead of Django. Of course, Django is a still a brilliant framework, but
from the project point of view has a many unnecessary for us functionalities such user creation and authentication,
form processing, ORM layer and so on. Flask gives us a kind of freedom in tool selection.
<br><b>Grades</b><br>
-- 0 - writing server without any framework or library<br>
-- 1 - create web application but overloaded with many unnecessary features<br>
-- 2 - create a web application with one of common web framework but not quite tailored to our needs<br>
-- 3 - create a web application with a suitable web framework

- Project layout - might be quite obvious, but good directories and files structure within a project, can
save a lot of effort and time. 
<br><b>Grades</b><br>
-- 0 - unclear directory structures, all project is within one file<br>
-- 1 - the project is split among many files but without any directory structures<br>
-- 2 - the project is split among many files and many directories but without any order or logic<br>
-- 3 - the project is split among many files and many directories with reasonable logic

- Git clean code - git commits should be atomic - so small as possible, should contain only simple change and should
has a proper commit message. Good git history allows us to track a story of implementation or fixes.
<br><b>Grades</b><br>
-- 0 - all project is contained in one commit with an unclear commit message like 'project'<br>
-- 1 - all project is split into two commits with unclear<br>
-- 2 - all project is contained in one commit but with some app description within commit message<br>
-- 3 - all project is split into two commits with the descriptive commit message

- Keep logic out from view - according to KISS and DRY principles, we should keep projects business logic
as simple with reusable components.
<br><b>Grades</b><br>
-- 0 - repetitive functions declarations and too complex logic in project<br>
-- 1 - no repetitive functions, easy and clear logic 

- User documentation - user documentation is crusial, esspesialy in case when we have application with API endpoints.
<br><b>Grades</b><br>
-- 0 - no user documentation, lack of README file or even docstrings<br>
-- 1 - README file within project<br>
-- 2 - REAMDE and docstring within project

- Clean code - there are many clues about how to keep code in a more Pythonic way, according to PEP8 or even
legendary Uncle Bob. But in case of that specific project, without advanced functionalities let say
we will grade a naming convention.
<br><b>Grades</b><br>
-- 0 - unclear function or view names<br>
-- 1 - clear and understandable names 

- Easy to deploy - every developer who would like to deploy the application on his server, should be able to do that
with at least one or two commands. Easy deployment is also important in case when we want to implement or fix new features.
Fortunately, the docker image provides us with a proper solution. Furthermore, the end-user or developer can find
clues about the deployment process at the beginning of the article.
<br><b>Grades</b><br>
-- 0 - no deployment option except standard 'flask run'<br>
-- 1 - implemented deployment system but not very easy<br>
-- 2 - easy and clear deployment<br>
-- 3 - easy and clear deployment with some clues within the documentation

Total amount of points to achieve: 14.
