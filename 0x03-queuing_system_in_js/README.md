# **0x03. Queuing System in JS**

This project involves building a **queuing system** using **Node.js**, **Kue**, **Redis**, and several **ES6** features. The system handles job creation, management, and stock/reservation functionalities through various APIs.

## **Technologies Used**
- **Node.js**: JavaScript runtime environment for building server-side applications.
- **Express.js**: Web framework for building APIs.
- **Kue**: Redis-based priority job queue.
- **Redis**: In-memory data structure store used as a database and caching system.
- **Mocha/Chai**: Testing framework for unit and integration testing.
- **ES6 Features**: Arrow functions, async/await, spread/rest operators, and more.

---

## **Table of Contents**
1. [Project Overview](#project-overview)
2. [Implemented Features](#implemented-features)
3. [Setup Instructions](#setup-instructions)
4. [Key Learnings](#key-learnings)
5. [How to Run](#how-to-run)
6. [Testing](#testing)

---

## **Project Overview**

This project simulates a system where jobs are queued and processed asynchronously. Redis handles data caching, and Kue manages the job queue. It's useful for scenarios such as stock and seat reservation management where handling multiple requests efficiently is crucial.

---

## **Implemented Features**

### 1. **Job Creation with Kue**
- **Functionality**: A function `createPushNotificationsJobs` is created to handle job creation. The function:
  - Accepts an array of jobs and a Kue queue.
  - Validates the jobs array.
  - Logs the creation, completion, failure, and progress of each job.
  
### 2. **Test Suite for Job Creation**
- **Testing Framework**: **Mocha** and **Chai** are used to test the `createPushNotificationsJobs` function.
  - Ensure jobs are added to the queue.
  - Validate that errors are handled when an incorrect data type is passed.

### 3. **Stock Management with Redis**
- **Functionality**: A stock management system that:
  - Stores product details (ID, name, price, stock) in an array.
  - Allows querying product stock using Redis.
  - Implements routes to get product lists and manage stock reservations.

### 4. **Seat Reservation System**
- **Functionality**: Built a system to manage seat reservations:
  - Seats are initialized with a fixed number.
  - Seat availability is managed using Redis.
  - Jobs are queued using Kue to reserve seats.

---

## **Setup Instructions**

1. **Clone the repository**:
   ```bash
   git clone https://github.com/<your-username>/0x03-queuing_system_in_js.git
   cd 0x03-queuing_system_in_js
