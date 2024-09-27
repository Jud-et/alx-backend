0x03. Queuing System in JS
This project focuses on building a queuing system using Node.js, Kue, Redis, and various ES6 features. The system handles job creation, job management, and stock/reservation management through APIs. Below is a summary of everything learned and implemented while completing the tasks.

Technologies Used
Node.js: A JavaScript runtime used for building the server-side logic.
Express.js: A minimal and flexible Node.js web application framework.
Kue: A priority job queue backed by Redis.
Redis: An in-memory key-value store used for queuing and caching.
ES6 Features: Focused on arrow functions, async/await, spread/rest operators, and more modern JavaScript practices.
Tasks Implemented
1. Kue Setup
We learned how to set up a queue using Kue. This involves creating jobs that can be processed asynchronously. Redis is utilized as a backend to manage the job queue efficiently.

2. Writing the Job Creator
Created a function named createPushNotificationsJobs. This function:

Accepts an array of jobs and a queue.
Validates if jobs are in array format.
Creates a job for each entry, logs its progress, and handles completion and failure events.
Key Learnings:

Handling job creation and tracking job states (completed, failed, etc.).
Managing a queue with events and understanding the logging process in a job lifecycle.
3. Writing the Tests
Implemented tests for createPushNotificationsJobs to ensure:

Error handling when jobs are not passed in as arrays.
Job creation validation to confirm jobs are added to the queue.
Key Learnings:

Using Mocha and Chai for testing.
Learning how to simulate and validate job creation without processing them.
4. Stock Management with Redis
Created a stock management system using Redis:

Products Array: Stored product details such as price and stock.
Redis Client: Implemented a Redis client to handle stock reservation.
Routes: API routes to get product details and reserve items.
Key Learnings:

Using Redis to store and manage product stock.
Creating RESTful APIs with Express to handle stock inquiries and reservations.
5. Seat Reservation System
Developed a seat reservation system with a queue for job processing:

Redis: Managed seat availability.
Kue Queue: Implemented job creation for reserving seats.
Routes: Added endpoints to query seat availability, reserve seats, and process the job queue.
Key Learnings:

Handling concurrency and race conditions using queues.
Managing limited resources (seats) and ensuring jobs are processed correctly.
Key Features
Job Creation: With Kue, jobs can be created dynamically and processed in the background.
Stock and Reservation Management: A scalable system to manage product stock using Redis.
Seat Reservation: Implemented a queuing system to reserve seats efficiently.
ES6 Mastery: Implemented advanced features like async/await, arrow functions, spread/rest operators, and promisify for handling asynchronous code in Redis.
How to Run the Project
Install Dependencies:

bash
Copy code
npm install
Start Redis Server: Make sure Redis is installed and running. If not:

bash
Copy code
redis-server
Run the Queuing System:

bash
Copy code
npm run dev <file_name.js>
Run Tests:

bash
Copy code
npm test
