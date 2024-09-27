0x03. Queuing System in JS
This project involves building a queuing system using Node.js, Kue, Redis, and several ES6 features. The system handles job creation, management, and stock/reservation functionalities through various APIs.

Technologies Used
Node.js: JavaScript runtime environment for building server-side applications.
Express.js: Web framework for building APIs.
Kue: Redis-based priority job queue.
Redis: In-memory data structure store used as a database and caching system.
Mocha/Chai: Testing framework for unit and integration testing.
ES6 Features: Arrow functions, async/await, spread/rest operators, and more.
Table of Contents
Project Overview
Implemented Features
Setup Instructions
Key Learnings
How to Run
Testing
Project Overview
This project simulates a system where jobs are queued and processed asynchronously. Redis handles data caching, and Kue manages the job queue. It's useful for scenarios such as stock and seat reservation management where handling multiple requests efficiently is crucial.

Implemented Features
1. Job Creation with Kue
Functionality: A function createPushNotificationsJobs is created to handle job creation. The function:
Accepts an array of jobs and a Kue queue.
Validates the jobs array.
Logs the creation, completion, failure, and progress of each job.
2. Test Suite for Job Creation
Testing Framework: Mocha and Chai are used to test the createPushNotificationsJobs function.
Ensure jobs are added to the queue.
Validate that errors are handled when an incorrect data type is passed.
3. Stock Management with Redis
Functionality: A stock management system that:
Stores product details (ID, name, price, stock) in an array.
Allows querying product stock using Redis.
Implements routes to get product lists and manage stock reservations.
4. Seat Reservation System
Functionality: Built a system to manage seat reservations:
Seats are initialized with a fixed number.
Seat availability is managed using Redis.
Jobs are queued using Kue to reserve seats.
Setup Instructions
Clone the repository:

bash
Copy code
git clone https://github.com/<your-username>/0x03-queuing_system_in_js.git
cd 0x03-queuing_system_in_js
Install the dependencies:

bash
Copy code
npm install
Ensure Redis is installed and running:

bash
Copy code
redis-server
Set up the environment: You will need Node.js and Redis installed locally.

Key Learnings
Job Queuing with Kue: Learned how to create and manage jobs with Kue, utilizing Redis to handle queued tasks asynchronously.
Redis Integration: Used Redis for caching and handling the availability of products and seats.
Express.js: Built several routes to interact with the queue and manage stock/reservations.
ES6 Features: Applied modern JavaScript features such as:
Arrow Functions: Shorter function syntax.
Async/Await: For managing asynchronous operations.
Spread and Rest Operators: For handling objects and arrays dynamically.
How to Run
Start Redis Server: Make sure Redis is installed and running:

bash
Copy code
redis-server
Run the project: To run individual scripts (for example, job creation or seat reservation):

bash
Copy code
npm run dev <script-file.js>
Example:

bash
Copy code
npm run dev 8-job-main.js
Available Routes:

GET /list_products: Returns a list of all products.
GET /list_products/
: Returns the stock and details of a specific product.
GET /reserve_product/
: Reserves a product if stock is available.
GET /available_seats: Returns the number of available seats.
GET /reserve_seat: Reserves a seat if available and queues the reservation.
GET /process: Processes the queue for seat reservations.
Testing
To run tests, use the following command:

bash
Copy code
npm test
The test suite covers:

Validating job creation with Kue.
Checking the stock management system.
Ensuring error handling is correct for invalid inputs.
