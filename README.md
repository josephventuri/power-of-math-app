# 📊 Power of Math – AWS Serverless Web App

## Project Overview
When first learning AWS, it's common to understand individual services like S3, Lambda, and EC2 — but much harder to tie them together into a working application. I built this project to practice combining multiple AWS services into a real, functioning app.

The goal was to create a fully serverless, end-to-end system where:
- A user could input a base number and an exponent
- The calculation would be processed automatically
- The result would be stored in a database
- The user would see the result in real time

The solution had to be serverless, scalable, and fit within AWS Free Tier limits.

---

## How It Works
Built a complete cloud-native application using AWS services:
- **AWS Amplify**: Host the frontend static web app
- **AWS Lambda (Python 3.9)**: Perform the math calculation
- **Amazon API Gateway**: Serve as the backend API trigger
- **Amazon DynamoDB**: Store calculation results and timestamps
- **AWS IAM**: Manage permissions and service communication

### Workflow Summary
1. A user enters two numbers on the web app.
2. The web app triggers an API Gateway POST request.
3. API Gateway invokes a Lambda function to perform the math.
4. The result is saved into DynamoDB.
5. The calculated answer is returned to the user's browser instantly.

---

## Tech Stack
- AWS Amplify
- AWS Lambda (Python 3.9)
- Amazon API Gateway
- Amazon DynamoDB
- AWS IAM
- HTML/CSS/JavaScript

---

## Key Lessons Learned
- Connected frontend and backend cloud services end-to-end
- Set CORS permissions correctly for cross-origin API calls
- Managed IAM roles for Lambda to access DynamoDB securely
- Practiced full serverless app deployment using Amplify and API Gateway

---

## Demonstration
- **Live Demo:** [Power of Math App](https://dev.d2nhcxnngqpa6w.amplifyapp.com)
- **GitHub Repo:** [power-of-math-app](https://github.com/josephventuri/power-of-math-app)
